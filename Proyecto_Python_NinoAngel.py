from funciones.FuncionesGastos import * 
from tabulate import tabulate
from datetime import date, datetime, timedelta 
listaGastos=abrirJSON()

booleano=True
#
while(booleano):
    listaGastos=abrirJSON()
    #En este punto se actualiza la lista de gastos cada vez que se hace un cambio
    print("=============================================")
    print("         Simulador de Gasto Diario")
    print("=============================================")
#CRUD (CREATE , READ , UPDATE & DELETE)
    print("Seleccione una opción:")
    print(" ")
    print("1. Registrar nuevo gasto")
    print("2. Lista de gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Infomacion reporte de gastos")
    print("6. Salir")
    print("=============================================")

    print(" ")
    opcion=int(input("Ingresa una opcion numerica: "))
    print(" ")

    if(opcion==1):
        print("=============================================")
        print("==========Registrar Nuevo Gasto============\n")
        print("=============================================")
        print("Ingrese la informacion del gasto: \n")
        monto=int(input("- Monto del gasto:  "))
        unidades=(input("Cantidad: "))
        categoria=(input("Categoria ( comida, transporte, entretenimientos, otros):  "))
        info=(input("Descripcion(opcional): "))
        print("Ingresa la fecha del gasto: ")
        dia = int(input("Dia: "))
        mes = int(input("Mes: "))
        ano = int(input("Año: "))
        hora= datetime.now().strftime("%H:%M:%S")
        #Aqui hacemos un for para confirmar si deseas guardar el gasto
        print(" ")
        dicGastonuevo={
            "id": (listaGastos[len(listaGastos)-1]["id"])+1,
            "montoGasto":monto,
            "cantidad":unidades,
            "categoria":categoria,
            "descripcion":info,
            "fechas": str(datetime(ano, mes, dia).date()),
            "hora":hora
        }
        confirmacion=input("Introduzca " ' s '"para guardar o " ' c ' "para cancelar: ")
        print("=============================================\n")
        if(confirmacion=='s'):
            listaGastos.append(dicGastonuevo)
            guardarJSON(listaGastos)
            print("Gasto nuevo guardado!")
        else:
            print("Gasto no ingresado")
        print(" ")
##Menu Dos
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
        if (confirmacion==1):
            print(tabulate(listaGastos, tablefmt="double_outline"))
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
                else: print("¡No existen gastos!")
                            
        elif(confirmacion==3):#Filtrar por rango de fechas
                        print("Ingresa la fecha inicial!!!")
                        mes=int(input("Mes: "))
                        dia= int(input("Dia: "))
                        ano=int(input("Año: "))
                        fecha1 =datetime(ano,mes,dia).date()

                        print("Ingresa fecha final!!!")
                        dia= int(input("Dia: "))
                        mes=int(input("Mes: "))
                        ano=int(input("Año: "))
                        fecha2= datetime(ano,mes,dia).date()
                        for q in range(len(listaGastos)):
                            fechaStr= listaGastos[q]["fechas"]
                            fechaForm = datetime.strptime(fechaStr, "%Y-%m-%d").date()#convierte cadena a fecha
                            print("============================")
                            if fecha1 <= fechaForm <= fecha2:
                                for a in listaGastos[q]:
                                    print(f"{a}\t{listaGastos[q][a]}") #\t tabulador
        elif(confirmacion==4):
                print("Regresando al menu principal!")
        else: print("¡Ingrese una opcion valida!")
    if(opcion==3):
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
        #######Calcular total semanal
        elif(opcioncal==2):
                fechaHoy=datetime.today().date()
                fechaSemana= fechaHoy- timedelta(days=7)
                gastoSemanal=[]
                totalGastos=0
                for i in range (len(listaGastos)):
                    fechaGastos=datetime.strptime(listaGastos[i] ["fecha"],"%Y-%m-&d").date()
                    if (fechaSemana <= fechaGastos <= fechaHoy):
                        gastoSemanal.append(listaGastos[i])
                        totalGastos += listaGastos[i]["montoGasto"]
                if gastoSemanal:
                    print(tabulate(gastoSemanal, headers="keys", tablefmt="pipe"))
                    print("\nTotal Gastos diarios: {totalGastos}")
                else:
                    print("No existen gastos esta semanas!!!!")
        elif(opcioncal==3):
            fechaHoy=datetime.today().date()
            fechaMes=fechaHoy-timedelta(days=30)
            gastoMes=[]
            totalGastos=0
            for i in range (len(listaGastos)):
                fechaMes=datetime.strptime(listaGastos[i]["fecha"],"%Y-%m-&d").date()
                if(fechaMes<=listaGastos<=fechaHoy):
                    gastoMes.append(listaGastos[i])
                    totalGastos += listaGastos[i]["montoGasto"]
            if gastoMes:
                print (tabulate(gastoMes, headers="keys", tablefmt="pipe") )
                print(f"\nTotal gasto Mensual: {totalGastos}")
            else:
                print("No hay registros del mes")
        elif(opcioncal==4):
            print("Regresando al menu principal")
    if(opcion==4):
        print("=============================================") 
        print("==========Generar Reporte de Gastos==========")
        print("=============================================")
        print("\n")
        print("1. Reporte diario")
        print("2. Reporte semanal")
        print("3. Reporte mensual")
        print("4. Regresar al menú principal")
        print("=============================================")
        opcion=int(input())
        if(opcion==1):
            for i in range (len(listaGastos)):
                print(tabulate(listaGastos, tablefmt="github"))

    if(opcion==5):
        print("=============================================") 
        print("=======Informacion Reporte de Gastos=========")
        print("=============================================")
        print("\n")
        print("1. Actualizar reporte de gasto")
        print("2. Eliminar reporte de gasto")
        print("3. Visualizar reporte de gasto individual")
        print("4. Regresar al menú principal")
        print("=============================================")
        opcionIndividual=int(input("Ingrese una opcion numerica:  "))
        if (opcionIndividual==1):
            print("=============================================")
            print("INFORMACION QUE VAS ACTUALIZAR!!!")
            print("=============================================")
            opcionIndividual = int(input("Por favor ingresar el numero del Gasto deseado a modificar:\n "))
            mostrarUna(listaGastos,opcionIndividual)

            usuarioTemporal = listaGastos[opcionIndividual-1]
            montoTemporal=int(input("Monto del gasto:  "))
            unidadesTemporal=(input("Cantidad: "))
            categoriaTemporal=(input("Categoria ( comida, transporte, entretenimientos, otros):  "))
            infoTemporal=(input("Descripcion(opcional): "))
            print("Ingresa la fecha del gasto: ")
            diaTemporal = int(input("Dia: "))
            mesTemporal = int(input("Mes: "))
            anoTemporal = int(input("Año: "))
            horaTemporal= datetime.now().strftime("%H:%M:%S")

            
            diccionarioAgregar={"id":listaGastos[opcionIndividual-1]["id"], "monto":montoTemporal,"unidades":unidadesTemporal,"categoria":categoriaTemporal,"info":infoTemporal,"hora":horaTemporal}
            listaGastos[opcionIndividual-1]=diccionarioAgregar
            guardarJSON(listaGastos)
    if (opcion==6):
        print("¿Desea salir del programa? (S/N):")
        confirmacion2= (input("Dime la respuesta: "))
        if((confirmacion2=="s") or(confirmacion2=="S")):
            print("HASTA LUEGO!!!!!")
            booleano= False
        elif((confirmacion2=="n")or (confirmacion2=="n")):
            print("No es una opción válida")
            



