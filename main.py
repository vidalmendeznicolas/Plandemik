#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importar modulos
import pygame
from Codigo.Menus.menuPrincipal import Menu
from Codigo.director import Director
import configparser

if __name__ == '__main__':

    # Inicializamos la libreria de pygame
    pygame.init()
    # Creamos el director
    director = Director()
    # Creamos la escena con la pantalla inicial
    escena = Menu(director)
    # Le decimos al director que apile esta escena
    director.apilarEscena(escena)
    # Y ejecutamos el juego
    director.ejecutar()
    # Cuando se termine la ejecución, finaliza la librería
    pygame.quit()
