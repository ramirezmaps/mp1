from turtle import clear


a = ['Bulbasaur']
b = tuple(['Grass;Poison'])
c= tuple(b)
diccionario = {}

diccionario = dict(zip(a,c))
print(b)

for v in diccionario.values():
    print(type(v))
  

print(diccionario)