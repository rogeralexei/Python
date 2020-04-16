#Lista de palabras prohibidas

# Abriendo el archivo con las palabras prohibidas
with open('palabras.txt') as rarastxt:
    prohibido = rarastxt.read().split('\n')

# Funcion que hace el juego entero jejeje
def prueba():
    
    
    while True:
        
        fallo = True
        
        while fallo:

            palabra = input('\nIngresa una palabra: \n R/. ')
            
            fallo = unapalabra(palabra)

        fallo = True
        if palabra.capitalize() in prohibido:
        
            print(f'\n{palabra.capitalize()} => Palabra Invalida... Intente nuevamente')
        
        else:
           
            print(f'\n{palabra.capitalize()} => Palabra Valida')

            # Viendo si el usuario quiere jugar de nuevo
            while fallo:
                
                masintentos = input('\nTe gustaria jugar otra vez?? (Si o No) \nR/. ')

                fallo = siono(masintentos)  

            if masintentos.lower() == 'no':
                print('\nMuchas gracias por participar de este juego, nos vemos pronto!')
                break
        
# Funcion para forzar al usuario a responder 'si' o 'no' solamente
def siono(resp): 
        
    if resp.lower() != 'si' and resp.lower() != 'no':
        print('\nDebes responder Si o No solamente!\n Aqui vamos de nuevo...')
        return True
    return False


# Funcion para forzar al usuario a escribir una sola palabra
def unapalabra(palabra):
    if ' ' in palabra:
        print('Solo palabras, no oraciones ni expresiones, vamos denuevo...')
        return True
    return False

# Reglas del juego
def reglasdeljuego():
    
    print('\nReglas')
    print('\n1.) Me vas a escribir una palabra.')
    print('2.) Si el palabra es valido, te lo dire.')
    print('3.)Si no es valido (uno de los prohibidos en nuestra base de datos ), te regresare hasta que des con un palabra valido.')


if __name__ == '__main__':
    
    fallo = True

    print('Bienvenido a esta lista de usuarios prohibidos...')
    print('\nTe explico como funciona: ')
    
    reglasdeljuego()

    while fallo:
        
        resp = input('\nEstas preparado?? (Si o No...) \nR/. ')

        fallo = siono(resp)

    if resp.lower() == 'si':

        prueba()
    elif resp.lower() == 'no':
        print('\n De acuerdo, nos veremos cuando estes listo!')
    
    