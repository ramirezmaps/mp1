from collections import defaultdict

def def_value():
    return "No es una opción"

## Definición funciones ##

def orden_segun(tipo, criterio):
    if criterio == "HP":
        for tipo_ in tipos_de_pokemon:
            if tipo_ == tipo:
                pass
        
    if criterio == "Defense":
        pass
    if criterio == "Attack":
        pass  
    pass

def estadisticas(tipo, criterio):
    if criterio == 'HP':
        for k,v in pokemon_por_tipo.items():
            if k == tipo:
                return(v)
    pass
def tipo_segun_nombre(nombre):
    for k,v in info_pokemon.items():
        if pokemon_por_tipo[k] == nombre:
            tipos_= v
        return(k, v)
    


## Lectura archivo y definicion estructuras ##
archivo = open("pokemon.csv","r",encoding="UTF-8")
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

suma_HP = 0
cont_HP = 0

suma_ataque = 0
cont_ataque = 0

suma_defensa = 0
cont_defensa =0

for linea in lineas:
    linea = linea.rstrip("\n")
    columna = linea.split(",")
    tipo_pok = columna[2]
    tipo_pok_2 = tipo_pok.split(";")
    desc_pok_list.append(tipo_pok_2[0])
    r = id_list.append(columna[0])
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

for llave in tipos_de_pokemon:
    pokemon_para_HP[llave] = [[]]
    for valor in lineas:
        aux = valor.split(",")
        separador = aux[2].split(";")
        if llave == separador[0]:
            pokemon_para_HP[llave][0].append(aux[3])

for llave in tipos_de_pokemon:
    pokemon_para_ataque[llave] = [[]]
    for valor in lineas:
        aux = valor.split(",")
        separador = aux[2].split(";")
        if llave == separador[0]:
            pokemon_para_ataque[llave][0].append(aux[4])

for llave in tipos_de_pokemon:
    pokemon_para_defensa[llave] = [[]]
    for valor in lineas:
        aux = valor.split(",")
        separador = aux[2].split(";")
        if llave == separador[0]:
            pokemon_para_defensa[llave][0].append(aux[5])

info_pokemon = dict(zip(id_list,info_pokemon_list))

for k,v in pokemon_para_HP.items():
    for numeros_v in v:
        for numero in numeros_v:
            r = (int(numero))
            suma_HP = suma_HP + r
            cont_HP = cont_HP + 1


promedio_HP = suma_HP/cont_HP

for k,v in pokemon_para_ataque.items():
    for numeros_v in v:
        for numero in numeros_v:
            r = (int(numero))
            suma_ataque = suma_ataque + r
            cont_ataque = cont_ataque + 1

promedio_ataque = suma_ataque/cont_ataque

for k,v in pokemon_para_defensa.items():
    for numeros_v in v:
        for numero in numeros_v:
            r = (int(numero))
            suma_defensa = suma_defensa + r
            cont_defensa = cont_defensa + 1

promedio_defensa = suma_defensa/cont_defensa




## Menu flujo principal ##

acciones = defaultdict(def_value)
acciones["1"] = "orden segun"
acciones["2"] = "estadisticas"
acciones["3"] = "encontrar tipo"
acciones["4"] = "revisar"
acciones["0"] = "salir"

continuar = True
while continuar:
    
    print('''
¿Que desea hacer?
1.- Ordenar segun criterio
2.- Obtener estadísticas
3.- Saber el tipo de un pokemon
4.- Revisar Estructuras
0.- Salir
    ''')

    accion = input()
    accion = acciones[accion]

    if accion == "orden segun":
        tipo = input()
        criterio = input()

        orden = orden_segun(tipo, criterio)

        print(f"Ordenando pokemon de tipo {tipo} segun {criterio}:")
        for elem in orden:
            print(f"  - {elem}")

    elif accion == "estadisticas":
        tipo = input()
        criterio = input()

        datos = estadisticas(tipo, criterio)

        print(f"Informacion de {criterio} en pokemon de tipo {tipo}")
        print(f"  - Máximo: {datos['max']}")
        print(f"  - Mínimo: {datos['min']}")
        print(f"  - Promedio: {round(datos['prom'],1)}")

    elif accion == "encontrar tipo":

        nombre = input()

        tipos = tipo_segun_nombre(nombre)
        print(f"El tipo principal de {nombre} es {tipos[0]}")

        if tipos[1] == "":
            print(f"{nombre} no tiene tipo secundario")
        else:
            print(f"El tipo secundario de {nombre} es {tipos[1]}")

    elif accion == "revisar":
        try:
            print("Tipos Encontrados:")
            for tipo in sorted(list(tipos_de_pokemon)):
                print(f"  - {tipo}")

            print("")

            p = pokemon_por_tipo["Electric"]
            print(f"Revisando Primarios: {'25' in p[0]}")
            print(f"Revisando Secundarios: {'170' in p[1]}")

            print("")

            print("Pokemon Ejemplo:")
            i = info_pokemon["25"]
            esta = "Electric" in i
            print(f"  - ID: 25")
            print(f"  - Nombre: {i[0]}")
            print(f"  - Esta Tipo: {esta}")
        except NameError:
            print("Esta parte no se puede ejecutar ya que aún no has definido todas las estructuras")
            

    elif accion == "salir":
        continuar = False

    else:
        print(accion)