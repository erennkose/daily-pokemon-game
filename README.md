# Pokemon Wordle - Tahmin Oyunu

Bu proje, Wordle tarzında bir Pokemon tahmin oyunudur. Oyuncu, verilen ipuçlarını kullanarak günlük Pokemon'u bulmaya çalışır.

## Oyun Kuralları
- Oyuncunun **6 tahmin hakkı** vardır.
- Her tahminde, girilen Pokemon'un **isim, boy, kilo ve tür** bilgileri kontrol edilir.
- Doğru tahminler **🟢 (Yeşil)** ile gösterilir.
- Yakın tahminler **🟡 (Sarı)** ile gösterilir (Boy ve kilo için geçerlidir).
- Yanlış tahminler **🔴 (Kırmızı)** ile gösterilir.
- Eğer oyuncu Pokemon'u doğru tahmin ederse, oyun sona erer.
- Tüm haklar bitene kadar doğru tahmin yapılamazsa, günün Pokemon'u açıklanır.

## Oyun Akışı
1. Günlük Pokemon rastgele belirlenir.
2. Kullanıcı bir Pokemon ismi girerek tahminde bulunur.
3. Kullanıcının tahmini ile günlük Pokemon karşılaştırılır ve geribildirim verilir.
4. Kullanıcı doğru tahmine ulaşana kadar veya tahmin hakları bitene kadar devam eder.
5. Oyun sonunda sonuç gösterilir.

## Örnek Çıktı
```
Günün pokemonunu tahmin edin (6 hakkınız kaldı.): Pikachu
Name: Pikachu --> 🔴
Height: 0.4 meters --> 🟡
Weight: 6.0 kilograms --> 🔴
Type: Electric --> 🔴
...
Bugünün Pokemon'unu 4 tahminde buldunuz! 😄
```

## Geliştirme
- Henüz yalnızca konsol üzerinden kullanıma açık ancak yakın zamanda bir application veya web sitesi şekline de oyunu geliştirme amacım mevcuttur.

**İyi eğlenceler! 🎮**

