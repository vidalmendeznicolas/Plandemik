
from Codigo.gestorRecursos import GestorRecursos
from Codigo.Configuracion.constantes import (
    ALTO_PANTALLA, ANCHO_PANTALLA, SPRITE_SKY_ESPAÑA,
    SPRITE_FONDO_ESPAÑA, SPRITE_SKY_RUSIA, SPRITE_FONDO_RUSIA,
    SPRITE_SKY_CHINA, SPRITE_FONDO_CHINA)

import pygame

# -------------------------------------------------
# Clase CieloEspaña


class CieloEspaña:
    def __init__(self):
        self.fondo = GestorRecursos.CargarImagen(SPRITE_SKY_ESPAÑA)
        self.fondo = pygame.transform.scale(
            self.fondo, (1500, ALTO_PANTALLA))

        self.rect = self.fondo.get_rect()
        self.rect.bottom = ALTO_PANTALLA

        self.rectSubimagen = pygame.Rect(0, 0, ANCHO_PANTALLA, ALTO_PANTALLA)
        # El scroll horizontal empieza en la posicion 0 por defecto
        self.rectSubimagen.left = 0

    def update(self, scrollx):
        self.rectSubimagen.left = scrollx/5

    def dibujar(self, pantalla):
        pantalla.blit(self.fondo, self.rect, self.rectSubimagen)


# -------------------------------------------------
# Clase DecoradoEspaña

class DecoradoEspaña:
    def __init__(self):
        self.imagen = GestorRecursos.CargarImagen(
            SPRITE_FONDO_ESPAÑA, -1)
        self.imagen = pygame.transform.scale(self.imagen, (3200, 240))

        self.rect = self.imagen.get_rect()
        self.rect.bottom = ALTO_PANTALLA

        # La subimagen que estamos viendo
        self.rectSubimagen = pygame.Rect(0, 0, ANCHO_PANTALLA, ALTO_PANTALLA)
        # El scroll horizontal empieza en la posicion 0 por defecto
        self.rectSubimagen.left = 0

    def update(self, scrollx):
        self.rectSubimagen.left = scrollx

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect, self.rectSubimagen)

# -------------------------------------------------
# Clase CieloRusia


class CieloRusia:
    def __init__(self):
        self.fondo = GestorRecursos.CargarImagen(SPRITE_SKY_RUSIA)
        self.fondo = pygame.transform.scale(
            self.fondo, (1500, ALTO_PANTALLA))

        self.rect = self.fondo.get_rect()
        self.rect.bottom = ALTO_PANTALLA

        self.rectSubimagen = pygame.Rect(0, 0, ANCHO_PANTALLA, ALTO_PANTALLA)
        # El scroll horizontal empieza en la posicion 0 por defecto
        self.rectSubimagen.left = 0

    def update(self, scrollx):
        self.rectSubimagen.left = scrollx/5

    def dibujar(self, pantalla):
        pantalla.blit(self.fondo, self.rect, self.rectSubimagen)

# -------------------------------------------------
# Clase DecoradoRusia


class DecoradoRusia:
    def __init__(self):
        self.imagen = GestorRecursos.CargarImagen(
            SPRITE_FONDO_RUSIA, -1)
        self.imagen = pygame.transform.scale(self.imagen, (3200, 240))

        self.rect = self.imagen.get_rect()
        self.rect.bottom = ALTO_PANTALLA

        # La subimagen que estamos viendo
        self.rectSubimagen = pygame.Rect(0, 0, ANCHO_PANTALLA, ALTO_PANTALLA)
        # El scroll horizontal empieza en la posicion 0 por defecto
        self.rectSubimagen.left = 0

    def update(self, scrollx):
        self.rectSubimagen.left = scrollx

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect, self.rectSubimagen)


# -------------------------------------------------
# Clase CieloChina


class CieloChina:
    def __init__(self):
        self.fondo = GestorRecursos.CargarImagen(SPRITE_SKY_CHINA)
        self.fondo = pygame.transform.scale(
            self.fondo, (1500, ALTO_PANTALLA))

        self.rect = self.fondo.get_rect()
        self.rect.bottom = ALTO_PANTALLA

        self.rectSubimagen = pygame.Rect(0, 0, ANCHO_PANTALLA, ALTO_PANTALLA)
        # El scroll horizontal empieza en la posicion 0 por defecto
        self.rectSubimagen.left = 0

    def update(self, scrollx):
        self.rectSubimagen.left = scrollx/5

    def dibujar(self, pantalla):
        # Y ponemos el sol
        pantalla.blit(self.fondo, self.rect, self.rectSubimagen)


# -------------------------------------------------
# Clase DecoradoChina

class DecoradoChina:
    def __init__(self):
        self.imagen = GestorRecursos.CargarImagen(
            SPRITE_FONDO_CHINA, -1)
        self.imagen = pygame.transform.scale(self.imagen, (3200, 240))

        self.rect = self.imagen.get_rect()
        self.rect.bottom = ALTO_PANTALLA

        # La subimagen que estamos viendo
        self.rectSubimagen = pygame.Rect(0, 0, ANCHO_PANTALLA, ALTO_PANTALLA)
        # El scroll horizontal empieza en la posicion 0 por defecto
        self.rectSubimagen.left = 0

    def update(self, scrollx):
        self.rectSubimagen.left = scrollx

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect, self.rectSubimagen)
