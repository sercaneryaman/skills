# Teknoloji ve Gelecek: 8 Fikir (Görev 1, fikir turu)

Tarih: 2026-11-25. Brifing: analiz/teknoloji.md.

## Genel notlar

- Brifing zayıf kanıtlı: tek tek Shorts verisi, aykırı başarı, TR talep verisi yok. "Neden izlenir" satırlarında kanıt yoksa "kanıt yok" yazıldı.
- Dolaylı kanıtlar (brifing, KAYNAKLI): (a) makine/mekanik görsel Shorts'ta kayrılıyor (Tubefilter haftalık listeler, 2026); (b) şablonlu AI + stok görsel hem doygun hem demonetizasyon riskli (https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/); (c) özgün kurgu/animasyon "özgünlük" sinyali olarak avantajlı olabilir (The Next Web, Haziran 2026; kategoriye uygulanışı VARSAYIM).
- "Bilinen gerçekler" kaynakları bu oturumda açılıp doğrulanmadı (WebFetch yok, arama yapılmadı). Kaynaklar bilinen birincil/referans kaynaklardır; üretimden önce her sayı kaynağından teyit edilmeli. Teyit gerektirenler "TEYİT" ile işaretli.
- Tüm fikirler: tek ana fikir, kendi animasyon/model/diyagram. Şablon stok görsel yok.
- Eşleşme: fikirlerin ses dili Türkçe; İngilizce versiyon aynı akışla yapılabilir.

---

## Fikir 1

**Başlık:** İnternet okyanusun dibinden geçiyor (51 karakter)

**Kanca:** "Bu mesajı okurken, bir bahçe hortumu kalınlığındaki kablodan geçti."

**45 sn akış:**
1. (0-5) Kanca. Harita: kıtalar arası parlayan çizgiler.
2. (5-14) Uydu değil kablo: uluslararası veri trafiğinin büyük kısmı deniz altı kablolarından gider (TEYİT: oran, "yüzde 95+" sık anılır).
3. (14-24) 3D kesit: ortada ince cam lif, çevresinde bakır, yalıtım, çelik tel. Derin denizde kablo hortum kalınlığında.
4. (24-34) Kablo nasıl hasar görür: çoğunlukla gemi çapası ve balıkçı ağları; köpekbalığı ısırığı nadir, abartılır.
5. (34-42) Onarım gemisi kabloyu dipten kancayla çıkarır, birleştirir.
6. (42-45) Kapanış/döngü: "Şimdi sen de bu videoyu bir kablodan indirdin" ve açılıştaki hortum karesine dönüş.

**Neden izlenir:** Dolaylı: makine/mekanik görsel kayrılıyor (Tubefilter, brifing madde 1). Bu konuya özel kanıt yok.

**Görsel stil:** Harita animasyonu + kablo kesiti 3D model + kısa diyagram. Türkçe yapay zekâ seslendirme.

**Bilinen gerçekler:**
- Uluslararası veri trafiğinin ezici çoğunluğu deniz altı kablolarıyla taşınır. Kaynak: International Cable Protection Committee (iscpc.org) ve TeleGeography Submarine Cable Map (submarinecablemap.com). Kesin yüzde TEYİT.
- Derin deniz kablosu bahçe hortumu kalınlığındadır. Kaynak: ICPC "About Submarine Cables" (iscpc.org). TEYİT.
- Hasarın çoğu balıkçılık ve gemi çapasından kaynaklanır. Kaynak: ICPC (iscpc.org). Köpekbalığı ısırığı vakaları belgelenmiştir ama nadirdir (TEYİT).

**Risk:** Sayısal oran yanlış verilebilir, kaynaktan teyit et. Jeopolitik sabotaj tartışmasına girme (tartışmalı, bağlam ister). Doygunluk düşük-orta, ölçülmedi.

---

## Fikir 2

**Başlık:** Yapay zekâ kelime değil parça okur (token) (41 karakter)

**Kanca:** "Yapay zekâ bu cümleyi okumuyor. Parçalıyor."

