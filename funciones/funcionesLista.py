
from datetime import *


def recorrerLista(listaGastos):
        for i in range(len(listaGastos)):
            print("======================")
            print("==== Gasto #",i+1," ==")
            print("=======================")
            print("MontoGasto:",listaGastos[i]["montoGasto"])
            print("Cantidad:",listaGastos[i]["cantidad"])
            print("Categoria:",listaGastos[i]["categoria"])
            print("Descripcion:",listaGastos[i]["descripcion"])
            print("Fechas",listaGastos[i]["fechas"])    
            print("Hora",listaGastos[i]["hora"])
            print("===========================")



def totalDiario(listaGastos):
    fecha_actual=datetime.today().date()
    gastosReportes=[]
    for i in range (len(listaGastos)):
        fechaGasto=datetime.strptime(listaGastos[i]["fechas"],  "%Y-%m-%d").date() 
        if (fechaGasto==fecha_actual):
            gastosReportes.append(listaGastos[i])
    return reportes(gastosReportes)

def totalSemana(listaGastos):
    fecha_actual=datetime.today().date()
    fechaSemana=fecha_actual-timedelta(days=7)
    gastosReportes=[]
    for i in range (len(listaGastos)):
        fechaGasto=datetime.strptime(listaGastos[i]["fechas"], "%Y-%m-%d").date()
        if (fechaSemana <= fechaGasto <= fecha_actual):
            gastosReportes.append(listaGastos[i])
    return reportes(gastosReportes)

def totalMes(listaGastos):
    fecha_actual=datetime.today().date()
    fechaMensual=fecha_actual-timedelta(days=30)
    gastosReportes=[]
    for i in range (len(listaGastos)):
        fechaGasto=datetime.strptime(listaGastos[i]["fechas"], "%Y-%m-%d").date()
        if (fechaMensual<=fechaGasto<=fecha_actual):
            gastosReportes.append(listaGastos[i])
    return reportes(gastosReportes)
    
def reportes(gastosReportes):
    totalComida=0
    totalTransporte=0
    totalEntretenimiento=0
    totalOtros=0
    totales = {
        "comida": 0,
        "transporte" : 0,
        "entrretenimiento": 0,
        "otros": 0
    }
    for i in gastosReportes:
        totalComida = comida (i,totales, totalComida)
        totalTransporte= transporte (i,totales,totalTransporte)
        totalEntretenimiento= entretenimiento (i, totales, totalEntretenimiento)
        totalOtros= otros (i, totales, totalOtros)
    print(f"comida: ${totalComida}\
        \n-Transporte: ${totalTransporte}\
        \n-Entretenimiento: $ {totalEntretenimiento}\
        \n-Otros: $ {totalOtros}")
    return (totalComida, totalTransporte, totalEntretenimiento, totalOtros, totales )

def comida(i, totales, totalComida):
    if i["categoria"] == "comida":
        totalComida += i["montoGasto"]
        totales["comida"] = totalComida
        return totalComida

def transporte(i,totales, totalTransporte):
    if i["categoria"] == "transporte":
        totalTransporte += i["montoGasto"]
        totales["transporte"] = totalTransporte
        return totalTransporte

def entretenimiento(i,totales, totalEntretenimiento):
    if i["categoria"] == "entretenimiento":
        totalEntretenimiento += i["montoGasto"]
        totales["transporte"] = totalEntretenimiento
        return totalEntretenimiento

def otros(i,totales, totalOtros):
    if i["categoria"] == "otros":
        totalOtros += i["montoGasto"]
        totales["otros"] = totalOtros
    return totalOtros

def guardarReporte (opcionGuardar, totalComida, totalTransporte, totalEntretenimiento, totalOtros):
    temporal={}
    if opcionGuardar == 1:
        temporal = {
            "comida": totalComida,
            "Transporte":totalTransporte,
            "Entretenimiento": totalEntretenimiento,
            "Otros": totalOtros
        }
    else: 
        return temporal

def guardarlos(logsJSON,guardarJSON, temporal, listaGastos):
    logsJSON(temporal)
    guardarJSON(listaGastos)
    