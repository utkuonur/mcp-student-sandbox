# MCP Student Sandbox

Bu proje, öğrenci sandbox ortamında çeşitli Python modüllerini test etmek ve geliştirmek için oluşturulmuştur. Kod kalitesi, güvenlik ve modülerlik üzerine odaklanılmıştır.

## Dosyalar

### failing_calculator.py
Ortalama oran hesaplayıcı fonksiyonu. Sıfıra bölme hatası düzeltilmiştir.
- **Fonksiyon**: `average_ratios(numbers)`
- **Kullanım**: Sayı listesi alır, her birinin 100/x oranını hesaplar ve ortalamasını döndürür. 0 değerleri atlanır, tümü 0 ise hata fırlatır.

### mystery_module.py
İkinci derece denklem köklerini hesaplayan modül.
- **Fonksiyon**: `fn_x(a, b, c)`
- **Kullanım**: a*x² + b*x + c = 0 denkleminin köklerini döndürür. Gerçek kök yoksa None döndürür.

### secret_leak.py
AWS bağlantı modülü. Güvenlik için hardcoded key kaldırılmıştır.
- **Fonksiyon**: `connect()`
- **Kullanım**: Environment variable'dan AWS_SECRET_KEY alır. Yoksa hata fırlatır.

### spaghetti_logic.py
Veri işleme modülü. Modüler hale getirilmiştir.
- **Fonksiyonlar**: `calculate_total`, `format_total`, `process_data_pure`, `print_results`, `log_results`, `process_data`
- **Kullanım**: Veri listesi alır, çarpan uygular, formatlar, yazdırır ve loglar.

## Kurulum
1. Python 3.8+ gerekli.
2. Virtual environment oluştur: `python -m venv .venv`
3. Aktifleştir: `.venv\Scripts\activate` (Windows)
4. Gerekli paketler: `pip install python-dotenv` (secret_leak için)

## Kullanım Örnekleri

### mystery_module.py
```python
from mystery_module import fn_x

roots = fn_x(1, -3, 2)  # x² - 3x + 2 = 0
print(roots)  # (2.0, 1.0)
```

### Diğer Modüller
Her dosya bağımsız çalıştırılabilir veya import edilebilir.

## Güvenlik Notları
- Hiçbir dosyada hardcoded şifre veya key bulunmaz.
- Environment variables kullanın.
- Kod, clean code prensiplerine göre düzenlenmiştir.

## Katkıda Bulunma
1. Branch oluşturun.
2. Değişikliklerinizi commit edin.
3. Pull Request açın.

## Lisans
Bu proje eğitim amaçlıdır.