class Mangas :
    
    def __init__(self, Nombre, Autor, Lanzamiento):
        self.Nombre = Nombre
        self.Autor = Autor
        self.Lanzamiento = Lanzamiento
        print('se ha publicado el manga:', self.Nombre)
        
    def __str__(self):
        return '{}({})'.format(self.Autor, self.Lanzamiento)  
    
class revista :
    
    Mangas = [] 
    
    def __init__(self, mangas=[]):
        revista.mangas = mangas
        
    def agregar(self, m):
        revista.mangas.append(m)  
        
    def mostrar(self):
        for m in revista.mangas:
            print(m)      
            
m = Mangas("one piece", "Eiichiro Oda", 1997)   
r = revista([m])  
r.mostrar()
r.agregar(Mangas("Naruto", "Masashi Kishimoto", 1999)) 
r.mostrar()
r.agregar(Mangas("Bleach", "Tite Kubo", 2001))      