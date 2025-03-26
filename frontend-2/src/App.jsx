import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [bets, setBets] = useState([]);

  useEffect(() => {
    axios.get("https://ai-bets-2.onrender.com/bets")
      .then((res) => setBets(res.data))
      .catch((err) => console.error("API error:", err));
  }, []);

  const handleBet = async (bet) => {
    await axios.post("https://ai-bets-2.onrender.com/place-bet", bet);
    alert(`Placed bet on ${bet.team} at +${bet.odds}`);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-100 font-sans">
      <header className="bg-white shadow-md sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-4 py-5 flex justify-between items-center">
          <h1 className="text-3xl font-bold text-blue-800">💸 AI Bets</h1>
          <p className="text-sm text-gray-500">Smartest sports bets, auto-ranked</p>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-4 py-10">
        <section className="text-center mb-12">
          <h2 className="text-4xl font-extrabold text-gray-800 mb-2">Find Your Edge. Win More.</h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Powered by live FanDuel odds and AI insights. These are the top value bets right now — filtered and ranked for real edge.
          </p>
        </section>

        {bets.length === 0 ? (
          <p className="text-center text-gray-500">Loading smart bets...</p>
        ) : (
          <div className="grid md:grid-cols-2 gap-6">
            {bets.map((bet, idx) => (
              <div key={idx} className="bg-white p-6 rounded-xl shadow hover:shadow-lg transition">
                <h3 className="text-xl font-semibold text-blue-700 mb-1">{bet.event}</h3>
                <p className="text-md">Bet on: <strong>{bet.team}</strong> @ <span className="text-green-600 font-bold">+{bet.odds}</span></p>
                <p className="text-sm text-gray-500 mb-3">Starts: {new Date(bet.start_time).toLocaleString()}</p>
                <button
                  onClick={() => handleBet(bet)}
                  className="px-4 py-2 rounded bg-blue-600 text-white hover:bg-blue-700"
                >
                  Place Bet
                </button>
              </div>
            ))}
          </div>
        )}
      </main>

      <footer className="text-center py-6 text-gray-400 text-sm">
        &copy; {new Date().getFullYear()} AI Bets • Smarter Wagers Start Here
      </footer>
    </div>
  );
}

export default App;
