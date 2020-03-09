
if __name__:"__main__"

class cucaracha:
  def __init__(self, name, cantidad):
    self.name = name
    self.cantidad = cantidad


p1 = cucaracha("cucaracha", 10)

print(f"bienvenido, eres tan asqueroso(a) que tienes {p1.cantidad} cucarachas aqui")

for x in range(6):
  print("Que quieres hacer con ellas?\n")
  print("1. Pisar\n")
  print("2. Fumigar\n")
  print("3. Reproducir\n")
  decision=int(input("Que quieres hacer?\n R/. "))
  
  def pisar():
      p1.cantidad-=1
      print(f"Bueno, estas mejorando tu basura, ahora tienes {p1.cantidad} cucarachas\n")

  def fumigar():
      p1.cantidad-=3
      print(f"Bueno, me alegra que seas aseado, ahora tienes {p1.cantidad} cucarachas\n")

  def reproducir():
      p1.cantidad+=5
      print(f"Eres la cosa mas asquerosa del mundo, tienes {p1.cantidad} cucarachas\n")

  if decision == 1:
      pisar()
  elif decision == 2: 
      fumigar()
  elif decision == 3: 
      reproducir()
  if p1.cantidad<0:
    print("Ya no tienes cucarachas, adios\n")

if p1.cantidad>10:
  print(f"No has aprendido nada, tienes {p1.cantidad} de cucarachas al final... nos vemos")
elif p1.cantidad<10:
  print(f"Bueno, has mejorado, tienes {p1.cantidad} de cucarachas al final... nos vemos")
elif p1.cantidad==10:
  print(f"Ni bien, ni mal, tienes {p1.cantidad} de cucarachas al final... nos vemos2 ")