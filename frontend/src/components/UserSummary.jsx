import { useState } from "react";
import { getUserSummary } from "../services/api";

export default function UserSummary() {
  const [userId, setUserId] = useState("");
  const [summary, setSummary] = useState(null);

  const load = async () => {
    const data = await getUserSummary(userId);
    setSummary(data);
  };

  return (
    <div>
      <div className="form">
        <input
          className="input"
          placeholder="User ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
        />
        <button className="btn" onClick={load}>
          Générer résumé
        </button>
      </div>

      {summary && (
        <div className="summary">
          <p> Total: {summary.total_events}</p>
          <p> Premier: {summary.first_event}</p>
          <p> Dernier: {summary.last_event}</p>
        </div>
      )}
    </div>
  );
}