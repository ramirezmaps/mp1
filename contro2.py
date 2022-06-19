# class Plato:
#     def __init__(self, nombre, ingredientes):
#         self.nombre = nombre
#         self.ingredientes = ingredientes
    
#     def agregar_ingredientes(self, i):
#         self.ingredientes.append(i)
    
#     def calorias(self):
#         c = 0
#         for i in self.ingredientes:
#             c = c + i[1]
#         return c

# p = Plato("Tallarines con salsa", [("fideos", 131),("Salsa", 29),("Carne", 241)])

# p2 = Plato()







class Plato:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes
    
    def agregar_ingredientes(self, ing, cal):
        self.ingredientes[ing] = cal
    
    def calorias(self):
        c = 0
        for k in self.ingredientes:
            c += self.ingredientes[k]
        return c

p = Plato("Tallarines con salsa", {"fideos": 131,"Salsa": 29,"Carne":241})

print(p.calorias())
