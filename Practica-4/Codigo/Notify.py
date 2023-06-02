import smtplib
import datetime
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Agent import *

# Define params
rrdpath = '/media/brayan/Nuevo vol/ESCOM/Redes3/Practica-3/RRD/'
imgpath = '/media/brayan/Nuevo vol/ESCOM/Redes3/Practica-3/IMG/'

mailsender = "origen@gmail.com"
mailreceip = "destino@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'contraseña'

def send_alert_attached(subject, community, ip, port, obj):
    agent = Agent(community, 'v1', port, ip)
    
    tm = datetime.now()
    date = str(tm.hour) + ':' + str(tm.minute) + ' at ' + str(tm.day) + '-' + str(tm.month) + '-' + str(tm.year)

    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip

    msg.attach(MIMEText('\r\r\nAlumno: Ramirez Benitez Brayan', _charset='utf-8'))    
    msg.attach(MIMEText('\r\r\n', _charset='utf-8'))
    msg.attach(MIMEText('\r\r\nInventario de la configuración: ', _charset='utf-8'))
    msg.attach(MIMEText('\r\r\nNombre del dispositivo: ' + agent.getAgentName(), _charset='utf-8'))
    msg.attach(MIMEText('\r\r\nVersión del Sistema Operativo: ' + agent.getOSversion(), _charset='utf-8'))
    msg.attach(MIMEText('\r\r\nTiempo de actividad: ' + agent.getActiveTime(), _charset='utf-8'))
    msg.attach(MIMEText('\r\r\nFecha y hora del host: ' + date, _charset='utf-8'))
    msg.attach(MIMEText('\r\r\nComunidad SNMP: ' + community, _charset='utf-8'))
    
    fp = open(imgpath+'deteccion'+obj +'_' + community +'.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)


    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()