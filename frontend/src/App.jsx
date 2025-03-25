import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [bets, setBets] = useState([]);

  useEffect(() => {
    axios.get("https://ai-bets.onrender.com/bets") // Update with your actual backend URL
      .then((res) => setBets(res.data))
      .catch((err) => console.error("API error:", err));
  }, []);

  const handleBet = async (bet) => {
    await axios.post("https://ai-bets.onrender.com/place-bet", bet);
    alert(`Placed bet on ${bet.team} at +${bet.odds}`);
  };

  return (
    <div className="p-6 font-sans">
      <h1 className="text-3xl font-bold mb-6">🎯 AI Bets - Smart Picks</h1>
      <div className="grid gap-4">
        {bets.map((bet, idx) => (
          <div key={idx} className="border p-4 rounded shadow-md bg-white">
            <h2 className="text-xl font-semibold">{bet.event}</h2>
            <p>Bet on: <strong>{bet.team}</strong> at <strong>+{bet.odds}</strong></p>
            <p>Start Time: {new Date(bet.start_time).toLocaleString()}</p>
            <button
              onClick={() => handleBet(bet)}
              className="mt-2 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
            >
              Place Bet
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
