import React from "react";
import ComicPanel from "./ComicPanel";

export default function ExplainerCard({ data }) {
  return (
    <section className="explainer-card">
      <h2 style={{ marginTop: 0 }}>{data.topic}</h2>
      <div className="explainer-text">{data.text}</div>

      {data.image_url && (
        <div style={{ textAlign: "center" }}>
          <ComicPanel src={data.image_url} alt={data.topic} />
        </div>
      )}

      {data.voice_url && (
        <div style={{ marginTop: 12 }}>
          <audio controls src={data.voice_url}>Your browser does not support audio.</audio>
        </div>
      )}
    </section>
  );
}
