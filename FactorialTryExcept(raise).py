#******************* Factorial Try-Except (raise Method) *******************#

def _factorial():
    # Sonsuz döngü, geçerli bir değer alana kadar ya da break komutuna gelene kadar devam et.
    while True:
        try:
            n = int(input('Number: ')) # Kullanıcıdan değer alıyoruz.
            if n <= 0:# Girilen değer 0 eşit ya da 0 dan küçükse if döngüsüne gir.
                raise Exception("Factorial cannot take numbers less than 0.") # raise methodu ile kendi hata mesajımızı yazdırıyoruz.
            else: # Girilen değerin faktoriyelini alıp kullanıcıya gösterir.
                total = 1
                for i in range(1,n+1):
                    total *= i 
                print(f'Result = {total}')
                break # İşlem doğruysa döngüden çık.
        except ValueError: # Eğer kullanıcı geçersiz bir giriş yaparsa fırlatılacak hata.
            print(f"Enter a number!")
        except Exception as exc: # Eğer kullanıcı 0 y ada 0 dan düşük bir sayı girerse fırlatılacak hata.
            print(f"Exception: {exc}")
        
# Fonksiyonu çağırıyoruz.            
_factorial()