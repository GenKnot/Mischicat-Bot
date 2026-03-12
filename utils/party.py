import uuid
import time
from sqlalchemy import select, text
from utils.db_async import AsyncSessionLocal, Party, Player


async def get_party(party_id: str) -> dict | None:
    async with AsyncSessionLocal() as session:
        party = await session.get(Party, party_id)
        if not party:
            return None
        return {"party_id": party.party_id, "leader_id": party.leader_id, "city": party.city, "created_at": party.created_at}


async def get_party_members(party_id: str) -> list[dict]:
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Player).where(Player.party_id == party_id)
        )
        return [
            {c.key: getattr(p, c.key) for c in Player.__table__.columns}
            for p in result.scalars()
        ]


async def create_party(leader_id: str, city: str) -> str:
    party_id = str(uuid.uuid4())[:8]
    async with AsyncSessionLocal() as session:
        session.add(Party(party_id=party_id, leader_id=leader_id, city=city, created_at=time.time()))
        leader = await session.get(Player, leader_id)
        if leader:
            leader.party_id = party_id
        await session.commit()
    return party_id


async def add_to_party(party_id: str, uid: str) -> bool:
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Player).where(Player.party_id == party_id)
        )
        count = len(result.scalars().all())
        if count >= 4:
            return False
        player = await session.get(Player, uid)
        if not player:
            return False
        player.party_id = party_id
        await session.commit()
    return True


async def remove_from_party(uid: str) -> str:
    async with AsyncSessionLocal() as session:
        player = await session.get(Player, uid)
        if not player or not player.party_id:
            return "你不在任何队伍中。"
        party_id = player.party_id
        party = await session.get(Party, party_id)
        player.party_id = None
        await session.flush()
        if not party:
            await session.commit()
            return "已退出队伍。"
        result = await session.execute(
            select(Player).where(Player.party_id == party_id)
        )
        remaining = result.scalars().all()
        if not remaining:
            await session.delete(party)
        elif uid == party.leader_id and remaining:
            party.leader_id = remaining[0].discord_id
        await session.commit()
    return "已退出队伍。"


async def disband_party(uid: str) -> tuple[str, list[str]]:
    async with AsyncSessionLocal() as session:
        player = await session.get(Player, uid)
        if not player or not player.party_id:
            return "你不在任何队伍中。", []
        party_id = player.party_id
        party = await session.get(Party, party_id)
        if not party or party.leader_id != uid:
            return "只有队长才能解散队伍。", []
        result = await session.execute(
            select(Player).where(Player.party_id == party_id)
        )
        members = result.scalars().all()
        member_ids = [m.discord_id for m in members]
        for m in members:
            m.party_id = None
        await session.delete(party)
        await session.commit()
    return "队伍已解散，所有成员已退出。", member_ids
