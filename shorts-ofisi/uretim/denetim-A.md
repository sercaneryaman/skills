# Denetim A: video üretim promptları 1-18 (2026-11-26)

Okunanlar: `uretim/STIL-ATAMALARI.md`, `uretim/SABLON.md`, `uretim/promptlar/{yemek,doga,teknoloji,uzay,tarih,bilim}.md`, `2026-11-25/pano/{yemek,doga,teknoloji,uzay,tarih,bilim}.md`.

## Yöntem

- Altı ölçüt, her biri 1-5: (1) şablon eksiksizliği, (2) süre, kelime sayısı ve altyazı uyumu, (3) ilk 2 sn kancası, (4) monetizasyon riski (5 = risk düşük), (5) pano şartlarına uyum, (6) diğer videolardan farklılık.
- Kelime sayısı: "Tam İngilizce seslendirme metni" elle sayıldı (±2). Yıllar ve büyük sayılar konuşmada 2-3 kelimeye çıktığı için "konuşulan" sayı ayrıca verildi.
- Süre tahmini: kelime / promptun kendi "Ses yönergesi"ndeki hız + yazılı duraklamalar. Sabit kuraldaki 2,3 kelime/sn de ayrıca kontrol edildi.
- Satır numaraları ilgili prompt dosyasınındır.

## Özet tablo

| No | Şablon | Süre/altyazı | Kanca | Monetizasyon | Pano | Farklılık | Ort. | Karar |
|---|---|---|---|---|---|---|---|---|
| 1 | 5 | 4 | 5 | 4 | 5 | 4 | **4,50** | GÜÇLÜ |
| 2 | 5 | 2 | 4 | 4 | 5 | 4 | **4,00** | DÜZELTİLMELİ (süre) |
| 3 | 4 | 5 | 3 | 4 | 5 | 3 | **4,00** | DÜZELTİLMELİ (kanca) |
| 4 | 5 | 3 | 5 | 4 | 5 | 3 | **4,17** | GÜÇLÜ (küçük kesinti) |
| 5 | 5 | 2 | 4 | 5 | 4 | 2 | **3,67** | DÜZELTİLMELİ |
| 6 | 5 | 2 | 4 | 4 | 3 | 2 | **3,33** | DÜZELTİLMELİ |
| 7 | 5 | 5 | 5 | 4 | 4 | 3 | **4,33** | GÜÇLÜ |
| 8 | 5 | 3 | 3 | 5 | 4 | 2 | **3,67** | DÜZELTİLMELİ |
| 9 | 5 | 3 | 3 | 5 | 4 | 3 | **3,83** | DÜZELTİLMELİ |
| 10 | 5 | 4 | 4 | 5 | 3 | 3 | **4,00** | DÜZELTİLMELİ (küçük) |
| 11 | 5 | 4 | 3 | 4 | 3 | 2 | **3,50** | DÜZELTİLMELİ |
| 12 | 5 | 4 | 4 | 3 | 2 | 2 | **3,33** | DÜZELTİLMELİ (ağır) |
| 13 | 5 | 5 | 4 | 4 | 3 | 3 | **4,00** | DÜZELTİLMELİ (başlık) |
| 14 | 5 | 2 | 3 | 4 | 5 | 3 | **3,67** | DÜZELTİLMELİ |
| 15 | 5 | 3 | 3 | 4 | 4 | 2 | **3,50** | DÜZELTİLMELİ |
| 16 | 5 | 3 | 3 | 3 | 3 | 2 | **3,17** | DÜZELTİLMELİ (ağır) |
| 17 | 4 | 5 | 3 | 5 | 4 | 3 | **4,00** | DÜZELTİLMELİ (küçük) |
| 18 | 4 | 2 | 5 | 3 | 5 | 3 | **3,67** | DÜZELTİLMELİ |

Hiçbir video ZAYIF değil. Hepsi panodan "ÜRET" kararıyla geldi, olgu çekirdekleri doğrulanmış. Sorunlar metin ve tasarım düzeyinde, düzeltilebilir. En zayıf üç video 16, 12 ve 6. Bu üçü düzeltilmeden çekime girmemeli.

---

## Seri geneli: tekrar eden kalıplar (ölçüt 6)

Bu bölüm tek tek videolardaki düzeltmelerin kaynağıdır. Stil ataması çeşitliliği sağlamış, ama uzmanlar kapanışta, renkte ve fontta aynı alışkanlıklara dönmüş.

1. **Döngü kapanışı 18 videonun 18'inde var.** Hepsinde "son kare ilk kareye bağlanır" yazıyor. Pano/uzay.md satır 12 bunu açıkça yasaklıyor: "aynı döngü kapanışı arka arkaya tekrarlanmaz". 10, 11 ve 12 art arda döngüyle bitiyor. Şablon hissinin en büyük kaynağı bu.
   **Düzeltme:** Kategori başına en çok bir döngü kalsın. Döngü 1, 4, 7, 10, 13 ve 17'de kalabilir, çünkü bu videolarda döngü kavramın parçası. Diğerleri sürpriz ya da son kareyle bitsin (aşağıda videoya göre yazıldı).
2. **Abone cümlesi kalıbı:**
   - "...for the next ___" yedi videoda var: 5 race, 7 level, 11 sky alert, 12 note, 14 next one, 15 machine, 16 guess.
   - "Subscribe, and we'll keep ___" üç videoda var: 3 digging, 9 weaving, 10 the line open.
   - "Kazmak" mecazı iki videoda var: 3 "keep digging" ve 14 "unearth".
   **Düzeltme:** "next" yalnız 7 ve 16'da kalsın (oyun ve quiz yapısına uyuyor). Yeni cümleler videoların altında.
