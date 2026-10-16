# Pilot Geri Bildirim + Rollout Kararı

## Form (Bozok, 2 hafta)

1. Günlük işin ne kadar hızlandı? (1-5) Neden?
2. En çok takıldığın ekran/adım hangisi?
3. Veri kaybı/eksik senkron yaşadın mı?
4. Gizlilik sızıntı şüphesi gördün mü?
5. Tüm ekibe açılsın mı? (Evet/Hayır + şartın)

## Karar

| Renk | Kriter | Aksiyon |
|---|---|---|
| YEŞİL | crash=0, senkron ≥%99, sızıntı PASS, memnuniyet ≥4/5 | Tam rollout |
| SARI | crash ≤2/gün, %95-99, minör bug, 3-4/5 | 1 hafta uzat |
| KIRMIZI | veri kaybı ≥1, sızıntı FAIL, crash>2, <3/5 | Rollback, durdur |

## Karar logu

Tarih: / Veren: / Kapsam: / Metrikler: crash=X senkron=%Y memnuniyet=A/5 / Sızıntı: PASS/FAIL + kanıt / Bug: H-xxx / Karar: YEŞİL/SARI/KIRMIZI / Neden (2 cümle): / Sonraki adım+tarih:
