from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3
from Agent import *
from Functions import *

def report(name):
    agt = getAgent(name)
    agent = Agent(agt[0], agt[1], agt[2], agt[3])

    try:
        c = canvas.Canvas(agent.getCommunity() + "_Reporte.pdf", pagesize = A3)
        
        txt = c.beginText(80, 1100)
        txt.setFont("Times-Roman", 24)
        txt.textLine("Administración de Servicios en Red")
        txt.textLine("Práctica 01 - Adquisición de información")
        txt.textLine("Ramirez Benitez Brayan - 4CM14 - 2020630592")
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

