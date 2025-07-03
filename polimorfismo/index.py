class animal():
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        print("som de animal")
    
class cachorro(animal):
    def emitir_som(self):
        return "au au!"

class gato(animal):
    def emitir_som(self):
        return "miau"