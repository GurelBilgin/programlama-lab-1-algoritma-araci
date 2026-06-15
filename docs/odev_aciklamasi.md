# Ödev Açıklaması

Bu çalışma, temel Python programlama konularını uygulamalı olarak göstermek amacıyla hazırlanmıştır. Program, kullanıcıdan veri alarak farklı algoritma problemlerini çözen menülü bir konsol uygulamasıdır.

## Kapsanan Konular

1. Liste işlemleri
2. İç içe döngüler
3. Fonksiyon kullanımı
4. Matris işlemleri
5. Dosya okuma
6. Sözlük ve frekans hesaplama
7. Hata yönetimi
8. Recursive/iteratif algoritma karşılaştırması
9. Matematiksel algoritmalar
10. Modüler proje yapısı

## Geliştirme Notları

İlk sürümde tüm kod tek Python dosyasında bulunuyordu. Bu sürümde algoritmalar `algorithms.py` dosyasına, kullanıcı menüsü ise `cli.py` dosyasına taşındı. Böylece kodun okunabilirliği, test edilebilirliği ve sürdürülebilirliği artırıldı.

## Çalıştırma

```bash
pip install -e .
algoritma-araci
```

## Test

```bash
python -m unittest discover -s tests
```
