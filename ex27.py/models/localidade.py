class Localidade:
    def __init__(self, localidade , id):
        self._localidade = localidade
        self._id = id
 
    def __str__(self):
        return f"Localidade: {self._localidade} "