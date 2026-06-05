import { useState } from "react";
import { createEvent } from "../services/api";

export default function EventForm({ onCreated }) {
  const [userId, setUserId] = useState("");
  const [type, setType] = useState("");
  const [message, setMessage] = useState("");

  const submit = async (e) => {
    e.preventDefault();

    if (!userId || !type) return;

    await createEvent({
      user_id: userId,
      event_type: type,
      timestamp: new Date().toISOString(),
      event_metadata: {
        message: message || null,
      },
    });

    setUserId("");
    setType("");
    setMessage("");

    onCreated();
  };

  return (
    <form className="form" onSubmit={submit}>
      <input
        className="input"
        placeholder="User ID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
      />

      <select
        className="input"
        value={type}
        onChange={(e) => setType(e.target.value)}
      >
        <option value="">Sélectionnez un type</option>
        <option value="connexion">Connexion</option>
        <option value="transaction">Transaction</option>
        <option value="signalement">Signalement</option>
      </select>

      <input
        className="input"
        placeholder="Message (optionnel)"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button className="btn">Créer l'événement</button>
    </form>
  );
}