from sqlalchemy import select
from utils.db_async import AsyncSessionLocal, Inventory


async def get_inventory(discord_id: str) -> dict:
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Inventory).where(Inventory.discord_id == discord_id)
        )
        return {r.item_id: r.quantity for r in result.scalars()}


async def has_item(discord_id: str, item_id: str) -> bool:
    async with AsyncSessionLocal() as session:
        row = await session.get(Inventory, (discord_id, item_id))
        return row is not None and row.quantity > 0


async def add_item(discord_id: str, item_id: str, quantity: int = 1):
    async with AsyncSessionLocal() as session:
        row = await session.get(Inventory, (discord_id, item_id))
        if row:
            row.quantity += quantity
        else:
            session.add(Inventory(discord_id=discord_id, item_id=item_id, quantity=quantity))
        await session.commit()


async def remove_item(discord_id: str, item_id: str, quantity: int = 1) -> bool:
    async with AsyncSessionLocal() as session:
        row = await session.get(Inventory, (discord_id, item_id))
        if not row or row.quantity < quantity:
            return False
        row.quantity -= quantity
        if row.quantity <= 0:
            await session.delete(row)
        await session.commit()
    return True
