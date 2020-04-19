from filecmp import cmp
from os import listdir, unlink
from os.path import isfile, join
from tkinter import filedialog
from tkinter import *
import csv
from pathlib import Path



def carpeta():
    root = Tk()
    root.filename =  filedialog.askdirectory()
    
    return root.filename

def eliminarduplicados(ruta):


    ficheros = [f for f in listdir(ruta) if
                    isfile(join(ruta, f))]

    for fichero in ficheros:
        for comp in ficheros:
            if fichero != comp:
                veredicto = cmp(f'{ruta}\{fichero}', f'{ruta}\{comp}', shallow=True)
                if veredicto:
                    
                    print(f"{fichero} = {comp} = SON IGUALES")
                    print("ELIMINANDO ARCHIVO: " + comp)
                    ficheros.remove(comp)
                    unlink( f'{ruta}\{comp}')
                else:
                    print(f"{fichero} != {comp} != SON DIFERENTES")

    print('\nAhora, solamente se encuentra en la carpeta los siguientes archivos: \n')
    
    for fichero in ficheros:
        print(fichero)
    
    print('\nAgradezco la espera Se le ofrece algo mas??')
    return ficheros


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
                else:
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
    
    base_path = Path(__file__).parent   
    ruta = (base_path / "Duplicados").resolve()

    print('\nBienvenido al mejor eliminador de archivos duplicados del mundo...')
    print('\n A continuacion, puedes escoger entre estas 2 opciones')

    while True:

        print('\n1.) Escoger la carpeta que contenga los duplicados. ')
        print(f'2.) Mover los elementos duplicados a la carpera origen: \n\t{ruta} ')
        print('3.) Salir. ')

        will = ask('\nQue prefieres??: ',int,range(1,4),None,'\nOops!!... Debias elegir un entero entre 1 y 3   ... Vamos de nuevo')

        if will == 1:

            ruta = carpeta()

            print('\nPerfecto! una vez elegida la carpeta, procederemos a la eliminacion...')

            eliminarduplicados(ruta)

        elif will == 2:

            print('\nPerfecto! se muevan los elementos a la carpeta de duplicados, procederemos a la eliminacion...')

            while True:

                will = ask('\n Los moviste??(si o no): ',str,'sinoSINO',None,'\n Debes responder Si o No solamente... Vamos de nuevo')
                
                if will.lower() == 'si':

                    ruta = (base_path / "Duplicados").resolve()
                    
                    print('\nGenial, comencemos...')
                    
                    eliminarduplicados(ruta)
                    break

                else:
                    print('\nDe acuerdo, mueve los elementos y responde cuando estes preparado...')
        else: 

            print('\nEspero haberte ayudado, nos vemos pronto...')
            break

        
