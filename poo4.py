#Exercício Usuario (privado)

class Usuario:
    
    __primeiroNome = ""

    def primeiroNome(self, primeiroNome):
        self.__primeiroNome = primeiroNome

    def nomeUsuario(self):
        return f"{self.__primeiroNome} é o primeiro nome do usuário."

user1 = Usuario()
user1.primeiroNome("Joe")
print(user1.nomeUsuario())

#Exercício Empregado

class Empregado:

    def __init__(self, nomeEmpregado, projeto):

        self.nomeEmpregado = nomeEmpregado
        __salario = ""
        self.projeto = projeto

    def trabalho (self):
        return f"Nome do funcionário: {self.nomeEmpregado} \nNome do projeto: {self.projeto}"

    def setSalario(self, salario):
        self.__salario = salario
    
    def mostrar (self):
        return f"Nome do funcionário: {self.nomeEmpregado} \nSalário: {self.__salario}"

funcionario1 = Empregado("Mariana", "Projeto das Crianças")
print(funcionario1.trabalho())

funcionario1.setSalario(2000.00)
print(funcionario1.mostrar())

#Exercício Robo

class Robo():
    __nome = ""
    __ano_construcao = ""

    def diga_alo(self):
        return f"O nome do robô é {self.__nome} , ano de construção: {self.__ano_construcao}"
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setAnoConstrucao(self, ano_construcao):
        self.__ano_construcao = ano_construcao
    
robo1 = Robo()
robo1.setNome("Taylor")
robo1.setAnoConstrucao("1989")
print(robo1.diga_alo())

#Exercício Laptop

class Laptop:

    __preco = ""

    def get_preco(self):
        return f"Preço do laptop: {self.__preco}"
    
    def set_preco(self, preco):
        self.__preco = preco

laptop1 = Laptop()
laptop1.set_preco(4700.00)
print(laptop1.get_preco())   

#Exercício pessoa

class Pessoa:

    __primeiroNome = ""
    __ultimoNome = ""

    def getPrimeiroNome(self):
        return f"O nome é {self.__primeiroNome}"
    
    def getUltimoNome(self):
        return f"O sobrenome é {self.__ultimoNome}"

    def setPrimeiroNome(self,nome):
        self.__primeiroNome = nome

    def setUltimoNome(self, sobrenome):
        self.__ultimoNome = sobrenome

pessoa = Pessoa()
pessoa.setPrimeiroNome("João")
pessoa.setUltimoNome("Carvalho")
print(pessoa.getPrimeiroNome())
print(pessoa.getUltimoNome())