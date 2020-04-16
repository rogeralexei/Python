#Lista de nombres prohibidos

with open('usuarios.txt') as usuariosprob:
    usuarios = usuariosprob.read().split('\n')
    print(usuarios)

def pruebanombre(nombre):

    if nombre.capitalize() in usuarios:
    
       return print('Nombre invalido... Intente nuevamente')
    
    else:

       return print('Nombre valido')

def reglasdeljuego():
    
    print('\nMe vas a escribir un nombre, si el nombre es valido te lo dire')
    print('\nSi no es valido (uno de los prohibidos en nuestra base de datos ), te regresare hasta que des con un nombre valido.')

if __name__ == '__main__':
    
    print('Bienvenido a esta lista de usuarios prohibidos...')
    print('\nTe explico como funciona: ')
    reglasdeljuego()

    resp = input('Estas preparado?? \nR/. ')
    if resp == 'si':

        nombreprueba = ''

        while True:

            nombreprueba = input('\nIngresa un nombre: \n R/. ')

            pruebanombre(nombreprueba)

            if nombreprueba.capitalize() not in usuarios:
                break
    
    print('Fue un placer, nos vemos!!!')

    
    