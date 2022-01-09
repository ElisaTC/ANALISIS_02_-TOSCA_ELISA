import csv
#Abriremos el archivo de base de datos en modo lectura para su análisis, el enconding lo utilicé para que pudiera obtener bien las variables
with open ('synergy_logistics_database.csv', 'r', encoding='utf-8-sig') as archivo_proyecto2:
    operaciones = csv.DictReader (archivo_proyecto2)
    #En "Lista", tendremos los datos en diccionario para su análisis
    lista = []
    for linea in operaciones:
        lista.append(linea) 

#>>>>>>>>>>>>>>>>>>>>>Rutas de importación y exportación más demandadas<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Creamos una función para obtener las 10 rutas más solicitadas de acuerdo a la dirección de la ruta, es decir si es importación o exportación
def rutasdemandadas (rutadirection):
    totalderutas = [] #Aquí se guardaran los datos de las rutas, como son origen, destino, número de veces que se utilizó la ruta y el valor monetario
    for ruta in lista:
        if ruta ['direction'] == rutadirection : # Este nos permite diferenciar las improtaciones y exportaciones de acuerdo al llamado que se haga
            origen = ruta['origin']
            destino = ruta['destination']
            valor = ruta['total_value']
            #Nos permite armar de primera mano una lista de todas las rutas utilizadas en importaciones o exportaciones, de acuerdo al origen y destino
            if origen and destino not in totalderutas :
                totalderutas.append ([origen, destino, 0, 0])
            
            #Nos permite analizar todos los datos e ir sumando los valores monetarios total de las rutas y cuantas veces fue solicitado el servicio
            for rutavista in totalderutas :
                origenn = rutavista[0]
                destinon = rutavista[1]
                if origenn == origen and destinon == destino :
                    rutavista [2] += 1
                    rutavista [3] += int (valor)
                    break

#Nos permite acomodar de mayor a menos de acuerdo al parámetro de solicitudes obteniendo únnicamente lo 10 primeros de la lista
    totalderutas.sort (reverse=True, key = lambda x:x [2])
    totalderutas10 = totalderutas [:10]
    return totalderutas10

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><Medios de transporte<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Este se utilizó para obtener cuantos medios de transporte utiliza Synergy Logistics en total
totaldemediosdetransporte = []
for linea in lista :
    if linea ['transport_mode'] not in totaldemediosdetransporte :
        totaldemediosdetransporte.append (linea ['transport_mode'])
#Se definió una función para obtener el uso y valor monetario que se le da a los distintos transportes de acuerdo a la dirección de la ruta, importación y exportación
def rutasdetransporte (rutadirection):
    totaldetransporte = [] #Aquí se guardaran los datos de los transportes utilizados
    for ruta in lista:
        if ruta ['direction'] == rutadirection : # Este nos permite diferenciar las improtaciones y exportaciones de acuerdo al llamado que se haga
            valort = ruta['total_value']
            transporte = ruta['transport_mode']
            #Nos permite hacer una lista de todos los transporte utilizados en improtaciones o exportaciones, para luego anexar el valor monetario
            #total de acuerdo a las rutas empleadas
            if transporte not in totaldetransporte :
                totaldetransporte.append ([transporte, 0])
            #Por cada transporte se añade el valor monetario total a cada transporte
            for tp in totaldetransporte :
                transporten = tp[0]
                if transporten == transporte :
                    tp [1] += int (valort)
                    break

#Nos permite acomodar de mayor a menos de acuerdo al parámetro de solicitudes obteniendo únnicamente los 3 primeros de la lista
    totaldetransporte.sort (reverse=True, key = lambda x:x [1])
    totaldetransporte = totaldetransporte [:3]
    return totaldetransporte

#>>>>>>>>>>>>>>>>>>>>>Ingresos por países<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Definimos una función, igualmente para saber que países representaban un mayor ingreso a Synergy Logistics de acuerdo a 
#dirección de ruta, exportación o importación
def paisesporcentaje (rutadirection):
    paisesorigen = [] #Aquí se guardaran los países que solicitaron el servicio
    for pais in lista:
        if pais['direction'] == rutadirection : # Este nos permite diferenciar las importaciones y exportaciones de acuerdo al llamado que se haga
            valorpais = pais['total_value']
            paisori = pais['origin']
            #Nos permite hacer una lista de todos países que solicitaron el servicio, improtaciones o exportaciones, para luego anexar el valor total
            # y el porcetaje que este representa de los ingresos
            if paisori not in paisesorigen :
                paisesorigen.append ([paisori, 0,0])
            #Nos permite agregar los valores monetarios total a cada país
            for pv in paisesorigen :
                paiso = pv[0]
                if paiso == paisori :
                    pv [1] += int (valorpais)
                    break
    #Numpaises nos permite saber cuantos países se trabajaron en esa ruta
    numpaises = len (paisesorigen)
    #Valor total nos permitirá obtener la suma de valor monetario que se obtuvo en las rutas, importación o exportación, para posteriormente
    #calcular el porcentaje y anexarlo a la lista
    valortotal = 0
    for pais in paisesorigen:
        valortotal += pais [1]
    for pais in paisesorigen:
        pais [2] = ((pais[1]*100)/valortotal)

    numpaises = len (paisesorigen)
    print (f'Contamos con un total de {numpaises} en las rutas de {rutadirection}')
