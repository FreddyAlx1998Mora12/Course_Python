import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Clase alien para representar flota"""
    def __init__(self, ai_game):
        super().__init__()
        # Obtiene la venta del juego, debo argumentar la clase principal
        self.screen = ai_game.ventana_juego

        # Carga la imagen de la flota
        self.image = pygame.image.load('graphcs/nave.bmp')

        # Obtiene los pixeles de la img
        self.rect = self.image.get_rect()
        # print(self.rect)

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Posicion de alien
        self.position_x = float(self.rect.x)

    def position_alien(self):
        """Metodo que posiciona la nave en el centro de la ventana"""
        # En la ventana del juego, dibuja la imagen redimensionada en la posicion que especificamos
        self.screen.blit(self.imagen_redimensionada, self.rect)
