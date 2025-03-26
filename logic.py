import json

def load_data():
    with open("sample_data.json") as f:
        return json.load(f)

def get_filtered_bets(min_odds=200, max_odds=600):
    events = from oddsjam import OddsJam
import os

def load_data():
    api_key = os.environ.get("ODDSJAM_API_KEY", "YOUR_API_KEY")
    oj = OddsJam(api_key)

    # You can adjust parameters here based on what OddsJam supports
    odds = oj.get_odds(
        sportsbook="fanduel",  # or None for all
        market="h2h",          # head-to-head market
        min_edge=0             # you can add filters here
    )
    return odds
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
