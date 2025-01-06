"""Proyecto Final Basico de Cisco
Requisitos de Proyecto
la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
todos los cuadros están numerados comenzando con el 1
el usuario ingresa su movimiento introduciendo el número de cuadro elegido
    - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10,
    y no puede ser un cuadro que ya esté ocupado;
el programa verifica si el juego ha terminado
    - existen cuatro posibles veredictos: el juego continua,
    el juego termina en empate, tu ganas, o la maquina gana;
la maquina responde con su movimiento y se verifica el estado del juego;
no se debe implementar algún tipo de inteligencia artificial
- la maquina elegirá un cuadro de manera aleatoria, es suficiente para este juego.
"""


class JuegoTicTac:

    def __init__(self):
        self.player_maquina = True
        self.player_turn = False
        self.game_over = True

    def iniciar_juego(self):
        self._dibujar_tablero()
        while not self.game_over:
            if self.player_turn:
                print('Tu turno')
                self.player_turn = False
            else:
                print('Tu turno maquina')
                self.player_maquina = False

    def _dibujar_tablero(self):
        """Funcion para dibujar una matriz o tablero
        dimensiones 3x3, desde 1 hasta 9
        +-------+
        |       |
        |  %d   |
        |       |
        +-------+
        """
        num = 0
        # Inicializa la matriz
        board = []

        for i in range(3):
            row = []
            for j in range(3):
                num += 1
                row.append(f"{num}")  # Guardar el número como string
            board.append(row)

        # Construir el dibujo del tablero
        for row in board:
            print("+-------+")
            print("|       |")
            for value in row:
                print(f"|   {value}   |")
            print("|       |")
        print("+-------+")


if __name__ == '__main__':
    jt = JuegoTicTac()
    jt.iniciar_juego()
