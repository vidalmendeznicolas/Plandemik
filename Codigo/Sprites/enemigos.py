
import pygame
import time
from Codigo.gestorRecursos import GestorRecursos
from Codigo.Sprites.sprites import MiSprite
from Codigo.Configuracion.constantes import MUERTE_E, SPRITE_MUERE_E, QUIETO_E, IZQUIERDA, DERECHA, ATACANDO_B, SPRITE_ATACANDO_B, SPRITE_QUIETO_E, SPRITE_MUERE_B, SPRITE_ANDANDO_E, ANCHO_PANTALLA, ALTO_PANTALLA
from Codigo.Sprites.armas import Salami


class Enemigo(MiSprite):
    "Enemigo"

    # Parametros pasados al constructor de esta clase:
    #  Archivo con la hoja de Sprites
    #  Archivo con las coordenadoas dentro de la hoja
    #  Numero de imagenes en cada postura
    #  Velocidad de caminar y de salto
    #  Retardo para mostrar la animacion del personaje
    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, velocidadCarrera, velocidadSalto, retardoAnimacion):

        # Primero invocamos al constructor de la clase padre
        MiSprite.__init__(self)
        # Variable que se utilizará para controlar el tiempo de la animación de muerto
        self.contador_muerto = 0
        # Se carga la hoja
        self.hoja = GestorRecursos.CargarImagen(archivoImagen, -1)
        self.hoja = self.hoja.convert_alpha()
        # El movimiento que esta realizando
        self.movimiento = QUIETO_E
        # Lado hacia el que esta mirando
        self.mirando = IZQUIERDA
        # Leemos las coordenadas de un archivo de texto
        datos = GestorRecursos.CargarArchivoCoordenadas(archivoCoordenadas)
        datos = datos.split()
        self.numPostura = QUIETO_E
        self.numImagenPostura = 0
        cont = 0
        self.coordenadasHoja = []
        for linea in range(0, 3):
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
        self.velocidadCarrera = velocidadCarrera
        self.velocidadSalto = velocidadSalto

        # El retardo en la animacion del personaje (podria y deberia ser distinto para cada postura)
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
            if self.mirando == DERECHA:
                self.image = self.hoja.subsurface(
                    self.coordenadasHoja[self.numPostura][self.numImagenPostura])
            #  Si no, si mira a la IZQUIERDA, invertimos esa imagen
            elif self.mirando == IZQUIERDA:
                self.image = pygame.transform.flip(self.hoja.subsurface(
                    self.coordenadasHoja[self.numPostura][self.numImagenPostura]), 1, 0)

    # Método para establecer la animación de muerto
    def muriendo(self):
        # Si está muriendo actualizamos la postura y si ya ha pasdo el tiempo correspondiente
        # destruimos el Sprite
        if self.numPostura == SPRITE_MUERE_E:
            self.actualizarPostura()
            if self.contador_muerto > 60:
                self.kill()
        # Si aún no está muriendo cambiamos su postura para que lo esté
        else:
            self.numPostura = SPRITE_MUERE_E
            self.numImagenPostura = 0

        self.velocidad = (0, 0)
        self.contador_muerto += 1

    def update(self, grupoPlataformas, tiempo, volumen):
        if self.contador_muerto == 0:
            # Las velocidades a las que iba hasta este momento
            (velocidadx, velocidady) = self.velocidad

            # Si vamos a la izquierda o a la derecha
            if (self.movimiento == IZQUIERDA) or (self.movimiento == DERECHA):
                # Esta mirando hacia ese lado
                self.mirando = self.movimiento

                # Si vamos a la izquierda, le ponemos velocidad en esa dirección
                if self.movimiento == IZQUIERDA:
                    velocidadx = -self.velocidadCarrera
                # Si vamos a la derecha, le ponemos velocidad en esa dirección
                else:
                    velocidadx = self.velocidadCarrera

                # La postura actual sera estar caminando
                self.numPostura = SPRITE_ANDANDO_E

            # Si no se ha pulsado ninguna tecla
            elif self.movimiento == QUIETO_E:
                self.numPostura = SPRITE_QUIETO_E
                velocidadx = 0

            # Actualizamos la imagen a mostrar
            self.actualizarPostura()

            # Aplicamos la velocidad en cada eje
            self.velocidad = (velocidadx, velocidady)

            # Y llamamos al método de la superclase para que, según la velocidad y el tiempo
            #  calcule la nueva posición del Sprite
            MiSprite.update(self, tiempo)
        return