3. **Aynı cümle iki videoda:** 5 "One bird's record, not the species average." ve 6 "One shark's estimate, not a species average." Aynı kategoride art arda geliyorlar.
4. **Aynı kanca kalıbı:** 13 "Over 3,100 years ago..." ve 15 "Eight hundred years ago...". İkisi de tarih kategorisinde ve aynı açılışı kullanıyor.
5. **Aynı mekanik:** 1 ve 16'nın ikisi de "guess" ile tik-tak sayaç kullanıyor.
6. **"Bilinmiyor" kapanışı:** Üç videoda var: 4 "Scientists don't fully know yet", 18 "We just don't know what yet", 3 "That one stays open". Ayrıca 14 "Still debated" diyor.
7. **Palet:** Koyu lacivert zemin üzerinde neon camgöbeği yedi videoda var (4, 5, 6, 7, 8, 12, 16).
   - Aynı hex kodlar: `#7DF9FF` hem 8'de hem 12'de, `#FFB000` hem 8'de hem 10'da.
   - Lacivert üstünde sarı üç videoda var: 5 `#FFD23F`, 7 `#FFD83D`, 16 `#FFD84D`.
   - 17 ile 18'in paletleri neredeyse aynı: krem zemin, lacivert etiket ve kırmızı ok (`#D64545` / `#D64F4F`).
   - 13 ile 15'in ikisi de lapis, aşı kırmızısı, okr/altın ve kâğıt zeminden oluşuyor.
8. **Font:**
   - Inter: 4, 5, 11, 16
   - Cinzel: 6, 14
   - Montserrat ExtraBold: 12, 16
   - Cormorant Garamond: 2, 4
   - Caveat: 1, 13
9. **Müzik ve geçiş:** Ney 6 ve 15'te var. Sayfa kayması/çevirme 1, 13, 15 ve 18'de (kart çevirme) var.
10. **Sentetik içerik beyanı:** Fotogerçekçi yapay zekâ sahnesi olan videolarda beyan zorunlu: 2, 4, 11, 14, 16. Diğerlerinde isteğe bağlı. Teknoloji dosyasında insan sesi birincil seçenek, TTS kullanılırsa beyan şart. Bu dosyalarda sorun yok, ama yükleme kontrol listesine video bazında yazılmalı.

---

## 1. Taze ananas jöleyi neden dondurmaz (yemek.md)
- **Şablon (5):** Tüm alanlar var. 5 hashtag ve 5 görsel prompt var.
- **Süre/altyazı (4):** 79 kelime / 35 sn = 2,26 kelime/sn. Toplam uyuyor, ama satır dağılımı bozuk:
  - 0-3 aralığında 12 kelime var, yani 4 kelime/sn.
  - 30-35 aralığında 15 kelime var, yani 3 kelime/sn.
  - Satır 20'de "2 sn sessiz bekleme", satır 50'de "1,5 sn duraklama" yazıyor. İkisi çelişiyor.
  - Altyazıların hepsi ≤6 kelime ve sıra doğru.
- **Kanca (5):** Gerçek çekimde ters çevrilen iki kase ve "Same jelly, same fridge" cümlesi kaydırmayı durdurur.
- **Monetizasyon (4):** Kendi deneyimiz özgün katkı. Kâğıt animasyonda beyan zorunlu değil. Risk düşük.
- **Pano (5):** "Donmuyor", "taze ananas", sıcaklık rakamının yokluğu ve McGill dışlaması uygulanmış.
- **Farklılık (4):** "Guess" ve tik-tak mekaniği 16 ile aynı.
- **Düzeltmeler:**
  - Satır 19-24'ün zamanlarını şöyle değiştir: 0-4 (9 kelime: "Same jelly, same fridge. One bowl holds, one runs."), 4-10 ("The difference? Pineapple. Before I show you, guess..." ve 1,5 sn duraklama), 10-17, 17-24, 24-29, 29-35.
  - Satır 20'deki "2 sn sessiz bekleme" ifadesini "1,5 sn duraklama" yap ve satır 50 ile eşitle.
  - Satır 20 SFX "Tik-tak sayaç, düşünme müziği" yerine "kâğıt çevirme 'flip', tek ukulele notası" yaz. Tik-tak 16'da kalsın.

## 2. Ekmeği buzdolabına koyarsan daha hızlı bayatlar (yemek.md)
- **Şablon (5):** Eksik alan yok.
- **Süre/altyazı (2):** Metin 69 kelime. Promptun kendi hızı ~120 kelime/dk (2,0 kelime/sn, satır 107). Bu hızla konuşma 34,5 sn, duraklamalarla ≈36 sn sürer; video 30 sn. 8-16 satırında 17 kelime ve 0,8 sn duraklama var, 8 saniyeye sığmıyor. Altyazıların hepsi ≤6 kelime ve sıra doğru.
- **Kanca (4):** Görsel ("tok" ses) güçlü. Fısıltı tonu ilk saniyede enerjiyi düşürüyor.
- **Monetizasyon (4):** Fotogerçekçi yapay zekâ makro promptları var (satır 115, 116, 119). Beyan zorunlu, "illüstrasyon" etiketi doğru.
- **Pano (5):** "Ana neden kuruma değil", "çok yavaşlatır" ve tavsiye yasağı uygulanmış.
- **Farklılık (4):** Fısıltılı anlatıcı 6 ile ortak (atama gereği). Cormorant fontu 4 ile ortak.
- **Düzeltmeler:**
  - Satır 87-92'yi şu ~59 kelimelik metinle değiştir:
    "Bread goes stale faster in the fridge. Drying isn't the main reason. Baking scatters the starch chains. As bread cools, they line up into crystals. Water shifts out. Same loaf, twenty-four hours: counter, fridge, freezer. Crystals form fastest at fridge temperature. The freezer slows it a lot. Warm it, and it softens for a while. Follow for more quiet science."
  - Satır 107'de hızı "~126 kelime/dk (2,1 kelime/sn)" yap.
  - Altyazı satır 96-97'yi "Ana neden kuruma değil." olarak birleştir. Satır 101'i "Aynı somun, 24 saat:" yap.
  - Döngü (satır 111): Buzdolabı kapağı döngüsünü kaldır. Video buharla yumuşayan dilimin yakın planıyla bitsin, çünkü yemek kategorisindeki döngü 1'de kalıyor.

