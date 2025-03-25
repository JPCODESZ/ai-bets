import json

def load_data():
    with open("sample_data.json") as f:
        return json.load(f)

def get_filtered_bets(min_odds=200, max_odds=600):
    events = load_data()
    filtered = []
    for event in events:
        for book in event.get("bookmakers", []):
            if book["key"] != "fanduel":
                continue
            for market in book.get("markets", []):
                if market["key"] != "h2h":
                    continue
                for outcome in market.get("outcomes", []):
                    price = outcome["price"]
                    if min_odds <= price <= max_odds:
                        filtered.append({
                            "event": f"{event['away_team']} @ {event['home_team']}",
                            "team": outcome["name"],
                            "odds": price,
                            "start_time": event["commence_time"]
                        })
    return filtered

def place_bet(data):
    print(f"Placing bet on {data['team']} at +{data['odds']}...")
    return {"status": "success", "details": data}
