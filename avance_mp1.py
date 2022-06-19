

archivo = open("pokemon.csv",encoding="UTF-8",)
next(archivo)
lineas = archivo.readlines()

desc_pok_list = []
tipos_de_pokemon = []
pokemon_por_tipo = {}

for linea in lineas:
    linea = linea.rstrip("\n")
    columna = linea.split(",")
    tipo_pok = columna[2]
    tipo_pok_2 = tipo_pok.split(";")
    desc_pok_list.append(tipo_pok_2[0])

for elemento in desc_pok_list:
      if elemento not in tipos_de_pokemon:
          tipos_de_pokemon.append(elemento)


for llave in tipos_de_pokemon:
    pokemon_por_tipo[llave] = [[],[]]
    for valor in lineas:
        aux = valor.split(",")
        separador = aux[2].split(";")
        if llave == separador[0]:
            pokemon_por_tipo[llave][0].append(aux[0])
        elif llave == separador[1]:
            pokemon_por_tipo[llave][1].append(aux[0])


print(desc_pok_list)





    
