#Exercício Registro-Email

class Usuario: 
    def __init__(self, nome):
        self.nome = nome

    def hello (self):
        return f"Olá, {self.nome}"
    def registrar (self):
        return ">> registrado."

    def mail (self):
        return ">> e-mail enviado."

        
usuario1 = Usuario ("Jane")
print(usuario1.hello(), usuario1.registrar(), usuario1.mail())


#Exercício Carro

class Carro:
    
    def __init__(self, marcaCarro, nomeMotorista):
        self.marcaCarro = marcaCarro    
        self.nomeMotorista = nomeMotorista
        
    def ligar (self):
        return f" O {self.marcaCarro} está sendo ligado"

    def dirigir (self):
        return f"{self.nomeMotorista} é quem dirige o/a {self.marcaCarro}."

    def frear (self):
        return f"O {self.marcaCarro} foi freado"

    def desligar (self):
        return f"{self.nomeMotorista} desligou o/a {self.marcaCarro}."

carro = Carro("BMW", "Mariana")
print(carro.ligar())
print(carro.dirigir())
print(carro.frear())
print(carro.desligar())
