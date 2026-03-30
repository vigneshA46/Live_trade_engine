""" import os
from dotenv import load_dotenv
from dhan_token import get_access_token
from dhanhq import dhanhq
from brokers.dhan import DhanAdapter


CLIENT_ID = os.getenv("CLIENT_ID")
access_token = get_access_token()
dhan = dhanhq(CLIENT_ID,access_token)

dhanadapter = DhanAdapter(
    client_id=CLIENT_ID,
    access_token=access_token
)

 
response = dhanadapter.place_order(
        security_id="54499",     # ⚠️ actual dhan securityId required
        side="BUY",
        quantity=65
        )

print(response) 

order_id = 362260327171231

res = dhan.get_order_by_id(order_id)

print(res) """

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import time
import asyncio
from strategy_cache import load_users
from signal_emitter import emit_signal
from brokers.dhan import DhanAdapter

strategy_id = "1fff432a-0411-40ff-aefd-c0b0026d5a6d"
loop = asyncio.get_event_loop()

load_users(strategy_id)

emit_signal({
    "strategy_id": strategy_id,
    "option": "CE",
    "side": "BUY",
    "quantity": 65,
    "security_id": "35105",
    "token": "54722",
    "symbol": "NIFTY30MAR2626800CE"
})

loop.run_until_complete(asyncio.sleep(5))