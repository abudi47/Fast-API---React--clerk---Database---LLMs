import React from "react";
import MCQChallenge from "../challenges/MCQChallenge";
import { useState, useEffect } from "react";

export default function HistoryPanel() {
  const [history, setHistory] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    setIsLoading(false);
    setError(null);
  };

  if (isLoading) {
    return <div className="loading">Loading...</div>;
  }

  if (error) {
    return (
      <div className="error-message">
        <p>{error}</p>
        <button onClick={fetchHistory}>Retry</button>
      </div>
    );
  }
  return (
    <div className="history-panel">
      <h2>Challenge History</h2>
      {history.length === 0 ? (
        <p>No challenge history</p>
      ) : (
        <div className="history-list">
          {history.map((challenge) => {
            return (
              <MCQChallenge
                key={challenge.id}
                challenge={challenge}
                showExplanation
              />
            );
          })}
        </div>
      )}
    </div>
  );
}
