from tkinter import messagebox
from Agent import *

# Practica 2
from CreateRRD import *
from updateRRD import *

# Practica 3
from trendCreate import *
from TrendUpdate import *
from trendGraphDetection import *
import threading

FILE = 'Agentes.txt'

# Creamos un agente y lo guardamos en el txt
def addAgent(community, version, port, ip):
    agent = Agent(community, version, port, ip)
    txt = open(FILE, 'a')
    txt.write(str(agent) + "\n")
    txt.close()

def showAgents():
    file = open(FILE, 'r')
    txt = file.read()
    file.close()
    agts = []

    for agt in enumerate(txt.split(sep = '\n')):
        if(agt[1] != ''):
            agts.append(agt[1].split(sep = ',')[0])

    return agts

def getAgent(name):
    file = open(FILE, 'r')
    txt = file.read()
    file.close()
    agts = []
    aux = []

    for agt in enumerate(txt.split(sep = '\n')):
        if(agt[1].startswith(name)):
            aux = agt[1].split(sep = ',')
            if(aux[0] == name):
                agts = aux
                break;

    return agts

def changeAgent(oldCommunity, newCommunity, version, port, ip):
    agent = Agent(newCommunity, version, port, ip)
    
    file = open(FILE, 'r')
    txt = file.read()
    file.close()
    agts = []
    aux = []

    for agt in enumerate(txt.split(sep = '\n')):
        if(agt[1].startswith(oldCommunity)):
            aux = agt[1].split(sep = ',')
            if(aux[0] == oldCommunity):
                continue
            else:
                agts.append(agt[1]) 
        elif(agt[1] == ''):
            continue
        else:
            agts.append(agt[1])    
    agts.append(str(agent))

    file = open(FILE, 'w')
    for dis in agts:
        file.write(dis + "\n")
    file.close()

def deleteAgent(community):
    file = open(FILE, 'r')
    txt = file.read()
    file.close()
    agts = []
    aux = []

    for agt in enumerate(txt.split(sep = '\n')):
        if(agt[1].startswith(community)):
            aux = agt[1].split(sep = ',')
            if(aux[0] == community):
                continue
            else:
                agts.append(agt[1]) 
        elif(agt[1] == ''):
            continue
        else:
            agts.append(agt[1])    

    file = open(FILE, 'w')
    for dis in agts:
        file.write(dis + "\n")
    file.close()

def updateAccounting(community):
    agt = getAgent(community)

    # Practica 2
    createRRD(community)
    threadAg = threading.Thread(target = updateRRD, args = (agt[0], agt[3], agt[2]))
    threadAg.start()

def updatePerformance(community):
    agt = getAgent(community)

    # Practica 3
    createDB('CPU', community)
    createDB('RAM', community)
    createDB('DISK', community)

    threadAg = threading.Thread(target = updateTrend, args = (agt[0], agt[3], agt[2]))
    threadAg.start()

def mailPerformance(community):
    agt = getAgent(community)

    threadAg1 = threading.Thread(target = performance, args = (agt[0], agt[3], agt[2]))
    threadAg1.start()


