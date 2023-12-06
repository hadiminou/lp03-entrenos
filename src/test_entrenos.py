from entrenos import*
from datetime import date
def test_lee_entrenos(datos:list[Entreno]):
    print("===> Test de lee_entrenos")
    print(f"Leídos {len(datos)} registros.")
    print("\nMostrando los 3 primeros:", datos[:3])
    print("\nMostrando los 3 últimos:", datos[-3:])
    
def test_filtra_por_ubicacion(datos:list[Entreno], ubic):
    print(f"===> Test de filtra por ubicacion", ubic) 
    print(filtra_por_ubicacion(datos, ubic))

def test_tipos_entrenamiento(datos:list, fecha1:date, fecha2:date):
    print("===> Test de tipos entrenamiento")
    print(f"El numero de ejercicios diferentes entre {fecha1},{fecha2} es:", tipos_entrenamiento(datos, fecha1, fecha2))

def test_distancia_total_de_momento_dia(entrenos:list[Entreno], momento:str)->float:
    print("===> Test de distancia total")
    print(f"distancia total de {momento} es:" ,distancia_total_de_momento_dia(entrenos, momento))

if __name__=="__main__":
    datos=lee_entrenos('Proyectos Python\WSPython\git\lp03-entrenos-hadiminou\data\entrenos.csv')
#    test_lee_entrenos(datos)
#    test_filtra_por_ubicacion(datos, 'Sevilla')
#    test_filtra_por_ubicacion(datos, 'Huelva')
#    test_tipos_entrenamiento(datos, None, None)
#    test_tipos_entrenamiento(datos, date(2019,5,4), None)
#    test_tipos_entrenamiento(datos, None, date(2019,5,4))
    test_distancia_total_de_momento_dia(datos, "manana")
    test_distancia_total_de_momento_dia(datos, "TARDE")
    test_distancia_total_de_momento_dia(datos, "Noche")