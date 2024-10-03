import pandas as pd 
import matplotlib.pyplot as plt

fig, ax = plt.subplots() 

x = pd. Series (range(0, 11))
y = 2*x + 2*x + 1 
fig, ax = plt.subplots()

ax.plot(x, y, label= "auto", color = "k")

ax.set_xlabel("Tiempo(Hs)")
ax.set_ylabel ("Distancia(Km)")

ax.set_title ("viaje en ruta")

fig.savefig("grafico_tp6.jpg")
