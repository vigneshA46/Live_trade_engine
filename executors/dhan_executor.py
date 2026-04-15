# executors/dhan_executor.py

from brokers.dhan import DhanAdapter
from dhan_token import get_access_token

async def dhan_order(user, signal):
    try:
        creds = user["credentials"]

        #print("CREDS:",creds)
        token= get_access_token()

        adapter = DhanAdapter(
            client_id=creds["clientId"],
            access_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzc2MzUwNDEyLCJpYXQiOjE3NzYyNjQwMTIsInRva2VuQ29uc3VtZXJUeXBlIjoiU0VMRiIsIndlYmhvb2tVcmwiOiIiLCJkaGFuQ2xpZW50SWQiOiIxMTA3NDI1Mjc1In0.KqQpGxQPsIxVULLdIAjA-GH9uAfoOoCIz37YtMyAwMqwEOmCm5WTP08bnqGJeTlOqlQCD9o7dYF5j6YR5KYM1w"   # you build this
        )

        qty = signal["quantity"] * user["multiplier"]

        response = adapter.place_order(
            security_id=signal["security_id"],
            side=signal["side"],
            quantity=qty
        )
        print(response)

        print(f"✅ DHAN order success {user['user_id']}")

    except Exception as e:
        print(f"❌ DHAN failed {user['user_id']}: {e}")