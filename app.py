import os
import smtplib
from email.message import EmailMessage
from segredos import senha

#configurar e-mail, senha
EMAIL_ADRESS ='seu@email.com'
EMAIL_PASSWORD = senha


#criar um email
msg = EmailMessage()
msg['Subject'] = 'Assunto'
msg['From'] = 'seu@email.com'
msg['To'] = 'quemvcquiser@email.com'
msg.set_content('lorem ipsum')

#enviar email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)