n = int(input("Numero de personas en el equipo: "))
players = {}

for i in range(n):
  name = input("Nombre {}: ".format(i+1))
  size = input("Talla: ")
  players[name] = size

name = input("Ingresa el nombre de la persona: ")

if name in players:
  print(players[name])
else:
  print("No existe dicha persona en el equipo")