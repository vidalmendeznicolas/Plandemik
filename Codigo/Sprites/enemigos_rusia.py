import pygame

from Codigo.Sprites.personaje import Personaje
from Codigo.Configuracion.constantes import (HOJA_MOVIMIENTOS_PUTIN, COORDENADAS_PUTIN, HOJA_MOVIMIENTOS_ENEMIGOS_RUSIA, COORDENADAS_ENEMIGOS_RUSIA, QUIETO_E,
                                             IZQUIERDA, DERECHA, SPRITE_QUIETO_E, SPRITE_ANDANDO_E, ANCHO_PANTALLA, ALTO_PANTALLA, VELOCIDAD_RUSIA, VELOCIDAD_SALTO_ESTANDAR, RETARDO_ANIMACION_ESTANDAR)
from Codigo.Sprites.enemigos import NoJugador, NoJugadorBoss
from Codigo.Sprites.armas import Botella

# -------------------------------------------------
# Clase Ruso


class Ruso(NoJugador):
    "El enemigo 'Ruso'"

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        NoJugador.__init__(self, HOJA_MOVIMIENTOS_ENEMIGOS_RUSIA, COORDENADAS_ENEMIGOS_RUSIA,
                           [4, 6, 15], VELOCIDAD_RUSIA, VELOCIDAD_SALTO_ESTANDAR, RETARDO_ANIMACION_ESTANDAR)

# -------------------------------------------------
# Clase Putin


class Putin(NoJugadorBoss):
    "El enemigo 'Putin'"

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        NoJugadorBoss.__init__(self, HOJA_MOVIMIENTOS_PUTIN, COORDENADAS_PUTIN,
                               [5, 2], 10)
        # Siempre mira a la izquierda
        NoJugadorBoss.mirando = IZQUIERDA

    # Se crea la instancia de su proyectil y lo lanza
    def atacar(self, jugador):
        arma = Botella(jugador)
        arma.establecerPosicion(
            (jugador.posicion[0], jugador.posicion[1]+20))
        return arma

    # Si está en la pantalla ataca, si no, está quieto
    def mover_cpu(self, jugador):
        if self.rect.left > 0 and self.rect.right < ANCHO_PANTALLA and self.rect.bottom > 0 and self.rect.top < ALTO_PANTALLA:
            self.atacar(jugador)
        else:
            NoJugadorBoss.mover(self, QUIETO_E)
