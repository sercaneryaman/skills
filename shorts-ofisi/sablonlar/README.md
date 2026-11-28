# Şablonlar (tekrar kullanılabilir betikler)

Bitmiş videolar silindi (2026-11-28); bu klasör yeni videolar için gereken kodu tutar. Ses profili `../ses/` içindedir.

- `ses/`: seslendirme zinciri. `vox_lines2.py` (VoxCPM2 referans modu, satır başına aday), `vox_lines3.py` (zor kelimeler için eşin kaydından başlatma), `trim_prompt.py` (başlatma kaydının kuyruğunu keser), `prep_voice.py` (Whisper + benzerlikle en iyi adayı seçer, duraklama ekler), `pace_one.py` (tek satırı elle seçip hızlandırmadan duraklatır), `assemble_tr.py` (satırları dizer, kelime zamanları, altyazı parçaları). Çalıştırma: `/opt/voxenv/bin/python <betik>`. Betiklerdeki `P`/`B` yolunu yeni proje klasörüne çevir.
- `hyperframes-kagit/`: kâğıt kesik stop-motion stili (ananaslı jöle videosu). `build.py` HTML+GSAP kompozisyonu üretir, `audio.py` ukulele + SFX.
- `hyperframes-belgesel/`: gece mavisi belgesel stili, EKG monitörü, Bentley kar kristalleri, yarı saydam hayvan çizimi (kurbağa videosu).
- `lemo-karatahta/`: Lemo-Opuscar Kara Tahta motoru, dikey 9:16 ve Türkçe altyazı uyarlaması (gökyüzü videosu). `js/film.js` sahneyi tanımlar; `build.sh` ses → zamanlama → olaylar → miks → render. Fontlar (EMS SVG, Nunito Sans) ve tebeşir sesleri (Openverse CC0) build öncesi yeniden indirilir.
