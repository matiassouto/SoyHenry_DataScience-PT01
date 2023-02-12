dicc_emisiones = {  'cod_pais' : [],
                    'nom_pais' : [],
                    'region' : [],
                    'anio' : [],
                    'co2' : [],
                    'co2_percapita' : []}

campos = []
with open('Emisiones_CO2.csv', 'r') as archivo2: 
    next(archivo2)
    lines = archivo2.readlines()
    for line in lines:
        line = line.strip()
        campos = line.split('|') # Separo los datos, '|' es el separador que se usa
#Orden del .csv --> Código de país|Nombre del país|Región|Año|CO2 (kt)|CO2 per cápita (toneladas métricas)
        dicc_emisiones['cod_pais'].append(campos[0])
        dicc_emisiones['nom_pais'].append(campos[1])
        dicc_emisiones['region'].append(campos[2])
        dicc_emisiones['anio'].append(campos[3])
        dicc_emisiones['co2'].append(campos[4])
        dicc_emisiones['co2_percapita'].append(campos[5])


# a) ¿Cuántas variables hay?
claves = [key for key in dicc_emisiones.keys()]
print("Existen {} variables en el csv {} \n".format(len(claves), "Emisiones_CO2.csv"))

#b) ¿Qué tipos de datos usar para cada una?
# Código de país: str
# Nombre del país: str
# Región: str
# Año: int o date 
# CO2 (kt): float
# CO2 per cápita (toneladas métricas): float

#CASTEO A TIPOS DE DATOS
for key in dicc_emisiones.keys():
    for i, element in enumerate(dicc_emisiones[key]):
        element = element.replace('.', '') #Elimino los puntos de los numeros 999.999.999 --> 999999999
        element = element.replace(',', '.') #Las , deben ser . 99,7 --> 99.7
        #Casteo las variables a sus correspondientes tipos de datos, las vacias a None (null)
        if element != '':
            if key == 'anio':
                dicc_emisiones[key][i] = int(element)
            if key == 'co2' or key == 'co2_percapita':
                dicc_emisiones[key][i] = float(element)
        else:
            dicc_emisiones[key][i] = None

# c) ¿Qué tipo de variables son?
# Código de país: cualitativa --> categorica 
# Nombre del país: cualitativa --> categorica
# Región: cualitativa --> categorica
# Año: cualitativa --> ordinal 
# CO2 (kt): cuantitativa (continua)
# CO2 per cápita (toneladas métricas): cuantitativa (continua)


# d) ¿Hay valores faltantes?
#En este caso estan con '', normalmente habría que modificar para que sean None
faltantes = {  'cod_pais' : 0, 'nom_pais' : 0, 'region' : 0, 'anio' : 0,'co2' : 0,'co2_percapita' : 0}
for key in dicc_emisiones.keys():
    for element in dicc_emisiones[key]:
        if element == None:
            faltantes[key] += 1
print("Datos faltantes por campo {}".format(faltantes))

# e) ¿Cuál es el total de emisiones de CO2 para 'América Latina y Caribe' en el año 2010?
region = 'América Latina y Caribe'
anio = 2010
totalEmiciones = 0.0
for i,emicion in enumerate( dicc_emisiones['co2'] ):
    if dicc_emisiones['anio'][i] == anio and dicc_emisiones['region'][i] == region:
        if emicion != None:
            totalEmiciones += emicion
print("El total de emiciones de co2 para 'América Latina y Caribe' es {} ".format( round(totalEmiciones, 2)) )