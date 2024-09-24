# -------------------------------------------------
# Clase PlataformaSuelo


from Codigo.Sprites.sprites import MiSprite
from Codigo.gestorRecursos import GestorRecursos
from Codigo.Configuracion.constantes import SPRITE_VALLA, SPRITE_PUERTA, PLATAFORMA_ESPAÑA, PLATAFORMA_RUSIA, PLATAFORMA_CHINA

import pygame


class PlataformaSuelo(MiSprite):
    def __init__(self, rectangulo):
        # Primero invocamos al constructor de la clase padre
        MiSprite.__init__(self)
        # Rectangulo con las coordenadas en pantalla que ocupara
        self.rect = rectangulo
        # Y lo situamos de forma global en esas coordenadas
        self.establecerPosicion((self.rect.left, self.rect.bottom))
        # En el caso particular de esta plataforma no se va a ver
        self.image = pygame.Surface((0, 0))


class PlataformaFinal(MiSprite):
    def __init__(self):
        # Primero invocamos al constructor de la clase padre
        MiSprite.__init__(self)
        # Rectangulo con las coordenadas en pantalla que ocupara
        self.rect = pygame.Rect(550, 0, 60, 550)
        # Y lo situamos de forma global en esas coordenadas
        self.establecerPosicion((self.rect.left, self.rect.bottom))
        self.image = GestorRecursos.CargarImagen(SPRITE_VALLA)
        self.image = pygame.transform.scale(
            self.image, (60, 550))


class Salida(MiSprite):
    def __init__(self):
        # Primero invocamos al constructor de la clase padre
        MiSprite.__init__(self)
        # Rectangulo con las coordenadas en pantalla que ocupara
        self.rect = pygame.Rect(2700, 465, 100, 200)
        # Y lo situamos de forma global en esas coordenadas
        self.establecerPosicion((self.rect.left, self.rect.bottom))
        self.image = GestorRecursos.CargarImagen(
            SPRITE_PUERTA)


class PlataformaValla(MiSprite):
    def __init__(self, fondo):
        # Primero invocamos al constructor de la clase padre
        MiSprite.__init__(self)
        # Rectangulo con las coordenadas en pantalla que ocupara
        self.rect = pygame.Rect(self.posicion[0], self.posicion[1], 234, 500)
        # Y lo situamos de forma global en esas coordenadas
        self.establecerPosicion((self.rect.left, self.rect.top))
        self.image = GestorRecursos.CargarImagen(
            fondo, colorkey=pygame.Color(255, 255, 255))


class PlataformaHorizontal(MiSprite):
    def __init__(self, fondo):
        # Primero invocamos al constructor de la clase padre
        MiSprite.__init__(self)
        # Rectangulo con las coordenadas en pantalla que ocupara
        self.rect = pygame.Rect(self.posicion[0], self.posicion[1], 150, 50)
        # Y lo situamos de forma global en esas coordenadas
        self.establecerPosicion((self.rect.left, self.rect.bottom))
        self.image = GestorRecursos.CargarImagen(
            fondo)
