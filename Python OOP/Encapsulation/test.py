class Person:
    
    def __init__(self, age=0):
        self.__age = age
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age < 18: self.__age = 18
        else: self.__age = age
       
person = Person(25)
print(person.age) # 25
person.age = 10
print(person.age) # 18        
