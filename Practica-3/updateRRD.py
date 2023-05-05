import time
import rrdtool
from getSNMP import consultaSNMP

oid1 = 0
oid2 = 0
oid3 = 0
oid4 = 0
oid5 = 0

def updateRRD(community, IP, port):
    while 1:
        # Contiene el trafico de red actual
        oid1 = int(consultaSNMP(community, IP, '1.3.6.1.2.1.2.2.1.11.1', port))
        oid2 = int(consultaSNMP(community, IP, '1.3.6.1.2.1.4.3.0', port))
        oid3 = int(consultaSNMP(community, IP, '1.3.6.1.2.1.5.21.0', port))
        oid4 = int(consultaSNMP(community, IP, '1.3.6.1.2.1.6.10.0', port))
        oid5 = int(consultaSNMP(community, IP, '1.3.6.1.2.1.7.1.0', port))

        # 'N' es el tiempo actual
        valor = "N:" + str(oid1) + ':' + str(oid2) + ':' + str(oid3) + ':' + str(oid4) + ':' + str(oid5)

        print (valor)
        
        rrdtool.update("DB_" + community + ".rrd", valor)
        rrdtool.dump("DB_" + community + ".rrd","DB_" + community + '.xml')
        time.sleep(1) # Cada segundo manda datos para evitar inundar el sistema

    # if ret:
        # print (rrdtool.error())
        # time.sleep(300)