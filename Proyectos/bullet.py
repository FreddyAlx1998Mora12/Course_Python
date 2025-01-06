import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.ventana_juego
        self.settings = ai_game.settings

        self.color = (240, 243, 244)
        # Config. balas
        self.bullet_speed = 1.15
        self.bullet_width = 8.5
        self.bullet_height = 25


        # crea un pixel para la bala
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)

        # Coloca la bala en la posicion de la nave
        self.rect.midtop = ai_game.nave.rect.midtop

        # Guarda la posicion de la bala como valor float
        self.bullet_y = float(self.rect.y)

    def update(self):
        """Metodo que actualiza la posicion o desplaz de la bala"""
        # Actualiza la posicion
        self.bullet_y -= self.bullet_speed

        # Actualiza la posicion en rect (pixel)
        self.rect.y = self.bullet_y

    def draw_bullet(self):
        # Dibuja la bala en la 'pantalla', con el 'color', y con las 'medidas'
        pygame.draw.rect(self.screen, self.color, self.rect)
