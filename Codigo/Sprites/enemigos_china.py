import pygame

from Codigo.Sprites.personaje import Personaje
from Codigo.Configuracion.constantes import (COORDENADAS_XI, HOJA_MOVIMIENTOS_XI, COORDENADAS_ENEMIGOS_CHINA, HOJA_MOVIMIENTOS_ENEMIGOS_CHINA, QUIETO_E,
                                             IZQUIERDA, DERECHA, SPRITE_QUIETO_E, SPRITE_ANDANDO_E, ANCHO_PANTALLA, ALTO_PANTALLA, VELOCIDAD_CHINA, VELOCIDAD_SALTO_ESTANDAR, RETARDO_ANIMACION_ESTANDAR)
from Codigo.Sprites.enemigos import NoJugador, NoJugadorBoss
from Codigo.Sprites.armas import Espada

# -------------------------------------------------
# Clase Chino


class Chino(NoJugador):
    "El enemigo 'Chino'"

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        NoJugador.__init__(self, HOJA_MOVIMIENTOS_ENEMIGOS_CHINA, COORDENADAS_ENEMIGOS_CHINA,
                           [4, 6, 15], VELOCIDAD_CHINA, VELOCIDAD_SALTO_ESTANDAR, RETARDO_ANIMACION_ESTANDAR)


# -------------------------------------------------
# Clase Xi

class Xi(NoJugadorBoss):
    "El enemigo 'Xi'"

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        NoJugadorBoss.__init__(self, HOJA_MOVIMIENTOS_XI, COORDENADAS_XI,
                               [5, 2], 10)

        # Siempre mira a la izquierda
        NoJugadorBoss.mirando = IZQUIERDA

    # Se crea la instancia de su proyectil y lo lanza
    def atacar(self, jugador):
        arma = Espada(jugador)
        arma.establecerPosicion(
            (jugador.posicion[0], jugador.posicion[1]+20))
        return arma

    def mover_cpu(self, jugador):
        # Si está en la pantalla ataca, si no, está quieto
        if self.rect.left > 0 and self.rect.right < ANCHO_PANTALLA and self.rect.bottom > 0 and self.rect.top < ALTO_PANTALLA:
            self.atacar(jugador)
        else:
            NoJugadorBoss.mover(self, QUIETO_E)
