const BASE = '/api/invites';

async function istek(path, opt = {}) {
  const r = await fetch(BASE + path, {
    headers: { 'Content-Type': 'application/json' },
    ...opt,
  });
  if (r.status === 404) throw { kod: 404, mesaj: 'Kod bulunamadı' };
  if (r.status === 429) throw { kod: 429, retryAfter: +r.headers.get('Retry-After') || 30, mesaj: 'Limit' };
  if (!r.ok) throw { kod: r.status, mesaj: (await r.json().catch(() => ({}))).detail || 'Hata' };
  return r.json();
}

export const createInvite = (b) => istek('/invite-create', { method: 'POST', body: JSON.stringify(b) });
export const joinByCode = (code) => istek('/join-by-code', { method: 'POST', body: JSON.stringify({ code }) });
export const listInvites = () => istek('/list');
export const approveInvite = (id, onay) => istek('/approve', { method: 'POST', body: JSON.stringify({ id, onay }) });
export const rejectInvite = (prefix) => istek('/reject', { method: 'POST', body: JSON.stringify({ prefix }) });
