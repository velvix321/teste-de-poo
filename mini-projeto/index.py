class  banco_de_dados():
    def __init__(self, nome, idade, numero):
        self._nome = nome
        self._idade = idade
        self._numero = numero
    
class usuario(banco_de_dados):
    def __init__(self, nome, idade, numero):
        super().__init__(nome, idade, numero)
    
    @property
    def mostra_usuario(self):
        print(f"{self._nome}, {self._idade}, {self._numero}")

class admin(banco_de_dados):
    def __init__(self, nome, idade, numero):
        super().__init__(nome, idade, numero)
    
    @property
    def idade(self):
        return self._idade
    
    @property
    def nome(self):
        return self._nome  
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def mostra_tudo(self):
        print(f"{self._nome}, {self._idade}, {self._numero}")
    
    @nome.deletar
    def nome(self):
        if hasattr(self, "_nome"):
            print("nome deletado")
            del self._nome
        else:
            print("nome ja foi deletado")

    @idade.deletar
    def idade(self):
        if hasattr(self, "_idade"):
            print("idade deletada")
            del self._idade
        else:
            print("idade ja foi deletado.")
    
    @numero.deletar
    def numero(self):
        if hasattr(self, "_numero"):
            print("numero deletado")
            del self._numero
        else:
            print("numero ja deletado")
