import { useState } from "react";
export default function Announcements({ items }) {
  const [pins, setPins] = useState([]);
  const pin = (id) => setPins((p) => (p.includes(id) ? p.filter((x) => x !== id) : [...p.slice(-2), id]));
  const sorted = [...items].sort((a, b) => pins.includes(b.id) - pins.includes(a.id));
  return <ul>{sorted.map((a) => (<li key={a.id}>{pins.includes(a.id) ? "📌 " : ""}<b>{a.title}</b> — {a.date}<button onClick={() => pin(a.id)}>Pin</button></li>))}</ul>;
}
