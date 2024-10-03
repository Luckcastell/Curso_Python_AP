llueve = True
frio = False

if (llueve and frio):   # llueve y frio ---> Verdadero si ambas son verdaderas
  print("Llueve y hace frio")

if (llueve or frio):   #o llueve o hace frio ---> es Verdadero si uno de los dos es verdadero
  print("O llueve o hace frio")

if (not llueve):   # not False: verdadero
  print("No llueve")

if (not frio):
  print("No hace frio")