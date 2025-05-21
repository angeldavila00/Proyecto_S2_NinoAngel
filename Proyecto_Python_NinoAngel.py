from funciones.FuncionesJson import *
from funciones.funcionesLista import * 
from tabulate import tabulate
from datetime import date, datetime, timedelta 
listaGastos=abrirJSON()

booleano=True
#
#CRUD (CREATE , READ , UPDATE & DELETE)
##INICIO DEL PROGRAMA
while(booleano):
    listaGastos=abrirJSON()
    #En este punto se actualiza la lista de gastos cada vez que se hace un cambio
    print("=============================================")
    print("         Simulador de Gasto Diario")
    print("=============================================")
    print("Seleccione una opción:")
    print(" ")
    print("1. Registrar nuevo gasto")
    print("2. Lista de gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Salir")
    print("=============================================")
    print(" ")
    opcion=int(input("Ingresa una opcion numerica: "))
    print(" ")

    if(opcion==1):
        print("=============================================")
        print("==========Registrar Nuevo Gasto==========\n")
        print("Ingrese la informacion del gasto: \n")
        
        monto=int(input("Monto del gasto:  "))
        unidades=str(input("Cantidad: "))
        categoria=str(input("Categoria ( comida, transporte, entretenimientos, otros):  "))
        info=str(input("Descripcion(opcional): "))
        print("Ingresa la fecha del gasto: ")
        fecha_actual= str(date.today())
        hora= datetime.now().strftime("%H:%M:%S")
        #Aqui hacemos un for para confirmar si deseas guardar el gasto
        print(" ")
        dicGastonuevo={
            "montoGasto":monto,
            "cantidad":unidades,
            "categoria":categoria,
            "descripcion":info,
            "fechas": fecha_actual,
            "hora":hora
        }
        confirmacion=input("Introduzca " ' s '"para guardar o " ' c ' "para cancelar: ")
        print("=============================================\n")
        if((confirmacion=="s") or (confirmacion=="S")):
            listaGastos.append(dicGastonuevo)
            guardarJSON(listaGastos)
            print("Gasto nuevo guardado!")
        else:
            print("Gasto no ingresado")
    if(opcion==2):
        print("=============================================")
        print("================Lista De Gastos================")
        print("=============================================")
        print("Seleccione una opción para filtrar los gastos:")
        print("1. Ver todos los gastos")
        print("2. Filtrar por categoria")
        print("3. Filtrar por rango de fechas")
        print("4. Regresar al menú principal")
        print("=============================================")
        confirmacion=int(input("Ingrese una opcion numerica: "))
        ##VER TODOS LOS GASTOS
        if (confirmacion==1):
            recorrerLista(listaGastos)
            
            ##FILTRAR POR CATEGORIAS
        elif (confirmacion==2):
                categoria=int(input("1. Comida\n2. Transporte\n3. Entretenimiento\n4. Otros\n Dime la opcion: "))
                if (categoria==1):
                    for i in range(len(listaGastos)):
                        if( listaGastos[i]["categoria"] == "comida"):
                            listaComida = [listaGastos[i]]
                            print(tabulate(listaComida, tablefmt="fancy_outline"))
                elif(categoria==2):
                    for i in range(len(listaGastos)):
                        if( listaGastos[i]["categoria"] == "transporte"):
                            listaTransporte = [listaGastos[i]]
                            print(tabulate(listaTransporte, tablefmt="double_outline"))
                elif(categoria==3):
                    for i in range(len(listaGastos)):
                        if( listaGastos[i]["categoria"] == "entretenimiento"):
                            listaEntretenimiento = [listaGastos[i]]
                            print(tabulate(listaEntretenimiento, tablefmt="double_outline"))
                elif(categoria==4):
                    for i in range(len(listaGastos)):
                        if( listaGastos[i]["categoria"] == "otros"):
                            listaOtros = [listaGastos[i]]
                            print(tabulate(listaOtros, tablefmt="double_outline"))
        ##FILTRAR POR FECHA DE RANGO
        elif(confirmacion==3):
            fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
            gastos_filtrados = [gasto for gasto in listaGastos if fecha_inicio <= gasto['fechas'] <= fecha_fin]
            print(tabulate(gastos_filtrados, tablefmt="double_outline")) #\t tabulador

        elif(confirmacion==4):
            print("Regresando al menu principal!")
        else:
            print("No existen resultados. Por favor, seleccione una opción del 1 al 4.")
    if (opcion==3):
        print("================================")
        print("======Calcular total de gastos==")
        print("================================")
        print(" selecciona el periodo de calculo:\n ")
        print("1. Calcular total diario\n")
        print("2. Calcular total semanal\n")
        print("3. Calcular total mensual\n")
        print("4. Regresar al menú principal\n")
        print("================================")
        opcioncal=int(input(""))
        ##Calcular total diario
        if (opcioncal==1):
            fechaHoy=datetime.today().date()
            gastosDiarios=[]
            totalGastos=0
            for i in range (len(listaGastos)):
                fechaGastos=datetime.strptime(listaGastos[i]["fechas"],"%Y-%m-%d").date()
                if (fechaGastos==fechaHoy):
                    gastosDiarios.append(listaGastos[i])
                    totalGastos += listaGastos[i]["montoGasto"]
            if gastosDiarios:
                print(tabulate(gastosDiarios, headers="keys", tablefmt="pipe"))
                print(f"\nTotal Gastos diarios: {totalGastos}")
            else:
                print("No existen gastos en el dia de hoy!!!!")
        ##Calcular total semanal
        elif(opcioncal==2):
                fechaHoy=datetime.today().date()
                fechaSemana= fechaHoy- timedelta(days=7)
                gastoSemanal=[]
                totalGastos=0
                for i in range (len(listaGastos)):
                    fechaGastos=datetime.strptime(listaGastos[i]["fechas"],"%Y-%m-%d").date()
                    if (fechaSemana <= fechaGastos <= fechaHoy):
                        gastoSemanal.append(listaGastos[i])
                        totalGastos += listaGastos[i]["montoGasto"]
                if gastoSemanal:
                    print(tabulate(gastoSemanal, headers="keys", tablefmt="pipe"))
                    print(f"\nTotal Gastos semanal: {totalGastos}")
                else:
                    print("No existen gastos esta semanas!!!!")
    ##Calcular total  MENSUAL
        elif(opcioncal==3):
                fechaHoy=datetime.today().date()
                fechaMes=fechaHoy-timedelta(days=30)
                gastoMes=[]
                totalGastos=0
                for i in range (len(listaGastos)):
                    fechaGastos=datetime.strptime(listaGastos[i]["fechas"],"%Y-%m-%d").date()
                    if(fechaMes <= fechaGastos <= fechaHoy):
                        gastoMes.append(listaGastos[i])
                        totalGastos += listaGastos[i]["montoGasto"]
                if gastoMes:
                    print (tabulate(gastoMes, headers="keys", tablefmt="pipe") )
                    print(f"\nTotal gasto Mensual: {totalGastos}")
                else:
                    print("No hay registros del mes")
        elif(opcioncal==4):
                print("Regresando al menu principal")
    if (opcion==4):
            print("=============================================") 
            print("==========Generar Reporte de Gastos==========")
            print("=============================================")
            print("\n")
            print("1. Reporte diario")
            print("2. Reporte semanal")
            print("3. Reporte mensual")
            print("4. Regresar al menú principal")
            print("=============================================")
            opcioncal=int(input())
            if(opcioncal == 1 ):
                totalDiario(listaGastos)
                (totalComida, totalTransporte, totalEntretenimiento, totalOtros, totales )=totalDiario(listaGastos)
                print("")
                opcionGuardar= int(input("1. Guardar registro, 2 .No guardar registro: "))
                if(opcionGuardar==1):
                    temporal = guardarReporte (opcionGuardar, totalComida, totalTransporte, totalEntretenimiento, totalOtros)
                    guardarlos(logsJSON,guardarJSON,temporal,listaGastos)
            elif(opcioncal==2):
                totalSemana(listaGastos)
                print("")
                (totalComida, totalTransporte, totalEntretenimiento, totalOtros, totales )=totalSemana(listaGastos)
                print("")
                opcionGuardar= int(input("1. Guardar registro, 2 .No guardar registro: "))
                if(opcionGuardar==1):
                    temporal = guardarReporte (opcionGuardar, totalComida, totalTransporte, totalEntretenimiento, totalOtros)
                    guardarlos(logsJSON,guardarJSON,temporal,listaGastos)
            elif(opcioncal==3):
                totalMes(listaGastos)
                print("")
                (totalComida, totalTransporte, totalEntretenimiento, totalOtros, totales )=totalMes(listaGastos)
                print("")
                opcionGuardar= int(input("1. Guardar registro, 2 .No guardar registro: "))
                if(opcionGuardar==1):
                    temporal = guardarReporte (opcionGuardar, totalComida, totalTransporte, totalEntretenimiento, totalOtros)
                    guardarlos(logsJSON,guardarJSON,temporal,listaGastos)
            elif(opcioncal==4):
                print("Regresando al menu principal")
            else:
                print("\nOpcion no valida\nRegresando al menu principal\n")
                
    if (opcion==5):
        print("¿Desea salir del programa? (S/N):")
        confirmacion2= str(input("Dime la respuesta: "))
        if((confirmacion2=="s") or (confirmacion2=="S") ):
            print("HASTA LUEGO!!!!!")
            booleano= False

        elif((confirmacion2=="n") or (confirmacion2=="N")):
            print("No es una opción válida")