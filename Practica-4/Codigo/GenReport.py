from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3
from Agent import *
from Functions import *
from graphRRD import *
import datetime
from getSNMP import *

oids = {"PaqUnicast", "PaqrecibidosIP", "msgICMP", "SegmentosRecv", "DtmsEntregado"}

def report(name):
    agt = getAgent(name)
    agent = Agent(agt[0], agt[1], agt[2], agt[3])

    try:
        c = canvas.Canvas(agent.getCommunity() + "_Reporte.pdf", pagesize = A3)
        
        txt = c.beginText(80, 1100)
        txt.setFont("Times-Roman", 24)
        txt.textLine("Administración de Servicios en Red")
        txt.textLine("Práctica 01 - Adquisición de información")
        txt.textLine("Ramirez Benitez Brayan - 4CM14 - Boleta")
        txt.setFont("Times-Roman", 12) 
        txt.textLine("Sistema Operativo: " + agent.getOS())
        txt.textLine("Version del Sistema operativo: " + agent.getOSversion())
        txt.textLine("Nombre del dispositivo: " + agent.getAgentName())
        txt.textLine("Información de contacto: " + agent.getContact())
        txt.textLine("Ubicación: " + agent.getLocation())
        txt.textLine("Numero de interfaces: " + agent.getInterNum())
        c.drawText(txt)
        
        c.drawImage("Img/"+str(agent.getOS())+".png", 600,800, width = 150, height = 150)
        
        interfaces = []
        interfaces = agent.getInterfaces()
        xlist = [200, 350, 500]
        ylist = [797, 817, 837, 857, 877, 897, 918]
        c.grid(xlist, ylist)

        txt2 = c.beginText(210, 900)
        txt3 = c.beginText(360, 900)
        txt2.setFont("Times-Roman", 16)
        txt3.setFont("Times-Roman", 16)
        txt2.textLine('Interfaz')
        txt3.textLine('Estado')
        for i, inter in enumerate(interfaces):
            txt2.textLine(str(i + 1))
            if(inter == '1'):
                txt3.textLine('Up')
            elif(inter == '2'):
                txt3.textLine('Down')
            else:    
                txt3.textLine(inter)
        c.drawText(txt2)
        c.drawText(txt3)

        c.save()
        messagebox.showinfo(message = "Reporte generado exitosamente!!")

    except Exception as error:
        messagebox.showinfo(message = "Error: " + str(error))

