class Usuario:

    def __init__(self, primeiroNome, ultimoNome):
        self.primeiroNome = primeiroNome
        self.ultimoNome = ultimoNome

    def getNomeCompleto(self):
        return f"O primeiro nome do usuário é {self.primeiroNome} e seu sobrenome é {self.ultimoNome}."

usuario1 = Usuario("Johhny" , "Bravo")
print (usuario1.getNomeCompleto())
