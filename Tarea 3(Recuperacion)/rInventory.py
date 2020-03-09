class Articulo:
  def __init__(self, nombre, precio, cantidad):
    self.nombre=nombre
    self.precio=precio
    self.cantidad=cantidad

if __name__ == '__main__':
  nombre=input("Bienvenido al sistema de manejo de Articulos Store. Favor de introducir su nombre: ")
  print("Hola "+nombre+". Bienvenido al sistema.")
  nuevo="si"
  articulos=[]
  precios=[]
  cantidad=[]
  #Añadir Articulos
  while (nuevo=="si"):
    nuevo = input('Te gustaria hacer un nuevo articulo?(si/no): ')
    if(nuevo=="si"):
      Articulo.nombre = input('Nombre de el articulo: ')
      articulos.append(Articulo.nombre)
      Articulo.precio = input('Precio de el articulo: ')
      precios.append(Articulo.precio)
      Articulo.cantidad = input('Cantidad de articulo: ')
      cantidad.append(Articulo.cantidad)
    else:
      nuevo=False
  
  #Buscar Articulo, modificar o eliminar
  buscar=input("Desea buscar un Articulo: (si/no): ")
  if (buscar=="si"):
    cual=input("Introduzca el articulo que desea buscar: ")
    if cual in articulos:
      print ("Este articulo se encuentra en la tienda y hay "+cantidad[articulos.index(cual)]+" a un precio de $"+precios[articulos.index(cual)])
      mod=input("Desea Modificar este articulo? (si/no: ")
      if (mod=="si"):
        nom=input("Desea Modificar el nombre ? (si/no: ")
        if (nom=="si"):
          new=input("Ingrese el nuevo nombre del Articulo ")
          articulos[articulos.index(cual)]=new
        can=input("Desea Modificar la cantidad ? (si/no): ")
        if (nom=="si" and can=="si"):
          cantidad[articulos.index(new)]=input("Ingrese la cantidad del nuevo articulo: ")
        elif(can=="si"):
          cantidad[articulos.index(cual)]=input("Ingrese la nueva cantidad: ")
        prec=input("Desea Modificar el precio ? (si/no) : ")
        if (nom=="si" and prec=="si"):
          precios[articulos.index(new)]=input("Ingrese el precio del nuevo articulo: ")
        elif(prec=="si"):
          precios[articulos.index(cual)]=input("Ingrese el nuevo precio: ")
      elim=input("Desea Eliminar un articulo? (si/no): ")
      if(elim=="si"):
        elige=input("Que articulo deseas eliminar? :")
        if elige in articulos:
          precios.pop(articulos.index(elige))
          cantidad.pop(articulos.index(elige))
          articulos.remove(elige)
  print("Gracias por usar el sistema te presentamos tus articulos")
  for e in range(len(articulos)):
    print("Articulo: "+articulos[e]+"| Precio Unitario: "+precios[e]+"| Cantidad: "+cantidad[e])