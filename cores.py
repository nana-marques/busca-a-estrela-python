import pygame
from pygame.locals import *
from sys import exit
from random import randint
from queue import PriorityQueue

pygame.init()


# Variaveis estaticas
largura = 630
altura = 630

verde = [(146, 209, 79), 1]
azul = [(85, 139, 213), 10]
marrom = [(148, 139, 82), 60]
vermelho = [(255, 0, 0), 1]
amarelo = (217, 217, 25)
cores = [verde[0], azul[0], marrom[0]]
tela = pygame.display.set_mode((largura, altura))

def draw():
    for x in range(0, largura, 15):
        for y in range(0, altura, 15):
            pos_x = x
            pos_y = y
            cor = cores[randint(0, 2)]
    pygame.display.set_caption('Jogo')

def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])


# Cria os quadrados coloridos
def mapa():
    posicoes = []
    for x in range(0, largura, 15):
        for y in range(0, altura, 15):
            posicoes.append((x, y))
            pos_x = x
            pos_y = y
            cor = cores[randint(0, 2)]

            if cor == 0:
                valor = 1
            if cor == 1:
                valor = 10
            if cor == 2:
                valor = 60
            
            pygame.draw.rect(tela, cor, (pos_x, pos_y, 15, 15))
            
    pygame.draw.rect(tela, (255, 0, 0), (315, 315, 15, 15))

# Busca heuristica
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# Refazer caminho
def reconstruct_path(came_from, current):
    while current in came_from:
        current = came_from[current]
        current = pygame.Color(amarelo)

# Algoritmo a*
def algorithm(mapa, start, end, cor):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in mapa for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in mapa for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

mapa()
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()
    
    
    for i in range(0, largura, 15):
        cor_vermelho = vermelho[0]
        valor_vermelho = vermelho[1]

        pygame.draw.rect(tela, cor_vermelho, (270, 270, 105, 105), 2)

    pygame.display.update()
