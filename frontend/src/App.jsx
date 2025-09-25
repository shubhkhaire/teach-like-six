import React, { useState } from "react";
import Navbar from "./components/Navbar";
import SearchBox from "./components/SearchBox";
import ExplainerCard from "./components/ExplainerCard";
import { createExplainer } from "./services/api";

export default function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  async function handleExplain(topic, options = { include_image: true, include_voice: false }) {
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const res = await createExplainer(topic, options);
      setResult(res);
    } catch (e) {
      console.error(e);
      setError(e.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app">
      <Navbar />
      <main className="container">
        <h1>Explain It Like I'm Six</h1>
        <p className="tagline">Type a topic — get a short, kid-friendly explanation with a comic.</p>
        <SearchBox onExplain={handleExplain} loading={loading} />
        {loading && <div className="loader">Thinking…</div>}
        {error && <div className="error">{error}</div>}
        {result && <ExplainerCard data={result} />}
      </main>
    </div>
  );
}
