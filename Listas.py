database = {
    "protagonistas": [
        {"id": 1,"nombre": "Superman","edad": "desconocida","descripcion": "Superhéroe kryptoniano con habilidades sobrehumanas."},
        {"id": 2,"nombre": "Spider-Man","edad": 17,"descripcion": "Superhéroe con habilidades arácnidas y un gran sentido de la responsabilidad."},
        {"id": 3,"nombre": "Wonder Woman","edad": 3500,"descripcion": "Princesa amazona con habilidades sobrehumanas y un lazo de la verdad mágico."},
        {"id": 4,"nombre": "Batman","edad": "desconocida","descripcion": "Vigilante multimillonario con habilidades de combate y tecnología avanzada."},
        {"id": 5,"nombre": "Iron Man","edad": 53,"descripcion": "Vigilante multimillonario con armadura tecnológica avanzada."}
    ],
    "autores": [
        {"nombre": "Stan Lee","estilo de dibujo": "estilo clásico","protagonistas": [1, 2, 4, 5]},
        {"nombre": "Jim Lee","estilo de dibujo": "estilo detallado","protagonistas": [1, 3]},
        {"nombre": "Brian Michael Bendis","estilo de dibujo": "estilo realista","protagonistas": [2]}
    ],
    "comics": [
        {"nombre": "Action Comics #1","id_protagonista": 1,"numero_paginas": 64,"portada_rustica": False,"rating": 8.5},
        {"nombre": "The Amazing Spider-Man #1","id_protagonista": 2,"numero_paginas": 25,"portada_rustica": True,"rating": 9.0},
        {"nombre": "Wonder Woman #1","id_protagonista": 3,"numero_paginas": 44,"portada_rustica": False,"rating": 7.5},
        {"nombre": "Batman: Year One","id_protagonista": 4,"numero_paginas": 96,"portada_rustica": True,"rating": 8.0}
    ],
    "series": [
        {"titulo": "Smallville","prom_caps": 23,"numero_temporadas": 10,"duracion": 45,"id_protagonista": 1,"generos": ["Acción", "Drama", "Ciencia ficción"],"rating": 8.8},
        {"titulo": "Spider-Man: The Animated Series","prom_caps": 14,"numero_temporadas": 5,"duracion": 22,"id_protagonista": 2,"generos": ["Acción", "Aventura"],"rating": 9.2},
        {"titulo": "Gotham","prom_caps": 22,"numero_temporadas": 5,"duracion": 43,"id_protagonista": 4,"generos": ["Crimen", "Drama", "Thriller"],"rating": 8.4}
    ],
    "peliculas": [
        {"titulo": "Spider-Man: No Way Home","co_prod": "Sony","formato_lanzamiento": "Cine","duracion": 148,"id_protagonista": 2,"generos": ["Acción", "Aventura", "Ciencia ficción"],"rating": 9.5},
        {"titulo": "Wonder Woman 1984","co_prod": "WanerBross","formato_lanzamiento": "Cine","duracion": 151,"id_protagonista": 3,"generos": ["Acción", "Aventura"],"rating": 8.0},
        {"titulo": "The Dark Knight","co_prod": "WanerBross","formato_lanzamiento": "Cine","duracion": 152,"id_protagonista": 4,"generos": ["Acción", "Crimen", "Drama"],"rating": 9.3},
        {"titulo": "Iron Man","co_prod": "Marvel Studios","formato_lanzamiento": "Cine","duracion": 126,"id_protagonista": 5,"generos": ["Acción", "Aventura", "Ciencia ficción"],"rating": 8.7},
        {"titulo": "Iron Man 3","co_prod": "Marvel Studios","formato_lanzamiento": "Cine","duracion": 130,"id_protagonista": 5,"generos": ["Acción", "Aventura", "Ciencia ficción","Comedia"],"rating": 7.1},
        {"titulo": "Injustice","co_prod": "WanerBross","formato_lanzamiento": "Streaming","duracion": 78,"id_protagonista": 1,"generos": ["Acción", "Drama", "Fantasía", "Gore"],"rating": 6.4}
    ]
}
