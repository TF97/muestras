class Minato():
    
    def __init__(self, sueño, tecnica, jutsu):
        self.sueño = sueño
        self.tecnica = tecnica
        self.jutsu = jutsu
    
    def __str__(self):
        return "Minato: {} - {}".format(self.sueño, self.tecnica, self.jutsu)  
    
class Naruto(Minato):
    
    def __str__(self):
        return "Naruto: {} - {}".format(self.sueño, self.tecnica, self.jutsu)

minato = Minato("Ser Hokage", "Rasengan", "Hiraishin no jutsu" )
print(minato)

naruto = Naruto("ser Hokage", "RasenShuriken", "Kage Bunshin no jutsu" )
print(naruto)

    
        