## 3. Marco Polo makarnayı getirmedi (yemek.md)
- **Şablon (4):** Satır 126-127'de iki başlık var ve "tercih edilen alternatif" deniyor. Bu belirsiz.
- **Süre/altyazı (5):** Metin 81 kelime, yıllarla birlikte konuşmada ≈91 kelime. 40 sn içinde 2,3 kelime/sn ediyor. Altyazıların hepsi ≤6 kelime ve sıra doğru.
- **Kanca (3):** "Marco Polo brought pasta from China. That's the story." Pano bu efsaneyi Türk izleyicinin bilmeyebileceğini söylüyor (kanca puanı 3). İlk 2 saniyede çelişki yok.
- **Monetizasyon (4):** Haber filmi estetiği özgün üretim. Arşiv klibi yok. Risk düşük.
- **Pano (5):** "Kaynak olarak gösterilen", 1929 yayınının biçimi ve Bastone/sago dışlamaları uygulanmış.
- **Farklılık (3):** "Subscribe, and we'll keep digging" kalıbı 9 ve 10'la, kazma mecazı 14 ile ortak.
- **Düzeltmeler:**
  - Satır 127'yi yalnız "Marco Polo makarnayı Çin'den mi getirdi?" olarak bırak.
  - Satır 132, 137, 145 ve 153: İlk cümleyi "Everyone says Marco Polo brought pasta from China. The records disagree." yap. Altyazıyı "Herkes Polo getirdi der. / Kayıtlar öyle demiyor." yap.
  - Satır 142, 150, 169 ve 174: CTA'yı "Follow if you like your history with receipts." yap. Altyazı: "Kaynaklı tarih seviyorsan takip et."
  - Döngü kalabilir, ama 1 zaten döngüyle bittiği için tercihen iris kapanışında son kare "Soru açık" kartı olsun. Makarna demetine geri dönülmesin.

## 4. Kalbi duran kurbağa (doga.md)
- **Şablon (5):** Eksik alan yok. Atama değişikliği gerekçeli.
- **Süre/altyazı (3):** Metin 83 kelime. Promptun hızı 2,0 kelime/sn (satır 50). Bu hızla konuşma 41,5 sn, duraklamalarla ≈43 sn; video 40 sn. Altyazıların hepsi ≤6 kelime ve sıra doğru.
- **Kanca (5):** Atan monitör çizgisi buzla düzleşiyor ve "This frog's heart stops." deniyor. Güçlü.
- **Monetizasyon (4):** Fotogerçekçi orman var (prompt 2, 5), beyan zorunlu. Hayvan illüstrasyon olarak çiziliyor, doğru.
- **Pano (5):** Üçte iki, söylenmeyecekler listesi ve ekranda kaynak uygulanmış.
- **Farklılık (3):**
  - Lacivert zemin ve buz mavisi seri genelindeki kümeye giriyor.
  - Inter ve Cormorant fontları başka videolarla ortak.
  - "Bilinmiyor" kapanışı 18 ile ortak.
- **Düzeltmeler:**
  - Satır 27, 31 ve 47: "Frozen in winter, alive in spring." cümlesini ve 15. altyazıyı çıkar. 0:32-0:36 satırında yalnız "Dead... or alive?" kalsın. Sonuç 77 kelime ≈40 sn.
  - Satır 26 ve 31: "Scientists don't fully know yet." cümlesini "Nobody has fully cracked that yet." yap. Altyazı 14: "Bunu henüz kimse tam çözemedi."
  - Satır 51-52: Etiket fontu Inter yerine Türkçe glif testli başka bir sans olsun (ör. Nunito Sans).

## 5. 11 gün konmadan uçan kuş (doga.md)
- **Şablon (5):** Eksik alan yok.
- **Süre/altyazı (2):**
  - Metin ≈82 kelime, yıllarla birlikte konuşmada ≈88 kelime. Promptun hızı 2,4 kelime/sn: konuşma ≈36,7 sn, duraklamalarla ≈38 sn. Video 35 sn.
  - 0:25-0:31 satırında 6 saniyede ≈20 konuşulan kelime var, yani 3,3 kelime/sn. Sığmıyor.
  - "And they're off!" cümlesinin altyazısı yok.
  - "They're" tek kuş için yanlış zamir.
- **Kanca (4):** Çizilen rota ve sayaç iyi. Daha sert bir sürüm: "Eleven days. No landing." (4 kelime).
- **Monetizasyon (5):** Gerçekçi kuş yok, "Rota temsili" etiketi var.
- **Pano (4):** Pano/doga.md satır 9 "ekranda kaynak yazılır" diyor. Videoda ekranda kaynak etiketi yok.
- **Farklılık (2):** "Not the species average" cümlesi 6 ile aynı. Navy, neon camgöbeği ve sarı paleti 7 ve 16 ile ortak. "Next race" CTA'sı "next" kalıbında.
- **Düzeltmeler:**
  - Satır 83 ve 91: "And they're off!" yerine "And it's off!" yaz. Satır 93'ten sonra altyazı ekle: "Ve yola çıktı!"
  - Satır 87 ve 91: Skor cümlesini "Scoreboard! 2021: about thirteen thousand fifty. 2007, E7: about eleven thousand seven hundred." yap.
    - "Adult male" ve "over eight days" yalnız ekran yazısında kalsın.
    - Altyazı 11-13 şöyle olsun: "2021: ≈13.050 km." / "2007, E7: ≈11.700 km."
  - Satır 86'nın ekran yazısına "Kaynak: USGS · Guinness" ekle.
  - Satır 88, 113 ve 116: CTA'yı "Follow. This scoreboard isn't finished." yap. Altyazı: "Takip et, skor tablosu bitmedi."
  - Döngüyü kaldır. Video skor tablosunda dursun.
  - Satır 110: Rota neon `#00E5FF` yerine spor turuncusu `#FF8A3D` kullan. Etiket fontunu Inter yerine Barlow yap.

## 6. Yaklaşık 400 yaşında köpekbalığı (doga.md)
- **Şablon (5):** Eksik alan yok.
- **Süre/altyazı (2):** Metin ≈96 kelime. Promptun hızı 2,0 kelime/sn (satır 169). Bu hızla konuşma ≈48 sn, duraklamalarla ≈49 sn; video 45 sn. Altyazıların hepsi ≤6 kelime ve sıra doğru.
- **Kanca (4):** "This shark may have been born in the Ottoman era." Türk izleyiciye özgün bir bağ. Yavaş fısıltı ilk 2 saniyeyi zayıflatıyor, bu yüzden görsel hemen başlamalı.
- **Monetizasyon (4):** Minyatürler özgün, fotogerçekçi köpekbalığı yok. Risk düşük.
- **Pano (3):**
  - Pano satır 63'te "cinsel olgunluk **en az** yaklaşık 150" diyor. Metin "They mature around age one hundred fifty" diyor, yani "en az" düşmüş.
  - Ekranda kaynak yok (pano/doga.md satır 9).
  - Ek olgusal not: Köpekbalıkları 2010-2013'te yakalandı, 2016 yayın yılı. Doğum aralığını 2016'dan geri saymak birkaç yıl kaydırıyor. Pano bu hesabı kabul ediyor, ama "yaklaşık" kelimesi her yerde kalmalı.
