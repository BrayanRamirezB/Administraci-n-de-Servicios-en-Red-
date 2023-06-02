#!/usr/bin/env python
import rrdtool
import os

def createRRD(community):
    if (not os.path.exists("DB_"+ community +".rrd")):
        collections = {"PaqUnicast", "PaqrecibidosIP", "msgICMP", "SegmentosRecv", "DtmsEntregado"}
        aux = []

        for obj in collections:
            aux.append("DS:{}:COUNTER:120:U:U".format(obj))

        # Crea la BD con el nombre DB_community.rrd
        ret = rrdtool.create("DB_"+ community +".rrd",
                            "--start",'N', # Inicia en el tiempo actual 'N'
                            "--step",'60', # Step de 60 segundos
                            aux, # Generan las colecciones de datos
                            "RRA:AVERAGE:0.5:1:288") # longitud de 288 filas, cada minuto calcula el average
        
        if ret:
            print(rrdtool.error())
    else:
        print("La BD ya existe")    



    # rrdtool.dump("traficoRED.rrd", "traficoRED.xml")

    # Paso 1 - crear la BD
    # Paso 2 - Ejecutar el script de update y dejarlo un tiempo
    # Paso 3 - graficar el trafico
