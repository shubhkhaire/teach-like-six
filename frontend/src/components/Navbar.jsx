import React from "react";

export default function Navbar() {
  return (
    <nav className="nav">
      <div className="container" style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <div className="brand">Explain I'm Six</div>
        <div style={{ fontSize: 14, color: "#64748b" }}>Simple explainers for curious minds</div>
      </div>
    </nav>
  );
}
