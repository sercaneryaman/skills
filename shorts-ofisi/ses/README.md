# Seslendirme sesi (varsayılan)

Bütün Shorts videoları Türkçe ve eşin kopyalanmış sesiyle seslendirilir (onay: 26 Kasım 2026, bölüm 01 kaydı).

- Ses örnekleri (12 sn, temizlenmiş): `ses/ref/{notr,belgesel,gizem,masal,heyecan,haber,samimi,komik,duygu,serbest}.wav`. Herkese açık depoya konmaz; yedek `ses_profili.zip` kullanıcıda. Yeni oturumda zip yüklenir ve `ses/ref/` altına açılır.
- Üretim: `python3 tts_tr.py <proje_klasörü> ses/ref/<ton>.wav` — `lines.json` içindeki her satır için 3 aday üretir, Whisper eşleşmesine göre seçer (`picks.json`). Satıra özel ton için satıra `"ref": "ses/ref/heyecan.wav"` eklenir.
- Model: Chatterbox Multilingual (`language_id='tr'`). İlk denemede konuşmacı benzerliği 0,92-0,95 (gerçek kayıt 0,95).
- YouTube'da her videoda "altered or synthetic content" beyanı işaretlenir.
