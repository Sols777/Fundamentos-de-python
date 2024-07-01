# class Person:
#     # definimos propriedades e comportamentos (métodos)
#     # construtor - inicializa uma instância
#     def __init__(self, name: str, age: int):
#         self.__name = name
#         self.__age = age
#         # self.__name - private
#         # self._name - protected
   
#     def __str__(self): # toString __repr__
#         return f"O(a) {self.__name} tem {self.__age} anos!"
 
#     # getters - buscar informação
#     def getName(self):
#         return self.__name
    
#     def getAge(self):
#         return self.__age
   
#     # setters - atualizar
#     def setName(self, name):
#          self.__name = name


        
#     def setAge(self, age):
#          self.__age = age


 
# p = Person("Bruno", 33) # instância do objeto Pessoa
# p.setName("Bruna")
# p.setAge(25)
# print(p.getName())
# print(p.getAge())
# print(p)

# [3:53 PM] Pedro Mendonça - FORMADOR PRT
# class Person:
#     def __init__(self, name: str, age: int):
#         self._name = name
#         self._age = age
   
#     def __str__(self): # toString
#         return f"O(a) {self._name} tem {self._age} anos!"
   
#     def hello(self):
#         print("Hello from Person class")
 
#     # getters - buscar informação
#     def getName(self):
#         return self._name
   
#     def getAge(self):
#         return self._age
   
#     # setters - atualizar
#     def setName(self, name):
#         self._name = name
 
#     def setAge(self, age):
#         self._age = age
 
# class Employee(Person):
#     def __init__(self, name: str, age: int, salary: float):
#         super().__init__(name, age)
#         self._salary = salary
   
#     def __str__(self):
#         return super().__str__() + f" O meu salário é {self._salary}"
   
#     def hello(self):
#         print("Hello from Employee class")
 
# def addEmployee():
#     print("\nPor favor insira os dados do empregado:\n")
#     name = input("Nome: ")
#     age = int(input("Idade: "))
#     salary = eval(input("Salário: "))
#     return Employee(name, age, salary)
 
 
# listEmployee = []
# for i in range(2):
#     listEmployee.append(addEmployee())
 
# for employee in listEmployee:
#     print(employee)
#     print(type(employee))
#     print(employee.getName())
 