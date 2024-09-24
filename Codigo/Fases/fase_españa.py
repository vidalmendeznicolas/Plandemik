# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import time

from Codigo.Configuracion.constantes import (POSICION_POWER_UP_ESPAÑA, PLATAFORMA_SUELO, POSICION_JUGADOR, MUSICA_ESPAÑA, POSICION_LIMON,
                                             SPRITE_VALLA, POSICION_PLATAFORMA_HORIZONTAL_ESPAÑA_1, POSICION_PLATAFORMA_HORIZONTAL_ESPAÑA_2,
                                             POSICION_PLATAFORMA_HORIZONTAL_ESPAÑA_3, POSICION_PLATAFORMA_HORIZONTAL_ESPAÑA_4, MUSICA_MENU,
                                             PLATAFORMA_ESPAÑA, POSICION_PLATAFORMA_VERTICAL_ESPAÑA_1, POSICION_ENEMIGO_1,
                                             POSICION_ENEMIGO_2, POSICION_ENEMIGO_3, POSICION_ENEMIGO_4)
from Codigo.Fases.fase_rusia import FaseRusia
from Codigo.Sprites.armas import Jeringuilla
from Codigo.Sprites.enemigos_españa import Limon, Español
from Codigo.Sprites.estatico import Trump
from Codigo.Dialogos.dialogo import DialogoTrumpEspaña
from Codigo.Sprites.powerUps import PowerUp
from Codigo.Sprites.plataformas import PlataformaHorizontal, PlataformaSuelo, PlataformaValla, Salida
from Codigo.Sprites.decorado import DecoradoEspaña, CieloEspaña
from Codigo.Fases.fase import Fase

# -------------------------------------------------
# Clase FaseEspaña


