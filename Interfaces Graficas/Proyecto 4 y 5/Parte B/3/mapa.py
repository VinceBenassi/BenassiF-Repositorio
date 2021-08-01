# Programa de Franco Benassi
# Proyecto #4 y 5 Interfaces Graficas 2020
# Ejercicio 3
from flask import Flask as fk, jsonify, render_template as rt, request as req

aplicacion = fk(__name__)

Material_Particulado = {
                    0:[],
                    1:[],
                    2:[]
}

@aplicacion.route("/datillos", methods = ['POST'])
def hola_mundo():
    datos = req.json
    Material_Particulado[0] =  datos['01']
    Material_Particulado[1] =  datos['25']
    Material_Particulado[2] =  datos['10']

    print(Material_Particulado)
    return 'Datos Recibidos - Operación Exitosa'

@aplicacion.route('/')
def inicio():
    return rt('mapa.html')

@aplicacion.route('/Get_Data')
def ObtenerDatos():
    return Material_Particulado

if __name__ == '__main__':
    aplicacion.run(debug = True, host = '127.0.0.1', port=5000)