class Pessoa():
    def __init__(self, nome, peso, idade, comendo=False, dormindo=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
    def comer(self, comendo):
        if self.dormir:
            print(f"{self.nome} não pode comer dormindo")
            return
        if self.falar():
            print(f"{self.nome} não pode falar comendo ")
            return
        print(f"{self.nome} está comendo")
        self.comendo=True
    def falar(self):
        print("aaa")
    def dormir(self):
        print("Dorme muito")


