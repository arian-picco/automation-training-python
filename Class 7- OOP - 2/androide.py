class Humano:
    def __init(self, nombre, apellido, documento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento

class Maquina:
    def __init__(self, modelo, serie, so):
        self.modelo = modelo
        self.serie = serie
        self.so = so

class Androide(Humano, Maquina):
    def __init__(self, nombre, apellido, documento, modelo, serie, so, conversion):
        Humano.__init__(self, nombre, apellido, documento)
        Maquina.__init__(self, modelo, serie, so)
        self.conversion = conversion

