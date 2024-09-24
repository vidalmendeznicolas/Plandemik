import pygame

from Codigo.Configuracion.constantes import TRUMP
from Codigo.Sprites.sprites import MiSprite
from Codigo.gestorRecursos import GestorRecursos

# -------------------------------------------------
# Clase Estático


class Estatico(MiSprite):
    "Personajes que no se moverán"

    def __init__(self, archivoImagen):
        # Primero invocamos al constructor de la clase padre con los parametros pasados
        MiSprite.__init__(self)

        # Cargamos la imagen
        self.image = GestorRecursos.CargarImagen(archivoImagen, -1)
        self.image = self.image.convert_alpha()


# -------------------------------------------------
# Clase Trump

class Trump(Estatico):

    def __init__(self):
        Estatico.__init__(self, TRUMP)
        # Rectangulo con las coordenadas en pantalla que ocupara
        self.rect = pygame.Rect(250, 420, 100, 100)
        # Y lo situamos de forma global en esas coordenadas
        self.establecerPosicion((self.rect.left, self.rect.bottom))
