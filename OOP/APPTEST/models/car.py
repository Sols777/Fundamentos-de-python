
class Car:
    def __init__(self, make, model):
        self._make = make
        self._model = model
 
    def __str__(self):
        return f"{self._make} - {self._model}"