**45 sn akış:**
1. (0-4) Kanca; cümle ekranda kırılır.
2. (4-14) Dil modeli metni "token" denen parçalara böler; bazı kelimeler tek parça, uzun/nadir kelimeler birkaç parça.
3. (14-26) Her parça bir sayıya çevrilir. Animasyon: kelime, parça, numara.
4. (26-36) Sonuç: model harf saymakta zorlanabilir ("strawberry" içindeki r sayısı örneği viral oldu), çünkü harfleri değil parçaları görür. Türkçe ekli kelimeler daha çok parçaya bölünebilir (TEYİT, tokenizer'a bağlı).
5. (36-43) Neden önemli: sınır "kelime" değil token ile ölçülür.
6. (43-45) Kapanış: ekrandaki cümleyi canlı tokenize et, parça sayısını göster.

**Neden izlenir:** Kanıt yok (bu konuya özel). AI "nasıl çalışır" anlatımının Shorts'ta performansına dair kanıt bulunamadı (brifing, kalıplar bölümü). Doygunluk riski var.

**Görsel stil:** Diyagram animasyonu (metin parçalanma), temiz tipografi. Yapay zekâ seslendirme.

**Bilinen gerçekler:**
- Büyük dil modelleri girdiyi token'lara böler. Kaynak: OpenAI Tokenizer sayfası ve belgeleri (platform.openai.com/tokenizer). Genel yöntem: Sennrich ve ark., "Neural Machine Translation of Rare Words with Subword Units", 2015 (arxiv.org/abs/1508.07909).
- Harf sayma hataları token yapısıyla açıklanır; bu açıklama yaygın ama her model için ölçülmemiştir. Etiket: yaygın açıklama, TEYİT.
- Aynı metnin token sayısı dile ve tokenizer'a göre değişir. Kaynak: aynı tokenizer aracıyla elle denenebilir (üretimde ekran kaydı al).

**Risk:** Hızlı eskiyen konu; model sürümüne göre örnek bozulabilir, örneği üretimden önce canlı dene. Doymuş konu (AI içerik). Telif yok.

---

## Fikir 3

**Başlık:** Bilgisayarın atası bir dokuma tezgâhı (41 karakter)

**Kanca:** "İlk programlanabilir makine bilgisayar değildi. Kumaş dokuyordu."

**45 sn akış:**
1. (0-5) Kanca; kara kalem çizimle dokuma tezgâhı.
2. (5-15) 1804: Jacquard tezgâhı, delikli kartlarla desen belirler. Delik var = iğne geçer, yok = geçmez (ikili mantık benzetmesi).
3. (15-26) Kartlar zincirlenir; kart değişir, desen değişir: yazılım fikri.
4. (26-36) Babbage Analitik Makine için bu kartları ödünç alır; Ada Lovelace bunu "makine kumaş dokur gibi cebirsel desen dokur" diye anlatır.
5. (36-43) 20. yüzyıl bilgisayarlarında delikli kart veri girişinin standardı olur.
6. (43-45) Döngü: kart deliği, piksel ışığına dönüşür.

**Neden izlenir:** Kanıt yok. Kara kalem/parşömen stili için kategoriye özgü kanıt yok; özgün animasyon "özgünlük" sinyali olabilir (The Next Web, VARSAYIM).

**Görsel stil:** Kara kalem/parşömen animasyon, tezgâh için kısa 3D model. Yapay zekâ seslendirme.

**Bilinen gerçekler:**
- Jacquard tezgâhı 1804'te tanıtıldı, delikli kartlarla desen kontrol eder. Kaynak: Britannica "Jacquard loom"; Science Museum Group.
- Babbage, Analitik Makine'de Jacquard kartlarından esinlenmiştir. Kaynak: Computer History Museum; Britannica "Analytical Engine".
- Lovelace'in "cebirsel desenler dokur" benzetmesi 1843 notlarında geçer. Kaynak: Lovelace, Menabrea çevirisine Notlar, 1843 (Note A). Alıntıyı birebir teyit et.
- "İlk programlanabilir makine" iddiası tartışmalıdır (daha eski programlanabilir otomatlar var, ör. Heron çalışmaları, el yapımı dönemi). Videoda "ilk" yerine "ilk yaygın ticari kullanım" de.

**Risk:** "İlk" iddiası tartışmalı; başlık/kanca yumuşatılabilir. Lovelace'in "ilk programcı" tartışmasına girme. Tarihî konu, doygunluk düşük.

---

## Fikir 4

**Başlık:** QR kodun yarısı kapalıyken neden okunur? (45 karakter)

**Kanca:** "Bu QR kodun yüzde 30'unu karalasam bile okunur. Nasıl?"

**45 sn akış:**
1. (0-5) Kanca; QR üstüne boya fırçası.
2. (5-14) Kare ızgara: siyah/beyaz hücre = 1/0. Üç köşedeki büyük kare konum işaretidir.
3. (14-26) Veri kadar "fazlalık" da saklanır: Reed-Solomon hata düzeltme.
4. (26-36) Dört seviye: L, M, Q, H. En yüksek seviyede yaklaşık yüzde 30'a kadar bozulma düzeltilebilir.
5. (36-43) Bu yüzden ortaya logo konabilir.
6. (43-45) Kapanış/döngü: kapalı QR telefonla okunur; açılışa dönüş.

**Neden izlenir:** Kanıt yok (konu özelinde). Dolaylı: oddly satisfying/mekanik görsel eğilimi (Tubefilter), ama QR bunun doğrudan örneği değil.

**Görsel stil:** Diyagram animasyonu, gerçek telefon kamerası çekimi veya ekran kaydı (özgünlük için). Yapay zekâ seslendirme.

**Bilinen gerçekler:**
- QR kodu 1994'te Denso Wave tarafından icat edildi. Kaynak: qrcode.com (Denso Wave resmî sitesi).
- Hata düzeltme seviyeleri L, M, Q, H; yaklaşık 7%, 15%, 25%, 30% kurtarma. Kaynak: ISO/IEC 18004; Denso Wave "Error correction feature" sayfası.
- Hata düzeltme Reed-Solomon kodlarıyla yapılır. Kaynak: ISO/IEC 18004; Denso Wave.
- Gerçek dayanıklılık kaybın nerede olduğuna bağlıdır (konum işaretleri zarar görürse okunmaz). Videoda "yaklaşık, uygun yerden" de.

**Risk:** "Yarısı kapalı" abartı olur; yüzde 30 sınırını koru. QR dolandırıcılığına (quishing) girme, ayrı konu. Doygunluk düşük.

---

## Fikir 5

**Başlık:** İnternetin ilk mesajı "LO" idi, çünkü çöktü (47 karakter)

**Kanca:** "İnternetin ilk mesajı yarım kaldı, çünkü sistem çöktü."

**45 sn akış:**
1. (0-5) Kanca; 1969, eski terminal çizimi.
2. (5-15) UCLA'dan Stanford Araştırma Enstitüsü'ne "LOGIN" yazılacaktı.
3. (15-25) İki harften sonra sistem çöker: "LO".
4. (25-35) Neden önemli: ARPANET'te ilk bağlantı o gece kurulur; saatler sonra düzelip tam giriş yapılır.
5. (35-42) Mesaj paketlere bölünür: bugünkü internetin temeli (paket anahtarlama).
6. (42-45) Döngü: "LO" ekranda parlar, "Lo and behold" şakasıyla biter.

**Neden izlenir:** Kanıt yok.

**Görsel stil:** Kara kalem/parşömen animasyon, retro terminal. Yapay zekâ seslendirme.

**Bilinen gerçekler:**
- İlk ARPANET mesajı 29 Ekim 1969'da UCLA'dan SRI'ya gönderildi; "LO" iletildi, sonra sistem çöktü. Kaynak: UCLA Samueli Engineering / Leonard Kleinrock anlatımı; Computer History Museum.
- Saat ve ayrıntılar (akşam saati, kimin yazdığı) anlatımlara göre değişir. TEYİT; videoda saat verme.
- "Lo and behold" şakası sonradan yapılmış, tarihsel bir anekdot. Etiket: anekdot.
- Paket anahtarlama fikri 1960'larda Paul Baran ve Donald Davies'e dayanır. Kaynak: Britannica "packet switching"; Computer History Museum.

**Risk:** Anekdotun ayrıntıları kaynaklar arasında farklı; "çöktü" ifadesi yaygın ama ayrıntı TEYİT. Çok anlatılmış hikâye (doygunluk orta, ölçülmedi).

---

## Fikir 6

**Başlık:** GPS, görelilik olmadan günde 10 km şaşar (44 karakter)

**Kanca:** "Einstein olmasaydı, telefonun seni her gün 10 kilometre yanlış gösterirdi."

**45 sn akış:**
1. (0-5) Kanca; yer küresi ve uydu 3D.
2. (5-14) GPS konumu, uydudan gelen sinyalin zamanına bakarak hesaplar. Saat hatası = konum hatası.
3. (14-26) Uydu hızlı hareket ettiği için saat yavaşlar (özel görelilik), yerçekimi zayıf olduğu için hızlanır (genel görelilik).
4. (26-36) Net etki: uydu saati günde yaklaşık 38 mikrosaniye ileri gider.
5. (36-43) Işık hızıyla çarpınca birkaç on kilometre/gün değil, yaklaşık 10 km mertebesinde hata birikir; sistem bu yüzden saati baştan ayarlıdır.
6. (43-45) Kapanış: konum noktası yerine oturur, açılışa dönüş.

**Neden izlenir:** Kanıt yok. Dolaylı: 3D makine/uydu görseli (Tubefilter eğilimi, dolaylı).

**Görsel stil:** 3D model (Dünya, uydu, saatler), diyagram. Yapay zekâ seslendirme.

**Bilinen gerçekler:**
- Özel görelilik uydu saatini günde yaklaşık 7 mikrosaniye geri, genel görelilik yaklaşık 45 mikrosaniye ileri götürür; net yaklaşık 38 mikrosaniye/gün. Kaynak: Ashby, "Relativity in the Global Positioning System", Living Reviews in Relativity, 2003.
- Düzeltilmezse konum hatası günde kilometre mertebesinde birikir (sık anılan değer yaklaşık 10 km/gün). Kaynak: Ashby 2003; kesin sayı TEYİT, videoda "yaklaşık" de.
- Uydu saatleri yer saatine göre fabrikada ayarlanır. Kaynak: Ashby 2003.

**Risk:** Sayılar yaklaşık; "10 km" değerini Ashby'den teyit et, değilse kancayı "kilometrelerce" yap. Fizik hatası riski: iki etkinin işaretini doğru anlat. Doygunluk orta (popüler fizik anlatımı).

---

## Fikir 7

**Başlık:** Uçağa yıldırım düşse neden bir şey olmaz? (46 karakter)

**Kanca:** "Ticari uçaklara yıldırım düşer. Yolcular çoğu zaman fark etmez."

**45 sn akış:**
1. (0-5) Kanca; fırtınada uçak, yıldırım çakıyor.
2. (5-15) Uçağın gövdesi iletkendir; akım dışarıdan akıp gider, içeriye girmez (Faraday kafesi fikri).
3. (15-26) Diyagram: akım burun ucundan girer, gövde boyunca kuyruktan çıkar.
4. (26-36) Kompozit gövdelerde iletken tel ağı/folyo katmanı bu işi yapar.
5. (36-43) Sertifikasyon: yıldırım koruması test edilir.
6. (43-45) Kapanış: akım yolu çizgisi başa döner.

**Neden izlenir:** Kanıt yok. Dolaylı makine/mekanik eğilim (Tubefilter), konuya özel kanıt yok.

**Görsel stil:** 3D uçak modeli + akım yolu animasyonu, diyagram. Yapay zekâ seslendirme.

**Bilinen gerçekler:**
- Ticari uçaklar ortalama yılda yaklaşık bir kez yıldırım yer (sık aktarılır). Kaynak: NASA / FAA yıldırım koruma anlatımları; oran TEYİT.
- Alüminyum gövde iletken kafes gibi davranır (Faraday kafesi). Kaynak: Britannica "Faraday cage"; NASA.
- Kompozit gövdelerde iletken katman (örgü/folyo) kullanılır. Kaynak: FAA Advisory Circular AC 20-136 (aircraft electrical and electronic system lightning protection) TEYİT.
- Yıldırım uçağa zarar verebilir (yüzeyde yanık, anten/sensör hasarı); "hiçbir şey olmaz" demek yanlış olur.

**Risk:** "Hiçbir şey olmaz" aşırı iddia; videoda "yolcular güvende, uçak kontrol edilir" de. Uçuş güvenliği konusu hassas ama kaygı yaratmayacak çerçeve. Tartışmalı değil. Doygunluk düşük-orta.

---

## Fikir 8

**Başlık:** Mikrodalga fırın bir çikolata yüzünden doğdu mu? (50 karakter)

**Kanca:** "Mikrodalga fırın, bir mühendisin cebindeki çikolatanın erimesiyle bulundu. Öyle mi?"

**45 sn akış:**
1. (0-5) Kanca; kara kalem çizim, radar odası.
2. (5-15) Percy Spencer, 1940'lar, Raytheon, radar tüpü magnetron üzerinde çalışıyor.
3. (15-25) Anekdot: cebindeki yiyecek eridi; deney olarak patlamış mısır denedi (anlatım değişir).
4. (25-35) Fiziği: mikrodalga su moleküllerini sallar, ısı oluşur. Neden tabak soğuk kalır: tabakta su az.
5. (35-42) İlk fırın "Radarange", çok büyük ve pahalıydı.
6. (42-45) Döngü: "Peki çikolata mıydı?" ve anekdotun tartışmalı olduğu notu.

**Neden izlenir:** Kanıt yok. "Efsane mi gerçek mi" çerçevesi için bu kategoride kanıt yok.

**Görsel stil:** Kara kalem/parşömen animasyon + kısa diyagram (su molekülü). Yapay zekâ seslendirme.

**Bilinen gerçekler:**
- Percy Spencer Raytheon'da magnetron üzerinde çalışırken mikrodalganın ısıtma etkisini fark etti (1945 civarı). Kaynak: Britannica "Percy Spencer"; Smithsonian.
- Cebindeki yiyecek anekdotu (çikolata/yer fıstığı çubuğu, anlatıma göre değişir) tartışmalı/anekdot. Etiket: EFSANE olasılığı, birincil kaynak yok. Videoda "anlatılır" de.
- Mikrodalga, özellikle su moleküllerinin dönmesiyle ısıtır (basitleştirilmiş anlatım). Kaynak: Britannica "microwave oven"; FDA "Microwave Oven Radiation".
- Ticari "Radarange" 1947'den itibaren üretildi (yıl TEYİT). Kaynak: Smithsonian / Britannica.

**Risk:** Anekdot kesin bilgi gibi sunulmamalı, açıkça "anlatılır/tartışmalı" etiketle. Sağlık yönüne (radyasyon korkusu) girme; girersen FDA kaynaklı kısa not. Çok anlatılmış hikâye, doygunluk orta.

---

## Özet tablo

| # | Başlık | Stil | Kanıt |
|---|---|---|---|
| 1 | İnternet okyanusun dibinden geçiyor | harita + 3D | dolaylı |
| 2 | Yapay zekâ kelime değil parça okur (token) | diyagram | kanıt yok |
| 3 | Bilgisayarın atası bir dokuma tezgâhı | kara kalem | kanıt yok |
| 4 | QR kodun yarısı kapalıyken neden okunur? | diyagram + çekim | kanıt yok |
| 5 | İnternetin ilk mesajı "LO" idi, çünkü çöktü | kara kalem | kanıt yok |
| 6 | GPS, görelilik olmadan günde 10 km şaşar | 3D | kanıt yok |
| 7 | Uçağa yıldırım düşse neden bir şey olmaz? | 3D + diyagram | kanıt yok |
| 8 | Mikrodalga fırın bir çikolata yüzünden doğdu mu? | kara kalem | kanıt yok |
