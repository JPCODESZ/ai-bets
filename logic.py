import requests
import os

# Set your Odds API key here
API_KEY = os.environ.get("ODDS_API_KEY", "YOUR_ODDS_API_KEY")

# Example function to fetch odds from The Odds API
def load_data():
    url = "https://api.theoddsapi.com/v4/sports/upcoming/odds"
    params = {
        "apiKey": API_KEY,
        "regions": "us",  # You can adjust this based on region
        "markets": "h2h",  # Market type (head-to-head)
        "bookmakers": "fanduel"  # Only FanDuel odds
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()  # Return the JSON data
    except Exception as e:
        print(f"❌ Error fetching odds: {e}")
        return []

# Update get_filtered_bets to use the new Odds API
def get_filtered_bets(limit=20):
    events = load_data()
    results = []

    for event in events:
        for book in event.get("bookmakers", []):
            if book["key"] != "fanduel":
                continue
            for market in book.get("markets", []):
                if market["key"] != "h2h":
                    continue
                for outcome in market.get("outcomes", []):
                    results.append({
                        "event": f"{event['away_team']} @ {event['home_team']}",
                        "team": outcome["name"],
                        "odds": outcome["price"],
                        "start_time": event["commence_time"]
                    })
        # Check the limit after processing each event
        if len(results) >= limit:
            break

    return results[:limit]
