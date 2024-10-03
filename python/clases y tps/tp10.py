import yagmail
import random

gmail = "gmlspython@gmail.com"

contraseña = "ggsfkqexnsnkvccx"

destinatarios = ["gmlspython@gmail.com"]

yag = yagmail.SMTP(user= gmail, password= contraseña) 

saludos = [
    "Hola,",
    "Buenos días,",
    "Buenas tardes,",
    "Estimado/a,",
    "Hola  " + gmail + ",",
    "¡Buenos días  " + gmail + "!",
    "¡Saludos cordiales!",
    "Estimad señor/a,",
    "Estimado " + gmail + ",",
    "Querido " + gmail + ",",
]

asunto = "Agradecimiento"

mensaje = [saludos[random.randrange(0, 12)] + " te queriamos decir que gracias por participar en nuestra encuesta."]

print("enviando...")
#yag.send(destinatarios, asunto, mensaje)
print("enviado")
print (mensaje)