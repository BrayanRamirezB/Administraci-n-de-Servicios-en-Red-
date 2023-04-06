from getSNMP import *

class Agent(object):
    # Clase para guardar los agentes
    def __init__(self, community, version, port, ip):
        self.community = community
        self.version = version
        self.port = port
        self.ip = ip

    def __str__(self):
        return self.community + "," + self.version + "," + self.port + "," + self.ip    
    
    # Definimos los metodos get para acceder a los datos del agente
    def getCommunity(self):
        return self.community
    
    def getVersion(self):
        return self.version
    
    def getPort(self):
        return self.port
    
    def getIp(self):
        return self.ip
    
    # Definimos los metodos set para modificar los datos del agente
    def setCommunity(self, com):
        self.community = com

    def setVersion(self, ver):
        self.version = ver

    def setPort(self, prt):
        self.port = prt
    
    def setIp(self, ip):
        self.ip = ip
    
    # metodos para consultas SNMP
    def getOS(self):
        os = consultaSNMPextended(self.community, self.ip, '1.3.6.1.2.1.1.1.0', self.port)
        if(os.find("Linux") > 0):
            return 'Linux'
        elif(os.find("Windows") > 0):
            return 'Windows'
        else:
            return 'Otro'

    def getOSversion(self):
        os = consultaSNMPextended(self.community, self.ip, '1.3.6.1.2.1.1.1.0', self.port)
        if(os.find("Ubuntu") > 0):
            sc = os.split(sep = ' ')
            sc = sc[5].split(sep = '~')
            vos = sc[1]
        elif(os.find("Windows") > 0):
            vos = os.split()[16]
        else:
            vos = 'Otro'

        return vos

    def getAgentName(self):
        name = consultaSNMP(self.community, self.ip, '1.3.6.1.2.1.1.5.0', self.port)
        return name
    
    def getContact(self):
        contact = consultaSNMP(self.community, self.ip, '1.3.6.1.2.1.1.4.0', self.port)
        return contact
    
    def getLocation(self):
        location = consultaSNMP(self.community, self.ip, '1.3.6.1.2.1.1.6.0', self.port)
        return location
    
    def getInterNum(self):
        num = consultaSNMP(self.community, self.ip, '1.3.6.1.2.1.2.1.0', self.port)
        return num

    def getInterfaces(self):
        i = 1
        interfaces = []

        while(i < (int(self.getInterNum()))):
            if(i <= 5):
                interfaces.append(consultaSNMP(self.community, self.ip, '1.3.6.1.2.1.2.2.1.8.' + str(i), self.port))
                i += 1
            else:
                break

        return interfaces    