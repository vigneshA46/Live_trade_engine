# broker_router.py

import asyncio
from executors.dhan_executor import dhan_order
from executors.angel_executor import angel_order

async def route_signal(signal, users):
    tasks = []

    if "dhan" in users:
        tasks.append(execute(users["dhan"], signal, dhan_order))

    if "angel" in users:
        tasks.append(execute(users["angel"], signal, angel_order))

    await asyncio.gather(*tasks)


async def execute(user_list, signal, broker_func):
    await asyncio.gather(*[
        broker_func(user, signal) for user in user_list
    ])