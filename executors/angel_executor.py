# executors/angel_executor.py

from brokers.angel_adapter import AngelAdapter

async def angel_order(user, signal):
    try:
        creds = user["credentials"]

        adapter = AngelAdapter(
            api_key=creds["apiKey"],
            client_id=creds["clientId"],
            password=creds["password"],
            totp_secret=creds["totp"]
        )

        adapter.login()

        qty = signal["quantity"] * user["multiplier"]

        order_id = adapter.place_order(
            symbol=signal["symbol"],
            token=signal["token"],
            side=signal["side"],
            quantity=qty
        )

        print(f"✅ ANGEL order success {user['user_id']}")

    except Exception as e:
        print(f"❌ ANGEL failed {user['user_id']}: {e}")