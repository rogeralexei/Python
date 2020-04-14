
# Putting Article Object

class Articulo:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity




# Getting Users
with open('usuarios.txt') as userfiles:
    usuarios = eval(userfiles.read())

# Getting Articlees
with open('articulos.txt') as articlefiles:
    articulos = eval(articlefiles.read())

# Add Articles Function
def addarticles(name,quantity,price):
    if name in articulos.keys():
        print('Ese articulo ya esta aqui!')
    else:
        articulos[name] = {}
        articulos[name]['Precio'] = price
        articulos[name]['Cantidad'] = quantity

# Modifi Articles Function
def modarticles(name):
    if name not in articulos.keys():
        print('Este articulo no esta en el inventario')
        return
    else:
        print('Que quisieras cambiar? \n')
        print('1. Nombre')
        print('2. Precio')
        print('3. Cantidad')

        while True:
            try:

                modopt = int(input('\n R./ '))
                
            except ValueError:

                print('Porfavor, elija un numero entero entre 1 y 3')

            else:

                if modopt == 1 or modopt == 2 or modopt == 3:

                    break

                else:

                    print('Porfavor, elija entre el numero 1 y 3')

        if modopt == 1:
            quantity = articulos[name]['Cantidad']
            price = articulos[name]['Precio']
            articulos.pop(name)
            newname = input('Como quisiera llamarlo?\n R./  ')
            addarticles(newname,quantity,price)
            return
        elif modopt == 2:
            while True:
                try:

                    newprice = float(input('Que precio le pondra al articulo?\n R./  '))
                    
                except ValueError:

                    print('Porfavor, solamente escriba numeros (se aceptan decimales para este cambio)')
                else:
                    break

            articulos[name]['Precio'] = newprice
            return
        elif modopt == 3:
            while True:
                try:

                    newquantity = int(input(f'Cuanto hay de {name}?\n R./  '))
                    
                except ValueError:

                    print('Porfavor, Solo numeros enteros')
                else:
                    break

            articulos[name]['Cantidad'] = newquantity

# Show Articles Function
def articleslist():
    i = 1
    print('Articulo / Precio / Cantidad')
    for articulo,props in articulos.items():
        precio = props['Precio']
        cantidad = props['Cantidad']
        print(f'=> {articulo} / $ {precio} / {cantidad}u  ') 
        i+=1         

# Sign in Sign Up Function
def signinup():

    while True:
        print('\n1. Iniciar Sesion')
        print('\n2. Registrarse')
        try:
            resp = int(input('\n R/. '))
            
        except ValueError:

            print('Porfavor, elija un numero entero entre 1 y 2')

        else:

            if resp == 2 or resp == 1:

                break

            else:

                print('Porfavor, elija entre el numero 1 y 2')

    if resp == 1:

        user = input('\nPorfavor, ingrese su usuario \n R/. ')
        
        while user not in usuarios:

            logtry = user
            
            user = input("\nUsuario incorrecto favor ingrese su usuario nuevamente. \n R/. ")

            if user in usuarios:
                break 
            elif user == 'regresar':
                break
    if resp == 2:

        user = input('\nPorfavor, ingrese su nuevo nombre de usuario \n R/. ')
         
        while user in usuarios:

            user = input('Este usuario ya esta registrado, porfavor ingrese otro \n R/. ')
        
        usuarios.append(user)
        

    return user

if __name__ == '__main__':
    
    user = signinup()
        

    print(f'\nBienvenido {user}, que deseas hacer?')
    
    while True:

        print('\n1. Crear un nuevo Articulo.')
        print('2. Modificar un Articulo.')
        print('3. Eliminar un Articulo.')
        print('4. Ver Lista')
        print('5. Salir.')
        
        while True:
            try:

                will = int(input('R/. '))

            except ValueError:

                print('Porfavor, elija un numero entero entre 1 y 4')
            
            else:

                if will == 1 or will == 2 or will == 3 or will == 4 or will == 5:

                    break

                else:

                    print('Porfavor, elija entre el numero 1 y 4')


        if will == 1:

            # Getting New Article Data
            newarticlename = input("Porfavor ingresa el nuevo articulo a agregar: \n R/. ")
            while True:
                try: 
                    newarticleprice = float(input('Cuanto costara el nuevo articulo? \n R/. '))
                except ValueError:
                    print('Porfavor, solamente numeros...')
                else:
                    break
            while True:
                try: 
                    newarticlequantity = int(input("Ahora ingresa la cantidad: \n R/. "))
                except ValueError:
                    print('Porfavor, solamente numeros...')
                else:
                    break
            articulo1 = Articulo(newarticlename,newarticleprice,newarticlequantity)
            addarticles(newarticlename,newarticlequantity,newarticleprice)

        elif will == 2:
            # Modifying
            articleslist()
            modart = input('Cual articulo quisieras modificar? \n R/. ')
            modarticles(modart)

        elif will == 3:
            # Deleting
            articleslist()
            modart = input('Que articulo quisiera eliminar? \n R/. ')
            
            if modart not in articulos.keys():

                print('Este articulo no esta en el inventario')

            else:

                articulos.pop(modart)
                print('Algo mas?')
        elif will == 4:

            articleslist()
            print('\n Algo mas??')
        else: 

            print('De acuerdo... nos vemos!')
            break
    with open('usuarios.txt', mode='w') as userfiles:
        userfiles.write(repr(usuarios))

    with open('articulos.txt', mode='w') as articlefiles:
        articlefiles.write(repr(articulos))




