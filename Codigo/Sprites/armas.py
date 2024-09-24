
import pygame

from Codigo.Sprites.sprites import MiSprite
from Codigo.gestorRecursos import GestorRecursos
from Codigo.Configuracion.constantes import (RETARDO_SALAMI, VELOCIDAD_SALAMI, HOJA_MOVIMIENTOS_SALAMI,
                                             COORDENADAS_SALAMI, QUIETO_E, DERECHA_ARMA, IZQUIERDA_ARMA, IZQUIERDA, DERECHA,
                                             ANCHO_PANTALLA, ALTO_PANTALLA, HOJA_MOVIMIENTOS_JERINGUILLA, COORDENADAS_JERINGUILLA,
                                             VELOCIDAD_JERINGUILLA, RETARDO_JERINGUILLA, HOJA_MOVIMIENTOS_BOTELLA, COORDENADAS_BOTELLA,
                                             VELOCIDAD_BOTELLA, RETARDO_BOTELLA, HOJA_MOVIMIENTOS_ESPADA, COORDENADAS_ESPADA,
                                             VELOCIDAD_ESPADA, RETARDO_ESPADA)

# -------------------------------------------------
# Clase Arma


class Proyectil(MiSprite):
    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, velocidadArma, retardoAnimacion, jugador):

        # Primero invocamos al constructor de la clase padre
        MiSprite.__init__(self)

        # Se carga la hoja
        self.hoja = GestorRecursos.CargarImagen(archivoImagen, -1)
        self.hoja = self.hoja.convert_alpha()
        # El movimiento que esta realizando
        self.movimiento = 0
        # Lado hacia el que esta mirando
        self.mirando = jugador.mirando
        # Leemos las coordenadas de un archivo de texto
        datos = GestorRecursos.CargarArchivoCoordenadas(archivoCoordenadas)
        datos = datos.split()
        # Postura inicial
        self.numPostura = 0
        # Número de la postura inicial
        self.numImagenPostura = 0

        cont = 0
        self.coordenadasHoja = []
        for linea in range(0, 1):
            self.coordenadasHoja.append([])
            tmp = self.coordenadasHoja[linea]
            for postura in range(1, numImagenes[linea]+1):
                tmp.append(pygame.Rect((int(datos[cont]), int(
                    datos[cont+1])), (int(datos[cont+2]), int(datos[cont+3]))))
                cont += 4

        # El retardo a la hora de cambiar la imagen del Sprite (para que no se mueva demasiado rápido)
        self.retardoMovimiento = 0

        # En que postura esta inicialmente
        self.numPostura = QUIETO_E

        # El rectangulo del Sprite
        self.rect = pygame.Rect(100, 100, self.coordenadasHoja[self.numPostura][self.numImagenPostura]
                                [2], self.coordenadasHoja[self.numPostura][self.numImagenPostura][3])

        # Las velocidades de caminar y salto
        self.velocidadArma = velocidadArma - jugador.velocidad[0]

        # El retardo en la animacion del personaje
        self.retardoAnimacion = retardoAnimacion

        # Y actualizamos la postura del Sprite inicial, llamando al metodo correspondiente
        self.actualizarPostura()

    # Metodo base para realizar el movimiento: simplemente se le indica cual va a hacer, y lo almacena

    def mover(self, movimiento):
        self.movimiento = movimiento

    def actualizarPostura(self):
        self.retardoMovimiento -= 1
        # Miramos si ha pasado el retardo para dibujar una nueva postura
        if (self.retardoMovimiento < 0):
            self.retardoMovimiento = self.retardoAnimacion
            # Si ha pasado, actualizamos la postura
            self.numImagenPostura += 1
            if self.numImagenPostura >= len(self.coordenadasHoja[self.numPostura]):
                self.numImagenPostura = 1
            if self.numImagenPostura < 0:
                self.numImagenPostura = len(
                    self.coordenadasHoja[self.numPostura])-1
            self.image = self.hoja.subsurface(
                self.coordenadasHoja[self.numPostura][self.numImagenPostura])

            # Si esta mirando a la DERECHA, cogemos la porcion de la hoja
            if self.mirando == DERECHA_ARMA:
                self.image = self.hoja.subsurface(
                    self.coordenadasHoja[self.numPostura][self.numImagenPostura])
            #  Si no, si mira a la IZQUIERDA, invertimos esa imagen
            elif self.mirando == IZQUIERDA_ARMA:
                self.image = pygame.transform.flip(self.hoja.subsurface(
                    self.coordenadasHoja[self.numPostura][self.numImagenPostura]), 1, 0)

    def update(self, grupoPlataformas, tiempo, volumen):

        # Las velocidades a las que iba hasta este momento
        (velocidadx, velocidady) = self.velocidad

        # Si vamos a la izquierda, le ponemos velocidad en esa dirección
        if self.mirando == IZQUIERDA:
            velocidadx = -self.velocidadArma
        # Si vamos a la derecha, le ponemos velocidad en esa dirección
        else:
            velocidadx = self.velocidadArma

        # Actualizamos la imagen a mostrar
        self.actualizarPostura()

        # Aplicamos la velocidad en cada eje
        self.velocidad = (velocidadx, velocidady)

        # Y llamamos al método de la superclase para que, según la velocidad y el tiempo
        #  calcule la nueva posición del Sprite
        MiSprite.update(self, tiempo)

        # Devolverá True o False según esté en la pantalla
        if self.rect.left > 0 and self.rect.right < ANCHO_PANTALLA and self.rect.bottom > 0 and self.rect.top < ALTO_PANTALLA:
            return False
        else:
            return True


class Salami(Proyectil):
    def __init__(self, jugador):
        Proyectil.__init__(self, HOJA_MOVIMIENTOS_SALAMI,
                           COORDENADAS_SALAMI, [8], VELOCIDAD_SALAMI, RETARDO_SALAMI, jugador)


class Jeringuilla(Proyectil):
    def __init__(self, jugador):
        Proyectil.__init__(self, HOJA_MOVIMIENTOS_JERINGUILLA,
                           COORDENADAS_JERINGUILLA, [5], VELOCIDAD_JERINGUILLA, RETARDO_JERINGUILLA, jugador)


class Botella(Proyectil):
    def __init__(self, jugador):
        Proyectil.__init__(self, HOJA_MOVIMIENTOS_BOTELLA,
                           COORDENADAS_BOTELLA, [5], VELOCIDAD_BOTELLA, RETARDO_BOTELLA, jugador)


class Espada(Proyectil):
    def __init__(self, jugador):
        Proyectil.__init__(self, HOJA_MOVIMIENTOS_ESPADA,
                           COORDENADAS_ESPADA, [5], VELOCIDAD_ESPADA, RETARDO_ESPADA, jugador)
