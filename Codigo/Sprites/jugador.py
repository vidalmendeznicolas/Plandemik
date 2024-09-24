
import pygame

from Codigo.Sprites.personaje import Personaje
from Codigo.gestorRecursos import GestorRecursos
from Codigo.Configuracion.constantes import GOLPE, COORDENADAS_PERSONAJE, HOJA_MOVIMIENTOS_PERSONAJE, ARRIBA, IZQUIERDA, DERECHA, ATAQUE, QUIETO, VELOCIDAD_JUGADOR, VELOCIDAD_SALTO_JUGADOR, RETARDO_ANIMACION_JUGADOR


# -------------------------------------------------
# Clase Jugador

class Jugador(Personaje):
    "Cualquier personaje del juego"

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Personaje.__init__(self, HOJA_MOVIMIENTOS_PERSONAJE, COORDENADAS_PERSONAJE,
                           [5, 6, 3, 3, 6, 3, 6], VELOCIDAD_JUGADOR, VELOCIDAD_SALTO_JUGADOR, RETARDO_ANIMACION_JUGADOR)

    def mover(self, teclasPulsadas, arriba, abajo, izquierda, derecha, ataque, quieto=False):

        # Forzar movimiento a estar quieto si está en una animación o en un diálogo
        if quieto:
            Personaje.mover(self, QUIETO)
            return

        # Indicamos la acción a realizar segun la tecla pulsada para el jugador
        if teclasPulsadas[arriba]:
            Personaje.mover(self, ARRIBA)
        elif teclasPulsadas[izquierda]:
            Personaje.mover(self, IZQUIERDA)
        elif teclasPulsadas[derecha]:
            Personaje.mover(self, DERECHA)
        elif teclasPulsadas[ataque]:
            Personaje.mover(self, ATAQUE)
        else:
            Personaje.mover(self, QUIETO)
