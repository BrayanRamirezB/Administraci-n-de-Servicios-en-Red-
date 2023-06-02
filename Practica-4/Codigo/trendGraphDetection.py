import sys
import rrdtool
import time
import datetime
from datetime import datetime
from  Notify import send_alert_attached
import time

rrdpath = '/media/brayan/Nuevo vol/ESCOM/Redes3/Practica-3/RRD/'
imgpath = '/media/brayan/Nuevo vol/ESCOM/Redes3/Practica-3/IMG/'

# True, True, True Arreglo para enviar alertas
CPU = [True, True, True]
RAM = [True, True, True]
DISK = [False, True, True]

def Grafica(ultima_lectura, obj, ready, sett, go, community):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800

    try:
        ret = rrdtool.graphv(imgpath + "deteccion" + obj + "_" + community + ".png",
                        "--start",str(tiempo_inicial),
                        "--end",str(tiempo_final),
                        "--vertical-label=" + obj + " load",
                        '--lower-limit', '0',
                        '--upper-limit', '100',
                        "--title=Carga de " + obj + " del agente Usando SNMP y RRDtools",
                        "DEF:carga" + obj + "="+ rrdpath+"trend" + obj + "_"  + community + ".rrd:" + obj + "load:AVERAGE",
                        "CDEF:umbral" + str(ready) + "=carga" + obj + "," + str(ready) + ",LT,0,carga" + obj + ",IF", # CDEF REGRESA LA MISMA COLECCION PERO MANIPULADA
                        "CDEF:umbral" + str(sett) + "=carga" + obj + "," + str(sett) + ",LT,0,carga" + obj + ",IF", 
                        "CDEF:umbral" + str(go) + "=carga" + obj + "," + str(go) + ",LT,0,carga" + obj + ",IF", 

                        "AREA:carga" + obj + "#00FF00:Carga de " + obj,
                        "AREA:umbral" + str(ready) + "#334CFF:Carga " + obj + " mayor de " + str(ready),
                        "AREA:umbral" + str(sett) + "#FF7800:Carga " + obj + " mayor de " + str(sett),
                        "AREA:umbral" + str(go) + "#990EE8:Carga " + obj + " mayor de " + str(go), 
                        
                        "HRULE:" + str(ready) + "#00FFFF:Umbral  " + str(ready) + "%",
                        "HRULE:" + str(sett) + "#FFFF00:Umbral  " + str(sett) + "%",
                        "HRULE:" + str(go) + "#FF0000:Umbral  " + str(go) + "%")
    except Exception as error:
        print('Error al graficar ' + obj + ':' + error)
    # print (ret)

