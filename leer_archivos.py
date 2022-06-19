archivo = open("pokemon.csv",encoding="UTF-8",)
next(archivo)
lineas = archivo.readlines()

info_pokemon_list = []
id_list = []
poke_tipo_list = []
nombres_y_tipos = []

for linea in lineas:
    linea = linea.rstrip("\n")
    columna = linea.split(",")
    nombres_y_tipos.append(columna[1:3])


print (nombres_y_tipos)

for nombre_y_tipo in nombres_y_tipos:
    print(nombre_y_tipo)