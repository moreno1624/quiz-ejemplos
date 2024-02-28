from Listas import database
x=database
protago_list=[]
auto_list=[]
comi_list=[]
serie_list=[]
peli_list=[]
class Persona():
   def __init__(self,id,nombre):
    self.id=id
    self.nombre=nombre 

class Protagonistas(Persona):
    def __init__(self, id, nombre,edad,descripcion):
         super().__init__(id, nombre)
         self.edad=edad
         self.descripcion=descripcion
    def show(self):
        return f"""nombre: {self.nombre},
    edad: {self.edad}
    descripcion: {self.descripcion}"""

class Autores():
    def __init__(self,nombre,estilo,protagonistas):
        self.nombre=nombre
        self.estilo=estilo
        self.protagonistas=protagonistas 
    def show(self):
        return f"""nombre: {self.nombre},
    edad: {self.estilo}
    descripcion: {self.protagonistas}"""

class Comic():
    def __init__(self,nombre,id_protagonista,numero_paginas,portada_rustica,rating):
        self.nombre=nombre
        self.id_protagonista=id_protagonista
        self.numero_paginas=numero_paginas 
        self.portada_rustica=portada_rustica
        self.rating=rating
        
    def show(self):
        return f"""nombre: {self.nombre},
    protagonista: {self.id_protagonista}
    paginas: {self.numero_paginas}
    protada: {self.portada_rustica}
    rating: {self.rating}"""
    
class seriies():
    def __init__(self,titulo,prom_caps,numero_temporadas,duracion,id_protagonista,generos,rating):
     self.titulo=titulo
     self.prom_caps=prom_caps
     self.numero_temporadas=numero_temporadas 
     self.duracion=duracion
     self.id_protagonista=id_protagonista
     self.generos=generos
     self.rating=rating
     
    def show(self):
     return f"""nombre: {self.titulo},
protagonista: {self.prom_caps}
paginas: {self.numero_temporadas}
protada: {self.duracion}
rating: {self.id_protagonista}
rating: {self.generos}
rating: {self.rating}"""
    
class Peliculas():
        def __init__(self,titulo,co_prod,formato_lanzamiento,duracion,id_protagonista,generos,rating):
         self.titulo=titulo
         self.co_prod=co_prod
         self.formato_lanzamiento=formato_lanzamiento 
         self.duracion=duracion
         self.id_protagonista=id_protagonista
         self.generos=generos
         self.rating=rating
         
        def show(self):
         return f"""nombre: {self.titulo},
    protagonista: {self.co_prod}
    paginas: {self.formato_lanzamiento}
    protada: {self.duracion}
    rating: {self.id_protagonista}
    rating: {self.generos}
    rating: {self.rating}"""        
    
    
    
    
    
    
def enlistar(x):     
 for i,j  in x.items():
     
     if i == "protagonistas":
         print("1")
         for k in range(0,len(j)):
             protago_list.append(Protagonistas(j[k]["id"],j[k]["nombre"],j[k]["edad"],j[k]["descripcion"] ))
             
            
             
     if i == "autores":
         print("2")
         for k in range(0,len(j)):
             auto_list.append(Autores(j[k]["nombre"],j[k]["estilo de dibujo"],j[k]["protagonistas"] ))
             
         
         
     if i == "comics":
         print("3")
         for k in range(0,len(j)):
             comi_list.append(Comic(j[k]["nombre"],j[k]["id_protagonista"],j[k]["numero_paginas"],j[k]["portada_rustica"],j[k]["rating"] ))
             
        
        
     if i == "series":
         print("4")
         for k in range(0,len(j)):
             serie_list.append(seriies(j[k]["titulo"],j[k]["prom_caps"],j[k]["numero_temporadas"],j[k]["duracion"],j[k]["id_protagonista"],j[k]["generos"] ,j[k]["rating"]  ))
            
         
         
     if i == "peliculas":
         print("5")
         for k in range(0,len(j)):
             peli_list.append(Peliculas(j[k]["titulo"],j[k]["co_prod"],j[k]["formato_lanzamiento"],j[k]["duracion"],j[k]["id_protagonista"],j[k]["generos"] ,j[k]["rating"]  ))
             
def bucle(comi_list,i):  
 for k in range(0,len(comi_list)):
                if protago_list[i].id==comi_list[k].id_protagonista:
                    if len(comi_list)==4:
                      print(comi_list[k].nombre)                      
                    else:
                        print(comi_list[k].titulo)
                          
whilo=True        
enlistar(x)
def main():
 while whilo==True:
   print("""
   1)ver nombres
   2)ver apariciones
   3)añadir un comic
   4)modificar generos""")
   print("="*35)
   accion=input("elija una opcion: ") 
   print("="*35)
   if accion=="1":
       for i in range(0,len(protago_list)):
           print(protago_list[i].show())
           
           for q in range(0, len(auto_list)):
               for k in auto_list[q].protagonistas:
                if k==protago_list[i].id:
                    print(auto_list[q].show()) 
           print("="*35)        
   elif accion=="2":
       for i in range(0,len(protago_list)):
           print(protago_list[i].nombre)
           bucle(comi_list,i)
           bucle(serie_list,i)
           bucle(peli_list,i)
           print("="*35)         
   elif accion=="3":
        pass
   elif accion=="4": 
        pass
   else:
       print("elija un valor valido")
       continue
main()
"""for k in range(0,len(comi_list)):
               if protago_list[i].id==comi_list[k].id_protagonista:
                   print(comi_list[k].nombre)
                   print("="*35)   
               bucle(comi_list,i)"""