def accounting(name, ti, tf):
    agt = getAgent(name)
    agent = Agent(agt[0], agt[1], agt[2], agt[3])

    try:
        c = canvas.Canvas(agent.getCommunity() + "_ReporteContable.pdf", pagesize = A3)
        
        today = datetime.date.today()
        ti = ti.split(sep=":")
        tf = tf.split(sep=":")
        t_start = datetime.datetime(today.year, today.month, int(ti[2] ) if len(ti) > 2 else today.day, int(ti[0] ), int( ti[1] ), 0)
        t_end = datetime.datetime(today.year, today.month, int(tf[2] ) if len(tf) > 2 else today.day, int(tf[0] ), int(tf[1] ), 0)
 

        rdate = str(datetime.datetime.fromtimestamp(t_start.timestamp() ) ) + "  to  " + str(datetime.datetime.fromtimestamp(t_end.timestamp()))

        txt = c.beginText(80, 1100)
        txt.setFont("Times-Roman", 24)
        txt.textLine("Administración de Servicios en Red")
        txt.textLine("Práctica 02 - Servidor de contabilidad")
        txt.textLine("Ramirez Benitez Brayan - 4CM14 - 2020630592")
        
        txt.setFont("Times-Roman", 14) 
        txt.textLine("")
        txt.textLine("Device Information #" + agent.getCommunity())
        txt.textLine("") 
        txt.setFont("Times-Roman", 12)
        txt.textLine("Version: " + agent.getVersion())
        txt.textLine("Device: " + agent.getAgentName())
        txt.textLine("Description: " + agent.getContact())
        txt.textLine("date: " + time.strftime("%c"))
        txt.textLine(" ")
        txt.textLine("rdate: "+ rdate)
        txt.textLine("#NAS-IP-Address")
        txt.textLine("4: " + agent.getIp())
        txt.textLine("#NAS-Port-Type")
        txt.textLine("61: " + agent.getPort())
        txt.textLine("#User-Name: ")
        txt.textLine("1: " + agent.getContact())
        #txt.textLine("#Acct-Status-Type")
        #txt.textLine("40: ")
        #txt.textLine("#Acct-Delay-Time")
        #txt.textLine("41: ")
        txt.textLine("#Acct-Input-Octets")
        txt.textLine("42: " + consultaSNMP(agent.getCommunity(), agent.getIp(), '1.3.6.1.2.1.2.2.1.10.1', agent.getPort()))
        txt.textLine("#Acct-Output-Octets")
        txt.textLine("43: " + consultaSNMP(agent.getCommunity(), agent.getIp(), '1.3.6.1.2.1.2.2.1.16.1', agent.getPort()))
        #txt.textLine("#Acct-Session-Id")
        #txt.textLine("44: ")
        #txt.textLine("#Acct-Authentic")
        #txt.textLine("45: ")
        #txt.textLine("#Acct-Session-Time")
        #txt.textLine("46: ")
        txt.textLine("#Acct-Input-Packets")
        txt.textLine("47: " + consultaSNMP(agent.getCommunity(), agent.getIp(), '1.3.6.1.2.1.4.3.0', agent.getPort()))
        txt.textLine("#Acct-Output-Packets")
        txt.textLine("48: " + consultaSNMP(agent.getCommunity(), agent.getIp(), '1.3.6.1.2.1.4.10.0', agent.getPort()))
        #txt.textLine("# Acct-Terminate-Cause")
        #txt.textLine("49: ")
        #txt.textLine("#Acct-Multi-Session-Id")
        #txt.textLine("50: ")
        #txt.textLine("#Acc-Link-Count")
        #txt.textLine("51: ")
        txt.textLine("#Paquetes unicast que ha recibido")
        txt.textLine("una interfaz de red de un agente")
        txt.textLine("01: " + consultaSNMP(agent.getCommunity(), agent.getIp(), '1.3.6.1.2.1.2.2.1.11.1', agent.getPort()))
        txt.textLine("#Paquetes recibidos a protocolos IP")
        txt.textLine(", incluyendo los que tienen errores")
        txt.textLine("02: " + consultaSNMP(agent.getCommunity(), agent.getIp(), '1.3.6.1.2.1.4.3.0', agent.getPort()))
        txt.textLine("#Mensajes ICMP echo que ha enviado")
        txt.textLine("el agente")
        txt.textLine("03: " + consultaSNMP(agent.getCommunity(), agent.getIp(), '1.3.6.1.2.1.5.21.0', agent.getPort()))
        txt.textLine("#Segmentos recibidos, incluyendo los")
        txt.textLine("que se han recibido con errores")
        txt.textLine("04: " + consultaSNMP(agent.getCommunity(), agent.getIp(), '1.3.6.1.2.1.6.10.0', agent.getPort()))
        txt.textLine("#Datagramas entregados a usuarios UDP")
        txt.textLine("05: " + consultaSNMP(agent.getCommunity(), agent.getIp(), '1.3.6.1.2.1.7.1.0', agent.getPort()))

        c.drawText(txt)
        
        c.drawImage("Img/"+str(agent.getOS())+".png", 600,900, width = 150, height = 150)

        y = 700
        for oid in oids:
            graphRRD(agent.getCommunity(), t_start, t_end, oid)
            img = "Img/DB_" + agent.getCommunity() + "_" + oid + ".png"
            c.drawImage(img, 400, y, width=400, height=150)
            y = y - 160

        c.save()
        messagebox.showinfo(message = "Reporte contable generado exitosamente!!")

    except Exception as error:
        messagebox.showinfo(message = "Error: " + str(error))
