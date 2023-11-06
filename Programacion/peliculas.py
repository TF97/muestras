class Peliculas:
    
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la pelicula:', self.titulo)
        
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento) 
    
class Catalogo:
    
    peliculas = []
    
    def __init__(self, peliculas=[]):
        Catalogo.peliculas = peliculas
    
    def agregar(self, p):
        Catalogo.peliculas.append(p)
    
    def mostrar(self):
        for p in Catalogo.peliculas:
            print(p) 
                          
p = Peliculas("El Padrino", 175, 1972)
c = Catalogo([p])
c.mostrar()
c.agregar(Peliculas("El Padrino: Parte 2", 202, 1974))
c.mostrar()  
c.agregar(Peliculas("Volver al Futuro", 156, 1985))          