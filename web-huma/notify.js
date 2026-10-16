export function watchAnnounce(cb) {
  return null;
}
export async function push(title, body) {
  if (window.__TAURI__) await window.__TAURI__.notification.send({ title, body });
  else if ("Notification" in window) new Notification(title, { body });
}
