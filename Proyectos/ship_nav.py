import pygame

from Proyectos.bullet import Bullet


class Ship:
    """Clase que gestiona atributos de la nave del jugador"""

    # Recibe un objeto el juego AlienInvasion
    def __init__(self, game_ai):
        # Obtiene las caracteristicas de la ventana de juego
        self.screen = game_ai.ventana_juego
        # Obtiene el get_rect, es decir fracciones de pixeles de ;a pantalla
        self.screen_rect = self.screen.get_rect()

        # Carga la imagen de la nave
        self.image_ship = pygame.image.load('graphcs/rocket_cohet.bmp')
        self.imagen_redimensionada = pygame.transform.scale(self.image_ship,
                                                            (game_ai.settings.window_width // 14,
                                                             game_ai.settings.window_height // 10))

        # obtiene las fracciones de pixeles de la nave para posicionar
        self.rect = self.imagen_redimensionada.get_rect()

        # Coloca la nave en la posicion central, midbottom abajo centro
        self.rect.midbottom = self.screen_rect.midbottom

        # Bandera de movimiento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Posicion horizontal, es decir hacia la iz y derech de la nave
        self.position_x = float(self.rect.x)

        # Posicion vertical de la nave
        self.position_y = float(self.rect.y)

        # Config. velocidad de la nave por default
        self.ship_speed = 0.5
        # Balas que puede disparar continuament
        self.bullet_max = 5

    def position_ship(self):
        """Metodo que posiciona la nave en el centro de la ventana"""
        # En la ventana del juego, dibuja la imagen redimensionada en la posicion que especificamos
        self.screen.blit(self.imagen_redimensionada, self.rect)

    def update_move(self):
        """Metodo que actualiza movimiento de la nave"""
        # Actualiza la posicion x de la nave
        # Verifica que las fracciones de pixeles de la nave no superen al de la pantalla
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.position_x += self.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.position_x -= self.ship_speed

        if self.moving_up and self.rect.top > 0:
            self.position_y -= self.ship_speed
            # print(self.position_y)

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.position_y += self.ship_speed
            # print(self.position_y)

        # Actualiza el movimiento para cada pixel
        self.rect.x = self.position_x
        self.rect.y = self.position_y

