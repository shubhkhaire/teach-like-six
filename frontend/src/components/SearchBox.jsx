import React, { useState } from "react";

export default function SearchBox({ onExplain, loading }) {
  const [topic, setTopic] = useState("");

  function submit(e) {
    e.preventDefault();
    if (!topic.trim()) return;
    onExplain(topic.trim());
  }

  return (
    <form className="search-box" onSubmit={submit}>
      <input
        placeholder="e.g., What is WiFi? Or: How do credit cards work?"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        disabled={loading}
      />
      <button type="submit" disabled={loading}>
        Explain
      </button>
    </form>
  );
}
