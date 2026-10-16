# Hüma: Kulüp Proje Yönetim Uygulaması Planı

Platform: **Web + Masaüstü uygulaması**

## Zaman Çizelgesi (4-5 kişi, haftada ~10 saat)

| Hafta | İş | Sorumlu | Durum |
|---|---|---|---|
| 1 | Gereksinimler, roller, Figma wireframe (geniş ekran odaklı) | | Başlanmadı |
| 2 | UI tasarımı, DB şeması, repo + Supabase kurulumu | | Başlanmadı |
| 3-4 | Auth, departman, davet kodu, rol sistemi | | Başlanmadı |
| 5-7 | Proje/görev modülü, Kanban, yorum, dosya | | Başlanmadı |
| 8 | Bildirimler, duyurular | | Başlanmadı |
| 9 | Yetki testleri, hata düzeltme | | Başlanmadı |
| 10 | Web yayını (Vercel/Netlify) | | Başlanmadı |
| 11 | Masaüstü paketleme (Windows önce, sonra macOS/Linux) + otomatik güncelleme | | Başlanmadı |
| 12 | Kulüp içi beta, geri bildirim | | Başlanmadı |

## MVP Özellikleri

| Özellik | Kategori | Sorumlu | Durum |
|---|---|---|---|
| Kayıt/giriş (e-posta + şifre, üniversite maili doğrulaması opsiyonel) | Güvenlik | | Başlanmadı |
| Departmana davet koduyla katılma (süreli/yenilenebilir kod) | Güvenlik | | Başlanmadı |
| Kritik departmanlarda lider onayı | Güvenlik | | Başlanmadı |
| Roller: Admin → Departman Lideri → Üye → Misafir | Güvenlik | | Başlanmadı |
| Departman ve proje oluşturma | Çekirdek | | Başlanmadı |
| Görev yönetimi (başlık, açıklama, sorumlu, son tarih, öncelik, durum) | Çekirdek | | Başlanmadı |
| Kanban panosu ve liste görünümü | Çekirdek | | Başlanmadı |
| Görevlere yorum ve dosya ekleme | Çekirdek | | Başlanmadı |
| Bildirimler (tarayıcı + masaüstü) | Bildirim | | Başlanmadı |
| Duyuru panosu (kulüp geneli ve departman bazlı) | İletişim | | Başlanmadı |
| Masaüstü otomatik güncelleme (Tauri/Electron updater) | Masaüstü | | Başlanmadı |

## Sonraki Sürümler

| Sürüm | Özellik | Sorumlu | Durum |
|---|---|---|---|
| Sürüm 2 | Takvim ve toplantı planlama | | Başlanmadı |
| Sürüm 2 | Gantt/zaman çizelgesi | | Başlanmadı |
| Sürüm 2 | Departmanlar arası görev talebi | | Başlanmadı |
| Sürüm 2 | Dosya/doküman kütüphanesi | | Başlanmadı |
| Sürüm 2 | Görev şablonları (ör. Test atışı hazırlığı) | | Başlanmadı |
| Sürüm 2 | Aktivite geçmişi | | Başlanmadı |
| Sürüm 2 | Çevrimdışı mod | | Başlanmadı |
| Sürüm 3 | Raporlama paneli (tamamlanma oranı, iş yükü) | | Başlanmadı |
| Sürüm 3 | Uygulama içi sohbet/kanallar | | Başlanmadı |
| Sürüm 3 | Üye profilleri ve kulüp arşivi | | Başlanmadı |
| Sürüm 3 | Karanlık mod, çoklu dil (TR/EN) | | Başlanmadı |

## Teknoloji Önerisi

| Katman | Öneri | Son karar |
|---|---|---|
| Web frontend | React + Next.js (veya Vue/Nuxt) | |
| Masaüstü paketi | Tauri (hafif) veya Electron (yaygın) | |
| Backend + DB | Supabase (Auth, PostgreSQL, Storage, Realtime, RLS) | |
| UI kütüphanesi | Tailwind + shadcn/ui | |
| Bildirim | Web push + masaüstü yerel bildirimi | |
| Tasarım | Figma | |
| Versiyon kontrol | GitHub (ayrı branch + PR akışı) | |
| Hosting | Vercel/Netlify (ücretsiz katman) | |

## Veri Modeli (özet)

| Tablo | Alanlar |
|---|---|
| users | id, ad, e-posta |
| departments | id, ad, davet_kodu, onay_gerekli |
| memberships | user_id, department_id, rol |
| projects | id, department_id, ad, açıklama |
| tasks | id, project_id, parent_task_id, başlık, durum, öncelik, sorumlu_id, son_tarih |
| comments / attachments / notifications / announcements | Detaylar şema aşamasında netleşecek |

## Roller, Riskler, Açık Sorular

| Tür | Konu | Not / Karar |
|---|---|---|
| Risk | Kapsam şişmesi | Önce sadece MVP bitsin |
| Risk | Yetki açıkları | Başka departman verisine erişim için ayrı test yapın (RLS) |
| Risk | Kullanım / benimseme | Önce tek departmanla (ör. Bozok) pilot |
| Risk | Devamlılık | Dokümantasyon ve kod standardı baştan olsun |
| Açık soru | Departman liderini ve davet kodlarını kim yönetecek? | |
| Açık soru | Kulüp başkanı her departmanı görebilsin mi? | |
| Açık soru | Hosting/veritabanı maliyetini kim karşılayacak? | |