class FaseEspaña(Fase):
    def __init__(self, director):

        # Primero invocamos al constructor de la clase padre con los parámetros
        # base de una fase, su música, su decorado y su fondo
        Fase.__init__(self, director, MUSICA_ESPAÑA,
                      DecoradoEspaña(), CieloEspaña())

        # Creamos una instancia del diálogo de la fase
        self.dialogoTrump = DialogoTrumpEspaña()

        # Creamos una estancia del Sprite con el que dialogaremos
        trump = Trump()

        # Lo pones en un grupo específico
        self.grupoEstaticos = pygame.sprite.Group(trump)

        # Ponemos a los jugadores en sus posiciones iniciales
        self.jugador.establecerPosicion(POSICION_JUGADOR)

        # Creamos las plataformas del decorado
        # La plataforma que conforma todo el suelo
        plataformaSuelo = PlataformaSuelo(pygame.Rect(PLATAFORMA_SUELO))

        # Plataforma en la que saltar para subirse
        plataformaHorizontal1 = PlataformaHorizontal(PLATAFORMA_ESPAÑA)
        plataformaHorizontal1.establecerPosicion(
            POSICION_PLATAFORMA_HORIZONTAL_ESPAÑA_1)
        plataformaHorizontal2 = PlataformaHorizontal(PLATAFORMA_ESPAÑA)
        plataformaHorizontal2.establecerPosicion(
            POSICION_PLATAFORMA_HORIZONTAL_ESPAÑA_2)
        plataformaHorizontal3 = PlataformaHorizontal(PLATAFORMA_ESPAÑA)
        plataformaHorizontal3.establecerPosicion(
            POSICION_PLATAFORMA_HORIZONTAL_ESPAÑA_3)
        plataformaHorizontal4 = PlataformaHorizontal(PLATAFORMA_ESPAÑA)
        plataformaHorizontal4.establecerPosicion(
            POSICION_PLATAFORMA_HORIZONTAL_ESPAÑA_4)

        # Muro para no poder avanzar
        self.plataformaVertical1 = PlataformaValla(SPRITE_VALLA)
        self.plataformaVertical1.establecerPosicion(
            POSICION_PLATAFORMA_VERTICAL_ESPAÑA_1)

        # y el grupo con las mismas
        self.grupoPlataformas = pygame.sprite.Group(
            plataformaSuelo, plataformaHorizontal1, plataformaHorizontal2, plataformaHorizontal3, plataformaHorizontal4)
        self.grupoPlataformasVerticales = pygame.sprite.Group(
            self.plataformaVertical1)

        # Power Ups
        fruta = PowerUp()
        fruta.establecerPosicion(POSICION_POWER_UP_ESPAÑA)

        # Y los enemigos que tendran en este decorado
        enemigo1 = Español()
        enemigo1.establecerPosicion(POSICION_ENEMIGO_1)

        enemigo2 = Español()
        enemigo2.establecerPosicion(POSICION_ENEMIGO_2)

        enemigo3 = Español()
        enemigo3.establecerPosicion(POSICION_ENEMIGO_3)

        enemigo4 = Español()
        enemigo4.establecerPosicion(POSICION_ENEMIGO_4)

        # Este será el boss del nivel
        self.limon = Limon()
        self.limon.establecerPosicion(POSICION_LIMON)

        # Creamos un grupo con los enemigos
        self.grupoEnemigos = pygame.sprite.Group(
            enemigo1, enemigo2, enemigo3, enemigo4, self.limon)

        # Y otro con los bosses
        self.grupoBosses = pygame.sprite.Group(self.limon)

        # Creamos un grupo para los proyectiles del boss
        self.grupoJeringuillas = pygame.sprite.Group()

        # Grupo de los PowerUps
        self.grupoPowerUps = pygame.sprite.Group(fruta)

        # Creamos un grupo con los Sprites que se mueven
        #  En este caso, los personajes, enemigos y proyectiles
        self.grupoSpritesDinamicos = pygame.sprite.Group(
            self.jugador, enemigo1, enemigo2, enemigo3, enemigo4, self.limon, self.grupoArmaPrincipal, self.grupoJeringuillas)

        # Creamos otro grupo con todos los Sprites
        self.grupoSprites = pygame.sprite.Group(trump, fruta,
                                                self.jugador, enemigo1, enemigo2, enemigo3, enemigo4, self.limon, plataformaSuelo, self.salida, plataformaHorizontal1, plataformaHorizontal2, plataformaHorizontal3, plataformaHorizontal4, self.plataformaVertical1)

    def update(self, tiempo):

        # Se llama al update de la clase padre que hace parte del trabajo básico
        Fase.update(self, tiempo)

        # Si el juego no está en pausa se hace lo siguiente
        if (not self.director.pausa):

            # Para cada boss (en nuestro caso uno), se crea un proyectil que lanzará
            for boss in iter(self.grupoBosses):
                if self.count < 5:
                    self.grupoJeringuillas = pygame.sprite.Group()
                    jeringuilla = Jeringuilla(self.limon)
                    jeringuilla.establecerPosicion(
                        (boss.posicion[0] - self.scrollx, boss.posicion[1]-20))
                    self.grupoJeringuillas.add(jeringuilla)

            # Cada boss terá una dificultad diferente en base al tiempo que pase entre cada proyectil
            if self.count > 60:
                self.count = 0
            self.count += 1

            # Si el proyectil del boss está fuera de los límites de la pantalla se elimina
            for jeringuilla in iter(self.grupoJeringuillas):
                if jeringuilla.update(jeringuilla, tiempo, self.director.volumen):
                    self.grupoJeringuillas = pygame.sprite.Group()

            # Comprobamos si hay colision entre algun jugador, algún enemigo o proyectil
            # Se comprueba la colision entre los grupos
            # Si la hay, indicamos a la clase padre que la ha habido
            if pygame.sprite.groupcollide(self.grupoJugadores, self.grupoEnemigos, False, False) != {} or pygame.sprite.groupcollide(self.grupoJugadores, self.grupoJeringuillas, False, True) != {}:
                self.colisionJugador()

            # Comprobamos si hay colisión entre el jugador y la salida
            # Si la hay pasamos al siguiente nivel o terminamos el juego si es el último nivel
            if pygame.sprite.groupcollide(self.grupoJugadores, self.grupoSalida, False, False) != {} and self.limon.contador_muerto:
                # Esperamos medio segundo
                time.sleep(0.5)
                # Activamos el checkpoint correspondiente
                self.director.españa = True
                # Pasamos a la siguientes fase
                siguienteFase = FaseRusia(self.director)
                self.director.cambiarEscena(siguienteFase)

            # Si los proyectiles del jugador y del boss colisionan se eliminan
            pygame.sprite.groupcollide(
                self.grupoArmaPrincipal, self.grupoJeringuillas, True, True)

            # Si el jefe final está muerto movemos la valla para poder avanzar
            if not (self.limon.contador_muerto == 0):
                self.plataformaVertical1.establecerPosicion(
                    (self.plataformaVertical1.posicion[0], self.plataformaVertical1.posicion[1] + 5))

    def dibujar(self, pantalla):
        # LLamamos a dibujar de la clase padre para que pinte todo y aquí se pintará lo específico del nivel
        Fase.dibujar(self, pantalla)
        # Si el juego no está pausado pintamos el grupo de proyectiles del boss
        if not self.director.pausa:
            self.grupoJeringuillas.draw(pantalla)
