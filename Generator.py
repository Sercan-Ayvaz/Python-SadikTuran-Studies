#**************************** GENERATOR ******************************

'''
Generator, Python'da bir iteratör oluşturmanın daha basit ve daha verimli 
bir yoludur. Generator'lar, bir fonksiyonun içinde 'yield' anahtar kelimesini 
kullanarak tanımlanır. Bu, fonksiyonun çalışmasını durdurup, mevcut durumu 
saklayarak bir değer döndürmesine olanak tanır. Daha sonra, fonksiyon tekrar 
çağrıldığında, kaldığı yerden devam eder.

Generator'ların bazı önemli özellikleri şunlardır:
1 - Bellek Verimliliği,
2 - Lazy Evaluation (Tembel Değerlendirme),
3 - Kolay Kullanım

/////////////////////////////////////////////////////////////////////////
A generator is a simpler and more efficient way to create an iterator in Python. 
Generators are defined using the yield keyword within a function. This allows 
the function to pause its execution, save its current state, and return a value.
Later, when the function is called again, it resumes from where it left off.

Some important features of generators are:

Memory Efficiency
Lazy Evaluation
Ease of Use
'''

def generator(num):
    count = 1
    while count <= num:
        yield count  # Mevcut sayıyı döndür ve durumu sakla - Return current number and store state
        count += 1   # Sayıyı bir artır - Increase the number by one

# Generator'ı oluştur - Creating generator
counter = generator(5)

# Generator'ı kullan - Using generator
for number in counter:
    print(number)