# Algoritma Aracı

Bu proje, **Programlama Lab 1** dersi kapsamında geliştirilen temel algoritma uygulamasının düzenlenmiş ve GitHub'a uygun hâle getirilmiş sürümüdür. Uygulama, kullanıcıya konsol üzerinden menü sunar ve seçilen algoritmayı çalıştırır.

## Özellikler

- k'ncı en küçük benzersiz elemanı bulma
- Hedef sayıya en yakın sayı çiftini bulma
- Tekrar eden elemanları listeleme
- Matris çarpımı yapma
- Metin dosyasından kelime frekansı hesaplama
- Listedeki en küçük değeri bulma
- Newton-Raphson yöntemiyle karekök hesaplama
- Öklid algoritmasıyla EBOB hesaplama
- Asal sayı kontrolü
- Fibonacci sayısı hesaplama

## Proje Yapısı

```text
programlama-lab-1-algoritma-araci/
├── data/
│   └── giris_metni.txt
├── docs/
│   └── odev_aciklamasi.md
├── src/
│   └── algoritma_araci/
│       ├── __init__.py
│       ├── algorithms.py
│       └── cli.py
├── tests/
│   └── test_algorithms.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Kurulum

Projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/GurelBilgin/algoritma-araci.git
cd algoritma-araci
```

Sanal ortam oluşturmanız önerilir:

```bash
python -m venv .venv
```

Windows için:

```bash
.venv\Scripts\activate
```

macOS/Linux için:

```bash
source .venv/bin/activate
```

Projeyi geliştirilebilir modda kurun:

```bash
pip install -e .
```

## Kullanım

Kurulumdan sonra menülü uygulamayı şu komutla başlatabilirsiniz:

```bash
algoritma-araci
```

Alternatif olarak doğrudan modül olarak da çalıştırabilirsiniz:

```bash
python -m algoritma_araci.cli
```

Kelime frekansı özelliğini denemek için örnek dosya yolu olarak şunu verebilirsiniz:

```text
data/giris_metni.txt
```

## Testleri Çalıştırma

Bu projede testler Python'un standart `unittest` modülüyle yazılmıştır. Ek paket kurulumu gerekmez.

```bash
python -m unittest discover -s tests
```

## Eski Sürüme Göre İyileştirmeler

- Kod tek dosyadan çıkarılarak modüler yapıya dönüştürüldü.
- Algoritma fonksiyonları `input()` ve `print()` işlemlerinden ayrıldı.
- Hatalı girişler için daha tutarlı hata yönetimi eklendi.
- Tip ipuçları ve docstring açıklamaları eklendi.
- Kelime frekansı hesabında noktalama işaretleri temizlendi ve Türkçe karakter desteği korundu.
- Asal sayı kontrolü `sqrt(n)` sınırına kadar optimize edildi.
- En yakın çift bulma algoritması iki işaretçili yöntemle iyileştirildi.
- Test dosyası eklendi.
- `README.md`, `.gitignore` ve `pyproject.toml` dosyaları eklendi.

## Algoritmaların Kısa Açıklaması

| İşlem | Kullanılan Yaklaşım | Açıklama |
|---|---|---|
| k'ncı en küçük eleman | Sıralama + benzersizleştirme | Liste `set()` ile benzersizleştirilir ve sıralanır. |
| En yakın çift | Sıralama + iki işaretçi | Toplamı hedefe en yakın olan çift aranır. |
| Tekrar eden elemanlar | `Counter` | Her elemanın kaç kez geçtiği hesaplanır. |
| Matris çarpımı | Çarp-topla | Klasik matris çarpımı uygulanır. |
| Kelime frekansı | Regex + `Counter` | Metin kelimelere ayrılır ve frekans hesaplanır. |
| Karekök | Newton-Raphson | Yaklaşık karekök iteratif olarak hesaplanır. |
| EBOB | Öklid algoritması | Bölme kalanına dayalı klasik yöntem kullanılır. |
| Asal kontrolü | Bölen arama optimizasyonu | Sadece `sqrt(n)` değerine kadar kontrol edilir. |
| Fibonacci | İteratif hesaplama | Gereksiz recursive çağrılar engellenir. |

## Katkıda Bulunanlar

- Gürel Bilgin
- Berkay Aras
