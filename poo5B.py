#Exercício Bola

class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor (self, novaCor):
        self.cor = novaCor

    def mostraCor(self):
        return f"A cor é {self.cor}"

    def mostraMaterial(self):
        return f"O matérial é {self.material}"


bola = Bola("Azul", 25, "Borracha")
bola.trocaCor("Amarela")
print(bola.mostraCor())
print(bola.mostraMaterial())

#Exercício Quadrado 

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudaValor(self, novoLado):
        self.lado = novoLado
        return f"O novo valor do lado é {self.lado} cm"
    
    def retornaValor(self):
        return f"O lado do quadrado é de {self.lado} cm"
    
    def calculaArea (self):
        return f"A área do quadrado é de {self.lado * 2} metros quadrados"

quadrado = Quadrado(8)
quadrado.mudaValor(10)
print(quadrado.retornaValor())
print(quadrado.calculaArea())

#Exercício Retângulo

class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudaLados(self, novaBase, novaAltura):
        self.base = novaBase
        self.altura = novaAltura
        return f"A nova base é de {self.base} cm e a nova altura de {self.altura} cm"

    def retornaLados(self):
        return f"A base é de {self.base} cm e a altura de {self.altura} cm"

    def areaRet(self):
        return f"A área do retângulo é de {(self.base * self.altura) / 2} metros quadrados"
    
    def perimetroRetangulo(self):
        return f"O perímetro é de {(self.base * 2)+(self.altura * 2)} cm"

retangulo = Retangulo(5,6)
print(retangulo.areaRet())
print(retangulo.perimetroRetangulo())

retangulo2 = Retangulo(
    base = int(input("Base do local: ")),
    altura = int(input("Altura do local: "))
)
print(retangulo2.areaRet())
print(retangulo2.perimetroRetangulo())

#Exercício Salário

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def nomeSalario(self):
        return f"O funcionário se chama {self.nome} e seu salário atual é de R$ {self.salario}"

    def salarioNovo (self, porcentagem):
        porcentagemAumento = (porcentagem * self.salario) / 100
        self.salario = self.salario + porcentagemAumento
        return f"O salário atual é de R$ {self.salario}"

func1 = Funcionario("Mariana", 5000)
print(func1.salarioNovo(15))
print(func1.nomeSalario())