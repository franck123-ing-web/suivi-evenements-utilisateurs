import { useState } from "react";
import EventForm from "./components/EventForm";
import EventList from "./components/EventList";
import UserSummary from "./components/UserSummary";
import "./style.css";

export default function App() {
  const [refresh, setRefresh] = useState(false);

  return (
    <div className="app-container">
      <header className="header">
        <h1> Suivi des événements utilisateurs</h1>
        <p className="subtitle">
          Mini plateforme de tracking et analyse d’activité
        </p>
      </header>

      <main className="grid">
        <section className="card">
          <h2>Créer un événement</h2>
          <EventForm onCreated={() => setRefresh(!refresh)} />
        </section>

        <section className="card">
          <h2>Liste des événements</h2>
          <EventList refresh={refresh} />
        </section>

        <section className="card">
          <h2>Résumé utilisateur</h2>
          <UserSummary />
        </section>
      </main>
    </div>
  );
}