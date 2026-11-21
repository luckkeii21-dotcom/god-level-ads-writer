# Müşteri Profili: Online Ticaret Üniversitesi (Digiens Akademi dahil)

_Oluşturulma: 2026-11 | Kaynak: Kullanıcı (ekip içi reklam yazım pratiği) | Durum: `[TESTED]` CTA mimarisi ekip pratiğinde kullanılıyor; ses tonu kalibrasyonu için örnek senaryolar bekleniyor_

> Bu dosya, kullanıcı **Online Ticaret Üniversitesi**, **OTÜ** veya **Digiens / Digiens Akademi / DGNS / Digiens AI**
> için reklam istediğinde otomatik okunur. Türkiye Modu (`../turkey-market.md`) her zaman
> birlikte açıktır. Bu dosyadaki kurallar, SKILL.md'deki genel kurallarla çatışırsa **bu dosya kazanır**.

---

## 1. Kimlik ve Reklam Türleri

- **Pazar:** Türkiye, Türkçe. Hitap: **sen**.
- **Alan:** E-ticaret, girişimcilik, dijital pazarlama ve kişisel gelişim eğitimleri.
- **Reklam türleri (sıklık sırasıyla):**
  1. **Lansman reklamları:** Ön lansman (bekleme listesi), kayıtların açılışı, kapanış/son gün
  2. **Eğitim satış reklamları:** Program, kurs, atölye, webinar kaydı
  3. **İşe alım reklamları:** Ekip ilanları (Digiens Akademi vb.)
- **Bağlam (yazarın bilgisi için, reklamda zorunlu değil):** Digiens Akademi (yazımı: "Digiens"), Fatih Çoban'ın ekibi;
  hedef kitlede bilinen bir marka. Marka adını hafifçe kullan; kurucu adını ve tanıtım
  bilgilerini kullanıcı istemedikçe reklama doldurma.
- **Ses:** Enerjik, net, girişimci dili. Somut rakam, gerçek sonuç, dürüst beklenti.
  Kurumsal broşür dili yok, abartı yok (Türkiye Modu Bölüm 4 yasaklı liste geçerli).

> **TODO (kalibrasyon):** Ekibin en iyi performans veren 2-3 reklam senaryosu bu dosyaya
> "Örnek Senaryolar" başlığıyla eklenince ses tonu bu örneklere göre ayarlanacak.

---

## 2. CTA Mimarisi (lansman ve eğitim reklamları; SKILL.md "tek CTA" kuralının yerine geçer)

> **İşe alım reklamlarında bu mimari UYGULANMAZ.** İşe alım ilanında tek CTA, sonda (Bölüm 5).

**Temel kural:** Tek **eylem**, birden çok **an.** CTA her seferinde aynı eylemi ister
(aynı link, aynı buton). İki farklı eylem ("forma git" + "DM at") asla aynı reklamda olmaz.
Değişen sadece CTA'nın söyleniş biçimi ve arkasındaki ikna ilkesidir.

### 2.1 Süreye göre CTA yerleşimi

| Reklam süresi | CTA sayısı | Yerleşim |
|---------------|-----------|----------|
| 60 sn'ye kadar | 2 | **Erken CTA** (hook bittikten sonra, en geç 20. saniye) + **Final CTA** |
| 60 sn-2 dk | 3 | Erken CTA (en geç 20. sn) + **Orta CTA** (yaklaşık ortada) + Final CTA |
| 2 dk üzeri (mini VSL, lansman videosu) | 4+ | Erken CTA (en geç 20. sn) + her 60-90 saniyede bir hatırlatma + Final CTA (son bölümde 2 kez) |

### 2.2 Her CTA'nın görevi farklıdır

