import time
import rrdtool
from getSNMP import consultaSNMP

rrdpath = '/media/brayan/Nuevo vol/ESCOM/Redes3/Practica-3/RRD/'

carga_CPU = 0
carga_RAM = 0
carga_DISK = 0

def updateTrend(community, ip, port):
    while 1:
        carga_CPU = int(consultaSNMP(community,ip, '1.3.6.1.2.1.25.3.3.1.2.196608', port))

        ramUsado = int(consultaSNMP(community, ip, '1.3.6.1.2.1.25.2.3.1.6.3', port))
        ramTotal = int(consultaSNMP(community, ip, '1.3.6.1.2.1.25.2.3.1.5.3', port))
        carga_RAM = int((ramUsado*100)/ramTotal)

        diskUsado = int(consultaSNMP(community, ip, '1.3.6.1.2.1.25.2.3.1.6.1', port))
        diskTotal = int(consultaSNMP(community, ip, '1.3.6.1.2.1.25.2.3.1.5.1', port))
        carga_DISK = int((diskUsado*100)/diskTotal)


        valorCPU = "N:" + str(carga_CPU)
        rrdtool.update(rrdpath + 'trendCPU_' + community + '.rrd', valorCPU)
        rrdtool.dump(rrdpath + 'trendCPU_' + community + '.rrd', rrdpath + 'trendCPU_' + community + '.xml')

        valorRAM = "N:" + str(carga_RAM)
        rrdtool.update(rrdpath + 'trendRAM_' + community + '.rrd', valorRAM)
        rrdtool.dump(rrdpath + 'trendRAM_' + community + '.rrd', rrdpath + 'trendRAM_' + community + '.xml')

        valorDISK = "N:" + str(carga_DISK)
        rrdtool.update(rrdpath + 'trendDISK_' + community + '.rrd', valorDISK)
        rrdtool.dump(rrdpath + 'trendDISK_' + community + '.rrd', rrdpath + 'trendDISK_' + community + '.xml')

        print("CPU: " + valorCPU + " - " + "RAM: " + valorRAM + " - " + "DISK: " +  valorDISK)
        time.sleep(5) # Se detiene cada 5 segundos
