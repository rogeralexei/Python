class Articulo:
  def __init__(self, nombre, precio, cantidad):
    self.nombre=nombre
    self.precio=precio
    self.cantidad=cantidad
class Usuario:
    def __init__(self,nombre):
        self.nombre=nombre
lista={}
listaDeUsuarios=open("Usuarios.txt","a+").read().split('\n')
for usuario in listaDeUsuarios:
        if usuario in lista.keys():
            lista[usuario]+=1
        else:
            lista[usuario]=1
if __name__:"__main__"
# Creating a Registration Class
print("Hola, te gustaria registrarte?\n")
print("1.Si, me gustaria\n")
print("2. Ya estoy Registrado\n")
print("3. No, no quiero\n\n")

registration=int(input(("Seleccione la opcion(numero) deseada: ")))

if registration==1:
    print("\nDe acuerdo, vamos a registrarte...\n")
    Usuario.nombre=input('Dame un nombre de usuario: ')
    while(Usuario.nombre in lista.keys()):
        usuario=input('Ese usuario ya esta registrado; porfavor escribe otro: ')
    lista.write("\n"+usuario)

