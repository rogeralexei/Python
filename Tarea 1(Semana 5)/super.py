import msvcrt
if __name__ == "__main__":
    print("Lista de Supermercado")
    lista={}

#Abrir archivo para convertir sus lineas en keys
    
    listilla=open("Lista.txt","r").read().split('\n')
    for linea in listilla:
        if linea in lista.keys():
            lista[linea]+=1
        else:
            lista[linea]=1
  #imprimir lista
    for k,v in lista.items():
        print(k,v)
#Pedir si quiere algo mas...
    quiere=input("Quieres comprar algo mas? Me quiero ir...(Si o No)\nR/. ")
    while quiere.lower()=="si":
        nuevoproducto=input("\nDime que quieres... no tengo todo el dia para ti.\nR/. ")
        if nuevoproducto in lista.keys():
            lista[nuevoproducto]+=1
        else:
            lista[nuevoproducto]=1
 
        quiere=input("\nQue mas? espero que hayas pensado y no se te haya olvidado nada...(Si o no)\nR/. ")
    #imprimir lista
    for k,v in lista.items():
        print(k,v)
#A ver si quiere borrar algo  
    borrar=input("\nNo me digas que no puedes ni pensar bien\n Vas a borrar algo?(Si o no)\nR/. ")
    while borrar.lower()=="si":
        borrarproducto=input("\nDime que basura vas a borrar\nR/. ")
        if borrarproducto in lista.keys():
            lista[borrarproducto]-=1
            if lista[borrarproducto]==0:
                del lista[borrarproducto]
            borrar=input("\nYa... lo demas si lo quieres o me vas a hacer perder el tiempo??(Si o no)\nR/. ")
        else:
            print("\nTu no tienes cabeza o que? Eso no lo pusiste.")
    #imprimir lista
    for a,b in lista.items():
        print(a,b)
    #Sustituir
    sustituto=input("\nEres tan bobo que tengo que preguntarte...\nVas a cambiar algo?(Si o no)\nR/. ")
    while sustituto.lower()=="si":
        print("\nMaldicion, no puedes hacer algo bien??\n Que vas a reemplazar??\n muevete")
        cambio=input("\nR/. ")
        if cambio in lista.keys():
            del lista[cambio]
            
            artcam=input("\n Que quieres poner?? Mueve!!\nR/. ")
            if artcam in lista.keys():
                lista[artcam]+=1
            else:
                lista[artcam]=1
            sustituto="no"
        else: 
            print("\nTu mama te tiro de chico o que? Eso no lo pusiste!!")
    
    
    #imprimir lista
    for a,b in lista.items():
        print(a,b)
    print("\nAqui tienes, gracias al cielo ya te largas...")
    print("Toma tu vaina... Adios")
    listanueva=open("Lista.txt","a+")
    for e in lista:
        listanueva.write("\n"+e)
    listanueva.close()
    msvcrt.getch()