- **Farklılık (2):**
  - Tür ortalaması cümlesi 5 ile aynı.
  - Cinzel fontu 14 ile, ney 15 ile ortak.
  - Fısıltılı anlatıcı 2 ile ortak.
  - Lacivert ve camgöbeği paleti kümeye giriyor.
- **Düzeltmeler:**
  - Satır 143 ve 150: "Scientists measured radiocarbon ... nuclear tests." cümlesini "Radiocarbon in its eye lens was matched against fallout from 1950s nuclear tests." yap.
  - Satır 146 ve 150: "They mature around age one hundred fifty." yerine "They may not mature until about one hundred fifty." yaz. Altyazı 15: "En az ~150 yaşında olgunlaşıyor."
  - Satır 145 ve 150: "One shark's estimate, not a species average." yerine "And that's just one shark's estimate." yaz. Altyazı 14: "Ve bu, tek bir köpekbalığının tahmini."
  - Satır 169: Hızı 2,1 kelime/sn yap. Hedef ≈44 sn.
  - Satır 144'ün ekran yazısına "Kaynak: Nielsen vd., Science 2016" ekle.
  - Satır 170: Tarih kartında Cinzel yerine Türkçe glif testli başka bir serif kullan (ör. Spectral SC).
  - Satır 172: "Ney benzeri" yerine "cam armonika / derin su tınısı" yaz.
  - Döngüyü kaldır. Silüet karanlıkta kaybolsun, son kare siyah kalsın.

## 7. QR kodu karalasan bile neden okunur (teknoloji.md)
- **Şablon (5):** Eksik alan yok.
- **Süre/altyazı (5):** 69 kelime / 30 sn. Promptun hızı 2,4 kelime/sn; 0,5 sn sessizlikle ≈29,7 sn. Uyuyor. Altyazıların hepsi ≤6 kelime ve sıra doğru.
- **Kanca (5):** Konuşmadan önce gerçek okuma gösteriliyor, sonra "How did it read that?" geliyor.
- **Monetizasyon (4):**
  - Çekimdeki gerçek QR taranabilir. Adres "üretimde belirlenecek" diye bırakılmış.
  - Press Start 2P ve VT323 fontlarında Türkçe glifler (ğ, ş, ı, İ) test edilmemiş.
- **Pano (4):**
  - Kanca görseli (satır 16) "yarısı çizilmiş görünen" QR diyor. Bu, satır 50'deki "kodun yarısı kapalıyken okunur" yasağını görsel olarak ima ediyor.
  - Satır 52'deki yedek cümle ("Corner squares are the risky spot") metinde hiç geçmiyor. Değiştirme talimatı belirsiz.
- **Farklılık (3):** Neon renkler lacivert üstünde, sarı vurgu 5 ve 16 ile ortak. Oyun estetiği yine de ayırt edici.
- **Düzeltmeler:**
  - Satır 16 ve 21: "yarısı çizilmiş görünen" yerine "veri bölgesinin bir kısmı markörle karalanmış, köşe kareleri temiz" yaz.
  - Satır 52: Şöyle yaz: "Okunduysa 18,5-25 satırı EN 'Corner squares are the critical spot.' ve TR 'Köşe kareleri kritik bölgedir.' olur; 'reading gets very hard' çıkar."
  - Satır 53'e ekle: "Adres kanalın kendi alan adı olacak; kısaltıcı, yönlendirme ve izleme parametresi yok; yükleme öncesi iki ayrı telefonla taranacak."
  - Satır 44'e ekle: "Press Start 2P/VT323 için ğ ş ı İ ç ö ü glif testi; eksik glif varsa Türkçe destekli piksel font."

## 8. Uçağa yıldırım düşünce kimse neden çarpılmaz (teknoloji.md)
- **Şablon (5):** Eksik alan yok.
- **Süre/altyazı (3):**
  - 81 kelime / 35 sn. Promptun hızı 2,3 kelime/sn; duraklamalarla ≈35,7 sn. Sınırda.
  - Altyazı 1 (satır 86) "Ortalama bir uçağa yılda yaklaşık bir kez" 7 kelime. 6 kelime sınırını aşıyor.
- **Kanca (3):** İlk 2 saniyede "On average, an airliner is..." duyuluyor. Zayıf, edat ve zarfla açılıyor.
- **Monetizasyon (5):** Gerçek yıldırım ya da kaza görüntüsü yok, ton kaygı yaratmıyor.
- **Pano (4):** Pano "ortalama bir **ticari** uçağa" diyor. TR altyazıda "ticari" düşmüş.
- **Farklılık (2):** `#7DF9FF` 12 ile, `#FFB000` 10 ile aynı.
- **Düzeltmeler:**
  - Satır 71, 76 ve 84: İlk cümleyi "Lightning hits the average airliner about once a year. So why isn't anyone inside shocked?" yap.
  - Altyazı 1-3 (satır 86-88) şöyle olsun: "Ortalama bir yolcu uçağına" / "yılda yaklaşık bir kez yıldırım düşer." / "İçeridekiler neden çarpılmaz?"
  - Satır 82 ve 84: "Modern planes are built with protection." cümlesini çıkar, süre 35 sn'ye iner. Ekranda "KORUMALI TASARIM" kalsın.
  - Satır 101: Neon yıldırım `#7DF9FF` yerine mor-elektrik `#B388FF` kullan, çekirdek `#FFFFFF` kalsın. Uyarı amberini `#FFB000` yerine `#F2C14E` yap.
  - Döngüyü kaldır. Video panoda "KORUMA: AKTİF" satırında sakin bitsin.

## 9. Delikli kart dokuma tezgâhından geldi (teknoloji.md)
- **Şablon (5):** Eksik alan yok.
- **Süre/altyazı (3):**
  - 99 kelime / 45 sn. Promptun hızı 2,2 kelime/sn: konuşma ≈45 sn, yıllar ve duraklamalarla ≈47 sn.
  - "Swap the card, and the pattern changes." cümlesi 2. cümlenin tekrarı.
  - Altyazı 1 ve 17 yedişer kelime. Satır 161'deki not yeterli değil, çünkü listenin kendisi bölünmüş olmalı.
  - Satır 138'deki tablo altyazısı ("Delik var ya da yok: evet ya da hayır,") 9 kelime.
  - Lovelace alıntısının TR sırası EN'yi tersine çeviriyor (satır 154-156).