def performance(community, ip, port):
    while (1):
        # ------------------Para el CPU---------------------------------------------------------
        ready = 45
        sett = 55
        go = 70

        ultima_actualizacion = rrdtool.lastupdate(rrdpath + "trendCPU_" + community + ".rrd")
        timestamp = ultima_actualizacion['date'].timestamp()
        dato = ultima_actualizacion['ds']['CPUload']

        tm = datetime.now()
        date = str(tm.hour) + ':' + str(tm.minute) + ' at ' + str(tm.day) + '-' + str(tm.month) + '-' + str(tm.year)

        if dato >= ready and CPU[0]:
            Grafica(int(timestamp), 'CPU', ready, sett, go, community)
            send_alert_attached('ALERTA: El CPU sobrepaso el umbral Ready(' + str(ready) + '%) durante ' + date, community, ip, port, 'CPU')
            CPU[0] = False
            print('Alerta de CPU enviada ' + str(ready))
            time.sleep(10)

        elif dato >= sett and CPU[1]: 
            Grafica(int(timestamp), 'CPU', ready, sett, go, community)
            send_alert_attached('ALERTA: El CPU sobrepaso el umbral Set(' + str(sett) + '%) durante ' + date, community, ip, port, 'CPU')
            CPU[1] = False
            print('Alerta de CPU enviada ' + str(sett))
            time.sleep(10)
        
        elif dato >= go and CPU[2]: 
            Grafica(int(timestamp), 'CPU', ready, sett, go, community)
            send_alert_attached('ALERTA: El CPU sobrepaso el umbral Go(' + str(go) + '%) durante ' + date, community, ip, port, 'CPU')
            CPU[2] = False
            print('Alerta de CPU enviada ' + str(go))
            time.sleep(10)
        
        else:
            print('CPU: ' + str(dato))

        # ------------------Para la RAM---------------------------------------------------------
        ready = 50
        sett = 70
        go = 80

        ultima_actualizacion = rrdtool.lastupdate(rrdpath + "trendRAM_" + community + ".rrd")
        timestamp = ultima_actualizacion['date'].timestamp()
        dato = ultima_actualizacion['ds']['RAMload']

        tm = datetime.now()
        date = str(tm.hour) + ':' + str(tm.minute) + ' at ' + str(tm.day) + '-' + str(tm.month) + '-' + str(tm.year)

        if dato >= ready and RAM[0]:
            Grafica(int(timestamp), 'RAM', ready, sett, go, community)
            send_alert_attached('ALERTA: La RAM sobrepaso el umbral Ready(' + str(ready) + '%) durante ' + date, community, ip, port, 'RAM')
            RAM[0] = False
            print('Alerta de RAM enviada ' + str(ready))
            time.sleep(10)

        elif dato >= sett and RAM[1]: 
            Grafica(int(timestamp), 'RAM', ready, sett, go, community)
            send_alert_attached('ALERTA: La RAM sobrepaso el umbral Set(' + str(sett) + '%) durante ' + date, community, ip, port, 'RAM')
            RAM[1] = False
            print('Alerta de RAM enviada ' + str(sett))
            time.sleep(10)
        
        elif dato >= go and RAM[2]: 
            Grafica(int(timestamp), 'RAM', ready, sett, go, community)
            send_alert_attached('ALERTA: La RAM sobrepaso el umbral Go(' + str(go) + '%) durante ' + date, community, ip, port, 'RAM')
            RAM[2] = False
            print('Alerta de RAM enviada ' + str(go))
            time.sleep(10)
        
        else:
            print('RAM: ' + str(dato))


                # ------------------Para el DISK---------------------------------------------------------
        ready = 60
        sett = 80
        go = 90

        ultima_actualizacion = rrdtool.lastupdate(rrdpath + "trendDISK_" + community + ".rrd")
        timestamp = ultima_actualizacion['date'].timestamp()
        dato = ultima_actualizacion['ds']['DISKload']

        tm = datetime.now()
        date = str(tm.hour) + ':' + str(tm.minute) + ' at ' + str(tm.day) + '-' + str(tm.month) + '-' + str(tm.year)

        if dato >= ready and DISK[0]:
            Grafica(int(timestamp), 'DISK', ready, sett, go, community)
            send_alert_attached('ALERTA: El almacenamiento sobrepaso el umbral Ready(' + str(ready) + '%) durante ' + date, community, ip, port, 'DISK')
            DISK[0] = False
            print('Alerta de DISK enviada ' + str(ready))
            time.sleep(10)

        elif dato >= sett and DISK[1]: 
            Grafica(int(timestamp), 'DISK', ready, sett, go, community)
            send_alert_attached('ALERTA: El almacenamiento sobrepaso el umbral Set(' + str(sett) + '%) durante ' + date, community, ip, port, 'DISK')
            DISK[1] = False
            print('Alerta de DISK enviada ' + str(sett))
            time.sleep(10)
        
        elif dato >= go and DISK[2]: 
            Grafica(int(timestamp), 'DISK', ready, sett, go, community)
            send_alert_attached('ALERTA: El almacenamiento sobrepaso el umbral Go(' + str(go) + '%) durante ' + date, community, ip, port, 'DISK')
            DISK[2] = False
            print('Alerta de DISK enviada ' + str(go), community)
            time.sleep(10)
        
        else:
            print('DISK: '  + str(dato))           

        time.sleep(40)