archivo = open("pokemon.csv",encoding="UTF-8",)
next(archivo)
lineas = archivo.readlines()

info_pokemon_list = []
id_list = []
poke_tipo_list = []

for linea in lineas:
    linea = linea.rstrip("\n")
    columna = linea.split(",")
    p = id_list.append(columna[0])
    info_pokemon_list.append(columna[2])




for poke_ in info_pokemon_list:
    poke_ = poke_.split(";")
    poke_tipo_list.append(poke_)


print(lineas)
# print(id_list)



