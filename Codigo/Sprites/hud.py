from Codigo.gestorRecursos import GestorRecursos
from Codigo.Configuracion.constantes import HUD_VIDA, HUD_VIDA_VACIA

import pygame


class HUD:
    def __init__(self):
        # Se carga la imagen
        self.imagen_vida_vacia = GestorRecursos.CargarImagen(
            HUD_VIDA_VACIA)
        self.imagenes_vida = []
        # Se carga la imagen de los trozos de vida
        for index in range(5):
            self.imagenes_vida.append(
                GestorRecursos.CargarImagen(HUD_VIDA))
        self.rect = pygame.Rect(20, 20, 100, 20)

    def dibujar(self, pantalla, vida_actual):
        pantalla.blit(self.imagen_vida_vacia, self.rect)
        # Llenamos la barra en función de la vida actual
        for i in range(vida_actual):
            pantalla.blit(self.imagenes_vida[i], pygame.Rect(
                20 + i * 20, 20, 20, 20))
