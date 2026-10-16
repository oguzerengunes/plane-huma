import { useState } from 'react';
import { createInvite, approveInvite, rejectInvite } from './api';

export default function InviteCodePanel({ kodlar, yenile }) {
  const [modal, setModal] = useState(false);
  const [yeniKod, setYeniKod] = useState(null);
  const [onayli, setOnayli] = useState(false);
  const bekleyen = kodlar.filter((k) => k.pending > 0).length;

  const olustur = async () => {
    const r = await createInvite({ expiryDays: 7, maxUses: 50, requireApproval: onayli });
    setYeniKod(r.plaintext); yenile();
  };

  return (
    <div>
      <button onClick={() => { setModal(true); setYeniKod(null); }}>+ Yeni Kod</button>
      {bekleyen > 0 && <span>⏳ {bekleyen} onay bekliyor</span>}
      <table><tbody>
        {kodlar.map((k) => (
          <tr key={k.prefix}>
            <td>{k.prefix}</td><td>{k.olusturan}</td><td>{k.expiry}</td>
            <td>{k.kullanim}/50</td><td>{k.onay ? 'Onaylı' : 'Direkt'}</td>
            <td>
              <button onClick={() => navigator.clipboard.writeText(k.prefix)}>Kopyala</button>
              <button onClick={() => rejectInvite(k.prefix)}>İptal</button>
              {k.pending > 0 && (<>
                <button onClick={() => approveInvite(k.id, true)}>Onayla</button>
                <button onClick={() => approveInvite(k.id, false)}>Reddet</button>
              </>)}
            </td>
          </tr>
        ))}
      </tbody></table>
      {modal && (
        <div>
          <label><input type="checkbox" checked={onayli} onChange={(e) => setOnayli(e.target.checked)} /> Onay gerekli</label>
          <button onClick={olustur}>Oluştur (7 gün / 50)</button>
          {yeniKod && <p>⚠️ Bir kez: <b>{yeniKod}</b></p>}
          <button onClick={() => setModal(false)}>Kapat</button>
        </div>
      )}
    </div>
  );
}
