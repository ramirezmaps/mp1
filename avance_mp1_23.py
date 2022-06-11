archivo = open("pokemon.csv",encoding="UTF-8",)
next(archivo)
lineas = archivo.readlines()


nombre_tipo = []
tipo_separado = []
dict_nombre_tipo = {}


for linea in lineas:
    linea = linea.rstrip("\n")
    columna = linea.split(",")
    nombre_tipo.append(columna[1:3])

for llave in nombre_tipo:
    dict_nombre_tipo[llave] = [[],[]]
    for valor in lineas:
        x_aux = valor.split(",")
        tipo_separador = x_aux[2].split(";")
        if llave == tipo_separador[0]:
            dict_nombre_tipo[llave][0].append(x_aux[0])
        elif llave == tipo_separador[1]:
            dict_nombre_tipo[llave][1].append(x_aux[0])


print(dict_nombre_tipo)





