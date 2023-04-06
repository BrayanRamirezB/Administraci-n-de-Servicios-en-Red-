import sys
import rrdtool
import time
import datetime
import calendar
# Cuidar la manera en que se toma el tiempo

def graphRRD(community, tiempo_inicial, tiempo_actual, oid):
    t_inicial = str(time.mktime(tiempo_inicial.timetuple()))[:-2]
    t_actual = str(time.mktime(tiempo_actual.timetuple()))[:-2]

    ret = rrdtool.graph( "Img/DB_" + community + "_" + oid + ".png",
                        "--start",str(t_inicial), # Deben ser congruentes con el tiempo que estoy manejando
                        "--end",str(t_actual),
                        "--vertical-label=Paquetes",# Etiqueta eje vertical
                        "--title=" + community + " - " + oid, # titulo de la grafica
                        "DEF:" + oid + "=" + "DB_" + community + ".rrd:" + oid + ":AVERAGE",
                        "AREA:" + oid + "#0000FF:" + oid)# graficamos ambos traficos
