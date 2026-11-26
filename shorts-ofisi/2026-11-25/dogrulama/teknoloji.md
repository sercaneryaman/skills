# Doğrulama: teknoloji (2026-11-25), ikinci geçiş

Kapsam: kısa liste, Fikir 4, 1, 3, 7. Girdi: fikirler/teknoloji-revize.md.

SINIRLAR: Kaynaklar arama sonuçlarından (başlık, URL, özet) alındı. qrcode.com, cs.yale.edu, resources.telegeography.com ve submarinecablemap.com sayfa metni ağdan okunamadı. "Çift kaynak" ifadesi iki ayrı sonuçta göründüğü anlamına gelir. Birincil sayfası okunmayanlar işaretli; üretimden önce okunmalı.

---

## Fikir 4: QR kodu karalasan bile neden okunur? — GENEL: KISMEN DOĞRU (ifade biçimi gerekli)

| Olgu | Sonuç | Not / kaynak |
|---|---|---|
| QR kodu 1994'te Denso Wave tarafından icat edildi | DOĞRU | Britannica: https://www.britannica.com/technology/QR-code ; Wikipedia yansıması (2D Key): https://en.wikipedia.com/wiki/2D_Key |
| Seviyeler L, M, Q, H = yaklaşık %7, 15, 25, 30 | DOĞRU (bir çelişki notuyla) | Keyence: https://www.keyence.com/ss/products/auto_id/barcode_lecture/basic_2d/qr/ ; Aspose belgeleri: https://reference.aspose.com/barcode/aspose.barcode.generation/qrerrorlevel ; Seagull: https://help.seagullscientific.com/10.1/en/Content/ErrorCorrection_QRCode.html . Bir patent L/M için farklı (15/20) değer verir; H ve Q üzerinde herkes hemfikir. Videoda yalnız H (%30) kullanılıyor, bu yüzden risk yok. L/M sayısı söylenecekse Denso Wave belirtimi okunmalı. |
| Düzeltme Reed-Solomon ile yapılır | DOĞRU | Keyence; Seagull; https://xenospectrum.com/en/qr-code-error-correction-reed-solomon/ |
| %30 kod sözcüklerinin oranıdır, alan oranı değil; hasarın miktarı ve dağılımı belirleyici | DOĞRU | Denso tanımı (arama özetlerinde iki kez aynı ifade); https://maketecheasier.com/how-qr-codes-survive-damage/ (ikincil: hasar birkaç bloğa dağılabilir). |
| Konum/zamanlama desenlerine zarar gelirse kod, görünür alanın üçte biri örtülmeden okunmaz hâle gelebilir | KISMEN DOĞRU | Aynı ikincil kaynak. Standart metni okunmadı. "Hiç okunmaz" yerine "okunması çok zorlaşır" de. Canlı denemede zaten test edilir. |
| ISO/IEC 18004 ve qrcode.com kaynak gösterimi | DOĞRULANAMADI | İkisine de erişilemedi; kaynak olarak yazmadan önce teyit edin. |

Düzeltme: "%30'u karala" demeyin. "En yüksek (H) seviyede, kod sözcüklerinin yaklaşık %30'u, uygun yerde" deyin. Karalama deneyi gerçek kamerayla denenmeli.

---

## Fikir 1: Kıtalar arası internet bu kalınlıktaki kablodan geçer — GENEL: DOĞRULANAMADI (Türkiye bölümü); başlık olgusu DOĞRU