- **Kanca (3):** Kart ve desen değişimi soyut kalıyor. Cümle 10 kelime, ilk 2 saniyede yalnız "The punched-card idea" duyuluyor.
- **Monetizasyon (5):** Arşiv ve portre yok, tüm görsel özgün.
- **Pano (4):**
  - Başlıktan (satır 125) "fikri" kelimesi düşmüş. "Bilgisayarın delikli kartı ... geldi" kartın kendisinin tezgâhtan geldiğini söylüyor, bu fazla iddia.
  - Alıntı, Note A'daki "We may say most aptly that..." cümlesinin kırpılmış hâli. Teyit şartı zaten var.
- **Farklılık (3):** "Subscribe, and we'll keep weaving" kalıbı 3 ve 10 ile ortak. Kelime oyunu en uygun burada, bu yüzden 9'da kalsın ve diğerleri değişsin.
- **Düzeltmeler:**
  - Satır 125: Başlığı "Bilgisayarın delikli kart fikri dokuma tezgâhından geldi" yap (≤60 karakter).
  - Satır 128: Kancanın görseli tek karede olsun: kart değişince kumaştaki desen anında değişsin. İlk cümle: "Swap this card, and the fabric changes. That's where computer punch cards began." Not: "began" fazla iddia sayılırsa "That idea fed computer punch cards." kullan.
  - Satır 134 ve 140: "Swap the card, and the pattern changes." cümlesini ve altyazı 7'yi çıkar.
  - Satır 142-161: Altyazıları baştan bölünmüş yaz: "Delikli kart fikri" / "bir dokuma tezgâhından geldi." ... "Delik var ya da yok:" / "evet ya da hayır," / "bilgisayar bitleri gibi."
  - Satır 138'deki tablo altyazısını aynı biçimde böl.
  - Satır 154-156'yı şöyle yaz: "Analitik Makine cebirsel desenler dokur," / "tıpkı Jacquard tezgâhının" / "çiçek ve yaprak dokuması gibi."

## 10. Ay her yıl senden kaçıyor (uzay.md)
- **Şablon (5):** Eksik alan yok.
- **Süre/altyazı (4):** 71 kelime. Promptun hızı ≈2 kelime/sn (satır 47); geri sayım duraklarıyla ≈37 sn. Video 35 sn. Altyazıların hepsi ≤6 kelime ve sıra doğru.
- **Kanca (4):** "The Moon runs away from you" kişisel ve iyi. Tırnak benzetmesinin kaynağı hâlâ aranıyor.
- **Monetizasyon (5):** NASA fotoğrafı künyeli, logo yok.
- **Pano (3):** Pano/uzay.md satır 12 döngü kapanışının arka arkaya tekrarını yasaklıyor. 10, 11 ve 12'nin üçü de döngüyle bitiyor.
- **Farklılık (3):**
  - "Subscribe, and we'll keep..." kalıbı 3 ve 9 ile ortak.
  - Neon yeşil 7 ile, `#FFB000` 8 ile ortak.
- **Düzeltmeler:**
  - Satır 47: Hızı 2,2 kelime/sn yap. Hedef ≈34 sn.
  - Satır 27 ve 31: "We time the laser's round trip" yerine "Observatories time the laser's round trip" yaz. "We" ifadesi ölçümü bizim yaptığımızı ima ediyor.
  - Satır 30, 31 ve 51: CTA'yı "Subscribe before the Moon gets any farther." yap. Altyazı 14: "Ay daha da uzaklaşmadan abone ol."
  - Döngü 10'da kalsın, çünkü uzayan çizgi kavramın kendisi. 11 ve 12'de kaldırılsın.

## 11. Geminid yağmuru 13 Aralık (uzay.md)
- **Şablon (5):** Eksik alan yok.
- **Süre/altyazı (4):** 71 kelime. Promptun hızı 2,3 kelime/sn; duraklamalarla ≈31,7 sn. Video 30 sn. Altyazıların hepsi ≤6 kelime.
- **Kanca (3):** "On the night of December 13th, one of..." ile açılıyor. İlk 2 saniyede yalnız bir tarih duyuluyor, vaat yok.
- **Monetizasyon (4):**
  - Yapay zekâ gökyüzü "temsili" diye etiketli, bu doğru.
  - Başlık "nereye bakmalı?" diye soruyor, ama metindeki cevap yalnız "İkizler yönü, her yerde". Vaat yarım kalıyor ve hafif yanıltıcı başlık riski var.
- **Pano (3):**
  - Döngü yasağı ihlal ediliyor (pano satır 12).
  - Diğer şartlar uygulanmış: saat yok, "120" yok, "en bol yağmurlarından biri" ifadesi kullanılmış.
- **Farklılık (2):** CTA "Subscribe for the next sky alert" ile 12'nin "Subscribe for the next note" CTA'sı aynı yapıda. Inter fontu ve lacivert palet kümede.
- **Düzeltmeler:**
  - Satır 71, 76 ve 82: İlk cümleyi "December 13th, after midnight: one of the year's richest meteor showers." yap. Altyazı: "13 Aralık, gece yarısından sonra:" / "yılın en bol yağmurlarından biri."
  - Satır 77 ve 82: "That's the 13th into the 14th, midnight to dawn." yerine "The night of the 13th into the 14th, until dawn." yaz.
  - Satır 78'in ekran yazısına Türkiye (~39°K) için yön ekle: "00:00 sonrası İkizler: doğu-güneydoğu, giderek yükselir". Stellarium ile TEYİT edilsin; teyit yoksa başlığı "Geminid yağmuru: 13 Aralık gecesi nasıl izlenir?" yap.
  - Satır 80, 82 ve 102: CTA'yı "Subscribe. We'll say when to look up again." yap. Altyazı: "Abone ol, ne zaman bakacağını söyleyelim." (6 kelime). Ayrıca "How many did you count?" öncesindeki duraklamayı 0,5 sn yerine 0,3 sn yap.
  - Döngüyü kaldır. Video "KAÇ TANE SAYDIN?" kartında donsun.
  - Satır 100: Inter Light ince, yıldızlı gökte okunmaz. Inter SemiBold ve %50 koyu yumuşak kutu kullan.