class EnemigoBoss(MiSprite):
    "EnemigoBoss"

    # Parametros pasados al constructor de esta clase:
    #  Archivo con la hoja de Sprites
    #  Archivo con las coordenadoas dentro de la hoja
    #  Numero de imagenes en cada postura
    #  Velocidad de caminar y de salto
    #  Retardo para mostrar la animacion del personaje
    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, retardoAnimacion):

        # Primero invocamos al constructor de la clase padre
        MiSprite.__init__(self)
        # Variable que se utilizará para controlar el tiempo de la animación de muerto
        self.contador_muerto = 0
        # Se carga la hoja
        self.hoja = GestorRecursos.CargarImagen(archivoImagen, -1)
        self.hoja = self.hoja.convert_alpha()
        # El movimiento que esta realizando
        self.movimiento = ATACANDO_B
        # Lado hacia el que esta mirando
        self.mirando = IZQUIERDA
        # Leemos las coordenadas de un archivo de texto
        datos = GestorRecursos.CargarArchivoCoordenadas(archivoCoordenadas)
        datos = datos.split()
        self.numImagenPostura = 0
        cont = 0
        self.coordenadasHoja = []
        for linea in range(0, 2):
            self.coordenadasHoja.append([])
            tmp = self.coordenadasHoja[linea]
            for postura in range(1, numImagenes[linea]+1):
                tmp.append(pygame.Rect((int(datos[cont]), int(
                    datos[cont+1])), (int(datos[cont+2]), int(datos[cont+3]))))
                cont += 4

        # El retardo a la hora de cambiar la imagen del Sprite (para que no se mueva demasiado rápido)
        self.retardoMovimiento = 0

        # En que postura esta inicialmente
        self.numPostura = SPRITE_ATACANDO_B

        # El rectangulo del Sprite
        self.rect = pygame.Rect(100, 100, self.coordenadasHoja[self.numPostura][self.numImagenPostura]
                                [2], self.coordenadasHoja[self.numPostura][self.numImagenPostura][3])

        # El retardo en la animacion del personaje (podria y deberia ser distinto para cada postura)
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
            if self.mirando == DERECHA:
                self.image = self.hoja.subsurface(
                    self.coordenadasHoja[self.numPostura][self.numImagenPostura])
            #  Si no, si mira a la IZQUIERDA, invertimos esa imagen
            elif self.mirando == IZQUIERDA:
                self.image = pygame.transform.flip(self.hoja.subsurface(
                    self.coordenadasHoja[self.numPostura][self.numImagenPostura]), 1, 0)

    # Método para establecer la animación de muerto
    def muriendo(self):
        # Si está muriendo actualizamos la postura y si ya ha pasdo el tiempo correspondiente
        # destruimos el Sprite
        if self.numPostura == SPRITE_MUERE_B:
            self.actualizarPostura()
            if self.contador_muerto > 60:
                self.kill()
        # Si aún no está muriendo cambiamos su postura para que lo esté
        else:
            self.numPostura = SPRITE_MUERE_B
            self.numImagenPostura = 0

        self.velocidad = (0, 0)
        self.contador_muerto += 1

    def update(self, grupoPlataformas, tiempo, volumen):

        # Actualizamos la imagen a mostrar
        self.actualizarPostura()

        # Y llamamos al método de la superclase para que, según la velocidad y el tiempo
        #  calcule la nueva posición del Sprite
        MiSprite.update(self, tiempo)

        return

# -------------------------------------------------
# Clase NoJugador


class NoJugador(Enemigo):
    "NoJugador"

    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, velocidad, velocidadSalto, retardoAnimacion):
        # Primero invocamos al constructor de la clase padre con los parametros pasados
        Enemigo.__init__(self, archivoImagen, archivoCoordenadas,
                         numImagenes, velocidad, velocidadSalto, retardoAnimacion)

    def mover_cpu(self, jugador):
        # Movemos solo a los enemigos que esten en la pantalla
        if self.rect.left > 0 and self.rect.right < ANCHO_PANTALLA and self.rect.bottom > 0 and self.rect.top < ALTO_PANTALLA:

            # Y nos movemos hacia el jugador
            if jugador.posicion[0] < self.posicion[0]:
                Enemigo.mover(self, IZQUIERDA)
            else:
                Enemigo.mover(self, DERECHA)

        # Si este personaje no esta en pantalla
        elif jugador.movimiento:
            Enemigo.mover(self, QUIETO_E)
        return

# -------------------------------------------------
# Clase NoJugadorBoss


class NoJugadorBoss(EnemigoBoss):
    "NoJugadorBoss"

    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, retardoAnimacion):
        # Primero invocamos al constructor de la clase padre con los parametros pasados
        EnemigoBoss.__init__(self, archivoImagen, archivoCoordenadas,
                             numImagenes, retardoAnimacion)

    def mover_cpu(self, jugador):
        # Este enemigo no hará nada, solo atacar
        return
