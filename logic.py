import requests
import os

def load_data():
    api_key = os.environ.get("ODDS_API_KEY") or "9d71f7c5e796eec9bace56a35856504f"

    url = "https://api.the-odds-api.com/v4/sports/upcoming/odds"
    params = {
        "apiKey": api_key,
        "regions": "us",
        "markets": "h2h",
        "oddsFormat": "american",
        "bookmakers": "fanduel"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("❌ Odds API error:", e)
        return []

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
