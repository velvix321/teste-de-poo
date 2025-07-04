class  bancoDeDados():
    def __init__(self, nome, idade, numero):
        self._nome = nome
        self._idade = idade
        self._numero = numero
    
    def mostra_usuario(self):
        print(f"{self._nome}, {self._idade}, {self._numero}")
    
class usuario(bancoDeDados):
    def __init__(self, nome, idade, numero):
        super().__init__(nome, idade, numero)
    
    def mostra_usuario(self):
        super().mostra_usuario()


class admin(bancoDeDados):
    def __init__(self, nome, idade, numero):
        super().__init__(nome, idade, numero)
    
    def mostra_usuario(self):
        super().mostra_usuario()
    
    @property
    def nome(self):
        return self._nome  
    
    @nome.deleter
    def nome(self):
        if hasattr(self, "_nome"):
            print("nome deletado")
            del self._nome
        else:
            print("nome ja foi deletado")


    @property
    def idade(self):
        return self._idade

    @idade.deleter
    def idade(self):
        if hasattr(self, "_idade"):
            print("idade deletada")
            del self._idade
        else:
            print("idade ja foi deletado.")
    

    @property
    def numero(self):
        return self._numero
    
    @numero.deleter
    def numero(self):
        if hasattr(self, "_numero"):
            print("numero deletado")
            del self._numero
        else:
            print("numero ja deletado")
