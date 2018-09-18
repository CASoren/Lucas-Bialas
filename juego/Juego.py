#coding: utf-8

import pilasengine

pilas = pilasengine.iniciar()

Fondo = pilas.fondos.Tarde()
# Fondo.imagen = "./Imagenes/Laboratorioo.jpg"
# Fondo.escala = 0.5

def iniciar_juego():
    pilas.escenas.Normal()
    pilas.fondos.Espacio()

# Palos
    palo = pilas.actores.Palo()
    palo2 = pilas.actores.Palo()
    palo2.x = -311
    palo2.y = 170
    palo.escala = 0.5
    palo2.escala = 0.5
    palo.x = -207
    palo.y = 170

# Barra: aceituna
    aceituna = pilas.actores.Aceituna()
    aceituna.escala = 0.5
    aceituna.x = -207
    aceituna.y = 170

# Textos
    saludo = pilas.actores.Texto("Bienvenido al juego!!")
    saludo.x = 0
    saludo.y = 0
    saludo.escala = [1,0.9] * 20
    saludo.rotacion = [20,0,-20,0] * 5

# Cajones

# Potasio
    caja_de_potasio = pilas.actores.Actor()  # Cajon de potasio
    caja_de_potasio.imagen = "./Imagenes/cajones/Cajondepotasio.png"
    caja_de_potasio.escala = 0.4
    caja_de_potasio.x = -203
    caja_de_potasio.y = -175
    rectangulo = pilas.fisica.Rectangulo(0, 0, 132, 130, True, False)
    caja_de_potasio.figura_de_colision = rectangulo
    # cuadrado = pilas.fisica.Rectangulo(64,-46)

    # Berkelio
    caja_de_berkelio = pilas.actores.Actor()  # Cajon de potasio
    caja_de_berkelio.imagen = "./Imagenes/cajones/Cajondeberkelio.png"
    caja_de_berkelio.escala = 0.4
    caja_de_berkelio.x = -67
    caja_de_berkelio.y = -175
    rectangulo = pilas.fisica.Rectangulo(0, 0, 132, 130, True, False)
    caja_de_berkelio.figura_de_colision = rectangulo

# Cromo
    caja_de_cromo = pilas.actores.Actor()  # Cajon de potasio
    caja_de_cromo.imagen = "./Imagenes/cajones/Cajondecromo.png"
    caja_de_cromo.escala = 0.4
    caja_de_cromo.x = 69
    caja_de_cromo.y = -175
    rectangulo = pilas.fisica.Rectangulo(0, 0, 132, 130, True, False)
    caja_de_cromo.figura_de_colision = rectangulo

    # Cadmio
    caja_de_cadmio = pilas.actores.Actor() # Cajon de potasio
    caja_de_cadmio.imagen = "./Imagenes/cajones/Cajondecadmio.png"
    caja_de_cadmio.escala = 0.4
    caja_de_cadmio.x = 206
    caja_de_cadmio.y = -175

    rectangulo = pilas.fisica.Rectangulo(0, 0, 132, 130, True, False)
    caja_de_cadmio.figura_de_colision = rectangulo

    potasio = pilas.actores.Actor()
    potasio.imagen = "./Imagenes/K.png"
    potasio.decir("arrastrame hacia el nombre de mi nomenclatura!")

    # Potasio aprende
    potasio.aprender("arrastrable")
    potasio.aprender("AumentarConRueda")
    potasio.aprender("MoverseConElTeclado")
    potasio.aprender("LimitadoABordesDePantalla")

    # Propiedades de potasio
    potasio.escala = [0.3,0.35] * 30
    potasio.x = 0
    potasio.y = 100
    rectangulo = pilas.fisica.Rectangulo(0, 0, 46, 46, True, False)
    potasio.figura_de_colision = rectangulo

    def cuando_colisiona(caja_de_potasio, potasio):
        potasio.eliminar()
        pilas.colisiones.agregar(caja_de_potasio, potasio, cuando_colsiona)

def salir_juego():
    iniciar_juego()

menu = pilas.actores.Menu([
        ('iniciar juego', iniciar_juego),
        ('salir', salir_juego),
    ])

pilas.ejecutar()
