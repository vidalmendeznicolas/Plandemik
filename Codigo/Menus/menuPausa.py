# -*- encoding: utf-8 -*-

import pygame
from pygame.locals import *

from Codigo.Configuracion.constantes import (MENU_PAUSA_FONDO, VOLUMEN_TEXTO, VOLVER_TEXTO, MENU_PRINCIPAL_TEXTO, MENU_BOTON_BAJAR_VOLUMEN,
                                             MENU_BOTON_SUBIR_VOLUMEN, MENU_BOTON_AZUL_CLARO, MENU_BOTON_ROJO, ANCHO_PANTALLA, ALTO_PANTALLA, MUSICA_MENU)
from Codigo.Menus.menu import Boton, TextoGUI, PantallaGUI
from Codigo.Escenas.escena import Escena


class BotonMenuPrincipal(Boton):
    def __init__(self, pantalla):
        Boton.__init__(self, pantalla, MENU_BOTON_ROJO,
                       (ANCHO_PANTALLA/2 - 150/2, ALTO_PANTALLA/4*3 + 50), (150, 35))

    def accion(self):
        self.pantalla.menu.salirMenuPrincipal()
# -------------------------------------------------


class BotonVolver(Boton):
    def __init__(self, pantalla):
        Boton.__init__(self, pantalla, MENU_BOTON_AZUL_CLARO,
                       (ANCHO_PANTALLA/2 - 150/2, ALTO_PANTALLA/4*3 + 100), (150, 35))

    def accion(self):
        self.pantalla.menu.salirPantallaPausa()
# -------------------------------------------------


class BotonSubirVolumen(Boton):
    def __init__(self, pantalla):
        Boton.__init__(self, pantalla, MENU_BOTON_SUBIR_VOLUMEN,
                       (ANCHO_PANTALLA/2 + 100, ALTO_PANTALLA/4 + 100), (100, 100))

    def accion(self):
        self.pantalla.menu.subirVolumen()

# -------------------------------------------------


class BotonBajarVolumen(Boton):
    def __init__(self, pantalla):
        Boton.__init__(self, pantalla, MENU_BOTON_BAJAR_VOLUMEN,
                       (ANCHO_PANTALLA/2 - 200, ALTO_PANTALLA/4 + 100), (100, 100))

    def accion(self):
        self.pantalla.menu.bajarVolumen()

# -------------------------------------------------


class TextoMenuPrincipal(TextoGUI):
    def __init__(self, pantalla):
        fuente = pygame.font.SysFont('impact', 16)
        TextoGUI.__init__(self, pantalla, fuente,
                          (255, 255, 255), MENU_PRINCIPAL_TEXTO, (ANCHO_PANTALLA/2 - 150/2 + 38, ALTO_PANTALLA/4*3 + 40))

    def accion(self):
        self.pantalla.menu.salirMenuPrincipal()
# -------------------------------------------------


class TextoVolver(TextoGUI):
    def __init__(self, pantalla):
        fuente = pygame.font.SysFont('impact', 16)
        TextoGUI.__init__(self, pantalla, fuente,
                          (255, 255, 255), VOLVER_TEXTO, (ANCHO_PANTALLA/2 - 150/2 + 38, ALTO_PANTALLA/4*3 + 92))

    def accion(self):
        self.pantalla.menu.salirPantallaPausa()
# -------------------------------------------------


class TextoVolumen(TextoGUI):
    def __init__(self, pantalla):
        fuente = pygame.font.SysFont('impact', 30)
        TextoGUI.__init__(self, pantalla, fuente,
                          (255, 255, 255), VOLUMEN_TEXTO, (ANCHO_PANTALLA/2 - 60, ALTO_PANTALLA/4 + 65))

    def accion(self):
        ()
# -------------------------------------------------


class PantallaPausa(PantallaGUI):
    def __init__(self, menu):
        PantallaGUI.__init__(
            self, menu, MENU_PAUSA_FONDO)
        # Creamos los botones y el texto y los metemos en la lista
        botonMenuPrincipal = BotonMenuPrincipal(self)
        botonVolver = BotonVolver(self)
        botonSubirVolumen = BotonSubirVolumen(self)
        botonBajarVolumen = BotonBajarVolumen(self)
        textoVolver = TextoVolver(self)
        textoVolumen = TextoVolumen(self)
        textoMenuPrincipal = TextoMenuPrincipal(self)
        self.elementosGUI.append(botonVolver)
        self.elementosGUI.append(botonMenuPrincipal)
        self.elementosGUI.append(botonSubirVolumen)
        self.elementosGUI.append(botonBajarVolumen)
        self.elementosGUI.append(textoMenuPrincipal)
        self.elementosGUI.append(textoVolver)
        self.elementosGUI.append(textoVolumen)

# -------------------------------------------------
# Clase MenuPausa


class MenuPausa(Escena):

    def __init__(self, director):
        # Llamamos al constructor de la clase padre
        Escena.__init__(self, director)
        # Creamos la lista de pantallas
        self.listaPantallas = []
        # Creamos las pantallas que vamos a tener
        #   y las metemos en la lista
        self.listaPantallas.append(PantallaPausa(self))
        # En que pantalla estamos actualmente
        self.mostrarPantallaPausa()

    def update(self, *args):
        return

    def eventos(self, lista_eventos):
        # Se mira si se quiere salir de esta escena
        for evento in lista_eventos:
            # Si se quiere salir, se le indica al director
            if evento.type == pygame.QUIT:
                self.director.salirPrograma()

        # Se pasa la lista de eventos a la pantalla actual
        self.listaPantallas[self.pantallaActual].eventos(lista_eventos)

    def dibujar(self, pantalla):
        # Dibujamos la pantalla en la que nos encontremos
        self.listaPantallas[self.pantallaActual].dibujar(pantalla)

    # --------------------------------------
    # Metodos propios del menu

    def mostrarPantallaPausa(self):
        self.pantallaActual = 0

    def salirPantallaPausa(self):
        self.director.pausa = not self.director.pausa

    def salirMenuPrincipal(self):
        # Se carga la música del menú principal
        pygame.mixer.music.load(MUSICA_MENU)
        pygame.mixer.music.play(-1)
        # Se despausa el juego
        self.director.pausa = not self.director.pausa
        self.director.salirEscena()

    def subirVolumen(self):
        self.director.volumen += 0.05
        pygame.mixer.music.set_volume(self.director.volumen)

    def bajarVolumen(self):
        self.director.volumen -= 0.05
        pygame.mixer.music.set_volume(self.director.volumen)
