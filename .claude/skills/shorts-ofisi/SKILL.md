---
name: shorts-ofisi
description: YouTube Shorts fikir ofisini toplar - trend analisti, kategori uzmanları (tarih, bilim, sanat, çocuk, doğa, teknoloji), eleştirmen, doğrulayıcı ve yönetici ile veriye dayalı, kategorilere ayrılmış, tartışılmış ve doğrulanmış Shorts fikir panosu üretir. Kullanıcı yeni Shorts fikri, video konusu, "ofis toplansın", "fikir toplantısı" istediğinde veya yeni bir Shorts videosuna başlamadan önce kullan.
---

# Shorts Ofisi toplantısı

Alt ajanlar başka alt ajan çağıramaz; toplantıyı ana oturum yönetir. Ajan tanımları `~/.claude/agents/` altında: `trend-analisti`, `uzman-tarih`, `uzman-bilim`, `uzman-sanat`, `uzman-cocuk`, `uzman-doga`, `uzman-teknoloji`, `ofis-elestirmen`, `ofis-dogrulayici`, `ofis-yonetici`.

## Kurulum
- Toplantı klasörü: `$OFIS/<YYYY-MM-DD>/` (`OFIS` varsayılanı `/home/user/shorts-ofisi`). Alt klasörler: `analiz/ fikirler/ elestiri/ dogrulama/ pano/`.
- Kullanıcı kategori belirtmediyse altı kategorinin hepsi. Kategori anahtarları: tarih, bilim, sanat, cocuk, doga, teknoloji.
- Önceki toplantıların `pano/` dosyalarını her uzmana "zaten üretilmiş/önerilmiş fikirler" olarak ver; tekrar önerilmesin.
- YouTube Data API kontrolü: `curl -s -o /dev/null -w '%{http_code}' "https://www.googleapis.com/youtube/v3/videos?part=id&id=dQw4w9WgXcQ"`. 200 değilse analistlere "API yok, web kaynaklarıyla çalış ve bunu etiketle" de; kullanıcıya da söyle.

## Akış (her adımda kategoriler birbirinden ayrı)
1. **Analiz** - her kategori için bir `trend-analisti` çağrısı (paralel). Çıktı `analiz/<kategori>.md`.
2. **Fikir turu** - her kategori kendi uzmanına (paralel). Çıktı `fikirler/<kategori>.md`.
3. **Eleştiri** - her kategori için ayrı bir `ofis-elestirmen` çağrısı (paralel). Çıktı `elestiri/<kategori>.md`.
4. **Tartışma turu** - aynı kategori uzmanı eleştirilere yanıt verir, fikirleri düzeltir veya geri çeker. Çıktı `fikirler/<kategori>-revize.md`.
5. **Kısa liste** - her kategoriden eleştirmen puanı en yüksek 4 fikir (ZAYIF olanlar hariç).
6. **Doğrulama** - her kategori için bir `ofis-dogrulayici` çağrısı, sadece kısa liste. Çıktı `dogrulama/<kategori>.md`.
7. **Karar** - tek bir `ofis-yonetici` çağrısı tüm dosyaları okur, `pano/<kategori>.md` ve `pano/OZET.md` yazar.

Her ajan çağrısında ona toplantı klasörünün tam yolunu, kategorisini ve okuması/yazması gereken dosyaları ver. Bir ajan dosyasını yazmadıysa o adımı tekrar etme; kullanıcıya hangi adımın eksik kaldığını söyle.

## Güvenilirlik kuralları
- Hiçbir ajan sayı veya kaynak uydurmaz. "Çok izlenir" iddiası kanıt etiketi (DOĞRULANDI / KAYNAKLI / VARSAYIM) taşır.
- Doğrulayıcının YANLIŞ dediği fikir üretilmez.
- Panoyu kullanıcıya sunarken kanıtın hangi kaynaktan geldiğini (API mi, web mi) ve tarihini söyle.

## Sonuç
Kullanıcıya `pano/OZET.md` içeriğini kısa sun: kategori başına en iyi 3 fikir, puan ve tek cümle gerekçe. Video üretimi için seçilen fikir, üretim adımında bu panodaki akış ve olgularla başlar.