| Olgu | Sonuç | Not / kaynak |
|---|---|---|
| Kıtalar arası trafiğin ezici çoğunluğu (>%99) deniz altı kablosundan geçer | DOĞRU | TeleGeography mythbusting: iddia doğru, ama uydu verisi olmadan kesin hesap yapılamaz: https://resources.telegeography.com/2023-mythbusting-part-3 ; ICPC girdisi: https://www.wikipedia.org/wiki/International_Cable_Protection_Committee . "Neredeyse tamamı" doğru söz. |
| Derin deniz kablosu bahçe hortumu kalınlığında | DOĞRU (derin deniz için) | Ciena (ICPC'ye dayanır), derin suda yaklaşık 20 mm: https://www.ciena.com/insights/articles/Telecommunications-in-the-Harshest-Environment-on-Earth.html ; Make Tech Easier 17-20 mm: https://www.maketecheasier.com/mte-q-how-does-a-fibre-optic-cable-no-thicker-than-a-garden-hose-carry-roughly-99-per-cent-of-intercontinental-internet-traffic-across-13-000-kilometres-of-ocean-floor/ ; TeleGeography de "bahçe hortumu genişliği" der. |
| Kıyıda kablo daha kalın zırhlı (yaklaşık 50 mm) | DOĞRU | Ciena (yukarıda). |
| Türkiye'ye bağlanan kablolar ve iniş noktaları | DOĞRULANAMADI | Kısmi, ikincil: EMOS-1 (Yunanistan-İsrail-Türkiye-İtalya), MedNautilus (İstanbul dahil), SEA-ME-WE 5 (Marmaris), KAFOS (İğneada/İstanbul), Turcyos-1/2 (Kuzey Kıbrıs, Girne-Mersin) — Wikipedia kablo listesi, Middle East Eye ( https://www.middleeasteye.net/news/underwater-cables-internet-middle-east ), BTK raporu ( https://www.btk.gov.tr/uploads/announcements/denizalti-kablolarinin-dunya-haberlesmesindeki-onemi-arastirma-raporu-yayimlandi/denizalti-kablolarinin-dunya-haberlesmesindeki-onemi-v4.pdf ). Tam liste TeleGeography haritasından çıkarılamadı. Videoya girecek her kablo adı/iniş noktası https://www.submarinecablemap.com üzerinde ülke filtresiyle elle teyit edilmeli. TURMEOS-1 yurt içi (İzmir-İstanbul), "kıtalar arası" kapsamına girmez. |

Düzeltme: "Hortum kalınlığı" yalnız derin deniz kesiti için söylensin; kıyıda ~50 mm. Türkiye bölümü haritadan teyit edilene kadar ad söylenmesin.

---

## Fikir 3: Bilgisayarın ilk yazılımı kumaşa yazılmıştı — GENEL: KISMEN DOĞRU (başlık/kanca yeniden yazılmalı)

| Olgu | Sonuç | Not / kaynak |
|---|---|---|
| Jacquard 1801'de gösterim; 1804-05'te adını veren ek | DOĞRU | Britannica: https://www.britannica.com/biography/Joseph-Marie-Jacquard ; CHM: https://www.computerhistory.org/storageengine/punched-cards-control-jacquard-loom/ ; Columbia: 1804-05. "1800'lerin başı" güvenli. |
| Bouchon 1725 delikli kâğıt şerit | DOĞRU | https://wikipedia.com/wiki/Basile_Bouchon ; https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution |
| Falcon: şeridi delikli kart zinciriyle değiştirdi | KISMEN DOĞRU | Yıl çelişkisi: Duke 1728, Wikipedia 1737 ( https://WWW.Wikipedia.org/wiki/Joseph_Marie_Jacquard ). Videoda yıl verme; "1700'lerin ilk yarısı" de. |
| Babbage, Analitik Makine kartlarını Jacquard'dan esinlenerek tasarladı | KISMEN DOĞRU | IEEE Computer Society: "inanılır": https://history.computer.org/pioneers/jacquard.html ; CHM: Babbage 1837'de kart planı; Columbia tarihi ~1830 verir: https://www1.columbia.edu/cu/computinghistory/jacquard.html . "Esinlendiği kabul edilir" de; tarih söyleme. |
| Lovelace alıntısı gerçek, Note A, 1843: "weaves algebraical patterns just as the Jacquard-loom weaves flowers and leaves" | DOĞRU (sözcük teyidi kaldı) | Yale: https://www.cs.yale.edu/homes/tap/Files/ada-lovelace-notes.html ; Science History Institute: https://www.sciencehistory.org/stories/magazine/the-french-connection/ ("algebraical" yazımı). St Andrews "algebraic" yazar (ikincil). Sayfaları okuyamadım; çeviriden önce özgün Note A metnini (1843 Taylor's Scientific Memoirs) okuyun. |
| "Bilgisayarın İLK yazılımı kumaşa yazıldı" (başlık) | YANLIŞ / yanıltıcı | (1) Program kumaşa değil delikli karta/şeride yazıldı; kumaş çıktıydı. (2) Jacquard'dan önce Bouchon ve Falcon var. (3) Bu tezgâhlara "bilgisayarın yazılımı" demek anakronizm. Doğru: "Bilgisayarın delikli kart fikri bir dokuma tezgâhından geldi." |

Düzeltme: Başlık ve kanca "ilk"i bırakmalı. Öneri: "Bilgisayarın delikli kartı bir dokuma tezgâhından geldi".

---

## Fikir 7: Uçağa yıldırım düşünce içeride kimse neden çarpılmaz? — GENEL: KISMEN DOĞRU

| Olgu | Sonuç | Not / kaynak |
|---|---|---|
| Ticari uçağa ortalama yılda yaklaşık bir kez yıldırım düşer | KISMEN DOĞRU | FAA tahmini ~1000 uçuş saatinde bir (~yılda bir): https://www.livescience.com/32638-do-planes-get-struck-by-lightning.html ; Hong Kong Gözlemevi "yılda bir-iki": https://www.hko.gov.hk/en/education/weather/thunderstorm-and-lightning/00732-The-Aerial-Battle-Aircraft-vs-Thunder-God.html . FAA/NASA birincil sayfası okunmadı. Söyleyiş: "Ortalama bir ticari uçağa yılda yaklaşık bir kez". |
| Yıldırımı çoğu zaman uçak tetikler | KISMEN DOĞRU | NASA araştırması: uçak, yüklü bulutlara girince kendi yıldırımını başlatabilir; ~%40 deşarj fırtına bildirilmeyen yerde: https://flyingmag.com/ask-flying/how-can-an-aircraft-get-struck-by-lightning-without-a-close-thunderstorm ; https://www.scientificamerican.com/article/what-happens-when-lightni/ . "Çoğu zaman" kanıtlanmadı; "uçak kendi yıldırımını tetikleyebilir" de. |
| Alüminyum gövde Faraday kafesi gibi davranır; yük dış yüzeyde kalır, içeri geçmez | DOĞRU | Popular Science: https://www.popsci.com/breakdown/article/2008-06/electric-aviation-experience ; Hong Kong Gözlemevi (yukarıda). Britannica/NASA sayfası bulunamadı, ama iki bağımsız kaynak yeterli. "Lastikler korur" efsanesi yanlış. |
| Kompozit gövdede iletken katman (bakır/alüminyum örgü veya folyo) aynı koruma işini görür | DOĞRU (kaynak düzeyi zayıf) | USC Illumin: https://illumin.usc.edu/shocking-how-airplanes-defend-against-lightning/ ; patentler (787'de bakır ağ cilde gömülür; genişletilmiş metal folyo sektör standardı): https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7829796 , https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10351259 ; SAE: https://saemobilus.sae.org/articles/simulating-thermal-expansion-composites-expanded-metal-foil-lightning-protection-16aerp06_01 . Kurumsal (FAA/Boeing) kaynak yok; üretimden önce biri bulunmalı. |
| "FAA AC 20-136 kompozit katmanı kanıtlar" (planda kaynak) | YANLIŞ atıf | AC 20-136C (2026-05-15) elektrik/elektronik sistemlerin yıldırım korumasıdır; bölgeleme AC 20-155, test SAE ARP5416. Kompozit katman bu AC'ye bağlanmasın: https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-136C.pdf |
| 1963 Pan Am 214: yıldırım yakıt buharını tutuşturdu (CAB olası neden) | DOĞRU | https://en.wikipedia.org/wiki/Pan_Am_Flight_214 ; FAA: https://www.faa.gov/lessons_learned/transport_airplane/accidents/N709PA . 8 Aralık 1963, 81 ölü. "Olası neden" de; tutuşma yolu kesin değil. Sonrasında boşaltım fitilleri takıldı. |
| Yıldırım yanık, anten/sensör hasarı yapabilir; iniş sonrası kontrol | DOĞRU | https://www.nbcnews.com/news/amp/wbna31045261 ; https://flightsafety.org/wp-content/uploads/2016/11/asw_jun10_p18-23.pdf |

Düzeltme: Kaynak listesinden AC 20-136 çıkarılsın. "Çoğu zaman uçak tetikler" ve "bindiğin uçağa yılda bir" kalıplaşmasın. Kompozit adımında kurumsal kaynak bulunana kadar "iletken katman kullanılır" gibi genel ifade kullan.

---

## Özet

- Fikir 4: KISMEN DOĞRU; %30 kod sözcüğü oranı, alan değil.
- Fikir 1: DOĞRULANAMADI (Türkiye kablo/iniş listesi); "hortum" yalnız derin deniz.
- Fikir 3: KISMEN DOĞRU; "ilk yazılım kumaşa yazıldı" yanıltıcı, başlık değişmeli.
- Fikir 7: KISMEN DOĞRU; AC 20-136 atfı yanlış, "çoğu zaman uçak tetikler" ve oran ifadeleri yumuşatılmalı.
