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

from signal_emitter import emit_signal

# when condition matches
emit_signal({
    "strategy_id": "123456",
    "option": "CE",
    "side": "BUY",
    "quantity": 50,
    "security_id": "56w4"
})