## 12. Bu notayı bir kara delik çalıyor (uzay.md)
- **Şablon (5):** Eksik alan yok.
- **Süre/altyazı (4):** 89 kelime. Promptun hızı 2,2 kelime/sn; duraklamalarla ≈42 sn. Video 40 sn. Altyazıların hepsi ≤6 kelime ve sıra doğru.
- **Kanca (4):** Ses 0,3 saniyede başlıyor, osiloskop sesle oynuyor. Güçlü.
- **Monetizasyon (3):**
  - Chandra sesi 2022'den beri çok yeniden yüklendi. Videoda en çok bu ses "yeniden kullanılmış içerik" sayılabilir.
  - Ses lisansı doğrulanmadı. Kanca da tamamen bu sese bağlı.
- **Pano (2):**
  - Pano satır 74 "oktav oktav **yükseltme**: sessiz dalga formundan duyulur sese" diyor. Prompt (satır 130) tersini yapıyor, sesi 57 oktav aşağı indirip sessizlikte bitiyor. Satır 116 ise "Atama değişmedi" diyor; sapmanın gerekçesi yazılmamış.
  - Döngü yasağı ihlal ediliyor.
  - Olgusal risk: 2003'teki "57 oktav pes nota" hesaplanmış tek bir perdeydi. 2022 sonifikasyonu ise tek nota değil, çok tonlu bir uğultu. Kancada 2022 sesini çalıp "this note" demek ikisini karıştırıyor.
- **Farklılık (2):** `#7DF9FF` 8 ile, Montserrat ExtraBold 16 ile ortak. CTA 11 ile aynı yapıda.
- **Düzeltmeler:**
  - Satır 122 ve 127: Kancada kendi sentezlediğimiz tek sinüs tonunu çal. Nota adı söylenmesin; bu ton 2003 hesabındaki perdenin duyulur karşılığı olsun. Chandra 2022 sesi yalnız 5-14 aralığında ve ≤5 sn "Ses: NASA/CXC sonifikasyonu" künyesiyle kullanılsın. Böylece kanca lisansa bağımlı olmaz ve iki sesin karışma riski kalkar.
  - Satır 130 ve 134'ü pano yönüne çevir:
    - 22-31 satırının seslendirmesi: "Its real pitch is fifty-seven octaves lower. Watch it climb, octave by octave, until you can hear it."
    - Görsel: −57'den 0'a doğru tırmanan sayaç; düz çizgi giderek dalgaya dönüşür.
    - Altyazı: "Gerçek perdesi 57 oktav daha pes." / "Oktav oktav çıkıyor," / "ta ki duyana kadar."
  - Satır 132 ve 156: Döngüyü kaldır. Video duyulur sesin doruğunda "GERÇEK HALİ DUYULAMAZ" kartıyla bitsin.
  - Satır 116'ya gerekçe yaz ya da "atama ve pano akışı korunur" de.
  - Satır 132, 134 ve 156: CTA'yı "Hit subscribe and keep your ears on the sky." yap. Altyazı: "Abone ol, kulağın gökyüzünde kalsın."
  - Satır 153-154: Aktif kelime rengini `#7DF9FF` yerine limon `#C6FF3D` yap. Fontu Montserrat yerine Archivo Black yap.

## 13. Kayıtlı en eski grev (tarih.md)
- **Şablon (5):** Eksik alan yok.
- **Süre/altyazı (5):** 75 kelime. Promptun hızı 2,3 kelime/sn; duraklamalarla ≈33,6 sn. Video 35 sn. Altyazıların hepsi ≤6 kelime ve sıra doğru.
- **Kanca (4):** Keski ve "SON DAKİKA" şeridi iyi. Cümle ise haber flaşı formatını kullanmıyor ve 15 ile aynı "...years ago" kalıbında.
- **Monetizasyon (4):** "Son dakika" şeridi açıkça stilize olmalı, gerçek haber izlenimi vermemeli. Gerçek papirüs fotoğrafının lisansı teyit edilecek.
- **Pano (3):** Başlık (satır 15) "Bilinen en eski grev" diyor. Pano satır 67 "bilinen en eski **kayıtlı** grev" diyor. Başlıktaki eksik kelime pano şartını ihlal ediyor.
- **Farklılık (3):**
  - Kanca kalıbı 15 ile ortak.
  - Caveat Brush 1 ile ortak.
  - Lapis, aşı kırmızısı ve okr paleti 15 ile ortak.
- **Düzeltmeler:**
  - Satır 15: Başlığı "Bilinen en eski kayıtlı grev: tahıl gelmeyince" yap.
  - Satır 22, 28 ve 37: İlk cümleyi "Breaking news, over 3,100 years late: tomb builders walk off the job." yap. Altyazı 1-2: "Son dakika, 3100 yılı aşkın gecikmeyle:" / "mezar işçileri işi bıraktı."
  - Satır 62: Altyazı fontunu Caveat Brush yerine Noto Serif Black yap. Bu, promptun kendi yedeği; böylece 1 ile çakışma kalkar.
  - Döngü kalabilir, tarih kategorisinin tek döngüsü olsun.

## 14. BM'deki bakır kopya (tarih.md)
- **Şablon (5):** Eksik alan yok. Yapı değişikliği gerekçeli.
- **Süre/altyazı (2):**
  - Metin 90 kelime. Promptun hızı 2,1 kelime/sn: konuşma ≈42,9 sn, duraklamalarla ≈44,6 sn. Video 40 sn.
  - 0:00-0:05 satırında 13 kelime var, 6,2 sn sürüyor.
  - Altyazıların hepsi ≤6 kelime.
