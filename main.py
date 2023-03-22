import pygame
import math
from queue import PriorityQueue

WIDTH = 800

#window do jogo
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* Path")

#const de cores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

#nodes que definem as "paredes" w demonstram o estado de cada ponto
class Spot:
    def __init__(self, row, col, width, total_rows):
        #indica as configurações da janela pygame
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    #posição
    def get_pos(self):
        return self.row, self.col

    #pontos já visitados
    def is_closed(self):
        return self.color == RED

    #caminhos possiveis a serem seguidos
    def is_open(self):
        return self.color == GREEN

    #paredes do jogo
    def is_barrier(self):
        return self.color == BLACK

    #ponto inicial e representa o agente
    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE
    

    #devolve a cor aos ja pintados
    def reset(self):
        self.color == WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self): 
        self.color = PURPLE

    #desenhando a interface
    def draw(self, win):
        pygame.drae.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass


    
