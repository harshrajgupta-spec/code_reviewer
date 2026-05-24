export default function CommentsList({ comments }) {
  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 mt-8">
      <h2 className="text-2xl font-semibold text-white mb-4">
        AI Comments
      </h2>

      <div className="space-y-3">
        {comments.map((comment, index) => (
          <div
            key={index}
            className="bg-zinc-950 border border-zinc-800 rounded-xl p-4 text-zinc-300"
          >
            {comment}
          </div>
        ))}
      </div>
    </div>
  );
}