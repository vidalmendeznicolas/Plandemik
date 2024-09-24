import pygame
from pygame.locals import *

from Codigo.Escenas.escena import Escena
from Codigo.Configuracion.constantes import (
    MINIMO_X_JUGADOR, MAXIMO_X_JUGADOR, ANCHO_PANTALLA, SPRITE_SALTANDO, MUSICA_MENU)
from Codigo.Sprites.armas import Salami
from Codigo.Sprites.hud import HUD
from Codigo.Menus.menuPausa import MenuPausa
from Codigo.Sprites.jugador import Jugador
from Codigo.Sprites.plataformas import Salida


class Fase(Escena):
    def __init__(self, director, musica, decorado, cielo):

        # Primero invocamos al constructor de la clase padre
        Escena.__init__(self, director)

        # Se carga la música del nivel
        pygame.mixer.init()
        self.musica = pygame.mixer.music.load(musica)
        # Se reproduce en bucle
        pygame.mixer.music.play(-1)
        # Se establece el volumen que el usuario a configurado
        pygame.mixer.music.set_volume(director.volumen)

        # Creamos el decorado y el fondo
        self.decorado = decorado
        self.fondo = cielo

        # Variable que controla el pintado del diálogo
        self.dialogo = False
        # Contador para el lanzado de proyectiles del boss final
        self.count = 0

        # Se carga el HUD del jugador (vida)
        self.hud = HUD()

        # Se carga la instancia del menú de pausa
        self.menuPausa = MenuPausa(director)

        # Que parte del decorado estamos visualizando
        #  En ese caso solo hay scroll horizontal
        self.scrollx = 0

        # Creamos el sprite del jugador y lo metemos en un grupo propio
        self.jugador = Jugador()
        self.grupoJugadores = pygame.sprite.Group(self.jugador)

        # La plataforma que corresponde con la salida
        self.salida = Salida()
        self.grupoSalida = pygame.sprite.Group(self.salida)

        # Grupo para el arma del jugador
        self.grupoArmaPrincipal = pygame.sprite.Group()

        # Grupo para los sprites que están muertos
        self.grupoSpritesMuriendo = pygame.sprite.Group()

        # Grupo de los PowerUps
        self.grupoPowerUps = pygame.sprite.Group()

    # Devuelve True o False según se ha tenido que desplazar el scroll
    def actualizarScrollOrdenados(self, jugador):
        # Si el jugador se ha ido por el lado izquierdo
        if (jugador.rect.left < MINIMO_X_JUGADOR):

            # Lo colocamos a la izquierda del todo sin movel el scroll (NO PERMITIMOS RETROCEDER)
            jugador.establecerPosicion(
                (self.scrollx+MINIMO_X_JUGADOR, jugador.posicion[1]))

            return False  # No se ha actualizado el scroll

        # Si el jugador se encuentra más allá del borde derecho
        if (jugador.rect.right > MAXIMO_X_JUGADOR):

            # Se calcula cuantos pixeles esta fuera del borde
            desplazamiento = jugador.rect.right - MAXIMO_X_JUGADOR

            # Si el escenario ya está a la derecha del todo, no lo movemos mas
            if self.scrollx + ANCHO_PANTALLA >= self.decorado.rect.right:
                self.scrollx = self.decorado.rect.right - ANCHO_PANTALLA

                # En su lugar, lo colocamos a la derecha de todo
                jugador.establecerPosicion(
                    (self.scrollx+MAXIMO_X_JUGADOR-jugador.rect.width, jugador.posicion[1]))

                return False  # No se ha actualizado el scroll

            # Si no, es posible que el no se pueda desplazar tantos pixeles a la izquierda
            # por estar muy cerca del borde izquierdo
            elif ((jugador.rect.left-MINIMO_X_JUGADOR) < desplazamiento):

                return False  # No se ha actualizado el scroll

            # Si se puede hacer scroll a la derecha
            else:

                # Calculamos el nivel de scroll actual: el anterior + desplazamiento
                #  (desplazamos a la derecha)
                self.scrollx = self.scrollx + desplazamiento

                return True  # Se ha actualizado el scroll

        # Si el jugador está entre los dos límites de la pantalla, no se hace nada
        return False

    def actualizarScroll(self, jugador):
        # Se ordenan los jugadores según el eje x, y se mira si hay que actualizar el scroll
        cambioScroll = self.actualizarScrollOrdenados(jugador)

        # Si se cambio el scroll, se desplazan todos los Sprites y el decorado
        if cambioScroll:
            # Actualizamos la posición en pantalla de todos los Sprites según el scroll actual
            for sprite in iter(self.grupoSprites):
                sprite.establecerPosicionPantalla((self.scrollx, 0))

            # Ademas, actualizamos el decorado para que se muestre una parte distinta
            self.decorado.update(self.scrollx)

    def update(self, tiempo):

        # Si el juego no está en pausa se actualiza
        if (not self.director.pausa):

            # Se mueven los enemigos según su lógica
            for enemigo in iter(self.grupoEnemigos):
                enemigo.mover_cpu(self.jugador)

            # Si el jugador colisiona con un powerUp recupera vida
            if pygame.sprite.groupcollide(self.grupoJugadores, self.grupoPowerUps, False, True) != {}:
                self.jugador.setVidasPowerUp(
                    self.jugador.getVidas()+1, self.director.volumen)

            # Actualizamos los Sprites dinamicos
            # De esta forma, se simula que cambian todos a la vez
            # Esta operación de update ya comprueba que los movimientos sean correctos
            #  y, si lo son, realiza el movimiento de los Sprites
            # Dentro del update ya se comprueba que todos los movimientos son válidos
            #  (que no choque con paredes, etc.)
            self.grupoSpritesDinamicos.update(
                (self.grupoPlataformas, self.grupoPlataformasVerticales), tiempo, self.director.volumen)

            # Si el grupo de muertos no está vacio llamamos al método muriendo de cada Sprite del grupo
            if len(self.grupoSpritesMuriendo) != 0:
                for sprite in self.grupoSpritesMuriendo:
                    sprite.muriendo()
                    break

            collide = pygame.sprite.groupcollide(
                self.grupoArmaPrincipal, self.grupoEnemigos, True, False)
            if collide != {}:
                for item in collide.items():
                    self.grupoEnemigos.remove(item[1][0])
                    self.grupoSpritesMuriendo.add(item[1][0])
                    break

            # Actualizamos el scroll
            self.actualizarScroll(self.jugador)

            # Actualizamos el fondo:
            self.fondo.update(self.scrollx)

            # Si el arma está dentro de la pantalla se actualiza
            for arma in iter(self.grupoArmaPrincipal):
                # Si el arma está fuera de los límites se elimina del grupo
                if arma.update(arma, tiempo, self.director.volumen):
                    self.grupoArmaPrincipal = pygame.sprite.Group()

    def dibujar(self, pantalla):
        # Si el juego no está en pausa
        if not self.director.pausa:

            # Ponemos primero el fondo
            self.fondo.dibujar(pantalla)

            # Después el decorado
            self.decorado.dibujar(pantalla)

            # Luego los Sprites
            self.grupoSprites.draw(pantalla)

            # Pinto Boomerang
            self.grupoArmaPrincipal.draw(pantalla)

            # Dibujar HUD
            self.hud.dibujar(pantalla, self.jugador.getVidas())

            # Si está el diálogo abierto pinta el diálogo
            if self.dialogo:
                self.dialogoTrump.dibujar(pantalla)

        else:
            # Si se está en pausa pinta solo el menú de pausa
            self.menuPausa.dibujar(pantalla)

    def eventos(self, lista_eventos):
        # Miramos a ver si hay algun evento de salir del programa
        for evento in lista_eventos:
            # Si se quiere salir, se le indica al director
            if evento.type == pygame.QUIT:
                self.director.salirPrograma()
            # Si hay una tecla pulsada
            if evento.type == KEYDOWN:
                # Si se pulsa ESC se pausa el juego
                if evento.key == K_ESCAPE:
                    self.director.pausa = not self.director.pausa
                # Si se pulsa Z y no está salntando se crea una instancia de la arma del jugador
                if evento.key == K_z and self.jugador.numPostura != SPRITE_SALTANDO:
                    # Solo un salasmi a la vez
                    self.grupoArmaPrincipal = pygame.sprite.Group()
                    arma = Salami(self.jugador)
                    # Sale de la posición de jugador
                    arma.establecerPosicion(
                        (self.jugador.posicion[0] - self.scrollx, self.jugador.posicion[1]))
                    self.grupoArmaPrincipal.add(arma)
                # Si se pulsa espacio abre o cierra el diálogo
                if evento.key == K_SPACE and pygame.sprite.groupcollide(self.grupoJugadores, self.grupoEstaticos, False, False) != {}:
                    self.dialogo = not self.dialogo

        # Si estamos en pausa se pasan los eventos al menú de pausa
        if self.director.pausa:
            self.menuPausa.eventos(lista_eventos)

        # Indicamos la acción a realizar según la tecla pulsada
        teclasPulsadas = pygame.key.get_pressed()

        # Si hay un diálogo abierto no puedes moverte
        if self.dialogo:
            self.jugador.mover(teclasPulsadas, K_UP, K_DOWN,
                               K_LEFT, K_RIGHT, K_z, True)
        # Si no lo hay sí
        else:
            self.jugador.mover(teclasPulsadas, K_UP, K_DOWN,
                               K_LEFT, K_RIGHT, K_z)

    # Este método se encargará de realizar las acciones por defecto en caso de colisión entre el jugador y los enemigos o proyectiles
    def colisionJugador(self):
        # Si no tiene vida
        if self.jugador.getVidas() == 0:
            # Reproducir sonido de muerte
            self.jugador.setVidas(
                self.jugador.getVidas(), self.director.volumen)
            # y sale al menú principal
            # reproduce la música del menú principal
            pygame.mixer.music.load(MUSICA_MENU)
            pygame.mixer.music.play(-1)
            # Se le dice al director que salga de esta escena y ejecute la siguiente en la pila
            self.director.salirEscena()
        else:
            # Si aún tiene vidas se quita una y se reproduce el sonido correspondiente
            self.jugador.setVidas(
                self.jugador.getVidas()-1, self.director.volumen)
