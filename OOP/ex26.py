class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
   
    def __str__(self): # toString
        return f"O(a) {self._name} tem {self._age} anos!"
   
    def hello(self):
        print("Hello from Person class")
 
    # getters - buscar informação
    def getName(self):
        return self._name
   
    def getAge(self):
        return self._age
   
    # setters - atualizar
    def setName(self, name):
        self._name = name
 
    def setAge(self, age):
        self._age = age
 
class Aluno(Person):
    def __init__(self, name: str, age: int, curso: float):
        super().__init__(name, age)
        self._curso = curso
   
    def __str__(self):
        return super().__str__() + f" O meu Curso é {self._curso}"
   
    def hello(self):
        print("Hello from Aluno class")
 
class Funcionario(Person):
    def __init__(self, name: str, age: int, salary: float , cargo: str):
        super().__init__(name, age)
        self._salary = salary
        self._cargo = cargo
   
    def __str__(self):
        return super().__str__() + f" O meu salário é {self._salary} e o meu cargo e {self._cargo}"
   
    def hello(self):
        print("Hello from Funcionario class") 
 
def addAluno():
    print("\nPor favor insira os dados do Aluno:\n")
    name = input("Nome: ")
    age = int(input("Idade: "))
    curso = input("Curso: ")
    return Aluno(name, age, curso)

def addFuncionario():
    print("\nPor favor insira os dados do empregado:\n")
    name = input("Nome: ")
    age = int(input("Idade: "))
    salary = eval(input("Salário: "))
    cargo = input("Cargo: ")
    return Funcionario(name, age, salary , cargo)
 
 
listFuncionario = []
for i in range(3):
    listFuncionario.append(addFuncionario())

listAluno = []
for i in range(2):
    listAluno.append(addAluno()) 
 
for funcionario in listFuncionario:
    print(funcionario)

 
for aluno in listAluno:
    print(aluno)
