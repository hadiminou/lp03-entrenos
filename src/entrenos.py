from collections import namedtuple
import csv
from datetime import date, time, datetime
#from parsers import* 
Entreno = namedtuple('entreno', 'tipo, fechahora, ubicacion, duracion,\
                      calorias, distancia, frecuencia, compartido')

'''def parse_fecha_hora(cadena, formato="%d/%m/%Y %H:%M"):
#    fecha= datetime.strptime(cadena, "%d/%m/%Y %H:%M").date()
#    hora= datetime.strptime(cadena, "%d/%m/%Y %H:%M").time()
    cadena= datetime.strptime(cadena, "%d/%m/%Y %H:%M")
    return (cadena)'''

def a_booleano(a):
    booleano=None
    if a != None:
        if a.upper()=='N':
            booleano=False
        elif a.upper()=='S':
            booleano=True
    return booleano

def lee_entrenos(ruta)->list[Entreno]:
    entrenos = list()
    with open (ruta,'rt',encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion,\
                      calorias, distancia, frecuencia, compartido in lector:   
            fechahora= datetime.strptime(fechahora, "%d/%m/%Y %H:%M") 
            lista=Entreno(tipo, fechahora, ubicacion, int(duracion),\
                      int(calorias), float(distancia), int(frecuencia), a_booleano(compartido))
            entrenos.append(lista)
    return entrenos

def filtra_por_ubicacion(entrenos:list[Entreno], ubic:str)->list[Entreno]:
    res=[]
    for i in entrenos:
        if i.ubicacion == ubic:
            res.append((i))
    return res

'''def fecha_en_intervalo(entrenos:list[Entreno], fecha_i:date, fecha_f:date)->bool:
    res=False
    #fecha_entreno = (entrenos.fechahora.date())
    if fecha_i == None and fecha_f == None:
        res=fecha_i<=fecha_entreno
    elif fecha_i == None:
        res=fecha_f>=fecha_entreno
    elif fecha_f == None:
        res=fecha_i<=fecha_entreno
    return res'''

'''def fecha_en_intervalo(entrenos:list[Entreno], fecha_i, fecha_f):
    res = False
    fecha_entreno = entrenos.fechahora.date()
    if fecha_i <= fecha_entreno and fecha_entreno < fecha_f:
        res = True
    return res'''

def tipos_entrenamiento(entrenos:list[Entreno], fecha_i:date, fecha_f:date)->int:
    res = set()
    for i in entrenos:
        if (fecha_i==None or fecha_i<=i.fechahora.date()) and (fecha_f==None or i.fechahora.date()<fecha_f):
#        if fecha_en_intervalo(entrenos, fecha_i, fecha_f):        
            res.add((i.tipo))
    return len(res)

#def momento_dia(entrenos)->str:

def distancia_total_de_momento_dia(entrenos:list[Entreno], momento:str)->float:
    res = []
    for i in entrenos:
        if momento.upper()=="MANANA" and time(7,00) <= i.fechahora.time() < time(14,00):
            res.append(i.distancia)
        if momento.upper()=="TARDE" and time(14,00) <= i.fechahora.time() < time(21,00):
            res.append(i.distancia)
        if momento.upper()=="NOCHE" and time(21,00) <= i.fechahora.time() < time(7,00):
            res.append(i.distancia)
    return sum(res)    