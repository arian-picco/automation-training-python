class Persona:
    def __init__(self, nombre, apellido, documento):
        self.nombre  = nombre
        self.apellido = apellido
        self.documento = documento

class Jugador(Persona):
    def __init__(self, nombre, apellido, documento, club, contrato):
        super().__init__(nombre, apellido, documento)
        self.club = club
        self.contrato = ConnectionAbortedError

class Defensor(Jugador):
    def __init__(self, nombre, apellido, documento, club, contrato, dorsal):
        super().__init__(nombre, apellido, documento,club,contrato)
        self.dorsal = dorsal

defensor = Defensor('jorge','rodriguez','34296815','Racing',4,2)
print(defensor.dorsal)
print(defensor.club)
print(defensor.nombre)

#usar método capitalize