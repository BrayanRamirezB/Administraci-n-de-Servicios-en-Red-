import rrdtool

def createDB(name, community):
    rrd = rrdtool.create("/media/brayan/Nuevo vol/ESCOM/Redes3/Practica-3/RRD/trend" + name + "_" + community + ".rrd",
                        "--start",'N',
                        "--step",'60', # Cada 60 segundos
                        "DS:" + name + "load:GAUGE:60:0:100", # Gauge permite limitar el tipo de dato del numero de segundos que deben pasar para las muestras validas
                        "RRA:AVERAGE:0.5:1:600")
    if rrd:
        print (rrdtool.error())


