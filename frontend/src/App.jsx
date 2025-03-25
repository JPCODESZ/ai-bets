import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [bets, setBets] = useState([]);

  useEffect(() => {
   axios.get("https://ai-bets-2.onrender.com/bets") // Replace with your backend if needed
      .then((res) => setBets(res.data))
      .catch((err) => console.error("API error:", err));
  }, []);

  const handleBet = async (bet) => {
    await axios.post("https://ai-bets-2.onrender.com/place-bet", bet);
    alert(`Placed bet on ${bet.team} at +${bet.odds}`);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-blue-100 p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-10 text-blue-900">🎯 AI Smart Bets</h1>

        {bets.length === 0 ? (
          <p className="text-center text-gray-600">No bets available right now.</p>
        ) : (
          <div className="grid gap-6">
            {bets.map((bet, idx) => (
              <div key={idx} className="bg-white rounded-2xl shadow-md p-6 transition hover:shadow-lg">
                <h2 className="text-2xl font-semibold text-blue-800 mb-2">{bet.event}</h2>
                <p className="text-lg">
                  Bet on: <span className="font-semibold">{bet.team}</span> @ <span className="text-green-600 font-bold">+{bet.odds}</span>
                </p>
                <p className="text-sm text-gray-500 mb-4">Starts: {new Date(bet.start_time).toLocaleString()}</p>
                <button
                  onClick={() => handleBet(bet)}
                  className="mt-2 px-5 py-2 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 transition"
                >
                  Place Bet
                </button>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