#Nos permite acomodar de mayor a menos de acuerdo al parámetro de solicitudes obteniendo únnicamente lo 10 primeros de la lista
    paisesorigen.sort (reverse=True, key = lambda x:x [1])
    paisesorigen = paisesorigen [:10]
    return paisesorigen
#Para obtener datos de los países que generan más valor monetario en total, se definió ppaisesexpimpporcentaje, el cual
#es igual a la función anterior, únicamente omitiendo la selección por dirección de ruta
def paisesexpimpporcentaje ():
    paisesorigentotales = [] 
    for pais in lista:
            valorpais = pais['total_value']
            pais = pais['origin']
            if pais not in paisesorigentotales :
                paisesorigentotales.append ([pais, 0,0])
            for pv in paisesorigentotales :
                paiso = pv[0]
                if paiso == pais :
                    pv [1] += int (valorpais)
                    break
    
    numpaisestot = len (paisesorigentotales)

    valortotal = 0
    for pais in paisesorigentotales:
        valortotal += pais [1]
    for pais in paisesorigentotales:
        pais [2] = ((pais[1]*100)/valortotal)

    numpaisestot = len (paisesorigentotales)
    print (f'Contamos con un total de {numpaisestot} en las rutas de importación y exportación')
#Nos permite acomodar de mayor a menos de acuerdo al parámetro de solicitudes obteniendo únnicamente lo 10 primeros de la lista
    paisesorigentotales.sort (reverse=True, key = lambda x:x [1])
    paisesorigentotales = paisesorigentotales [:10]
    return paisesorigentotales

print (f'''------------------------------------------------------Synergy Logistics----------------------------------------------------------
Análisis de Estrategia Operativa para 2021.
Se plantea analizar la viabilidad de 3 opciones de enfoque: rutas de importación y exportación, medio de transporte utilizado y valor total de importaciones y exportaciones.

-OPCION 1) Rutas de importación y exportación. Rutas más demandadas de Importación y Exportación de acuerdo a su origen.
Contamos con un total de {len(lista)} rutas de exportación e importación.''')

exportaciones = rutasdemandadas ('Exports')
print ('\nDe acuerdo a la demanda del servicio, este es el top 10 rutas de exportación solicitadas:')
for rutasie in exportaciones :
    print (rutasie)

importaciones = rutasdemandadas ('Imports')
print ('\nDe acuerdo a la demanda del servicio, este es el top 10 rutas de importación solicitadas:')
for rutasie in importaciones :
    print (rutasie)

print ('\n-OPCION 2) Medios de transporte')
print (f'Los principales medios de transportes son {totaldemediosdetransporte}, en total se utilizan {len (totaldemediosdetransporte)} medios de transporte.')
exptransporte = rutasdetransporte ('Exports')
print ('\nDe acuerdo a la demanda del servicio, este es el top 3 rutas de exportación solicitadas:')
for expt in exptransporte  :
    print (expt)

imptransporte = rutasdetransporte ('Imports')
print ('\nDe acuerdo a la demanda del servicio, este es el top 3 rutas de importación solicitadas:')
for impt in imptransporte:
    print (impt)

print ('\n-OPCION 3) Porcentaje de ingresos por países')
exppaises = paisesporcentaje('Exports')
print ('\n El servicio de exportación se destacan destacan los siguientes países de acuerdo a su aportación:')
for paise in exppaises  :
    print (paise)

imppais = paisesporcentaje('Imports')
print ('\n El servicio de importación se destacan destacan los siguientes países de acuerdo a su aportación:')
for paisi in imppais:
    print (paisi)

ingresospaisestotales = paisesexpimpporcentaje ()
print ('\n De acuerdo a todas las rutas existentes, los países que destacan en su aportación monetaria a Synergy Logistics en importación y exportacion destacan:')
for pais in ingresospaisestotales:
    print (pais)