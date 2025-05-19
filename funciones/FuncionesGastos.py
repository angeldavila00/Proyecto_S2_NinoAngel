import json

def abrirJSON():
    listaGastos=[]
    with open("./data/data.json",'r') as openFile:
        listaGastos=json.load(openFile)
    return listaGastos

def guardarJSON(dic):
    with open("./data/data.json",'w') as outFile:
        json.dump(dic,outFile)

            
            
def mostrarUna(listaGastos,opcionIndividual):
    print("#################")
    print("#### Gasto#",opcionIndividual," ####")
    print("#################")
    print("ID:", listaGastos[opcionIndividual-1]["id"])
    print("MontoGasto:",listaGastos[opcionIndividual-1]["montoGasto"])
    print("Cantidad:",listaGastos[opcionIndividual-1]["cantidad"])
    print("Categoria",listaGastos[opcionIndividual-1]["categoria"])
    print("Descripcion",listaGastos[opcionIndividual-1]["descripcion"])
    print("Fechas",listaGastos[opcionIndividual-1]["fechas"])
    print("Hora",listaGastos[opcionIndividual-1]["hora"])

def cargarLogs():
    dicFinal=[]
    with open("./data/logs.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

