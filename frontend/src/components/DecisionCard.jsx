export default function DecisionCard({ decision }) {
  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 mt-8">
      <h2 className="text-2xl font-semibold text-white mb-4">
        Decision
      </h2>

      <div className="inline-flex px-4 py-2 rounded-full bg-green-500/20 border border-green-500/30 text-green-400">
        {decision}
      </div>
    </div>
  );
}