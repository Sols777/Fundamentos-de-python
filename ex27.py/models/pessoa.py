class Pessoa:
    def __init__(self, name, id , telefone , email , nif , localidade_id):
        self._name = name
        self._age = age
        self._id = id

 
    def __str__(self):
        return f"Nome: {self._name} Idade: {self._age}"