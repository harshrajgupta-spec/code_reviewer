export default function FindingsList({ findings }) {
  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 mt-8">
      <h2 className="text-2xl font-semibold text-white mb-4">
        Findings
      </h2>

      <div className="space-y-3">
        {findings.map((finding, index) => (
          <div
            key={index}
            className="bg-zinc-950 border border-zinc-800 rounded-xl p-4 text-zinc-300"
          >
            {finding}
          </div>
        ))}
      </div>
    </div>
  );
}