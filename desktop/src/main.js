import { check } from '@tauri-apps/plugin-updater';
import { sendNotification, requestPermission } from '@tauri-apps/plugin-notification';
import { relaunch } from '@tauri-apps/plugin-process';

const PLANE_URL = "https://plane.huma.local";
document.querySelector("#plane").src = PLANE_URL;

export async function notify(title, body) {
  if (await requestPermission() !== 'granted') return;
  sendNotification({ title, body });
}

export async function checkUpdate() {
  const update = await check();
  if (!update) return false;
  await notify("Hüma", `Yeni sürüm: ${update.version}`);
  await update.downloadAndInstall();
  await relaunch();
  return true;
}
window.addEventListener('DOMContentLoaded', checkUpdate);
