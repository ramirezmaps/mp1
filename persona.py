
class Persona:
    def __init__(self, n,a,id,edad ):
        self.nombre = n
        self.apellido = a
        self._rut = id
        self.edad = edad

    def __str__(self) -> str:
        return f"soy {self.nombre} {self.apellido} y tengo {self.edad}"

    def cumpleaños(self):
        self.edad = self.edad +1

    def deme_su_rut(self):
        return self._rut
        
if __name__ == "__main__":
    c = Persona("Ignacio", "Ramirez", "14195154-6", 35)
    d = Persona("Karim", "Muñoz", "15843045-k", 29)

    print(c)
    print(d)

    c.cumpleaños()
    d.cumpleaños()

    c.deme_su_rut()
    d.deme_su_rut()

    print(c)
    print(d)

    print(d.deme_su_rut())



    

