class Usuario():
  _nomeUsuario = ""

  def setNome(self, nome):
    self._nome = nome

  def getNome(self):
        return "Olá, me chamo " + self._nome 

class Admin(Usuario):

  def escrevaNome(self):
    return "Admin"

  def digaOla(self):
    return "Olá Admin " + self._nome 

admin1 = Admin()
admin1.setNome("Baltazar")
admin1.getNome()
print (admin1.getNome())
print (admin1.digaOla())


#O problema em questão é que não há como acessar uma propriedade privada. 