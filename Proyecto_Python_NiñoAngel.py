from funciones.FuncionesGastos import * 
from tabulate import tabulate

listaGastos=abrirJSON()

booleano=True

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
    print("5. Salir")
    print("=============================================")

    print(" ")
    opcion=int(input("Ingresa una opcion numerica: "))
    print(" ")

    if(opcion==1):
        print("=============================================")
        print("==========Registrar Nuevo Gasto==========\n")
        print("Ingrese la informacion del gasto: \n")
        
        monto=int(input("- Monto del gasto:  "))
        unidades=str(input("Cantidad: "))
        categoria=str(input("Categoria ( comida, transporte, entretenimientos, otros):  "))
        info=str(input("Descripcion(opcional): "))
        
        #Aqui hacemos un for para confirmar si deseas guardar el gasto
        print(" ")
        dicGastonuevo={
            "montoGasto":monto,
            "cantidad":unidades,
            "categoria":categoria,
            "descripcion":info
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
#################################################################################################################3
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
                            print(tabulate(listaGastos, tablefmt="double_outline"))
                elif(categoria==2):
                    for i in range(len(listaGastos)):
                        if( listaGastos[i]["categoria"] == "transporte"):
                            listaTransporte = [listaGastos[i]]
                            print(tabulate(listaGastos, tablefmt="double_outline"))
                elif(categoria==3):
                    for i in range(len(listaGastos)):
                        if( listaGastos[i]["categoria"] == "entretenimiento"):
                            listaEntretenimiento = [listaGastos[i]]
                            print(tabulate(listaGastos, tablefmt="double_outline"))
                elif(categoria==4):
                    for i in range(len(listaGastos)):
                        if( listaGastos[i]["categoria"] == "otros"):
                            listaOtros = [listaGastos[i]]
                            print(tabulate(listaGastos, tablefmt="double_outline"))
                            
                elif(confirmacion==3):#FALTAAAAAAAAAAA TERMINARRR
                    fechaInicio=int(input("Ingrese la fecha del inicio de busqueda"))
                    fechaFinal=(int(input("Ingrese la fecha del final de busqueda")))

                elif(confirmacion==4):
                    print("Regresando al menu principal!")
    if (opcion==3):
        print("================================")
        print("======Calcular total de gastos==")
        print("================================")
        print("1. selecciona el periodo de calculo:\n ")
        print("1. Calcular total diario\n")
        print("2. Calcular total semanal\n")
        print("3. Calcular total mensual\n")
        print("4. Regresar al menú principal\n")
        print("================================")
        opcioncal=int(input(""))
        if (opcioncal==1):
            print("")
        elif(opcioncal==2):
            print("")
        elif(opcioncal==3):
            print("")
        elif(opcioncal==4):
            print("")

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


    if (opcion==5):
        print("¿Desea salir del programa? (S/N):")
        confirmacion2= str(input("Dime la respuesta: "))
        if(confirmacion2=="s"):
            print("HASTA LUEGO!!!!!")
            booleano= False
        elif(confirmacion2=="n"):
            print("No es una opción válida")
            



