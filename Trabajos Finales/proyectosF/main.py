import matplotlib.pyplot as plt
import numpy as np
import re
'''
Banco de Donantes de Sangre de Adrien

'''
donantes = []
donatarios = []
datosporpaciente = [
    "Nombre",
    "Apellido",
    "Edad",
    "Sexo",
    "Tipo De Sangre",
    "Salir"]
menu = ["Añadir Donante de Sangre",
        "Añadir Donatario",
        "Modificar Donante",
        "Modificar Donatario",
        "Ver Listas",
        "Pedido de Transfusion",
        "Ver Estadisticas",
        "Salir"]
verificadordesangre = r'(o|a|b|ab)(\+|\-)'
verificadordenombreapellido = r'(^[a-zA-Z]+$)'
class Donante():
    def __init__(self, nombre,apellido,edad, sexo, sangre):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.sangre = sangre


class Donatario(Donante):

    def __init__(self, nombre,apellido,edad, sexo, sangre):
        super().__init__(nombre,apellido,edad, sexo, sangre)

    def posible(self):
        if self.sangre == "A+":
            sangre_permitida = ["A+", "A-", "O+", "O-"]
        elif self.sangre == "O+":
            sangre_permitida = ["O+", "O-"]
        elif self.sangre == "B+":
            sangre_permitida = ["B+", "B-", "O+", "O-"]
        elif self.sangre == "AB+":
            sangre_permitida = [
                "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
        elif self.sangre == "A-":
            sangre_permitida = ["A-", "O-"]
        elif self.sangre == "O-":
            sangre_permitida = ["O-"]
        elif self.sangre == "B-":
            sangre_permitida = ["B-", "O-"]
        elif self.sangre == "AB-":
            sangre_permitida = ["A-", "B-", "O-", "AB-"]
        else:
            return f"La Sangre {self.sangre} no existe."
        return sangre_permitida


def cargardatos(lista, archivotxt):
    try:
        with open(f'{archivotxt}.txt') as archivo:
            lista0 = archivo.read().split('\n')
            for linea in lista0:
                if '{' in linea:
                    lista.append(eval(linea))
    except FileNotFoundError:
        print(f'\n \"{archivotxt}\" file does not exist.')



def guardarcambios(lista, archivotxt):
    if archivotxt == '' or archivotxt == 'donantes' or archivotxt == 'donatarios':
        return print('There is no appropiate file for saving')
    with open(f'{archivotxt}.txt', 'w') as archivo:
        for paciente in lista:
            archivo.write('XXXXXXXXXXXXXXXXXXXXX\n')
            archivo.write(repr(paciente))
            archivo.write('\n')
            archivo.write('XXXXXXXXXXXXXXXXXXXXX\n')


def nuevo(lista, donante_donatario):

    if donante_donatario == 'donante':

        print('\nGracias por ofrecer su sangre, esta puede salvar a otras personas!!!')

    else:
        print(
            '\nFelicidades por dar este gran paso, es por ud que hacemos todo este esfuerzo')

    print('\nNecesitamos algunos de sus datos...')
    
    
    nombre = ask('Nombre: ',str,verificadordenombreapellido,'regex','\nOops! algo hiciste mal... vamos de nuevo: sin espacios, ni numeros ni simbolos\n').capitalize()
    apellido = ask('Apellido: ',str,verificadordenombreapellido,'regex','\nOops! algo hiciste mal... vamos de nuevo: sin espacios, ni numeros ni simbolos\n').capitalize()
    edad = ask('Edad: ',int,range(6,120),False,'\nDebes ingresar un numero entre 6 y 120... vamos de nuevo\n')
    sexo = ask('Sexo: ',str,'mf',False,'\nOops! algo hiciste mal... vamos de nuevo\n')
    sangre = ask('Tipo de Sangre: ',str,verificadordesangre,'regex','\nOops! algo hiciste mal... vamos de nuevo\n')

    norepeat = buscar(lista,donante_donatario,nombre,apellido)
    if norepeat:
        print(f'\nLo sentimos, el {donante_donatario} {nombre} {apellido} ya se encuentra registrado.\n')
    else:
        if donante_donatario == 'donante':

            paciente = Donante(nombre,apellido,edad, sexo.capitalize(), sangre.capitalize())
        else:
            paciente = Donatario(nombre,apellido,edad, sexo.capitalize(), sangre.capitalize())

        lista.append(dict(Nombre=paciente.nombre,
                        Apellido=paciente.apellido,
                        Edad=paciente.edad,
                        Sexo=paciente.sexo,
                        Sangre=paciente.sangre))

        if donante_donatario == 'donante':
            guardarcambios(donantes, 'donantes')
        else:
            guardarcambios(donatarios, 'donatarios')
        return f'\n{donante_donatario.capitalize()} Añadido, muchas gracias por su cooperacion...'


def modificar(lista, donante_donatario):

    print(
        f'\nEs importante mantener actualizados los datos de nuestros {donante_donatario}s para un mejor servicio...')
    print(
        f'\nA continuacion, denos sus datos para saber que {donante_donatario} vamos a modificar')

    nombre = ask('\nIngrese su nombre: ',str,verificadordenombreapellido,'regex','\nOops! algo hiciste mal... vamos de nuevo: sin espacios, ni numeros ni simbolos\n').capitalize()
    apellido = ask('\nIngrese su apellido: ',str,verificadordenombreapellido,'regex','\nOops! algo hiciste mal... vamos de nuevo: sin espacios, ni numeros ni simbolos\n').capitalize()

    cliente = buscar(lista, donante_donatario, nombre, apellido)

    if cliente:
        datospersonales(cliente)

        print('\nQue desea modificar?')

        i = 1
        for dato in datosporpaciente:
            print(f'{i}.) {dato}')
            i += 1

        will = ask('R/. ',int,range(1,6),False,'\nSolo puede ingresar un numero entre 1 y 6... vamos de nuevo.')

        if will == 1:

            nuevonombre = ask('Ingrese el nuevo nombre: ',str,verificadordenombreapellido,'regex','\nOops! algo hiciste mal... vamos de nuevo: sin espacios, ni numeros ni simbolos\n').capitalize()

            cliente = cambiodatos(lista,cliente, 'Nombre', nuevonombre,f'{donante_donatario}s')

        elif will == 2:

            nuevoapellido = ask('Ingrese el nuevo apellido: ',str,verificadordenombreapellido,'regex','\nOops! algo hiciste mal... vamos de nuevo: sin espacios, ni numeros ni simbolos\n').capitalize()

            cliente = cambiodatos(
                lista,
                cliente,
                'Apellido',
                nuevoapellido,
                f'{donante_donatario}s')

        elif will == 3:

            nuevaedad = ask('Ingrese la nueva Edad: ',int,range(6,120),False,'\nAqui debes poner un numero entre 6 y 120... vamos de nuevo\n')

            cliente = cambiodatos(lista,cliente, 'Edad', nuevaedad,f'{donante_donatario}s')

        elif will == 4:

            nuevosexo = ask('Ingrese el nuevo Sexo: ',str,'mf', False,'\nOops! algo hiciste mal... vamos de nuevo\n').capitalize()

            cliente = cambiodatos(lista,cliente, 'Sexo', nuevosexo,f'{donante_donatario}s')

        elif will == 5:

            nuevasangre = ask('Ingrese el nuevo Tipo de Sangre: ',str,verificadordesangre,'regex','\nOops! algo hiciste mal... vamos de nuevo\n').capitalize()

            cliente = cambiodatos(lista,cliente, 'Sangre', nuevasangre,f'{donante_donatario}s')

        else:
            return False
        return True
    else:
        print(f'\nLo sentimos, el {donante_donatario} {nombre} {apellido} no se encuentra registrado.\n')


def cambiodatos(lista,cliente, dato, valor,archivo):

    for paciente in lista:
        if paciente['Nombre'] == cliente['Nombre'] and paciente['Apellido'] == cliente['Apellido']:
            paciente[dato] = valor
            print('\nCambio realizado satisfactoriamente... aqui estan sus nuevos datos:')
            break
    
    guardarcambios(lista,archivo)    
    datospersonales(paciente)
    
    return paciente


def verlistas(lista, donante_donatario):
    if len(lista) == 0:
        print(f'Por el momento no hay {donante_donatario}s disponibles...')
    else:
        i = 1
        print(f'  {donante_donatario.capitalize()}s : Tipo de Sangre')
        for cliente in lista:
            nombre = cliente['Nombre']
            apellido = cliente['Apellido']
            sangre = cliente['Sangre']
            print(f'{i}.) {nombre} {apellido}: {sangre} ')
            i += 1
        print('\n')


def transfusion():
    print('\n Trataremos de hacer esto lo mas rapido posible...')
    nombredonatario = ask('\nIngrese el nombre del donatario: ',str,verificadordenombreapellido,'regex','\nOops! algo hiciste mal... vamos de nuevo: sin espacios, ni numeros ni simbolos\n').capitalize()
    apellidodonatario = ask('Ingrese el apellido del donatario: ',str,verificadordenombreapellido,'regex','\nOops! algo hiciste mal... vamos de nuevo: sin espacios, ni numeros ni simbolos\n').capitalize()

    print('\n')
    if len(donantes) == 0:
        print('Lo sentimos, no hay donantes para realizar una transfusion en estos momentos')
    else:
        donatario = buscar(
            donatarios,
            'donatario',
            nombredonatario,
            apellidodonatario)
        if donatario:
            print('\n')

            datospersonales(donatario)

            donatario = Donatario(
                donatario['Nombre'],
                donatario['Apellido'],
                donatario['Edad'],
                donatario['Sexo'],
                donatario['Sangre'])
            sangre_permitida = donatario.posible()

            for donante in donantes:
                if donante['Sangre'] in sangre_permitida:
                    print('\nFelicidades, tenemos un donante para ti...')
                    

            will = ask('\n Desea realizar la transfusion?(Si o No): ',str,'sino',False,'\nOops! algo hiciste mal... vamos de nuevo\n')

            if will.lower() == 'si':
                return '\nTransfusion en proceso... Gracias por la espera!'
            else:
                return '\nDe acuerdo, cuando desee realizar la transfusion, no dude en contactarnos... '
        else:
            return print(f'\nLo sentimos, el {donante_donatario} {nombre} {apellido} no se encuentra registrado.\n')


def datospersonales(dicc):
    for k, v in dicc.items():
        print(f'{k}: {v}')


def buscar(lista, donante_donatario, nombre, apellido):
    cliente_ = {}
    for cliente in lista:
        if nombre == cliente['Nombre'] and apellido == cliente['Apellido']:
            print(f'\n{donante_donatario.capitalize()} Encontrado!!\n')
            cliente_ = cliente
            break
    if nombre != cliente_['Nombre'] and apellido != cliente_['Apellido']:
        return False
    else:
        return cliente_

def estadisticas(lista,tipo, donante_donatario):
    sangres = {}
    edades = {}
    sexos = {}
    if tipo == 'Sangre':
        tipos = []
        nsangre = []
        for paciente in lista:
            sangre = paciente[tipo]
            if sangre in sangres.keys():
                sangres[sangre]+=1
            else:
                sangres[sangre] = 1
        for ts,n in sangres.items():   
            tipos.append(ts)
            nsangre.append(n)
        x = np.array(tipos)
        y = np. array(nsangre)

        plt.bar(x,y,align='center') 
        plt.title(f'Tipos de Sangre en {donante_donatario.capitalize()}s')
        plt.show()

    elif tipo == 'Edad':
        tipoe = []
        nedades = []
        infantes = range(6,11)
        adolescentes = range(12,18)
        juventud = range(14,26)
        adultez = range(27,59)
        vejez = range(60,120)
        for paciente in lista:
            edad = int(paciente[tipo])
            if edad in vejez:
                edad = 'Adultos Mayores'
            elif edad in adultez:
                edad = 'Adultos'
            elif edad in juventud:
                edad = 'Jovenes'
            elif edad in adolescentes:
                edad = 'Adolescentes'
            else:
                edad = 'Infantes'
            if edad in edades.keys():
                edades[edad] +=1
            else: 
                edades[edad] = 1
        for te,n in edades.items():   
            tipoe.append(te)
            nedades.append(n)
        x = np.array(tipoe)
        y = np. array(nedades)    
        plt.bar(x,y,align='center') 
        plt.title('Edades Donadoras de Sangre')
        plt.show()
    else:
        tiposex = []
        nsex = []
        for paciente in lista:
            sexo = paciente[tipo]
            if sexo in sexos.keys():
                sexos[sexo]+=1
            else:
                sexos[sexo] = 1
        for ts,n in sexos.items():   
            tiposex.append(ts)
            nsex.append(n)
        x = np.array(tiposex)
        y = np. array(nsex)

        plt.bar(x,y,align='center') 
        plt.title(f'Sexo de los {donante_donatario}s')
        plt.show()

def ask(input_sentence,type_,param,esparams,except_):
    while True:
        try:
            will = type_(input(input_sentence))
        except:
            print(except_)
        else:
            if type(param) is range:
                if will not in param:
                    print(except_)
                break
            elif esparams == 'regex':
                autenticator = re.fullmatch(param,will.lower())
                if autenticator == None:
                    print(except_)
                else:
                    break
            
            elif param != False:
                if will.lower() not in param:
                    print(except_)
                else:
                    break
            else:
                break
    return will

    
if __name__ == "__main__":

    cargardatos(donantes, 'donantes')
    cargardatos(donatarios, 'donatarios')

    print('Bienvenido a BDSA (Banco de Donantes de Sangre de Adrien)...')
    print('\nQue deseas hacer? ')

    while True:

        i = 1

        for opcion in menu:
            print(f'{i}.) {opcion}')
            i += 1
        will = ask('R/. ',int,range(1,8),False,'\nAqui debes poner un numero entre 1 y 8, vamos de nuevo...\n')
        if will == 1:
            print(nuevo(donantes, 'donante'))
            print('\nDesea hacer algo mas??')
        elif will == 2:
            print(nuevo(donatarios, 'donatario'))
            print('\nDesea hacer algo mas??')
        elif will == 3:
            state = modificar(donantes, 'donante')
            if state:
                print('\nDesea hacer algo mas??')
        elif will == 4:
            state = modificar(donatarios, 'donatario')
            if state:
                print('\nDesea hacer algo mas??')
        elif will == 5:
            print('1.) Donantes \n2.) Donatarios')

            will = ask('\nCual lista desea ver??: ',int,range(1,2),False,'\nAqui debes poner un numero entre 1 y 2, vamos de nuevo...\n')

            if will == 1:
                print('\n')
                verlistas(donantes, 'donante')
            else:
                print('\n')
                verlistas(donatarios, 'donatario')
        elif will == 6:
            print(transfusion())
            print('\nDesea hacer algo mas??')
        elif will == 7:
            print('1.) Tipos de Sangre\n2.) Edades Comunes\n3.) Sexo mas Comun')
            will = ask('\nCual estadistica desea ver??: ',int,range(1,2),False,'\nAqui debes poner un numero entre 1 y 2, vamos de nuevo...\n')
            if will == 1:
                print('1.) Donantes \n2.) Donatarios')
                will = ask('\nCual lista desea ver??: ',int,range(1,2),False,'\nAqui debes poner un numero entre 1 y 2, vamos de nuevo...\n')
                if will == 1:
                    estadisticas(donantes,'Sangre','donante')
                else:
                    estadisticas(donatarios,'Sangre','donatario')
            elif will == 2: 
                print('1.) Donantes \n2.) Donatarios')
                will = ask('\nCual lista desea ver??: ',int,range(1,2),False,'\nAqui debes poner un numero entre 1 y 2, vamos de nuevo...\n')
                if will == 1:
                    estadisticas(donantes,'Edad','donante')
                else:
                    estadisticas(donatarios,'Edad','donatario')
            else:
                print('1.) Donantes \n2.) Donatarios')
                will = ask('\nCual lista desea ver??: ',int,range(1,2),False,'\nAqui debes poner un numero entre 1 y 2, vamos de nuevo...\n')
                if will == 1:
                    estadisticas(donantes,'Sexo','donante')
                else:
                    estadisticas(donatarios,'Sexo','donatario')
    
        else:
            print('Que Tenga un buen dia...')
            break
