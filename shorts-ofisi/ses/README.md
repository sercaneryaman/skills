# Seslendirme sesi (varsayılan)

Bütün Shorts videoları Türkçe ve eşin kopyalanmış sesiyle seslendirilir (onay: 26 Kasım 2026, bölüm 01 kaydı).

- Ses örnekleri (12 sn, temizlenmiş): `ses/ref/{notr,belgesel,gizem,masal,heyecan,haber,samimi,komik,duygu,serbest}.wav`. Herkese açık depoya konmaz; yedek `ses_profili.zip` kullanıcıda. Yeni oturumda zip yüklenir ve `ses/ref/` altına açılır.
- Üretim: `python3 tts_tr.py <proje_klasörü> ses/ref/<ton>.wav` — `lines.json` içindeki her satır için 3 aday üretir, Whisper eşleşmesine göre seçer (`picks.json`). Satıra özel ton için satıra `"ref": "ses/ref/heyecan.wav"` eklenir.
- Model (varsayılan, 2026-11-26): VoxCPM2 (Apache-2.0, 48 kHz), "tam kopya" modu: `prompt_wav_path` + `prompt_text` + `reference_wav_path` = `ref2/samimi_tam.wav` (bölüm 10'un ilk 8,8 sn'si; metin: "Bak sana bir şey söyleyeceğim. Ekmeği buzdolabına koyuyorsan, aslında onu daha hızlı bayatlatıyorsun. Evet, ben de ilk duyduğumda şaşırmıştım."). Çıktının başındaki referans kuyruğu Whisper ile kesilir. Kurulum: `python3 -m uv venv --system-site-packages voxenv && python3 -m uv pip install --python voxenv/bin/python "voxcpm>=2.0.3"`. CPU'da ~4 sn hesap / 1 sn ses.
- Yedek model: Chatterbox Multilingual (`language_id='tr'`); kullanıcı robotik buldu.
- YouTube'da her videoda "altered or synthetic content" beyanı işaretlenir.
