#*********** Basic Inhertince-Polymorphism ****************

# Person sınıfı superclasses(mother class) olarak oluşturuldu. 
class Person:
    def __init__(self,firstName,lastName): # !! Yapıcı Method (Constructor) !!
        self.firstName = firstName
        self.lastName = lastName
        print(f"Person Created = Name: {firstName} Surname: {lastName}")
        
    def who_am_i(self): # !! Override !! -- !! Polimorfizm (Plymorphism) !!
        print('I am a person')
    
    def eat(self):
        print("I am a eating")                
# Person sınıfından miras alınmış student sınıfı subclasses (child class) olarak oluşturuldu.
class Student(Person):
    def __init__(self,firstName,lastName,studentNumber): # !! Yapıcı Method (Constructor) !!
        Person.__init__(self,firstName,lastName) # Superclassın yapıcı methodunu çağırıyoruz.
        self.studentNumber = studentNumber
    
    def who_am_i(self): # !! Override !! -- !! Polimorfizm (Plymorphism) !!
        print(f'I am a student number {self.studentNumber}')
        
        
# Person sınıfından miras alınmış teacher sınıfı subclasses (child class) olarak oluşturuldu.       
class Teacher(Person):
    def __init__(self,firstName,lastName,branch): # !! Yapıcı Method (Constructor) !!
        super().__init__(firstName,lastName) # Superclassın yapıcı methodunu 'super()' methoduyla çağırıyoruz.
        self.branch = branch
    
    def who_am_i(self): # !! Override !! -- !! Polimorfizm (Plymorphism) !!
        print(f'I am a {self.branch} teacher')
        
# Nesne oluşturma. -- Object created.
p1 = Person('Sercan','Ayvaz')
s1 = Student('Seçkin','Ayvaz',1234)
t1 = Teacher('Sadik','Turan','Math')

# Her nesnenin 'eat()' methodunu çağırıyoruz.
print(f'{p1.eat()} -- {s1.eat()} -- {t1.eat()}')

# Her nesnenin 'who_am_i()' methodunu çağırıyoruz.
print(f'{p1.who_am_i()} -- {s1.who_am_i()} -- {t1.who_am_i()}')
