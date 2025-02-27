#************************* Dekortor And Time Module *************************#

import math
import time

# Fonksiyonun çalışma süresini hesaplayan dekoratör
def calculateTime(func):
    def inner(*args, **kwargs):
        start = time.time()  # Başlangıç zamanını al
        result = func(*args, **kwargs)  # Orijinal fonksiyonu çağır
        finish = time.time()  # Bitiş zamanını al
        print(f'Fonksiyon {func.__name__} {finish - start:.6f} saniye sürdü')  # Süreyi yazdır
        return result  # Orijinal fonksiyonun dönüş değerini döndür
    return inner

@calculateTime
def usAlma(a, b):
    print(math.pow(a, b))  # a'nın b. kuvvetini hesapla ve yazdır

@calculateTime    
def faktoriyel(num):
    print(math.factorial(num))  # num'nun faktöriyelini hesapla ve yazdır

# Fonksiyonları çağır
usAlma(2, 3)
faktoriyel(5)