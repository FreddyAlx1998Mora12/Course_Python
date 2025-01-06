import pygame
import sys
from settings import Configuraciones
from ship_nav import Ship
from bullet import Bullet
from ship_ufo import Alien

class AlienInvasion:
    """Clase para gestionar recursos y comportamiento del juego"""

    def __init__(self):
        """Inicializa la clase AlienInvasion o juego y crea un recurso"""
        # Crea una ventana para dibujar el juego y la logica
        pygame.init()

        # Instancia como atributo
        self.settings = Configuraciones()
        # Una vez inicializado, redirecciona el tamanio de la ventana
        self.ventana_juego = pygame.display.set_mode((self.settings.window_width, self.settings.window_height))
        # Ponle titulo a la ventana
        pygame.display.set_caption(self.settings.title_game)
        # Configuracion para el fondo de pantalla
        # self.bg_color = (44, 62, 80)  # No hara falta debido a que tenemos una clase settings

        # SHip(self) -> self es el objeto como tal ALienInvasion
        # Instanciamos un objeto nave para el juego
        self.nave = Ship(self)

        # Grupo de balas activas para nave
        self.bullets = pygame.sprite.Group()
        # self.alien = Alien(self)

        self.aliens = pygame.sprite.Group()
        self._create_fleet_alien()

    # Metodo para iniciar el juego
    def run_game(self):
        """Inicia el juego, por medio de un bucle infinito"""
        while True:

            # metodo auxiliar para escuchar eventos
            self._check_eventos()
            # metodo que actualiza cada paso del bucle el movimiento
            self.nave.update_move()
            # metodo de actualizar bullets
            self._update_bullets()
            # metodo para crear flota de aliens

            # metodo auxiliar para redibujar y actualizar
            self._update_screen()

    def _check_eventos(self):
        # Busca o escucha eventos de teclado y de mouse
        for event in pygame.event.get():
            # Si el evento es de tipo QUIT o salida, es decir cuando cierra la ventana
            if event.type == pygame.QUIT:
                # Sale del sistema, y cierra sin errores
                # print('clickeaste en la x de la ventana')
                sys.exit()
            # Si el usuario presiono una tecla
            elif event.type == pygame.KEYDOWN:
                # Funcion segun el tipo de evento
                self._check_events_keydown(event.key)
            # Si el usuario mantuvo presionado y levanto la tecla
            elif event.type == pygame.KEYUP:
                self._check_events_keyup(event.key)

    def _create_fleet_alien(self):
        new_alien = Alien(self)
        self.aliens.add(new_alien)

    def _update_screen(self):
        # De fondo pon siempre ese color
        self.ventana_juego.fill(self.settings.bg_color)
        self.nave.position_ship()
        # self.alien.position_alien()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.ventana_juego)

        # Hace visible la ultima pantalla dibujada
        # Actualiza constantemente la pantalla, de modo que sea mas dinamico el juego
        pygame.display.flip()

    def _check_events_keydown(self, evento_clave):
        """Metodo que realiza una accion cuando pulsa una sola vez una tecla"""
        # Si la tecla que presiono es la tecla derecha
        if evento_clave == pygame.K_RIGHT:
            # Mueve la nave un rect a la derecha
            self.nave.moving_right = True
        elif evento_clave == pygame.K_LEFT:
            self.nave.moving_left = True
        elif evento_clave == pygame.K_UP:
            self.nave.moving_up = True
        elif evento_clave == pygame.K_DOWN:
            self.nave.moving_down = True
        elif evento_clave == pygame.K_q:
            sys.exit()
        elif evento_clave == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Crea un objeto de tipo bullet bala y aniade al grupo de bullets del juego"""
        # Comprueba que la longitud de balas con lo permitido
        if len(self.bullets) < self.nave.bullet_max:
            n_bullet = Bullet(self)
            self.bullets.add(n_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # Deshacerce de las balas que se ha disparado
        for bull in self.bullets.copy():
            if bull.rect.bottom <= 0:
                # elimina aquella bala que paso del borde
                self.bullets.remove(bull)
        # print(len(self.bullets))

    def _check_events_keyup(self, evento_clave):
        """Metodo que realiza una accion cuando mantiene pulsada hasta soltar una tecla realiza algo"""
        if evento_clave == pygame.K_RIGHT:
            self.nave.moving_right = False
        elif evento_clave == pygame.K_LEFT:
            self.nave.moving_left = False
        elif evento_clave == pygame.K_UP:
            self.nave.moving_up = False
        elif evento_clave == pygame.K_DOWN:
            self.nave.moving_down = False


if __name__ == '__main__':
    # Hace una instancia del juego
    game_ai = AlienInvasion()
    # Ejecuta el juego
    game_ai.run_game()
