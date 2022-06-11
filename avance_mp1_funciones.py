archivo = open("pokemon.csv",encoding="UTF-8")
next(archivo)
lineas = archivo.readlines()

desc_pok_list = []
tipos_de_pokemon = []
info_pokemon_list = []
id_list = []
info_pokemon = {}
pokemon_por_tipo = {}
dic_nombre_tipo = {}
nombre = []
tipo = []
tuple_tipo = tuple(tipo)


for linea in lineas:
    linea = linea.rstrip("\n")
    columna = linea.split(",")
    tipo_pok = columna[2]

    tipo_pok_2 = tipo_pok.split(";")
    desc_pok_list.append(tipo_pok_2[0])
    r = id_list.append(columna[0])
    nombre.append(columna[1])
    tipo.append(columna[2])
    columna.pop(2)
    columna.pop(0)
    info_pokemon_list.append(columna)
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

info_pokemon = dict(zip(id_list,info_pokemon_list))
dic_nombre_tipo = dict(zip(nombre,tipo))

print(tipos_de_pokemon)
print("------------------------------------")
print(pokemon_por_tipo)
print("------------------------------------")
print(dic_nombre_tipo)


def orden_segun(tipo, criterio):
    if criterio == "HP":
        for tipo_ in tipos_de_pokemon:
            if tipo_ == tipo:
                pass
        
    if criterio == "Defense":
        pass
    if criterio == "Attack":
        pass      
def estadisticas(tipo, criterio):
    pass

def tipo_segun_nombre(nombre):
    pass
    

# print(orden_segun("Grass", "HP"))
