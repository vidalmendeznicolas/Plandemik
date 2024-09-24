import pygame
import time
from Codigo.gestorRecursos import GestorRecursos

from Codigo.Sprites.sprites import MiSprite
from Codigo.Configuracion.constantes import (GOLPE, SONIDO_VIDA, SONIDO_GOLPE, SONIDO_ATACAR, SPRITE_GOLPEADO, SONIDO_SALTAR, QUIETO, SONIDO_VOLO,
                                             DERECHA, ARRIBA, SPRITE_SALTANDO, IZQUIERDA, SPRITE_ANDANDO, ATAQUE, SPRITE_ATACANDO, SPRITE_QUIETO, GRAVEDAD)


# -------------------------------------------------
# Clases Personaje

# class Personaje(pygame.sprite.Sprite):


class Personaje(MiSprite):
    "Cualquier personaje del juego"

    # Parametros pasados al constructor de esta clase:
    #  Archivo con la hoja de Sprites
    #  Archivo con las coordenadoas dentro de la hoja
    #  Numero de imagenes en cada postura
    #  Velocidad de caminar y de salto
    #  Retardo para mostrar la animacion del personaje
    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, velocidadCarrera, velocidadSalto, retardoAnimacion):

        # Primero invocamos al constructor de la clase padre
        MiSprite.__init__(self)

        # Establecemos la vidas que va a tener el personaje
        self.vidas = 5
        self.count = 33

        # Tiempo del último toque
        self.ultimo_toque = 0

        # Variables para cambiar el color cuando lo golpean
        self.value = 0
        self.newColor = [0, 0, 0, 0]

        # Se carga la hoja
        self.hoja = GestorRecursos.CargarImagen(archivoImagen, -1)
        self.hoja = self.hoja.convert_alpha()
        # El movimiento que esta realizando
        self.movimiento = QUIETO
        # Lado hacia el que esta mirando
        self.mirando = DERECHA
        # Leemos las coordenadas de un archivo de texto
        datos = GestorRecursos.CargarArchivoCoordenadas(archivoCoordenadas)
        datos = datos.split()
        self.numPostura = 5
        self.numImagenPostura = 0
        cont = 0
        self.coordenadasHoja = []
        for linea in range(0, 7):
            self.coordenadasHoja.append([])
            tmp = self.coordenadasHoja[linea]
            for postura in range(1, numImagenes[linea]+1):
                tmp.append(pygame.Rect((int(datos[cont]), int(
                    datos[cont+1])), (int(datos[cont+2]), int(datos[cont+3]))))
                cont += 4

        # El retardo a la hora de cambiar la imagen del Sprite (para que no se mueva demasiado rápido)
        self.retardoMovimiento = 0

        # En que postura esta inicialmente
        self.numPostura = QUIETO

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
        if movimiento == ARRIBA:
            # Si estamos en el aire y el personaje quiere saltar, ignoramos este movimiento
            if self.numPostura == SPRITE_SALTANDO:
                self.movimiento = QUIETO
            else:
                self.movimiento = ARRIBA
        else:
            self.movimiento = movimiento

    def actualizarPostura(self):
        self.retardoMovimiento -= 1
        # Miramos si ha pasado el retardo para dibujar una nueva postura
        if (self.retardoMovimiento < 0):
            self.retardoMovimiento = self.retardoAnimacion
            # Si ha pasado, actualizamos la postura
            self.numImagenPostura += 1
            if self.numImagenPostura >= len(self.coordenadasHoja[self.numPostura]):
                self.numImagenPostura = 0
            if self.numImagenPostura < 0:
                self.numImagenPostura = len(
                    self.coordenadasHoja[self.numPostura])-1
            self.imagen = self.hoja.subsurface(
                self.coordenadasHoja[self.numPostura][self.numImagenPostura])

            # Si esta mirando a la DERECHA, cogemos la porcion de la hoja
            if self.mirando == DERECHA:
                self.imagen = self.hoja.subsurface(
                    self.coordenadasHoja[self.numPostura][self.numImagenPostura])
            #  Si no, si mira a la IZQUIERDA, invertimos esa imagen
            elif self.mirando == IZQUIERDA:
                self.imagen = pygame.transform.flip(self.hoja.subsurface(
                    self.coordenadasHoja[self.numPostura][self.numImagenPostura]), 1, 0)

    def update(self, gruposPlataformas, tiempo, volumen):

        # Descomponemos la tupla de plataformas
        (grupoPlataformas, grupoPlataformasVerticales) = gruposPlataformas

        # Cargamos los sonidos
        sonidoSalto = pygame.mixer.Sound(
            SONIDO_SALTAR)
        sonidoSalto.set_volume(volumen)
        sonidoAtaque = pygame.mixer.Sound(
            SONIDO_ATACAR)
        sonidoAtaque.set_volume(volumen)

        # Las velocidades a las que iba hasta este momento
        (velocidadx, velocidady) = self.velocidad

        # Se hace una copia de la imagen original
        self.image = self.imagen.copy()

        # Se cambia la imagen si está siendo golpeado
        if (pygame.time.get_ticks() - self.ultimo_toque < 2000) and (pygame.time.get_ticks() > 2000):
            self.value += 50
            self.newColor[0] = self.value % 255
            self.image.fill(self.newColor[0:3] + [0, ],
                            None, pygame.BLEND_RGBA_ADD)

        # Si vamos a la izquierda o a la derecha
        if (self.movimiento == IZQUIERDA) or (self.movimiento == DERECHA):
            # Esta mirando hacia ese lado
            self.mirando = self.movimiento

            # Si chocamos con una plataforma por la izquierda o la derecha no poder avanzar
            plataforma = pygame.sprite.spritecollideany(
                self, grupoPlataformasVerticales)

            # Si vamos a la izquierda, le ponemos velocidad en esa dirección
            if self.movimiento == IZQUIERDA:
                velocidadx = -self.velocidadCarrera
            # Si vamos a la derecha, le ponemos velocidad en esa dirección
            else:
                # Si hay una plataforma no podemos avanzar
                if(plataforma != None) and (plataforma.rect.left <= self.rect.right):
                    self.establecerPosicion(
                        (plataforma.posicion[0] - self.rect.width - 1, self.posicion[1]))
                    velocidadx = 0
                else:
                    velocidadx = self.velocidadCarrera

            # Si no estamos en el aire
            if self.numPostura != SPRITE_SALTANDO:
                # La postura actual sera estar caminando
                self.numPostura = SPRITE_ANDANDO
                # Ademas, si no estamos encima de ninguna plataforma, caeremos
                if pygame.sprite.spritecollideany(self, grupoPlataformas) == None:
                    self.numPostura = SPRITE_SALTANDO

        elif self.movimiento == ATAQUE:
            # Si queremos atacar
            if self.numPostura != SPRITE_SALTANDO:
                # La postura actual sera estar atacando
                self.numPostura = SPRITE_ATACANDO
                if not pygame.mixer.get_busy():
                    # Reproducimos sonido de ataque
                    sonidoAtaque.play()

        # Si queremos saltar
        elif self.movimiento == ARRIBA:
            # Reproducimos sonido de salto
            sonidoSalto.play()
            # La postura actual sera estar saltando
            self.numPostura = SPRITE_SALTANDO
            # Le imprimimos una velocidad en el eje y
            velocidady = -self.velocidadSalto

        # Si no se ha pulsado ninguna tecla
        elif self.movimiento == QUIETO:
            # Si no estamos saltando, la postura actual será estar quieto
            if not self.numPostura == SPRITE_SALTANDO:
                self.numPostura = SPRITE_QUIETO
            velocidadx = 0

        # Además, si estamos en el aire
        if self.numPostura == SPRITE_SALTANDO:

            # Miramos a ver si hay que parar de caer: si hemos llegado a una plataforma
            #  Para ello, miramos si hay colision con alguna plataforma del grupo
            plataforma = pygame.sprite.spritecollideany(
                self, grupoPlataformas)
            #  Ademas, esa colision solo nos interesa cuando estamos cayendo
            #  y solo es efectiva cuando caemos encima, no de lado, es decir,
            #  cuando nuestra posicion inferior esta por encima de la parte de abajo de la plataforma
            if (plataforma != None) and (velocidady > 0) and (plataforma.rect.bottom > self.rect.bottom):
                # Lo situamos con la parte de abajo un pixel colisionando con la plataforma
                #  para poder detectar cuando se cae de ella
                self.establecerPosicion(
                    (self.posicion[0], plataforma.posicion[1]-plataforma.rect.height+1))
                # Lo ponemos como quieto
                self.numPostura = SPRITE_QUIETO
                # Y estará quieto en el eje y
                velocidady = 0
            # Si nuestra posición superior está por debajo de la parte de arriba de la plataforma chocar contra ellas
            elif (plataforma != None) and (velocidady < 0) and (plataforma.rect.top < self.rect.top):
                velocidady = 0
            # Si no caemos en una plataforma, aplicamos el efecto de la gravedad
            else:
                velocidady += GRAVEDAD * tiempo

        # Actualizamos la imagen a mostrar
        self.actualizarPostura()

        # Aplicamos la velocidad en cada eje
        self.velocidad = (velocidadx, velocidady)

        # Y llamamos al método de la superclase para que, según la velocidad y el tiempo
        #  calcule la nueva posición del Sprite
        MiSprite.update(self, tiempo)

        return

    # Método que devuelve las vidas
    def getVidas(self):
        return self.vidas

    # Método para establecer las vidas
    def setVidas(self, vidas, volumen):
        # Cargamos los sonidos y establecemos el volumen
        sonidoGolpe = pygame.mixer.Sound(
            SONIDO_GOLPE)
        sonidoGolpe.set_volume(volumen)
        sonidoVolo = pygame.mixer.Sound(
            SONIDO_VOLO)
        sonidoVolo.set_volume(volumen)

        # Si tiene vida se hace un cálcula para saber si tiene cooldown de daño o no
        # Si lo tiene no bajamos la vida y avanzamos en un contador
        # Si no lo tiene quitamos una vida y reproducimos sonido de daño
        # Tenemos un contador auxiliar para el cooldown en caso de daño permanente
        if self.vidas > 0:
            tiempo = pygame.time.get_ticks() - self.ultimo_toque
            if tiempo < 2000 and self.count >= 30:
                self.count = 0
                self.vidas -= 1
                sonidoGolpe.play()
                self.hit_countdown = 6
                self.ultimo_toque = pygame.time.get_ticks()
            elif tiempo < 2000 and self.count < 30:
                self.count += 1
                False
            elif tiempo >= 2000:
                self.count = 0
                self.vidas -= 1
                sonidoGolpe.play()
                self.hit_countdown = 6
                self.ultimo_toque = pygame.time.get_ticks()
        else:
            # Si no tiene vidas paramos la música y reproducimos el sonido correspondiente
            pygame.mixer.music.stop()
            sonidoVolo.play()
            time.sleep(4)
            pygame.mixer.music.play(-1)

    # Si el personaje recoge un Power Up sube una vida
    def setVidasPowerUp(self, vidas, volumen):
        sonidoVida = pygame.mixer.Sound(SONIDO_VIDA)
        sonidoVida.set_volume(volumen)

        if self.vidas != 5:
            self.count = 0
            self.vidas += 1
        sonidoVida.play()
