import random
import pygame
import math

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Algoritmo A*")

# Define as dimensões da grade
ROWS = 42
COLS = 42

# Define as dimensões das células
CELL_WIDTH = 20
CELL_HEIGHT = 20

# Define os possíveis valores da matriz (1, 10, 60) e as cores correspondentes 
# (Apenas anotação)
VALUES = [0, 1, 10, 60]
COLORS = {
    0: (255, 255, 255),  # Branco para as células vazias
    1: (146, 209, 79),      # Verde para as células com valor 1 - Grama
    10: (85, 139, 213),     # Azul para as células com valor 10 - Água
    60: (148, 139, 82)      # Marrom para as células com valor 60 - Montanha
}

# Cores
GREY = (136, 136, 136)
LIGHTGREY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (85, 139, 213)
BROWN = (148, 139, 82)
GREEN = (146, 209, 79)
ORANGE = (255, 165 ,0)
WHITE = (255, 255, 255)

# Definição de cada ponto/nó do mapa
class Node:
    def __init__(self, row, col, width, total_rows):

        #Linhas e colunas em pixel de cada bloquinho
        self.row = row
        self.col = col
        self.width = width

        #tamanho de cada ponto
        self.x = ROWS * width
        self.y = COLS * width

        # Cor do agente (Vermelho) e do radar (Cinza)
        self.color = RED
        self.radar = GREY

        # Lista de blocos vizinhos
        self.neighbors = []

    # Obtém a posição do nó
    def get_position(self):
        return self.ROWS, self.COLS

    # Indica caminhos já passados
    def is_closed(self):
        return self.color == BLACK

    # Indica caminhos possíveis
    def is_open(self):
        return self.color == LIGHTGREY

    # Define a cor do início
    def is_start(self):
        return self.color == RED


    # Dá os valores com base nas cores
    def get_color(self):
        if self.color == GREEN: 
            self.value = 1
            return self.value
        elif self.color == BLUE: 
            self.value = 10
            return self.value
        elif self.color == BROWN: 
            self.value = 60
            return self.value
        else:
            return False
        


    # Funções que definem as cores e valores
    def make_start(self):
        self.color = RED
        self.value = []

    def make_closed(self):
        self.color = (0, 0, 0)

    def make_open(self):
        self.get_color()
        # return self
        
    def make_end(self):
        self.color == ORANGE

    def make_path(self):
        self.color == WHITE

    #desenha o bloquinho
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    #Função que compara tamanho (lt = less-than)
    def __lt__(self, other):
        return False

# Desenho do caminho tomado pelo Agente
def reconstruct_path(origin, current, draw):
    while current in origin:
        current = origin[current]
        current.make_path()
        draw()

# Função que faz a matriz
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Node(i, j, gap, rows)
            grid[i].append(spot)
    return grid

# Função que desenha a matriz na tela
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, LIGHTGREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, LIGHTGREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill([BLUE, GREEN, BROWN])

    for row in grid:
        for spot in row:
            spot.draw(win[1])