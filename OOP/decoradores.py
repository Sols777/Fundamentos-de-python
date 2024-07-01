
class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
   
    def __str__(self): # toString
        return f"O(a) {self._name} tem {self._age} anos!"
   
    def hello(self):
        print("Hello from Person class")
 
    # getters - buscar informação
    @property
    def name(self):
        return self._name
 
    @property
    def age(self):
        return self._age
   
    # setters - atualizar
    @name.setter
    def name(self, name):
        self._name = name
 
    @age.setter
    def age(self, age):
        self._age = age
 
 
p1 = Person("João", 30)
p1.name = "Maria"
print(p1.name)
 
# print(p1.getName())
# p1.setName("Maria")