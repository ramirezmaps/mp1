

diccionario = {'Bulbasaur': 'Grass;Poison', 'Leafeon': 'Grass;', 'Kabuto': 'Rock;Water', 'Ivysaur': 'Grass;Poison', 'Venusaur': 'Grass;Poison', 'Charmander': 'Fire;'}
tupla_tipos = []
def tipos(nombre_pokemon):
    for k,v in diccionario.items():
        if k == nombre_pokemon:
            tipos_= v
        return(k, v)



print(type(tipos("Bulbasaur")))