import pandas as pd 
import matplotlib.pyplot as plt

fig, ax = plt.subplots() 

# x = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# y = x * 2 + 10
# print("x")
# print(x)
# print("--------")
# print("y")
# print(y)

#Uso range (-10,10) para no poner todos los números
x = pd. Series (range(-10,10)) 
fig, ax = plt.subplots()

# en el plej ax
ax.plot(x, x, label= "Lineal", color = "r")        #tambien se puede poner el  
ax.plot(x, x**2, label= "Cuadrática", color = "b") #color en rgb o en hexadecimal
ax.plot (x, x**3, label= "Cúbica", color = "y")

# Agrego el nombre de los ejes x e y
ax.set_xlabel ("eje x") # nombre para el eje x
ax.set_ylabel("eje y")

# Agrego un titulo
ax.set_title ("Funciones")

#Agrego limite
#plt.ylim(-10, 10)
#plt.xlim(-10, 10)

fig.savefig("grafico.jpg")
