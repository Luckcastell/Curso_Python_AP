#archivo_texto = "mails y txt/texto.txt"

#texto_lista = ["hola", "¿que tal?", 
#               "hola", "¿que tal?"]

#with open (archivo_texto, "w+") as f:
#    for e in texto_lista:
#        f.write(e)
#        f.write("\n")*/
        
archivo_texto = "mails y txt/texto.txt"

texto_lista = ["hola", "¿que tal?", 
               "hola", "¿que tal?"]

with open (archivo_texto, "r") as f:
    lineas = f.readlines()
    print (lineas)
    for linea in lineas:
        print (linea)