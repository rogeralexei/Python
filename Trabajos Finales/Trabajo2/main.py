from re import fullmatch




regex = r"(N|PE|E|(?:^[1-9]|1[0-3]$))(\-)(?:([0-9]|[1-8][0-9]|9[0-9]|[1-8][0-9]{2}|9[0-8][0-9]|99[0-9]))(\-)(?:([0-9]|[1-8][0-9]|9[0-9]|[1-8][0-9]{2}|9[0-8][0-9]|99[0-9]|[1-8][0-9]{3}|9[0-8][0-9]{2}|99[0-8][0-9]|999[0-9]))$"

with open('cedulasvalidas.txt') as validas:
    cipvalid = validas.read().split('\n')
    cedulas = []
    for linea in cipvalid:
        filtro = fullmatch(regex,linea)
        if filtro != None:
            cedulas.append(linea)
        
        
    


def autenticador(boole):
    while True:
        cedula = input('Ingrese el numero de cedula: ')

        match = fullmatch(regex,cedula)

        if match != None :
            cedulas.append(cedula)
            print('\nCedula Valida!')
            while boole:
                will = input('\nQuisiera validar alguna otra cedula? (Si o No)\nR/. ')

                boole = siono(will) 
            boole = True
            if will.lower() == 'no':
                print('\nMuchas gracias por su participacion...')
                return True
                break

        else:
            print('\nCedula Invalida... Intente Nuevamente')
            return False

def reglas():
    print('\n1.) Las cedulas deben estar separadas por guiones. ')
    print('\t Ej:XX-XXX-XXXX')
    print('2.) Ingrese el numero de cedula sin espacios')
    print('\tIncorrecto: XX - XXX - XXXX')
    print('\t Correcto:XX-XXX-XXXX')

# Funcion para forzar al usuario a responder 'si' o 'no' solamente
def siono(resp): 
        
    if resp.lower() != 'si' and resp.lower() != 'no':
        print('\nDebe responder Si o No solamente!\n Aqui vamos de nuevo...')
        return True
    return False
if __name__ == "__main__":

    fallo =True

    print('Bienvenido al autenticador de cedulas 5000.')
    print('\nRecuerde lo siguiente:\n ')
    reglas()
    while fallo:

        deseo = input('\n Le gustaria ver algunos ejemplos? \nR/. ')

        fallo = siono(deseo)
    fallo = True

    if deseo.lower() == 'si':

        cedulasejemplo = ['1-234-5678','12-345-5698','PE-001-597','E-400-891','N-789-3456']
        print('\nEjemplos de Cedulas Validas:\n\n')
        for ejemplo in cedulasejemplo:
            print(f'=> {ejemplo}')
        
    while fallo:
        will = input('\nListo para su validacion? (Si o No) \nR/. ')

        fallo = siono(will)
    fallo = True

    if will.lower() == 'si':
        print('\nListo!')
        autenticador(fallo)
    
    print('Que tenga un buen dia!')

    with open('cedulasvalidas.txt','a') as validas:
        for cedula in cedulas:
            if cedula not in cipvalid:
                validas.write(cedula)
                validas.write('\n')