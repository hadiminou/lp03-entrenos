from datetime import date, time, datetime
def a_booleano(a):
    booleano=None
    if a != None:
        if a.upper()=='N':
            booleano=False
        elif a.upper()=='S':
            booleano=True
    return booleano

def parse_fecha_hora(cadena, formato="%d/%m/%Y %H:%M"):
#    fecha= datetime.strptime(cadena, "%d/%m/%Y %H:%M").date()
#    hora= datetime.strptime(cadena, "%d/%m/%Y %H:%M").time()
    cadena= datetime.strptime(cadena, "%d/%m/%Y %H:%M")
    return (cadena)

def fecha_en_intervalo(entrenos:list, fecha_i:date, fecha_f:date)->bool:
    res=False
    fecha_entreno = (entrenos.fechahora.date())
    if fecha_i == None and fecha_f == None:
        res=fecha_i<=fecha_entreno
    elif fecha_i == None:
        res=fecha_f>=fecha_entreno
    elif fecha_f == None:
        res=fecha_i<=fecha_entreno
    return res

#def momento_dia(entrenos)

#if __name__=="__main__":
    # print(a_booleano('S')) #para probar funcion a_booleano
    # print(a_booleano('N'))
    # print(a_booleano('A'))
    # print(a_booleano('None'))