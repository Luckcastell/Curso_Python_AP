archivo_texto = "texto.txt"

texto_lista = ["hola", "¿que tal?", 
               "hola", "¿que tal?"]

with open (archivo_texto, "w+") as f:
    for e in texto_lista:
        f.write(e)
        f.write("\n")