# Pano: Teknoloji ve Gelecek (2026-11-25)

## Okumadan önce
- **Kanıt durumu:** Analiz yalnızca web aramasına dayanıyor (7 arama, sayfalar açılamadı, yalnızca özetler). YouTube Data API verisi yok (403). Video tablosu ve aykırı başarı listesi üretilemedi; Türkçe teknoloji Shorts örneği bulunamadı (analiz/teknoloji.md satır 5, 13, 29, 39). Tubefilter'ın "makine görseli kayrılıyor" bulgusu sessiz "oddly satisfying" videolar içindir; anlatımlı "nasıl çalışır" Shorts'a aktarılamaz (satır 9, 47). Bu panodaki hiçbir fikir "çok izlenir" diye sunulmuyor. ÜRET kararı, "test videosu olarak üret" anlamına gelir.
- **Puanlama:** Her ölçüt 1-5. Toplam = (Kanca + Shorts + 2×Kanıt + 2×Doğruluk + Üretilebilirlik + Politika) / 8.
- **Kanıt puanı:** 1 = kanıt yok. 2 = tek, zayıf, dolaylı sinyal.
- **Doğruluk puanı:** DOĞRU = 5. KISMEN DOĞRU (düzeltmeler uygulandı) = 4. EFSANE (efsane çerçevesiyle) = 3. DOĞRULANAMADI veya doğrulayıcıdan geçmedi = 2. YANLIŞ = panoya girmez.
- **Karar kuralı:** ÜRET = doğrulayıcıdan geçti ve toplam ≥ 3,00. YEDEK = doğrulanmadı / DOĞRULANAMADI ya da toplam < 3,00. RED = YANLIŞ ya da toplam < 2,50.
- **Ortak şartlar:** İlk seride insan sesi. Her videoda kanıtlanabilir özgün katkı (kendi çekim, canlı deney, kendi çizim/model). Akış iskeleti videodan videoya değişir. Görseller açıkça animasyon/diyagram; gerçekçi sahte yıldırım ya da sahte tarihî fotoğraf yok. "Çocuklar için yapılmamıştır". İlk test partisi ölçülmeden seri kurulmaz.

---

## 1. QR kodu karalasan bile neden okunur? — ÜRET

- **Kanca:** Konuşmadan önce, en yüksek (H) seviyede üretilmiş bir QR kod karalanır ve telefon onu okur. Ses: "Bunu nasıl okudu?"
- **45 sn akış:**
  1. (0-6) Kanca; gerçek telefon kamerası çekimi.
  2. (6-16) Izgara: siyah ve beyaz hücreler veriyi taşır; köşelerdeki üç büyük kare konum işaretidir.
  3. (16-28) Veriyle birlikte fazlalık da saklanır: Reed-Solomon hata düzeltme. "Bu kod en yüksek seviyede, H'de üretildi. Bu seviyede kod sözcüklerinin yaklaşık yüzde 30'u kurtarılabilir." (L ve M yüzdeleri söylenmez. "Yüzde 30'unu karala" denmez.)
  4. (28-38) Oran alanın değil, kod sözcüklerinin oranı. Konum karelerine zarar gelince okuma çok zorlaşır (deneyde gösterilir). Ortaya logo konabilmesinin nedeni bu.
  5. (38-45) Kapanış: karalanmış kod tekrar okunur; açılışa dönüş.
- **Görsel stil:** Gerçek telefon çekimi, ekran kaydı, kısa diyagram. Ekrandaki QR kod yalnızca kendi zararsız sayfamıza gider. Quishing konusu yok.

| Kanca | Shorts | Kanıt (×2) | Doğruluk (×2) | Üretilebilirlik | Politika | Toplam |
|---|---|---|---|---|---|---|
| 5 | 5 | 1 | 4 (KISMEN DOĞRU) | 5 | 5 | **3,75** |

