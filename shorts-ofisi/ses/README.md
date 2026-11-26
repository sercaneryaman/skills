# Seslendirme sesi (varsayılan)

Bütün Shorts videoları Türkçe ve eşin kopyalanmış sesiyle seslendirilir (onay: 26 Kasım 2026, bölüm 01 kaydı).

- Ses örnekleri (12 sn, temizlenmiş): `ses/ref/{notr,belgesel,gizem,masal,heyecan,haber,samimi,komik,duygu,serbest}.wav`. Herkese açık depoya konmaz; yedek `ses_profili.zip` kullanıcıda. Yeni oturumda zip yüklenir ve `ses/ref/` altına açılır.
- Üretim: `python3 tts_tr.py <proje_klasörü> ses/ref/<ton>.wav` — `lines.json` içindeki her satır için 3 aday üretir, Whisper eşleşmesine göre seçer (`picks.json`). Satıra özel ton için satıra `"ref": "ses/ref/heyecan.wav"` eklenir.
- Model (varsayılan, 2026-11-26): VoxCPM2 (Apache-2.0, 48 kHz), yalnız referans modu: `reference_wav_path=vc_hedef.wav` (bölüm 10'un ilk 13 sn'si + bölüm 2'nin ilk 10,2 sn'si, temizlenmiş, 23 sn), `cfg_value=2.0`, `inference_timesteps=12`, satır başına 3 aday; benzerlik ve Whisper doğruluğuna göre seç. Bu ayar konuşmacı benzerliğini 0,955-0,96'ya çıkardı (gerçek kayıt 0,954); "tam kopya" (prompt+metin) modu 0,84-0,90'da kaldı. Kurulum: `python3 -m uv venv --system-site-packages voxenv && python3 -m uv pip install --python voxenv/bin/python "voxcpm>=2.0.3"`. CPU'da ~4 sn hesap / 1 sn ses.
- Yedek model: Chatterbox Multilingual (`language_id='tr'`); kullanıcı robotik buldu.
- YouTube'da her videoda "altered or synthetic content" beyanı işaretlenir.
- Hız (kullanıcı tercihi): cümle sonlarına 0,45 sn, virgüllere 0,18 sn sessizlik eklenir, ardından `atempo=0.9`. Ham VoxCPM2 hızı kullanıcıya hızlı geldi.
