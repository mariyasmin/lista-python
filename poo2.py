class Usuario:
  primeironome = "Jonnie"
  ultimonome = "Bravo"

  def hello(self):
    return "Olá, " + self.primeironome + " " + self.ultimonome

usuario1 = Usuario()
print (usuario1.hello())