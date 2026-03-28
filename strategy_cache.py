import requests

strategy_cache = {}

API_URL = "https://dreaminalgo-backend-production.up.railway.app/api/deployments/today/"

def load_users(strategy_id):
    try:
        res = requests.get(f"{API_URL}{strategy_id}")
        data = res.json()

        grouped = {}

        for user in data:
            broker = user["broker_name"]  # dhan / angel

            grouped.setdefault(broker, []).append({
                "user_id": user["user_id"],
                "multiplier": user["multiplier"],
                "credentials": user["credentials"]
            })

        strategy_cache[strategy_id] = grouped

        print(f"✅ Loaded users for {strategy_id}")

    except Exception as e:
        print("❌ Error loading users:", e)