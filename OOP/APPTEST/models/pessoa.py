
class Pessoa:
    def __init__(self, name, age):
        self._name = name
        self._age = age
 
    def __str__(self):
        return f"Nome: {self._name} Idade: {self._age}"