- **Erken CTA (izin CTA'sı):** Kısa ve baskısız. Hemen karar vermiş olanı kaybetmemek için.
  "Link aşağıda, izlerken açık dursun." / "Kendini tanıdıysan başvuru linki açıklamada."
- **Orta CTA (gerekçe CTA'sı):** Az önce verilen bilgiye bağlanır. "Bunu zaten yapıyorsan
  seni arıyoruz, link açıklamada."
- **Final CTA (karar CTA'sı):** Kıtlık + süre + net eylem. Gerçek bir son tarih ve kontenjan
  varsa burada söylenir. "Kontenjan 40 kişi, kayıtlar pazar 23.59'da kapanıyor. Linke tıkla."

### 2.3 Görsel kural
CTA anlarında ekranda **aynı CTA sticker'ı / yazısı** görünür (örn. "BAŞVURU LİNKİ AŞAĞIDA ↓").
Final CTA'da sticker son saniyeye kadar ekranda kalır. Ses kapalı izleyen her CTA'yı okuyabilmeli.

### 2.4 Senaryo formatı (bu müşteri için)
```
[HOOK | 0-3 sn]
[BRIDGE | 3-x sn]
[CTA 1: ERKEN | en geç 20. sn]
[BODY 1]
[CTA 2: ORTA | sadece 60 sn üzeri]
[BODY 2]
[CTA 3: FİNAL | son 8-12 sn]
```
Her bloğun yanına kullanılan ikna ilkesi etiketlenir: `[CIALDINI: Kıtlık]`. Bu etiketler
ekip içi içindir; prompter metninden çıkarılır.

---

## 3. Cialdini'nin İkna İlkeleri (her reklamda zorunlu)

Ayrıntılı tanım ve örnekler: `../frameworks.md` Bölüm 12. Bu müşteri için kurallar:

- Her reklamda **en az 4 ilke** kullanılır ve senaryoda etiketlenir.
- Strateji planına "Cialdini Haritası" maddesi eklenir: hangi ilke, hangi saniyede, nasıl.
- **Kıtlık ve aciliyet gerçek olmalı.** Gerçek kontenjan, gerçek son tarih. Sahte geri sayım
  ve "son 3 kişi" yalanı Türk reklam hukukunda aldatıcı uygulamadır ve markaya güveni yakar.
- **Sosyal kanıt doğrulanabilir olmalı.** Öğrenci sayısı, mezun sonucu, takipçi sayısı
  kullanıcıdan alınır; yoksa `[X]` yer tutucusu konur. Uydurma rakam yazılmaz.
- **Otorite gerçek unvanla.** Türkiye Modu Bölüm 7.3 (yanıltıcı unvan yasağı).

### İlkelerin reklam türlerine göre öncelikli kullanımı

| Reklam türü | Öncelikli ilkeler |
|-------------|-------------------|
| Ön lansman / bekleme listesi | Karşılıklılık (ücretsiz değer), Tutarlılık (küçük evet: listeye katıl), Birlik |
| Kayıt açılışı | Sosyal kanıt, Otorite, Kıtlık (kontenjan) |
| Kapanış / son gün | Kıtlık (süre), Tutarlılık ("listeye katılmıştın"), Sosyal kanıt (kaç kişi katıldı) |
| Eğitim satışı (evergreen) | Otorite, Sosyal kanıt, Karşılıklılık |
| İşe alım | Kıtlık (pozisyon sayısı), Sempati (ekip içi), Tutarlılık (mikro evet + başvuru görevi), Karşılıklılık (videoda değer ver), Otorite/Sosyal kanıt (ekibin ölçeği) |

---

## 4. Lansman Reklamı Kalıpları

**Ön lansman (bekleme listesi):** Hook → değer (ücretsiz ipucu/mini ders) → Erken CTA
(listeye katıl) → neden şimdi → Final CTA. Teklifin fiyatı söylenmez; merak ve değer satılır.

**Kayıt açılışı:** Hook (sonuç veya merak) → Erken CTA → program ne veriyor (somut) → kanıt →
Orta CTA → kontenjan/süre → Final CTA.

**Kapanış (son 24-48 saat):** Hook doğrudan süre ile ("Kayıtlar bu gece 23.59'da kapanıyor.")
→ Erken CTA → kaç kişi katıldı → en sık sorulan itiraz cevabı → Final CTA.

**Eğitim reklamlarında Türkiye uyarısı:** Gelir vaadi ("ayda X TL kazan") Meta ve Reklam Kurulu
açısından risklidir. Gerçek ve belgeli öğrenci sonuçlarını, "sonuçlar kişiye göre değişir"
çerçevesiyle kullan (Türkiye Modu Bölüm 6.2).

---

## 5. İşe Alım Reklamları (Digiens Akademi ve ekip ilanları)

_Kullanıcı geri bildirimi, 2026-11: "Bu kadar prodüksiyonlu ve sürekli CTA olmasına gerek yok.
Aradığımız kişiye ulaşmamız daha önemli."_ `[TESTED: kullanıcı onaylı kural]`

Genel format: `../ad-formats.md` Format 9. Bu müşteri için kurallar:

- **Yapı sadece üç parça:** Hook → Ana metin → CTA. Strateji planı, çoklu CTA, Cialdini
  etiketleri, prodüksiyon notu, varyasyon yığını gerekmez (istenirse eklenir).
- **Prodüksiyon hafif:** Ekipten biri kameraya konuşur, altyazı. Ekran kaydı, sticker, efekt şart değil.
- **Tek CTA, sonda.** Başvuru kanalı açıklamada yazar (bu ekipte: CV + video linkleri e-postayla).
- **Maddeleri sıralama, kişiyi betimle.** İlan maddelerinin hepsini sayma. En önemli 3-4
  özelliği seçip, o özelliklere sahip kişiyi birkaç cümleyle "sen" diliyle anlat. Aday kendini
  bu betimlemede tanımalı. Tam liste açıklama metnine kısa bir paragraf olarak girer.
- **Betimleme şart kipiyle yazılır:** "çevirebiliyorsan, biliyorsan, deniyorsan" (sen + -sa/-se).
  "Çevirebiliyorsun, biliyorsun" gibi bildirme kipi kullanılmaz; aday kendini koşulda tanır.
- **Akış: paralel şart cümleleri, bağlaçsız.** Özellikler "ve", "yarı yoldasın" gibi bağlaç ya da
  ara yorumla birbirine bağlanmaz. Her biri kısa, aynı kalıpta bir şart cümlesi olur, alt alta
  dizilir ve tek bir sonuçta toplanır ("...aradığımız kişi sen olabilirsin."). Sıra işten
  sonuca gider (kurgu → yapay zekâ → algoritma → hesabı büyütme), böylece her ifade bir
  öncekini pekiştirir. Caydırıcı ya da "eksiksin" hissi veren ifade kullanılmaz.
- **Yetkinliği unvanla değil, yaptığı işle anlat:** "sosyal medya uzmanı", "algoritmaya hâkim"
  demek yerine davranışı söyle: "o videonun ne zaman, nasıl paylaşılınca öne çıkacağını
  biliyorsan", "bir hesabı büyütebiliyorsan".
- **Şirket yapısını anlatma:** Aynı ekip birden fazla şirkete çalışıyor; bunu ve marka
  konumlandırma iddialarını ("... denince akla gelen ekip") ilanda kullanma.
- **Özellik kısmı kısa:** En fazla 2 cümle. Öncelik: kurgu + yapay zekâ, girişimcilik/eğitim
  içerik deneyimi.
- **İş yerini öv:** Adayın ne kazanacağını anlat (işlerin büyük kitleye ulaşması, bilinen bir
  ekibin mutfağında olmak, uzaktan çalışma). Klişe ("dinamik ekip", "harika ortam") yok, somut ol.
- **Güncel tercih (2026-11-17): Maaşın dolar olduğu söylenmez.** Çekici unsurlar uzaktan çalışma
  ve kendi içerik fikirlerini hayata geçirebilmek; bunlar pozisyon cümlesinden hemen sonra,
  şart cümlelerinin ilki olarak gelir ("...bir ekibin parçası olmak istiyorsan,"). Aşağıdaki
  dolar kalıbı yalnızca kullanıcı açıkça isterse kullanılır.
- **(Eski) Maaş CTA'ya bağlanır:** Kullanıcının onayladığı kalıp: "Kariyerini bir üst noktaya taşıyıp
  dolar üzerinden gelir sağlayarak kendini geliştireceğin bir ekibe dahil olmak istiyorsan,
  CV'ni ve kurguladığın birkaç videonun linkini açıklamadaki mail adresine gönder."
- **Yapay zekâ "her gün kullanılan" bir şey olarak değil, projelerde destek alınan bir araç
  olarak anlatılır:** "yapay zekâdaki yenilikleri takip edip projelerinde ondan destek alabiliyorsan".
- **Pozisyonu etiketle değil, bakış açısıyla tanımla:** "grafik tasarım temelli video editör"
  yerine "tasarımcı gözüyle kurgu yapan video editör".
- **"Bir adım öndesin" kalabilir;** değişken olan, ondan önceki tercih edilen deneyimdir
  (sosyal medya ilanında girişimcilik/eğitim içeriği, içerik ilanında reklam videosu).
- **İş yeri artısı gerçek ve somut olmalı:** Erişim ("editlediğin reklamlar her gün binlerce
  kişiye ulaşıyor"), yeteneği farklı alanlarda kullanma, uzaktan çalışma. "Rakamlarla
  göreceksin" gibi soyut vaatler zayıf kalır.
- **Terim: "edit", "kurgu" değil.** Ekip edit yapıyor, video editör arıyor. Yaptığı iş
  "edit / editlemek" diye anlatılır ("editlediğin reklamlar", "editlerine yansıtabiliyorsan").
  Kurgu, editin güçlü olması gereken bir parçasıdır, işin adı değildir.
- **Ekibin tasarım işleri:** Statik reklam tasarımları ve landing page tasarımları. Reklam
  kapağı tasarımı YOK. "Her detayda senin imzan olacak" gibi gerçeği abartan ifadeler kullanılmaz.
  Uygun kalıp: "Tasarım altyapını statik reklamlarda, landing page'lerde de konuşturacaksın."
- **"Daha önce reklam videosu editlediysen bir adım öndesin"** bu ekip için onaylı bağlayıcıdır.
- **Aşırı spesifik iş yükü verme.** "Günde 6 video" gibi iç operasyon rakamları yerine tempo
  genel ifadeyle anlatılır ("yoğun üretim temposu", "her sabah kısa toplantı").
- **Çekici unsurlar net söylenir:** Tamamen uzaktan çalışma, dolar bazlı maaş. Bunlar başvuru
  getirir; betimleme ise yanlış kişiyi eler. İkisi birlikte kaliteli başvuru getirir.
- **Uyum:** Meta'da "İstihdam" özel reklam kategorisi; yaş, cinsiyet, medeni durum şartı yok;
  e-postayla gelen CV'ler için KVKK aday aydınlatma metni.

### Pozisyon özetleri
- **Sosyal Medya Video Editörü:** Öncelikli özellikler: (1) uzun yayından güçlü kısa video
  çıkarma ve hook, (2) hikâye bütünlüğü bozmadan kurgu, (3) kurgu araçları + yapay zekâ
  hâkimiyeti, (4) tercihen kişisel marka/girişimcilik/eğitim/iş dünyası içerik deneyimi.
  (5) sosyal medya hesap yönetimi: paylaşım düzeni, algoritma bilgisi, hesabı büyütme
  (ilanda örtük anlatılır, "uzman" denmez).
  Diğerleri: varyasyon üretimi, platform ve trend bilgisi, performans yorumu, üretim hızı,
  mesai ve iletişim disiplini.- **İçerik Ekibi Video Editörü (grafik tasarım temelli):** Grafik tasarım eğitimli, kariyerine
  video editör olarak devam eden, multidisipliner biri (kendi kendine öğrenmiş/alaylı profil
  aranmıyor, ama bu ilanda açıkça söylenmez; "tasarım eğitimini kurguyla birleştirebiliyorsan"
  gibi örtük ifade edilir). Premiere Pro, After Effects, Photoshop, Illustrator; yapay zekâyı
  ekibin bir parçası gibi aktif kullanır; hook mantığını bilir; ağırlıkla reklam videosu
  editler, gerektiğinde statik reklam ve landing page tasarımı yapar (kapak tasarımı yok).
  Ekip çalışmalarından çıkan ek ihtiyaçlar: telefonda okunan tipografi ve safe zone, kusursuz
  Türkçe yazım, sade ve tek fikirli grafik dili, aynı çekimden farklı kurgu versiyonları.

### Onaylanmış örnek senaryo (ses tonu referansı) `[KULLANICI ONAYLI]`
Sosyal Medya Video Editörü ilanı, kullanıcının son hâli:
```
Digiens Akademi'nin sosyal medya ekibine bir video editör arıyoruz.

Uzun bir yayının en güçlü anını kısa, akıcı bir videoya çevirebiliyorsan,
yapay zekâyı kurguna katabiliyorsan,
sosyal medya algoritmasına hâkimsen ve bir hesabı büyütebiliyorsan,
aradığımız kişi sen olabilirsin.

Daha önce girişimcilik, eğitim ya da kişisel marka içeriği kurguladıysan bir adım öndesin.

Burada kurguladığın videolar her gün binlerce girişimciye ulaşıyor. Üstelik tamamen uzaktan çalışıyoruz.

Kariyerini bir üst noktaya taşıyıp dolar üzerinden gelir sağlayarak kendini geliştireceğin bir
ekibe dahil olmak istiyorsan, CV'ni ve kurguladığın birkaç videonun linkini açıklamadaki mail
adresine gönder.
```
Kalıp: Pozisyon cümlesi → paralel şart cümleleri → "aradığımız kişi sen olabilirsin" →
"bir adım öndesin" (tercih edilen deneyim) → iş yeri artısı + uzaktan → maaşı bağlayan CTA.

## 6. Yayınlanan Reklamlar Kaydı

| Tarih | Reklam | Tür | Durum / Sonuç |
|-------|--------|-----|---------------|
| 2026-11 | Digiens Akademi: Sosyal Medya Video Editörü ilanı (v1, çok CTA'lı) | İşe alım | Kullanıcı reddetti: fazla prodüksiyon, fazla CTA, fazla spesifik |
| 2026-11 | Digiens Akademi: Sosyal Medya Video Editörü ilanı (v2, hook + ana metin + CTA) | İşe alım | Kullanıcı revize istedi: iş yerini öv, özellikleri kısalt, şart kipi, maaşı CTA'ya bağla |
| 2026-11 | Digiens Akademi: Sosyal Medya Video Editörü ilanı (v3) | İşe alım | Revize: sosyal medya/algoritma yetkinliği örtük eklendi, "akla gelen ekip" cümlesi çıkarıldı |
| 2026-11 | Digiens Akademi: Sosyal Medya Video Editörü ilanı (v4) | İşe alım | Revize: "yarı yoldasın" caydırıcı, akış karmaşık |
| 2026-11 | Digiens Akademi: Sosyal Medya Video Editörü ilanı (v5, paralel şart cümleleri) | İşe alım | Kullanıcı onayladı (küçük düzenlemeyle), yayına hazır |
| 2026-11 | Digiens Akademi: İçerik Ekibi Video Editörü ilanı (v1) | İşe alım | Revize: "grafik tasarım temelli" etiketi, AI "her gün", "bir adım öndesin", tasarım cümlesi ve zayıf ikna değişecek |
| 2026-11 | Digiens Akademi: İçerik Ekibi Video Editörü ilanı (v2) | İşe alım | Revize: "kurgu" yerine "edit", kapak değil statik reklam + landing page, "imzan olacak" çıkacak |
| 2026-11 | Digiens Akademi: İçerik Ekibi Video Editörü ilanı (v3) | İşe alım | Yazıldı, onay bekleniyor |
| 2026-11-17 | Digiens Akademi: Sosyal Medya Video Editörü ilanı (v6, kullanıcı taslağından) | İşe alım | Uzaktan/fikir artısı başa alındı, dolar maaş çıkarıldı; onay bekleniyor |
| 2026-11-17 | Digiens Akademi: İçerik Ekibi Video Editörü ilanı (v4) | İşe alım | "Tamamen uzaktan çalışacağın ve kendini geliştireceğin bir ekibe dahil olmak istiyorsan" başa alındı, dolar çıkarıldı; CTA "Kariyerini bir üst noktaya taşımak istiyorsan..." |
