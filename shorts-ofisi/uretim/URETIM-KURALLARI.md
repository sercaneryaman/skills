# Üretim kuralları (2026-11-27'den itibaren her video için)

## Görsel araştırma
- Her video için konuya ait gerçek kaynaklar taranır: ansiklopedi, makale, müze ve kütüphane arşivleri, kamu kurumu sayfaları.
- Yalnızca kamu malı (PD) veya açık lisanslı (CC BY, CC BY-SA) görsel kullanılır. Lisans, dosyanın Wikimedia Commons sayfasından (`action=raw`) okunarak doğrulanır.
- Öncelikli kaynaklar: Wikimedia Commons, ABD kamu kurumları (USGS, NOAA, NPS, NASA; PD-USGov), 1930 öncesi eserler (ör. Biodiversity Heritage Library levhaları).
- Ekranda kısa kaynak satırı yazılır: "Foto: USGS (kamu malı)", "Harita: …, CC BY-SA 3.0".
- Telifli belgesel klibi, stok video veya yapay zekâyla gerçek gibi gösterilen hayvan kullanılmaz. Kendi çizimimiz ana görseldir; gerçek görsel destek kartı olur.
- Ağ notu: Commons API'si bu ortamda sık sık 429 verir. Dosyayı doğrudan `upload.wikimedia.org/wikipedia/commons/<md5[0]>/<md5[:2]>/<Ad>` yolundan indirmek çalışır.

## Türkçe metin (seslendirme ve altyazı)
- Yazım TDK Yazım Kılavuzu'na göre yapılır: kesirler ayrı yazılır ("üçte iki"), özel ada gelen ek kesme işaretiyle ayrılır ("Kuzey Amerika'da"), "hâlâ" düzeltme işaretiyle yazılır.
- Cümleler devrik kurulmaz; özne başta, yüklem sonda olur. Soru cümleleri doğal konuşma sırasını korur.
- Yabancı terimler TDK sözlüğündeki biçimiyle yazılır (glikoz, antifriz). Bilimsel ad italik ve Latince kalır (Rana sylvatica).
- Seslendirmede zor kelimeler (j, ğ, uzun ünlüler) için ek çekim yapılır, Whisper ile kontrol edilir. Kötü okunan kelime varsa cümle yeniden kurulur.
- sozluk.gov.tr bu ortamdan erişilemiyor. Şüpheli kelimede web araması ve Yazım Kılavuzu kuralı ile karar verilir.
