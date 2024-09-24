# -*- encoding: utf-8 -*-

import pygame
from pygame.locals import *
import os

from Codigo.Escenas.escena import Escena
from Codigo.Fases.fase_españa import FaseEspaña
from Codigo.Fases.fase_china import FaseChina
from Codigo.Fases.fase_rusia import FaseRusia
from Codigo.Configuracion.constantes import (JUGAR_PRINCIPIO_TEXTO, JUGAR_TEXTO, CONFIGURACION_TEXTO, SALIR_TEXTO, VOLVER_TEXTO, VOLUMEN_TEXTO, MENU_FONDO, MENU_FONDO_CONFIGURACION,
                                             MENU_BOTON_AMARILLO, MUSICA_MENU, MENU_BOTON_SUBIR_VOLUMEN, MENU_BOTON_BAJAR_VOLUMEN, MENU_BOTON_AZUL_CLARO, MENU_BOTON_ROJO, MENU_BOTON_VERDE, MENU_BOTON_AZUL, ANCHO_PANTALLA, ALTO_PANTALLA)
from Codigo.Menus.menu import Boton, PantallaGUI, TextoGUI


class BotonNuevaPartida(Boton):
    def __init__(self, pantalla):
        Boton.__init__(self, pantalla, MENU_BOTON_AMARILLO,
                       (ANCHO_PANTALLA/2 - 150/2, ALTO_PANTALLA/4*3-50), (150, 35))

    def accion(self):
        self.pantalla.menu.ejecutarNuevaPartida()


class BotonJugar(Boton):
    def __init__(self, pantalla):
        Boton.__init__(self, pantalla, MENU_BOTON_VERDE,
                       (ANCHO_PANTALLA/2 - 150/2, ALTO_PANTALLA/4*3), (150, 35))

    def accion(self):
        self.pantalla.menu.ejecutarJuego()


class BotonConfiguracion(Boton):
    def __init__(self, pantalla):
        Boton.__init__(self, pantalla, MENU_BOTON_AZUL,
                       (ANCHO_PANTALLA/2 - 150/2, ALTO_PANTALLA/4*3 + 50), (150, 35))

    def accion(self):
        self.pantalla.menu.mostrarPantallaConfiguracion()


class BotonSalir(Boton):
    def __init__(self, pantalla):
        Boton.__init__(self, pantalla, MENU_BOTON_ROJO,
                       (ANCHO_PANTALLA/2 - 150/2, ALTO_PANTALLA/4*3 + 100), (150, 35))

    def accion(self):
        self.pantalla.menu.salirPrograma()


class BotonVolver(Boton):
    def __init__(self, pantalla):
        Boton.__init__(self, pantalla, MENU_BOTON_AZUL_CLARO,
                       (ANCHO_PANTALLA/2 - 150/2, ALTO_PANTALLA/4*3 + 100), (150, 35))

    def accion(self):
        self.pantalla.menu.mostrarPantallaInicial()


class BotonSubirVolumen(Boton):
    def __init__(self, pantalla):
        Boton.__init__(self, pantalla, MENU_BOTON_SUBIR_VOLUMEN,
                       (ANCHO_PANTALLA/2 + 100, ALTO_PANTALLA/4 + 100), (100, 100))

    def accion(self):
        self.pantalla.menu.subirVolumen()


class BotonBajarVolumen(Boton):
    def __init__(self, pantalla):
        Boton.__init__(self, pantalla, MENU_BOTON_BAJAR_VOLUMEN,
                       (ANCHO_PANTALLA/2 - 200, ALTO_PANTALLA/4 + 100), (100, 100))

    def accion(self):
        self.pantalla.menu.bajarVolumen()

# ---------------------------------------------------------------------------------------


class TextoJugar(TextoGUI):
    def __init__(self, pantalla):
        fuente = pygame.font.SysFont('impact', 16)
        TextoGUI.__init__(self, pantalla, fuente,
                          (255, 255, 255), JUGAR_TEXTO, (ANCHO_PANTALLA/2 - 150/2 + 38, ALTO_PANTALLA/4*3 - 8))

    def accion(self):
        self.pantalla.menu.ejecutarJuego()


class TextoNuevaPartida(TextoGUI):
    def __init__(self, pantalla):
        fuente = pygame.font.SysFont('impact', 16)
        TextoGUI.__init__(self, pantalla, fuente,
                          (255, 255, 255), JUGAR_PRINCIPIO_TEXTO, (ANCHO_PANTALLA/2 - 150/2 + 38, ALTO_PANTALLA/4*3 - 58))

    def accion(self):
        self.pantalla.menu.ejecutarNuevaPartida()


class TextoConfiguracion(TextoGUI):
    def __init__(self, pantalla):
        fuente = pygame.font.SysFont('impact', 16)
        TextoGUI.__init__(self, pantalla, fuente,
                          (255, 255, 255), CONFIGURACION_TEXTO, (ANCHO_PANTALLA/2 - 150/2 + 38, ALTO_PANTALLA/4*3 + 42))

    def accion(self):
        self.pantalla.menu.mostrarPantallaConfiguracion()


class TextoSalir(TextoGUI):
    def __init__(self, pantalla):
        fuente = pygame.font.SysFont('impact', 16)
        TextoGUI.__init__(self, pantalla, fuente,
                          (255, 255, 255), SALIR_TEXTO, (ANCHO_PANTALLA/2 - 150/2 + 38, ALTO_PANTALLA/4*3 + 92))

    def accion(self):
        self.pantalla.menu.salirPrograma()


