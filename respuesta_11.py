

archivo = open("pokemon.csv",encoding="UTF-8")
next(archivo)
lineas = archivo.readlines()



#['Grass', 'Rock', 'Fire', 'Electric', 'Water', 'Normal', 'Dark', 'Bug', 'Poison', 'Dragon', 'Ground', 'Fighting', 'Fairy', 'Ghost']
tipos_de_pokemon = []

#imprime lo mismo que tipos_de_pokemon, pero no filtra por unico.
descripcion_pokemon = []



for linea in lineas: 
    linea = linea.rstrip("\n")
    columna = linea.split(",")
    tipos_pokemon = columna[2]
    tipos_pokemon_auxiliar = tipos_pokemon.split(";")
    descripcion_pokemon.append(tipos_pokemon_auxiliar[0])
    
    
# elimina elementos repetidos de la lista   
for elemento in descripcion_pokemon:
      if elemento not in tipos_de_pokemon:
          tipos_de_pokemon.append(elemento)

print(descripcion_pokemon) 


