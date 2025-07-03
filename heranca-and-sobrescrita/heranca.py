class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def assinatura(self):
        print("esta pessoa esta assinando")
    
class aluno(pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    
    def cadastro(self):
        print(f"nome: {self.nome}, idade:{self.idade}, matricula:{self.matricula}")
    
    #sobreescrita abaixo
    def assinatura(self):
        super().assinatura()
        print("esta pessoa assinou a ata")