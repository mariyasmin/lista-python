class Usuario:
    nome = str(input("Digite seu primeiro nome: "))
    sobrenome = str(input("Digite seu sobrenome: "))    

    segundonome = "Jane"
    segundosobrenome = "Silva"

    def hello(self):
        return "Olá, "

usuario1= Usuario()
usuario2 = Usuario()
print(usuario1.hello(), usuario1.nome , usuario1.sobrenome) 
print(usuario2.hello(), usuario2.segundonome , usuario2.segundosobrenome)

