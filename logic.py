import requests
import os

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
        # ✅ Only check limit after a full event is processed
        if len(results) >= limit:
            break

    return results[:limit]
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("❌ Error fetching odds:", e)
        return []

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
                    if len(results) >= limit:
                        return results
    return results
