import pandas as pd

edades = pd.Series([22, 14, 35, 19, 5, 27, 56])
print(edades)

print("------------------------------------------------------")

print(edades[0])
print(edades[5])

print("------------------------------------------------------")

cadenasNumeros = pd.Series(["perro", 5.1, "gato", 4, "elefante", 56])
print(cadenasNumeros)

print("------------------------------------------------------")

edades.index

print("------------------------------------------------------")

cantidadElementos = edades.count()
print(cantidadElementos)

print("------------------------------------------------------")

cadenas = pd.Series(["perro", "perro", "gato", "elefante"])

cadenas.sum()

print("------------------------------------------------------")

lenCadena = len("hola")
print(lenCadena)

print("------------------------------------------------------")

print(edades.describe())

print("------------------------------------------------------")

elemDescribe = edades.describe()
print(elemDescribe[0])

print("------------------------------------------------------")

elemDescribe = edades.describe()
print(elemDescribe["mean"])

print("------------------------------------------------------")

print(cadenas.describe())

print("------------------------------------------------------")

nombre_altura = pd.DataFrame([["martina", 1.80],
                              ["liam", 1.50],
                              ["marcos", 1.57],
                              ["abril", 1.70],])

print(nombre_altura)

print("------------------------------------------------------")

nombre_altura.index

print("------------------------------------------------------")

print(nombre_altura.describe())

print("------------------------------------------------------")

nombres = nombre_altura[0]
print(nombres)

print("------------------------------------------------------")

nombre_altura.columns = ["nombres", "alturas"]
print(nombre_altura)

print("------------------------------------------------------")

print(nombre_altura["nombres"])

print("------------------------------------------------------")

print(nombre_altura.loc[0]) #fila con indice 0
print(nombre_altura.iloc[0]) #fila en pocicion 0

print("------------------------------------------------------")

print(nombre_altura.iloc[1:]) #fila con ocicion 1 en adelante

print("------------------------------------------------------")

print(nombre_altura.loc[1]) #fila con indice 1
print(nombre_altura.iloc[1]) #fila en pocicion 1

print("------------------------------------------------------")

df_nuevo = nombre_altura.iloc[1:]

print("------------------------------------------------------")

print(df_nuevo.loc[1]) #fila con indice 1
print(df_nuevo.iloc[0]) #fila en pocicion 0 (indice 1)