class TextoVolver(TextoGUI):
    def __init__(self, pantalla):
        fuente = pygame.font.SysFont('impact', 16)
        TextoGUI.__init__(self, pantalla, fuente,
                          (255, 255, 255), VOLVER_TEXTO, (ANCHO_PANTALLA/2 - 150/2 + 38, ALTO_PANTALLA/4*3 + 92))

    def accion(self):
        self.pantalla.menu.mostrarPantallaInicial()


class TextoVolumen(TextoGUI):
    def __init__(self, pantalla):
        fuente = pygame.font.SysFont('impact', 30)
        TextoGUI.__init__(self, pantalla, fuente,
                          (255, 255, 255), VOLUMEN_TEXTO, (ANCHO_PANTALLA/2 - 60, ALTO_PANTALLA/4 + 65))

    def accion(self):
        ()
# ---------------------------------------------------------------------------------------


class PantallaInicialGUI(PantallaGUI):
    def __init__(self, menu):
        PantallaGUI.__init__(
            self, menu, MENU_FONDO)

        # Creamos los botones y los metemos en la lista
        botonNuevaPartida = BotonNuevaPartida(self)
        botonJugar = BotonJugar(self)
        botonConfiguracion = BotonConfiguracion(self)
        botonSalir = BotonSalir(self)
        self.elementosGUI.append(botonNuevaPartida)
        self.elementosGUI.append(botonJugar)
        self.elementosGUI.append(botonConfiguracion)
        self.elementosGUI.append(botonSalir)
        # Creamos el texto y lo metemos en la lista
        textoNuevaPartida = TextoNuevaPartida(self)
        textoJugar = TextoJugar(self)
        textoConfiguracion = TextoConfiguracion(self)
        textoSalir = TextoSalir(self)
        self.elementosGUI.append(textoNuevaPartida)
        self.elementosGUI.append(textoJugar)
        self.elementosGUI.append(textoConfiguracion)
        self.elementosGUI.append(textoSalir)


class PantallaConfiguracionGUI(PantallaGUI):
    def __init__(self, menu):
        PantallaGUI.__init__(
            self, menu, MENU_FONDO_CONFIGURACION)
        # Creamos los botones y los metemos en la lista
        botonVolver = BotonVolver(self)
        botonSubirVolumen = BotonSubirVolumen(self)
        botonBajarVolumen = BotonBajarVolumen(self)
        self.elementosGUI.append(botonVolver)
        self.elementosGUI.append(botonSubirVolumen)
        self.elementosGUI.append(botonBajarVolumen)

        # Creamos el texto y lo metemos en la lista
        textoVolver = TextoVolver(self)
        textoVolumen = TextoVolumen(self)
        self.elementosGUI.append(textoVolver)
        self.elementosGUI.append(textoVolumen)

# ---------------------------------------------------------------------------------------
# Clase Menu, la escena en sí


class Menu(Escena):

    def __init__(self, director):
        # Llamamos al constructor de la clase padre
        Escena.__init__(self, director)

        pygame.mixer.init()
        self.musica = pygame.mixer.music.load(MUSICA_MENU)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

        # Creamos la lista de pantallas
        self.listaPantallas = []
        # Creamos las pantallas que vamos a tener
        #   y las metemos en la lista
        self.listaPantallas.append(PantallaInicialGUI(self))
        self.listaPantallas.append(PantallaConfiguracionGUI(self))
        # En que pantalla estamos actualmente
        self.mostrarPantallaInicial()

    def update(self, *args):
        return

    def eventos(self, lista_eventos):
        # Se mira si se quiere salir de esta escena
        for evento in lista_eventos:
            # Si se quiere salir, se le indica al director
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    self.salirPrograma()
            elif evento.type == pygame.QUIT:
                self.director.salirPrograma()

        # Se pasa la lista de eventos a la pantalla actual
        self.listaPantallas[self.pantallaActual].eventos(lista_eventos)

    def dibujar(self, pantalla):
        self.listaPantallas[self.pantallaActual].dibujar(pantalla)

    # --------------------------------------
    # Metodos propios del menu

    def salirPrograma(self):
        self.director.salirPrograma()

    def ejecutarNuevaPartida(self):
        # Reseteamos los checkpoints
        self.director.españa = False
        self.director.rusia = False
        # Cargamos el primer nivel
        fase = FaseEspaña(self.director)
        self.director.apilarEscena(fase)

    def ejecutarJuego(self):
        # Comprobamos que checkpoints están activados y cargamos el nivel correspondiente
        if self.director.españa and not self.director.rusia:
            fase = FaseRusia(self.director)
        elif self.director.españa and self.director.rusia:
            fase = FaseChina(self.director)
        else:
            fase = FaseEspaña(self.director)
        self.director.apilarEscena(fase)

    def mostrarPantallaInicial(self):
        self.pantallaActual = 0

    def mostrarPantallaConfiguracion(self):
        self.pantallaActual = 1

    def subirVolumen(self):
        self.director.volumen += 0.05
        pygame.mixer.music.set_volume(self.director.volumen)

    def bajarVolumen(self):
        self.director.volumen -= 0.05
        pygame.mixer.music.set_volume(self.director.volumen)
