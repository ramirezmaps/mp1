

class Auto:
    def __init__(self, ma, mo, a, c, k):
        self.marca  = ma
        self.modelo = mo
        self.año = a
        self.color = c
        self.__kilometraje = k

        ## valores por defecto
        self.__ubicacion = (-33,45, -70,63)
        self.dueño = None

    ## metodo especial : __str__

    def __str__(self):
        ## no imprime en pantalla
        ## retorna un STRING
        return f"Auto de {self.dueño}, año {self.año}, {self.__kilometraje} kms"
    
    ## metodo para conducir
    def conducir(self, kms):
        self.__kilometraje += kms
        self.__modificar_ubicacion(kms/20 , kms/30)

    ## metodo vender
    def vender(self, nuevo_dueño):
        self.dueño = nuevo_dueño
    
    ## MEtodo Getter para el atributo oculto __kiloometraje
    def leer_odometro(self):
        return self.__kilometraje

    ## metodo oculto
    def __modificar_ubicacion(self, dlat, dlong):
        print("calculando nueva ubicacion")
        self.__ubicacion = (self.__ubicacion[0] + dlat, self.__ubicacion[1]+dl



    