- **Kanca (3):** "Near the entrance to the UN Security Council chamber..." İlk 2 saniyede yalnız bir yer tarifi duyuluyor. Gerçek fotoğraf da 0:02'de geliyor.
- **Monetizasyon (4):** BM fotoğrafının lisansı teyit edilecek, yedek plan var. Fotogerçekçi tablet render'ı için beyan zorunlu.
- **Pano (5):** "Bakır kopya", "girişi yakınında", "kaynağı", yılın yokluğu ve "tartışmalı" uygulanmış.
- **Farklılık (3):** Cinzel fontu 6 ile ortak. "Unearth" kazma mecazı 3 ile ortak.
- **Düzeltmeler:**
  - Satır 93-95, 100 ve 109:
    - Gerçek BM fotoğrafı 0:00'da gelsin.
    - İlk cümle: "This copper copy at the UN reproduces a peace treaty over 3,200 years old."
    - İkinci cümle: "A 1970 gift from Turkey, near the Security Council chamber."
    - Altyazı: "BM'deki bu bakır kopya," / "3200 yılı aşkın bir barışın." / "Türkiye'nin 1970 hediyesi," / "Güvenlik Konseyi salonu yakınında."
    - 0:05-0:10 satırındaki eski "A copper copy..." cümlesini çıkar.
  - Satır 105 ve 109: "A battle still argued over. A promise that was written down." yerine "Rivals in battle. Partners on clay." yaz. Altyazı: "Savaşta rakip," / "kilde ortak."
  - Satır 106, 109 ve 140: CTA'yı "Follow for more promises carved in stone." yap. Altyazı: "Taşa yazılmış daha fazlası için takip et." (6 kelime).
  - Satır 130: Hızı 2,2 kelime/sn yap, duraklamaları 0,3 sn'ye indir. Hedef ≈40 sn.
  - Döngüyü kaldır. Video BM'deki bakır kopyanın fotoğrafında bitsin.

## 15. El-Cezeri'nin filli saati (tarih.md)
- **Şablon (5):** Eksik alan yok.
- **Süre/altyazı (3):**
  - Metin 102 kelime. Promptun hızı 2,2-2,3 kelime/sn: konuşma 44-46 sn, duraklamalarla ≈47 sn. Video 45 sn.
  - 0:26.5-0:37 satırında 27 kelime / 10,5 sn var, yani 2,57 kelime/sn.
  - Altyazı 2 "bir fil saat tasarladı" Türkçede bozuk.
- **Kanca (3):** "Eight hundred years ago..." kalıbı 13 ile aynı. Göz açan fil görseli iyi, ama cümle onu kullanmıyor.
- **Monetizasyon (4):** 1315 kopyası etiketli, Met açık erişimi teyit edilecek.
- **Pano (4):**
  - "Kova" yok, "kubbedeki adam topu bırakır" doğru, etnik etiket yok.
  - Gösteri sırası yalnız arama özetinden okundu, Met sayfası açılmadan yayın yok. Bu şart zaten yazılmış.
- **Farklılık (2):**
  - Kanca kalıbı ve paleti 13 ile ortak.
  - Ney ve minyatür üslubu 6 ile ortak.
  - CTA "next machine" kalıbında.
- **Düzeltmeler:**
  - Satır 170-171, 176 ve 186: İlk cümleyi "This elephant is a clock. And it runs without a motor." yap. "800 YIL ÖNCE" ekranda kalsın. Altyazı 1-2: "Bu fil bir saat." / "Üstelik motoru yok."
  - Satır 177 ve 186: "No motor. No electricity." yerine "No electricity either." yaz. Altyazı 4: "Elektrik de yok."
  - Satır 181 ve 186: "The rope sets off the show:" yerine "Then:" yaz. Altyazı 12: "Ardından:". Sonuç ≈95 kelime ≈43 sn.
  - Satır 183, 186 ve 217: CTA'yı "Follow if gears make you happy." yap. Altyazı: "Dişliler seni mutlu ediyorsa takip et."
  - Satır 209: Baskın rengi turkuaz `#2A8C8C` ve zümrüt `#2F6B4F` yap. Aşı kırmızısını çıkar, vurgu rengi altın kalsın.
  - Satır 216: Ney'i çıkar, yerine ud ve bakır zil koy.
  - Döngüyü kaldır. Video fil birleşip gözlerini açarken bitsin (ilk kareyle zıt).

## 16. Uzayda mum alevi neden küre olur (bilim.md)
- **Şablon (5):** Eksik alan yok.
- **Süre/altyazı (3):** 73 kelime. Promptun hızı 2,3 kelime/sn; duraklamalarla ≈32,6 sn. Video 30 sn. Altyazıların hepsi ≤6 kelime ve sıra doğru.
- **Kanca (3):** Kanca karesi (satır 14 ve 19) cevabı, yani küre ve mavi alevi, gösteriyor. 4-9 aralığındaki "In orbit, what shape?" sorusu böylece anlamsızlaşıyor. Bu yapısal bir çelişki.
- **Monetizasyon (3):** İstasyon modülünde açıkta yanan fotogerçekçi mum render'ı (prompt 1, satır 76) gerçek bir ISS sahnesi sanılabilir. Gerçek deneyler kapalı yanma haznesinde ya da düşme kulesinde yapıldı.
- **Pano (3):**
  - Pano satır 21 "oksijen **ağırlıkla** yayılarak ulaşır" diyor. Metin "Oxygen **only** spreads in" diyor (satır 23, 27, 40), bu daha mutlak bir iddia.
  - Pano gerçek NASA görüntüsünü ilk karede istiyor; prompt reveal anına taşımış. Gerekçe yazılmış ve quiz için mantıklı.
- **Farklılık (2):**
  - "Guess" ve tik-tak 1 ile ortak.
  - Lacivert ve sarı palet 5 ve 7 ile ortak.
  - Montserrat 12 ile ortak.
- **Düzeltmeler:**
  - Satır 14 ve 19: Kanca karesinde solda Dünya'daki damla alev, sağda buğulu ve "?" ile kapalı istasyon alevi olsun. Ses aynı kalsın. Küre yalnız 20-26 reveal'ında görünsün.
  - Satır 76 (prompt 1): "a single candle on a small tray floating" yerine "a candle inside a sealed transparent combustion chamber" yaz. Köşeye "TEMSİLİ" etiketi koy.
  - Satır 23, 27 ve 40: "Oxygen only spreads in." yerine "Oxygen mostly drifts in." yaz. Altyazı 11: "Oksijen çoğunlukla yayılarak gelir."
  - Satır 21 ve 27: "Soot at the tip glows yellow." cümlesini ve altyazı 7'yi çıkar. Ekran yazısına "SARI UÇ = IS" ekle. Sonuç 67 kelime ≈29,5 sn.
  - Satır 51-52: Quiz sarısı `#FFD84D` yerine mercan `#FF6B6B` kullan. Fontu Montserrat yerine Archivo Black değil, Inter Black olsun; 12 Archivo Black'e geçiyor.
  - Döngüyü kaldır. Video yan yana iki alev karesinde bitsin; bilimde döngü 17'de kalıyor.

