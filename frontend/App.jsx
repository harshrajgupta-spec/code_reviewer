// App.jsx

import { useState } from "react";
import axios from "axios";

export default function App() {
  const [repo, setRepo] = useState("");
  const [prNumber, setPrNumber] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function triggerReview() {
    try {
      setLoading(true);

      const response = await axios.post(
        "http://localhost:8000/github-webhook",
        {
          repository: {
            full_name: repo,
          },
          pull_request: {
            number: Number(prNumber),
          },
        }
      );

      setResult(response.data);
    } catch (err) {
      console.error(err);

      setResult({
        error: "Failed to review PR",
      });
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-zinc-950 text-white p-8">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-4xl font-bold mb-2">
          Agentic PR Reviewer
        </h1>

        <p className="text-zinc-400 mb-8">
          AI-powered GitHub Pull Request Review System
        </p>

        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 space-y-4">
          <div>
            <label className="block mb-2 text-sm text-zinc-400">
              Repository
            </label>

            <input
              type="text"
              placeholder="owner/repository"
              value={repo}
              onChange={(e) => setRepo(e.target.value)}
              className="w-full bg-zinc-950 border border-zinc-700 rounded-xl px-4 py-3 outline-none focus:border-blue-500"
            />
          </div>

          <div>
            <label className="block mb-2 text-sm text-zinc-400">
              Pull Request Number
            </label>

            <input
              type="number"
              placeholder="42"
              value={prNumber}
              onChange={(e) => setPrNumber(e.target.value)}
              className="w-full bg-zinc-950 border border-zinc-700 rounded-xl px-4 py-3 outline-none focus:border-blue-500"
            />
          </div>

          <button
            onClick={triggerReview}
            disabled={loading}
            className="w-full bg-blue-600 hover:bg-blue-500 transition rounded-xl py-3 font-semibold"
          >
            {loading ? "Reviewing..." : "Start AI Review"}
          </button>
        </div>

        {result && (
          <div className="mt-8 bg-zinc-900 border border-zinc-800 rounded-2xl p-6">
            <h2 className="text-2xl font-semibold mb-4">
              Review Result
            </h2>

            {result.error ? (
              <div className="text-red-400">
                {result.error}
              </div>
            ) : (
              <div className="space-y-4">
                <div>
                  <span className="text-zinc-400">
                    Decision:
                  </span>

                  <div className="mt-2 inline-flex px-4 py-2 rounded-full bg-green-600/20 text-green-400 border border-green-500/30">
                    {result.decision}
                  </div>
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
