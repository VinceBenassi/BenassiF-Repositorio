from sqlite3.dbapi2 import Cursor, converters
import serial as sr
import sqlite3


ser =  sr.Serial('/dev/pts/1',9600)
con = sqlite3.connect("/home/franco-os/Documentos/Proyectos Proteus/baseTemperatura.db")
cursor = con.cursor()
for i in range (4):
    datos = ser.readline().decode("ascii") 
    print(datos)
    tupla = (datos,"°C")
    consulta = '''INSERT INTO "Datos" (Data, Medición) VALUES (?,?)'''
    cursor.execute(consulta,tuple)
    con.commit()