## 17. Kahve halkasının nedeni (bilim.md)
- **Şablon (4):** Sahne tablosundaki altyazılar (satır 101, "Orta kısımdan kenara akış yenileme sağlar. / Parçacıklar kenara taşınır.") ile altyazı listesi (satır 114-115, "Ortadan kenara akış gelir. / Parçacıkları kenara taşır.") farklı.
- **Süre/altyazı (5):** 72 kelime / 35 sn ≈31 sn. Uyuyor. Altyazıların hepsi ≤6 kelime.
- **Kanca (3):** "Why this coffee stain is a ring was published in Nature." İngilizcede dolambaçlı bir cümle; TTS'te de kulakta da takılır.
- **Monetizasyon (5):** Kendi çekimimiz ve çizimimiz, risk düşük.
- **Pano (4):** Altyazı 4 "Su en çok kenardan çıkar" bir şiddet kıyası ekliyor. Promptun kendi doğruluk notu da bunu riskli buluyor (satır 151).
- **Farklılık (3):** Palet 18 ile neredeyse aynı. CTA "Follow along." çok genel.
- **Düzeltmeler:**
  - Satır 94, 99 ve 107: İlk cümleyi "Why does coffee dry into a ring? The answer ran in Nature." yap. Altyazı: "Kahve neden halka bırakır?" / "Cevap Nature'da yayımlandı."
  - Satır 100 ve 113: Altyazıyı "Su kenardan buharlaşır." yap.
  - Satır 101: Tablo altyazısını listeyle aynı yap: "Ortadan kenara akış gelir." / "Parçacıkları kenara taşır."
  - Satır 104, 107 ve 141: CTA'yı "Follow, and spill something on purpose with us." yap. Altyazı: "Takip et, bilerek dökelim." Bu, monetizasyon için de özgün bir ses tonu.
  - Döngü kalsın, bilim kategorisinin tek döngüsü bu olsun. 18 renk değiştiriyor.

## 18. Parmak suda buruşması ve sinirler (bilim.md)
- **Şablon (4):**
  - CTA'nın ("Subscribe for more.") altyazısı ne listede (satır 187-203) ne tabloda (satır 182) var.
  - Satır 181'deki ekran yazısında yazım hatası var: "KARELKAS". Doğrusu "KAREKLAS".
- **Süre/altyazı (2):**
  - Metin 82 kelime. Promptun temposu "yavaş-orta", ≈2,1 kelime/sn: konuşma ≈39 sn, duraklamalarla ≈40 sn. Video 35 sn.
  - Tablo altyazıları 7 kelime: satır 180 ("Bir hipotez: buruşukluklar yağmur lastiği dişi gibi,") ve satır 181 ("Bir deneyde ıslak bilyeler daha hızlı taşındı.").
- **Kanca (5):** Gerçek parmak çekimi ve "sinir kesilirse buruşmaz" en şaşırtıcı olguyu ilk saniyeye taşıyor.
- **Monetizasyon (3):**
  - Konu tıbbi, sinir kesisi. Yapay zekâ sesine "sakin doktor" personası verilmiş (atama ve satır 206). Bu, tıbbi otorite izlenimi ve sentetik sesle uzman taklidi riski taşıyor.
  - "Eğitim amaçlıdır" notu ve kansız kesik doğru seçimler.
- **Pano (5):** Hasta grubu yok, yüzde yok, hipotez dili kullanılmış, iki karşıt çalışma birlikte veriliyor.
- **Farklılık (3):** Palet 17 ile aynı. "Bilmiyoruz" kapanışı 4 ile ortak. CTA çok genel.
- **Düzeltmeler:**
  - Satır 166 ve 206: Personayı "sakin bilim anlatıcısı; doktor, uzman ya da hekim kimliği iddiası yok" yap. Gerekçesini yaz: yapay zekâ sesi ve sağlık konusu birleşince tıbbi otorite taklidi riski doğuyor.
  - Satır 179 ve 185: "An old observation from the 1930s:" yerine "A 1930s observation:" yaz. Altyazı 6: "1930'lardan bir gözlem:"
  - Satır 181 ve 185: "One experiment: wet marbles moved faster with wrinkled fingers. Another study found no advantage." yerine "One test found a wet-grip edge. Another found none." yaz. Altyazı: "Bir deney ıslakta avantaj buldu." / "Bir başkası bulamadı." Ekran yazısını "KAREKLAS 2013 / HASELEU 2014" olarak düzelt.
  - Satır 182 ve 185: "Your fingers know something. We just don't know what yet." yerine "Why they wrinkle? The jury's still out." yaz. Altyazı: "Neden buruşuyor?" / "Karar henüz çıkmadı."
  - Satır 182, 185 ve 223: CTA'yı "Subscribe, and check your fingers next bath." yap. Altyazı listesine ekle: "Abone ol, banyoda parmaklarına bak." Sonuç ≈68 kelime ≈34 sn.
  - Satır 180 ve 181: Tablo altyazılarını listedeki bölünmüş hâline getir.
  - Satır 209: Paleti 17'den ayır. Rapor mavisi `#2B6CB0` yerine petrol `#2A9D8F`, metin rengi `#264653`, damar kırmızısı `#D64F4F` yerine mercan `#E76F51` olsun. Sinir sarısı kalsın.
  - Döngüyü kaldır. Video "HENÜZ KESİN DEĞİL" kartında bitsin.

---

## Çekim öncesi kontrol listesi (açık TEYİT'ler, promptlardan derlendi)
- 1: Deneyin gerçek sonucu çekilecek; kanca ona göre yazılacak.
- 3: Britannica ve Oxford Companion girişleri okunacak. Ayrıca 5 dk Türkçe YouTube araması yapılacak (pano şartı).
- 7: QR adresi belirlenip iki telefonla taranacak.
- 9: Lovelace Note A metni birebir karşılaştırılacak.
- 10: Tırnak benzetmesinin kaynağı bulunacak.
- 11: IMO/AMS sayfaları ve Stellarium'dan yön kontrolü yapılacak. Yayın 8-11 Aralık.
- 12: Chandra ses lisansı okunacak.
- 13: Tapınak adları bilimsel baskıdan, papirüs lisansı Museo Egizio'dan kontrol edilecek.
- 14: BM fotoğrafının lisansı ve konumu kontrol edilecek.
- 15: Met 57.51.23 sayfası okunacak; gösteri sırası buna göre doğrulanacak.
- 16: NASA görselinin ISS mi düşme kulesi mi olduğu künyesinden teyit edilecek.
