from Codigo.Menus.menu import ElementoGUI, TextoGUI
from Codigo.gestorRecursos import GestorRecursos
import pygame
from Codigo.Configuracion.constantes import (ALTO_PANTALLA, ANCHO_PANTALLA, FONDO_DIALOGO, LINEA_1_DIALOGO_TRUMP,
                                             LINEA_2_DIALOGO_TRUMP, LINEA_3_DIALOGO_TRUMP, LINEA_4_DIALOGO_TRUMP,
                                             LINEA_5_DIALOGO_TRUMP, LINEA_6_DIALOGO_TRUMP, LINEA_7_DIALOGO_TRUMP,
                                             LINEA_8_DIALOGO_TRUMP, LINEA_9_DIALOGO_TRUMP, LINEA_10_DIALOGO_TRUMP,
                                             LINEA_11_DIALOGO_TRUMP, LINEA_12_DIALOGO_TRUMP, LINEA_13_DIALOGO_TRUMP,
                                             LINEA_14_DIALOGO_TRUMP, LINEA_15_DIALOGO_TRUMP, ULTIMA_LINEA_TRUMP)


class Texto(TextoGUI):
    def __init__(self, pantalla, texto, numLinea):
        # Se carga la fuente y se crea el texto en función
        # de la línea en la que debe aparecer
        fuente = pygame.font.SysFont('dejavusans', 19)
        TextoGUI.__init__(self, pantalla, fuente,
                          (0, 0, 0), texto, (80, 100 + numLinea*25))

    def accion(self):
        ()


class DialogoGUI:
    def __init__(self, nombreImagen):
        # Se carga la imagen de fondo
        self.imagen = GestorRecursos.CargarImagen(FONDO_DIALOGO)
        self.imagen = pygame.transform.scale(
            self.imagen, (ANCHO_PANTALLA-40, 400))

        self.elementosGUI = []

    def eventos(self):
        ()

    def dibujar(self, pantalla):
        # Dibujamos primero la imagen de fondo
        pantalla.blit(self.imagen, (20, 50))
        # Después el texto
        for elemento in self.elementosGUI:
            elemento.dibujar(pantalla)


# Diálogo de España
class DialogoTrumpEspaña(DialogoGUI):
    def __init__(self):
        # Se carga el fondo del diálogo
        DialogoGUI.__init__(self, FONDO_DIALOGO)

        self.elementosGUI.append(Texto(self, LINEA_1_DIALOGO_TRUMP, 0))
        self.elementosGUI.append(Texto(self, LINEA_2_DIALOGO_TRUMP, 1))
        self.elementosGUI.append(Texto(self, LINEA_3_DIALOGO_TRUMP, 2))
        self.elementosGUI.append(Texto(self, LINEA_4_DIALOGO_TRUMP, 3))
        self.elementosGUI.append(Texto(self, LINEA_5_DIALOGO_TRUMP, 4))
        self.elementosGUI.append(Texto(self, LINEA_6_DIALOGO_TRUMP, 5))
        self.elementosGUI.append(Texto(self, LINEA_7_DIALOGO_TRUMP, 6))
        self.elementosGUI.append(Texto(self, LINEA_8_DIALOGO_TRUMP, 7))
        self.elementosGUI.append(Texto(self, LINEA_9_DIALOGO_TRUMP, 8))
        self.elementosGUI.append(Texto(self, ULTIMA_LINEA_TRUMP, 10))


# Diálogo de Rusia
class DialogoTrumpRusia(DialogoGUI):
    def __init__(self):
        # Se carga el fondo del diálogo
        DialogoGUI.__init__(self, FONDO_DIALOGO)

        self.elementosGUI.append(Texto(self, LINEA_10_DIALOGO_TRUMP, 0))
        self.elementosGUI.append(Texto(self, LINEA_11_DIALOGO_TRUMP, 1))
        self.elementosGUI.append(Texto(self, LINEA_12_DIALOGO_TRUMP, 2))
        self.elementosGUI.append(Texto(self, ULTIMA_LINEA_TRUMP, 4))


# Diálogo de China
class DialogoTrumpChina(DialogoGUI):
    def __init__(self):
        # Se carga el fondo del diálogo
        DialogoGUI.__init__(self, FONDO_DIALOGO)

        self.elementosGUI.append(Texto(self, LINEA_13_DIALOGO_TRUMP, 0))
        self.elementosGUI.append(Texto(self, LINEA_14_DIALOGO_TRUMP, 1))
        self.elementosGUI.append(Texto(self, LINEA_15_DIALOGO_TRUMP, 2))
        self.elementosGUI.append(Texto(self, ULTIMA_LINEA_TRUMP, 4))
