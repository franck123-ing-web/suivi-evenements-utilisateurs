const API_URL = "http://localhost:8000";

export async function getEvents(params = "") {
  const res = await fetch(`${API_URL}/events${params}`);
  return res.json();
}

export async function createEvent(data) {
  const res = await fetch(`${API_URL}/events`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function getUserSummary(userId) {
  const res = await fetch(`${API_URL}/users/${userId}/summary`);
  return res.json();
}