- **Kanıt bağlantıları:** Kanıt yok. "İnsan sesi/özgün kurgu" fırsatı yalnızca kaynaklı bir genel eğilim; kategoriye uygulanışı varsayım (analiz/teknoloji.md satır 12). Olgular: [Britannica, QR code](https://www.britannica.com/technology/QR-code), [Keyence](https://www.keyence.com/ss/products/auto_id/barcode_lecture/basic_2d/qr/), [Aspose belgeleri](https://reference.aspose.com/barcode/aspose.barcode.generation/qrerrorlevel), [Seagull Scientific](https://help.seagullscientific.com/10.1/en/Content/ErrorCorrection_QRCode.html), [Xenospectrum](https://xenospectrum.com/en/qr-code-error-correction-reed-solomon/), [Make Tech Easier](https://maketecheasier.com/how-qr-codes-survive-damage/). ISO/IEC 18004 ve qrcode.com okunmadığı için atıf olarak yazılmaz.
- **Şart:** Canlı deney çalışmazsa video çıkmaz.
- **Karar: ÜRET.** Gerekçe: Kategorinin en yüksek puanı; canlı deney hem vaadi kanıtlıyor hem şablon riskini en çok düşürüyor.

---

## 2. Uçağa yıldırım düşünce içeride kimse neden çarpılmaz? — ÜRET

- **Kanca:** "Ortalama bir ticari uçağa yılda yaklaşık bir kez yıldırım düşer. İçeridekiler neden çarpılmaz?"
- **45 sn akış:**
  1. (0-6) Kanca; animasyon uçak, burundan giren ışık.
  2. (6-18) Metal gövde bir Faraday kafesi gibi davranır: akım dış yüzeyde kalır, içeri geçmez. Tek cümle: "Lastikler korumaz."
  3. (18-28) Kompozit gövdelerde iletken bir metal katman aynı işi görür. (Genel ifade; FAA AC 20-136 atfı yanlış olduğu için kullanılmaz.)
  4. (28-36) Uçak, yüklü bulutlara girince kendi yıldırımını tetikleyebilir. ("Çoğu zaman" denmez.)
  5. (36-45) Kapanış: uçak zarar görebilir (yüzeyde yanık, anten/sensör hasarı) ve inişte kontrol edilir; modern uçaklar bu yüzden korunur. Akım çizgisi başa döner.
- **Görsel stil:** 3D uçak modeli, akım yolu animasyonu, diyagram. Gerçek yıldırım videosu yok. Tarihî kaza ayrıntısı yok (tek fikir ve kaygı yaratmayan çerçeve için).

| Kanca | Shorts | Kanıt (×2) | Doğruluk (×2) | Üretilebilirlik | Politika | Toplam |
|---|---|---|---|---|---|---|
| 4 | 5 | 1 | 4 (KISMEN DOĞRU) | 4 | 4 | **3,38** |

- **Kanıt bağlantıları:** Kanıt yok; Tubefilter makine eğilimi bu formata aktarılamaz (analiz/teknoloji.md satır 47). Olgular: [Live Science, FAA tahmini](https://www.livescience.com/32638-do-planes-get-struck-by-lightning.html), [Hong Kong Gözlemevi](https://www.hko.gov.hk/en/education/weather/thunderstorm-and-lightning/00732-The-Aerial-Battle-Aircraft-vs-Thunder-God.html), [Flying Magazine](https://flyingmag.com/ask-flying/how-can-an-aircraft-get-struck-by-lightning-without-a-close-thunderstorm), [Scientific American](https://www.scientificamerican.com/article/what-happens-when-lightni/), [Popular Science](https://www.popsci.com/breakdown/article/2008-06/electric-aviation-experience), [USC Illumin](https://illumin.usc.edu/shocking-how-airplanes-defend-against-lightning/), [NBC News](https://www.nbcnews.com/news/amp/wbna31045261), [Flight Safety Foundation](https://flightsafety.org/wp-content/uploads/2016/11/asw_jun10_p18-23.pdf).
- **Şart:** Kompozit katman için yayından önce kurumsal (FAA/Boeing) bir kaynak bulunur; bulunamazsa genel ifade kalır.
- **Karar: ÜRET.** Gerekçe: Net bir soru, doğrulanmış Faraday kafesi açıklaması ve kendi 3D akım animasyonuyla ayırt edici görsel.

---

## 3. Bilgisayarın delikli kart fikri bir dokuma tezgâhından geldi — ÜRET

- **Kanca:** "Bilgisayarın delikli kart fikri bir dokuma tezgâhından geldi. Kart değişince kumaşın deseni değişiyordu." ("İlk yazılım kumaşa yazıldı" başlığı YANLIŞ bulunduğu için kaldırıldı; "ilk" iddiası yok.)
- **45 sn akış:**
  1. (0-6) Kanca; kara kalem delikli kart.
  2. (6-20) 1800'lerin başı: Jacquard tezgâhı. Delik varsa ilgili iplik kalkar, yoksa kalkmaz. Kart değişir, desen değişir. Tek cümle öncüler: Bouchon'un delikli kâğıt şeridi ve Falcon'un kart zinciri, 1700'lerin ilk yarısında. (Yıl verilmez.)
  3. (20-34) Babbage'ın Analitik Makine'de bu kartlardan esinlendiği kabul edilir (tarih verilmez). Ada Lovelace 1843'te yazdı: "Analitik Makine, Jacquard tezgâhının çiçek ve yaprak dokuması gibi cebirsel desenler dokur." (Çeviri, özgün Note A metniyle birebir karşılaştırılır.)
  4. (34-45) Kapanış: kart deliği ekranda piksel ışığına dönüşür.
- **Görsel stil:** Yetişkin tonunda kara kalem animasyon, kendi çizim. Müze fotoğrafı yok; Lovelace portresi yalnızca lisansı teyitli kamu malı kaynaktan.

| Kanca | Shorts | Kanıt (×2) | Doğruluk (×2) | Üretilebilirlik | Politika | Toplam |
|---|---|---|---|---|---|---|
| 3 | 4 | 1 | 4 (KISMEN DOĞRU) | 4 | 5 | **3,25** |

- **Kanıt bağlantıları:** Kanıt yok; kara kalem stilinin etkisi varsayım. Olgular: [Britannica, Jacquard](https://www.britannica.com/biography/Joseph-Marie-Jacquard), [Computer History Museum](https://www.computerhistory.org/storageengine/punched-cards-control-jacquard-loom/), [Columbia](https://www1.columbia.edu/cu/computinghistory/jacquard.html), [Wikipedia, Basile Bouchon](https://wikipedia.com/wiki/Basile_Bouchon), [IEEE Spectrum](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution), [IEEE Computer Society](https://history.computer.org/pioneers/jacquard.html), [Yale, Lovelace notları](https://www.cs.yale.edu/homes/tap/Files/ada-lovelace-notes.html), [Science History Institute](https://www.sciencehistory.org/stories/magazine/the-french-connection/).
- **Karar: ÜRET.** Gerekçe: Az doymuş, doğrulanmış bir köken hikâyesi; düzeltilmiş kanca daha az çarpıcı olduğu için puan orta.

---

## 4. Kıtalar arası internet bu kalınlıktaki kablodan geçer — YEDEK

- **Kanca:** "Kıtalar arası internetin neredeyse tamamı bu kalınlıktaki kablolardan geçiyor. Uydudan değil."
- **45 sn akış:**
  1. (0-6) Kanca; elde derin deniz kablosu kesiti (yaklaşık 2 cm).
  2. (6-18) 3D kesit: ortada cam lifler, çevresinde yalıtım ve çelik tel. Bu incelik yalnız derin denizde; kıyıya yakın zırhlı kablo yaklaşık 5 cm.
  3. (18-32) Kendi çizdiğimiz harita: Türkiye'ye bağlanan kablolar. Her kablo adı ve iniş noktası submarinecablemap.com üzerinde elle teyit edilmeden söylenmez.
  4. (32-45) Kapanış: kesit tekrar elde. "Uydu değil. Bu."
- **Görsel stil:** Kendi çizim harita + 3D kesit. TeleGeography haritası kaydedilmez. Jeopolitik sabotaj konusu yok.

| Kanca | Shorts | Kanıt (×2) | Doğruluk (×2) | Üretilebilirlik | Politika | Toplam |
|---|---|---|---|---|---|---|
| 4 | 5 | 1 | 2 (DOĞRULANAMADI) | 4 | 4 | **2,88** |

- **Kanıt bağlantıları:** Kanıt yok; makine görseli eğilimi dayanak olarak kullanılmıyor. Başlık olgusu DOĞRU: [TeleGeography mythbusting](https://resources.telegeography.com/2023-mythbusting-part-3), [Ciena](https://www.ciena.com/insights/articles/Telecommunications-in-the-Harshest-Environment-on-Earth.html). Türkiye bölümü DOĞRULANAMADI: kısmi, ikincil kaynaklar [Middle East Eye](https://www.middleeasteye.net/news/underwater-cables-internet-middle-east), [BTK raporu](https://www.btk.gov.tr/uploads/announcements/denizalti-kablolarinin-dunya-haberlesmesindeki-onemi-arastirma-raporu-yayimlandi/denizalti-kablolarinin-dunya-haberlesmesindeki-onemi-v4.pdf).
- **Karar: YEDEK.** Gerekçe: Doğrulayıcının genel sonucu DOĞRULANAMADI olduğu için en fazla yedek; videonun farkını yaratan Türkiye kablo listesi haritadan teyit edilince yeniden değerlendirilir.

---

## 5. GPS saatleri düzeltilmezse konum kayardı — YEDEK

- **Kanca:** İlk karede haritadaki mavi nokta kayıyor. Ses: "Bu düzeltme olmadan GPS günler içinde işe yaramaz hâle gelirdi."
- **45 sn akış:**
  1. (0-6) Kanca; harita, mavi nokta.
  2. (6-14) GPS konumu sinyalin zamanından hesaplar; saat hatası, mesafe hatası demek.
  3. (14-26) Hız uydu saatini yavaşlatır (yaklaşık 7 µs/gün); zayıf yerçekimi hızlandırır (yaklaşık 45 µs/gün).
  4. (26-38) Net fark yaklaşık 38 µs/gün; ışık bu sürede yaklaşık 11 km yol alır. ("Konum 10 km kayar" denmez.)
  5. (38-45) Uydu saatleri bu yüzden önceden ayarlıdır; mavi nokta yerine oturur.
- **Görsel stil:** 3D Dünya, uydu ve saatler; diyagram.

| Kanca | Shorts | Kanıt (×2) | Doğruluk (×2) | Üretilebilirlik | Politika | Toplam |
|---|---|---|---|---|---|---|
| 4 | 4 | 1 | 2 (doğrulayıcıdan geçmedi) | 4 | 5 | **2,88** |

- **Kanıt bağlantıları:** Kanıt yok. Ashby 2003 (Living Reviews in Relativity) uzmanın kaynağı; doğrulayıcıdan geçmedi.
- **Uzman-eleştirmen ayrılığı:** Eleştirmen konuyu İngilizcede yüksek doygunlukta saydı; uzman Türkçede ölçülmediğini söyleyerek kısmen savundu. **Karar:** Doygunluk yüksek kabul edilir; Türkçe olmak tek başına fark sayılmaz.
- **Karar: YEDEK.** Gerekçe: Gerçek fizik ama doymuş bir konu ve sayılar doğrulayıcıdan geçmedi; ikinci partiye bırakıldı.

---

## Panoya alınmayanlar
- **Yapay zekâ ve token:** Uzman geri çekti (doymuş, "strawberry" örneği eskidi, politika riski en yüksek biçim).
- **İnternetin ilk mesajı "LO":** Uzman geri çekti (çok doymuş anekdot, 45 sn'yi dolduracak tek fikir yok).
- **Mikrodalga ve çikolata:** Uzman geri çekti (cevapsız kanca, iki fikir, fizik tuzakları).
