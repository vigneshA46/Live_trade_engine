import asyncio
from signal_manager import process_signal

def emit_signal(signal):
    asyncio.create_task(process_signal(signal))