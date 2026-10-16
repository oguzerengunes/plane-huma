import { useState, useEffect } from 'react';
import { joinByCode } from './api';

export default function JoinByCode() {
  const [code, setCode] = useState('');
  const [durum, setDurum] = useState(null);
  const [mesaj, setMesaj] = useState('');
  const [bekleme, setBekleme] = useState(0);

  useEffect(() => {
    if (!bekleme) return;
    const t = setTimeout(() => setBekleme(bekleme - 1), 1000);
    return () => clearTimeout(t);
  }, [bekleme]);

  const formatla = (v) => {
    let s = v.toUpperCase().replace(/[^A-Z0-9]/g, '').replace(/^HUMA/, '');
    s = s.slice(0, 4);
    return s ? `HUMA-${s}` : 'HUMA-';
  };

  const katil = async () => {
    try {
      const r = await joinByCode(code);
      if (r.status === 'joined') window.location.href = '/workspace';
      else { setDurum('pending'); setMesaj('Onay bekleniyor'); }
    } catch (e) {
      setDurum('hata');
      if (e.kod === 429) { setBekleme(e.retryAfter || 30); setMesaj('Çok deneme'); }
      else setMesaj(e.mesaj || 'Geçersiz kod');
    }
  };

  if (durum === 'pending') return <div>⏳ {mesaj}</div>;
  return (
    <div>
      <input value={code} onChange={(e) => setCode(formatla(e.target.value))}
        onPaste={(e) => { e.preventDefault(); setCode(formatla(e.clipboardData.getData('text'))); }}
        placeholder="HUMA-XXXX" maxLength={9} />
      <button onClick={katil} disabled={bekleme > 0 || code.length < 9}>
        {bekleme > 0 ? `${bekleme}sn bekle` : 'Katıl'}</button>
      {durum === 'hata' && <p>{mesaj}</p>}
    </div>
  );
}
