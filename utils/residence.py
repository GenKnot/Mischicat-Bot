import time
from sqlalchemy import select
from utils.db_async import AsyncSessionLocal, Residence


async def has_residence(discord_id: str, city: str) -> bool:
    async with AsyncSessionLocal() as session:
        row = await session.get(Residence, (discord_id, city))
        return row is not None


async def get_residences(discord_id: str) -> list[str]:
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Residence).where(Residence.discord_id == discord_id)
        )
        return [r.city for r in result.scalars()]


async def add_residence(discord_id: str, city: str):
    async with AsyncSessionLocal() as session:
        existing = await session.get(Residence, (discord_id, city))
        if not existing:
            session.add(Residence(
                discord_id=discord_id,
                city=city,
                purchased_at=time.time(),
            ))
            await session.commit()
