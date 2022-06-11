
archivo = open("pokemon.csv",encoding="UTF-8",)
next(archivo)
lineas = archivo.readlines()

info_pokemon_list = []
id_list = []
info_pokemon = {}

for linea in lineas:
    linea = linea.rstrip("\n")
    columna = linea.split(",")
    r = id_list.append(columna[0])
    columna.pop(2)
    columna.pop(0)
    info_pokemon_list.append(columna)

info_pokemon = dict(zip(id_list,info_pokemon_list))
# print (info_pokemon)

print(id_list)
print(info_pokemon_list)






