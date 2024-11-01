import pywhatkit
phone_number = '+5517' #adicionar os numeros de telefone
message = 'Oi amor, estou testando enviar essa mensagem pelo Python'
hours = 16
minutes = 00
pywhatkit.sendwhatmsg(phone_number, message, hours, minutes)
print('Mensagem enviada!!')