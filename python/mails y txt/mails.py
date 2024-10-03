import yagmail

print("ingrese su gmail: ")
gmail = input()
# gmail = "gmlspython@gmail.com"luckcastell20@gmail.com
print("")

print("ingrese su contraseña de envio de terceros: ")
contraseña = input()
# contraseña = "ggsfkqexnsnkvccx"hwouiupzvufzxltp
print("")

destinatarios = input()
# destinatarios = "gmlspython@gmail.com"castelli.agustina@gmail.com
print("")

a = 0
while (a != 1):
    print("ingrese su destinatario: ")
    destinatario = input()
    print("")
    destinatarios.__add__(destinatario)
    print("¿desea ingresar algun destinatario mas?(si/no)")
    b = input()
    print("")
    c = 0
    while (c == 0):
        if (b == "si" or b == "SI" or b == "Si"):
            a = 0
            c = 1
        elif (b == "no" or b == "NO" or b == "No"):
            a = 1
            c = 1
        else:
            print("Respuesta invalida(responda solamente con si o no)")

yag = yagmail.SMTP(user= gmail, password= contraseña) 

# img = "mails y txt/imagen.jpg"

print("ingrese el asunto del mail: ")
asunto = input()
# asunto = "virus virus"
print("")



# print("ingrese el mensaje: ")
# mensaje = input()
mensaje = ["Este mensaje fue enviado por el programa de Lukcastell."]
a2 = 0
while (a2 != 1):
    print("ingrese su mensaje: ")
    linea = input()
    print("")
    mensaje.append(linea)
    print("¿desea ingresar algun salto de linea mas?(si/no)")
    b2 = input()
    print("")
    c2 = 0
    while (c2 == 0):
        if (b2 == "si" or b2 == "SI" or b2 == "Si"):
            a2 = 0
            c2 = 1
        elif (b2 == "no" or b2 == "NO" or b2 == "No"):
            a2 = 1
            c2 = 1
        else:
            print("Respuesta invalida(responda solamente con si o no)")
# mensaje = ["virus", img]

print("enviando...")
yag.send(destinatarios, asunto, mensaje)
print("enviado")