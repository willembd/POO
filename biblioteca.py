"""class Pessoa():
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
"""




"""class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f"O {self.nome} foi comer")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f"O gato {self.nome} foi miando...")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def late(self):
        print(f"O cachorro {self.nome} está  latindo...")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome, cor)

    def murge(self):
        print(f"A vaca {self.nome} está mugindo...")
    def comer(self):
        print(f"A vaca {self.nome} está comendo capim")

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def pula(self):
        print(f"O coelho {self.nome} está pulando...")"""

class Ingresso():
    def __init__(self, valor):
        self.valor=valor
    def imprimeValor(self):
        print(f"Valor do Ingresso R${self.valor}")

class Vip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor*1.5)

    def imprimeValor(self):
        print(f"Valor do Ingresso  Vip R${self.valor}")


class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcularArea(self, base, altura):
        self.area= base*altura
        print(f"A area do retangulo é {self.area}")

    def calcularPerimetro(self, base, altura):
        self.perimetro = (base+altura)*2
        print(f"A perimetro do retangulo é {self.perimetro}")

class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base=base
        self.altura=altura
    def calculaArea(self):
        self.area=(self.base*self.altura)/2
        print(self.area)
    def calculaPerimetro(self):
        self.perimetro=self.base*3
        print(self.perimetro)