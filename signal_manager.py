import asyncio

async def process_signal(signal):
    print("📡 Signal received:", signal)

def handle_signal(signal):
    asyncio.run(process_signal(signal))