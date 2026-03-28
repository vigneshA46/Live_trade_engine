import asyncio
from strategy_cache import strategy_cache
from broker_router import route_signal

async def process_signal(signal):
    print("📡 Signal:", signal)

    strategy_id = signal["strategy_id"]

    users = strategy_cache.get(strategy_id)

    if not users:
        print("⚠️ No users found")
        return

    await route_signal(signal, users)

