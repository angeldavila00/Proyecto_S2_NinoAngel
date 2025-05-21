
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