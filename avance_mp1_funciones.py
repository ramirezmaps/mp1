archivo = open("pokemon.csv",encoding="UTF-8")
next(archivo)
lineas = archivo.readlines()

desc_pok_list = []
tipos_de_pokemon = []
info_pokemon_list = []
id_list = []
info_pokemon = {}
pokemon_por_tipo = {}
pokemon_para_HP = {}
pokemon_para_ataque = {}
pokemon_para_defensa = {}
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
            pokemon_por_tipo[llave][0].append(aux[3])
        elif llave == separador[1]:
            pokemon_por_tipo[llave][1].append(aux[0])


# for llave in tipos_de_pokemon:
#     pokemon_para_HP[llave] = [[]]
#     for valor in lineas:
#         aux = valor.split(",")
#         separador = aux[2].split(";")
#         if llave == separador[0]:
#             pokemon_para_HP[llave][0].append(aux[3])

# suma_HP = 0
# cont_HP = 0

# suma_ataque = 0
# cont_ataque = 0

# suma_defensa = 0
# cont_defensa =0

# if pokemon_para_HP[tipo] = 
# for k,v in pokemon_para_HP.items():
#     for numeros_v in v:
#         for numero in numeros_v:
#             r = (int(numero))
#             suma = suma + r
#             cont_HP = cont_HP + 1
            
# promedio_HP = suma/cont_HP
# print(promedio_HP)


# for llave in tipos_de_pokemon:
#     pokemon_para_ataque[llave] = [[]]
#     for valor in lineas:
#         aux = valor.split(",")
#         separador = aux[2].split(";")
#         if llave == separador[0]:
#             pokemon_para_ataque[llave][0].append(aux[4])

# for llave in tipos_de_pokemon:
#     pokemon_para_defensa[llave] = [[]]
#     for valor in lineas:
#         aux = valor.split(",")
#         separador = aux[2].split(";")
#         if llave == separador[0]:
#             pokemon_para_defensa[llave][0].append(aux[4])

info_pokemon = dict(zip(id_list,info_pokemon_list))
dic_nombre_tipo = dict(zip(nombre,tipo))

#print("--------------TIPOS DE POKEMON----------------------")
# 'Grass', 'Rock', 'Fire'
#print(tipos_de_pokemon)

# print("---------POKEMON POR TIPO---------------------------")
#{'Grass': [['1', '470', '2', '3'], []], 'Rock': [['140'], []], 'Fire': [['4'], []]}
# print(pokemon_para_HP)

#print("---------------DICCIONARIO POKEMON---------------------")
#{'Bulbasaur': 'Grass;Poison', 'Leafeon': 'Grass;', 'Kabuto': 'Rock;Water', 'Ivysaur': 'Grass;Poison', 'Venusaur': 'Grass;Poison', 'Charmander': 'Fire;'}
#print(dic_nombre_tipo)


#print(dic_nombre_tipo)


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
    if criterio == 'HP':
        for k,v in pokemon_por_tipo.items():
            if k == tipo:
                return(v)
    pass


def tipo_segun_nombre(nombre):
    for k,v in dic_nombre_tipo.items():
        if k == nombre:
            tipos_= v
        return(k, v)
    pass

print(tipo_segun_nombre("Pidove"))