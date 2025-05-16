import json

def abrirJSON():
    listaGastos=[]
    with open("./data/data.json",'r') as openFile:
        listaGastos=json.load(openFile)
    return listaGastos

def guardarJSON(dic):
    with open("./data/data.json",'w') as outFile:
        json.dump(dic,outFile)
