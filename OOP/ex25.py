class Estudante:
    def __init__(self, name: str, telefone: int , email: str):
        self.__name = name
        self.__telefone = telefone
        self.__email = email

   
    def __str__(self):
        return f"EU sou  o(a) estudante {self.__name}!"

    # GETTERS
    def getName(self):
        return self.__name
    
    def getTelefone(self):
        return self.__telefone 
    
    def getEmail(self):
        return self.__email
   
    # setters 
    def setName(self, name):
         self.__name  = name

    def setTelefone(self, telefone):
        self.__telefone  = telefone

    def setEmail(self, email):
         self.__email = email


 
estudante1 = Estudante("Bruno", 916387437 , "email1@email.com") # instância do objeto Pessoa
estudante2 = Estudante("Joao", 916323437 , "email2@email.com") # instância do objeto Pessoa
estudante3 = Estudante("Maria", 912387437 , "email3@email.com") # instância do objeto Pessoa
estudante4 = Estudante("Joana", 911287437 , "email4@email.com") # instância do objeto Pessoa
print(estudante1.getName() , estudante1.getEmail() , estudante1.getTelefone())
estudante1.setName("Bruna")
estudante1.setTelefone(9199939191)
estudante1.setEmail("email@email.com")
print(estudante1.getName() , estudante1.getEmail() , estudante1.getTelefone())
print(estudante1)
