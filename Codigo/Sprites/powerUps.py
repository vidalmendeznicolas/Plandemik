

from Codigo.Sprites.sprites import MiSprite
import pygame
from Codigo.gestorRecursos import GestorRecursos
from Codigo.Configuracion.constantes import POWER_CARROT


class PowerUp(MiSprite):
    def __init__(self):
        # Primero invocamos al constructor de la clase padre
        MiSprite.__init__(self)
        # Rectangulo con las coordenadas en pantalla que ocupara
        self.rect = pygame.Rect(self.posicion[0], self.posicion[1], 30, 30)
        # Y lo situamos de forma global en esas coordenadas
        self.establecerPosicion((self.rect.left, self.rect.bottom))
        # Cargamos la imagen
        self.image = GestorRecursos.CargarImagen(
            POWER_CARROT, colorkey=pygame.Color(0, 0, 0))
