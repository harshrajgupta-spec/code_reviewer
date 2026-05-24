import { useState } from "react";

import API from "./services/api";

import Header from "./components/Header";
import ReviewForm from "./components/ReviewForm";
import DecisionCard from "./components/DecisionCard";
import FindingsList from "./components/FindingsList";
import CommentsList from "./components/CommentsList";

export default function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const startReview = async (data) => {
    try {
      setLoading(true);

      const response = await API.post("/github-webhook", data);

      setResult(response.data);
    } catch (error) {
      console.error(error);

      alert("Review failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-zinc-950 px-6 py-10">
      <div className="max-w-4xl mx-auto">
        <Header />

        <ReviewForm
          onSubmit={startReview}
          loading={loading}
        />

        {result && (
          <>
            <DecisionCard
              decision={result.decision}
            />

            <FindingsList
              findings={result.findings}
            />

            <CommentsList
              comments={result.comments}
            />
          </>
        )}
      </div>
    </div>
  );
}