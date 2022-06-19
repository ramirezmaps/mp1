class Perro:
    def __init__(self,n,e,s):
        self.nombre = n
        self.edad = e
        self.sexo = s
        self.juguete = []

    def agrgar_juguete(self, juguete):
        self.juguete.append(juguete)