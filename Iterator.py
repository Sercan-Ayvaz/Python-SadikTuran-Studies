
#********************** ITERATOR **********************
"""
Iterator, bir koleksiyonun (örneğin bir dizi, liste veya harita) elemanlarını sırayla gezmek için kullanılan bir tasarım desenidir.
An iterator is a design pattern used to traverse the elements of a collection (such as an array, list, or map) sequentially.

for item in list: # list elemanlarını gezer. - Iterates through the elements of the list.
    print(item)
"""
# list = [1,2,3,4,5,6,7,8,9,10]

# iterList = iter(list)

"""
print(next(iterList)) #list[0]
print(next(iterList)) #list[1]
print(next(iterList)) #list[2]
print(next(iterList)) #list[3]
print(next(iterList)) #list[4]
print(next(iterList)) #list[5]
"""

   
# İter yapısının while ile kullanımı - Using the 'iter' construct while
'''
while True:
    try:
        print(next(iterList))
    except StopIteration:
        break
'''
    
#******************** Sample Study ********************
class NumbersIter:
    def __init__(self, start,stop):
        # Returning itself to indicate that this class is an iterator
        # Başlangıç ve bitiş değerlerini ayarlıyoruz
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        # Returning itself to indicate that this class is an iterator
        # Bu sınıfın bir iterator olduğunu belirtmek için kendisini döndürüyoruz
        return self
    
    def __next__(self):
        # If the start value is less than or equal to the stop value, perform the if operation
        # Eğer başlangıç değeri bitiş değerine eşit veya küçükse if işlemini yapıyor
        if self.start <= self.stop:
            result = self.start #Mevcut başlangıç değerini kaydediyoruz - Storing the current start value
            self.start += 1 # Başlangıç değerini bir artırıyoruz - Incrementing the start value
            return result
        else:
            # If the start value is greater than the stop value, we raise a stop signal
            # Eğer başlangıç değeri bitiş değerinden büyükse, durma sinyali veriyoruz
             raise StopIteration

# Creating an instance of the NumbersIter class to return numbers from 10 to 20
# NumbersIter sınıfından bir nesne oluşturuyoruz, 10'dan 20'ye kadar sayıları döndürmek için         
list = NumbersIter(10,20)
myIter = iter(list)# Iterator nesnesini oluşturuyoruz - Creating the iterator object

while True:
    try:
        result = next(myIter)
        print(result)
    except StopIteration:
        # Eğer StopIteration hatası alırsak, döngüyü kırıyoruz
        # Breaking the loop if we receive a StopIteration error
        break
    


    
