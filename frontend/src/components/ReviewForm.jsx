import { useState } from "react";

export default function ReviewForm({ onSubmit, loading }) {
  const [repo, setRepo] = useState("");
  const [prNumber, setPrNumber] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    onSubmit({
      repo,
      pr_number: Number(prNumber),
    });
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-zinc-900 p-6 rounded-2xl border border-zinc-800"
    >
      <div className="mb-5">
        <label className="block text-zinc-400 mb-2">
          Repository
        </label>

        <input
          type="text"
          placeholder="facebook/react"
          value={repo}
          onChange={(e) => setRepo(e.target.value)}
          className="w-full bg-zinc-950 border border-zinc-700 rounded-xl px-4 py-3 text-white outline-none"
        />
      </div>

      <div className="mb-5">
        <label className="block text-zinc-400 mb-2">
          PR Number
        </label>

        <input
          type="number"
          placeholder="123"
          value={prNumber}
          onChange={(e) => setPrNumber(e.target.value)}
          className="w-full bg-zinc-950 border border-zinc-700 rounded-xl px-4 py-3 text-white outline-none"
        />
      </div>

      <button
        type="submit"
        disabled={loading}
        className="w-full bg-blue-600 hover:bg-blue-500 transition py-3 rounded-xl font-semibold text-white"
      >
        {loading ? "Reviewing..." : "Start Review"}
      </button>
    </form>
  );
}