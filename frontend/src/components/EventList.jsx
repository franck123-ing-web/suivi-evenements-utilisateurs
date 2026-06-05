import { useEffect, useState } from "react";
import { getEvents } from "../services/api";

export default function EventList({ refresh }) {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    load();
  }, [refresh]);

  const load = async () => {
    const data = await getEvents();
    setEvents(data);
  };

  return (
    <div className="list">
      {events.map((e) => (
        <div key={e.id} className="event-card">
          <div className="tag">{e.event_type}</div>
          <p><b>User:</b> {e.user_id}</p>
          <p className="date">{e.timestamp}</p>
        </div>
      ))}
    </div>
  );
}