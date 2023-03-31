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
laranja = (255, 173 ,0)
cores = [verde[0], azul[0], marrom[0]]
tela = pygame.display.set_mode((largura, altura))
tela2 = [(630, 630)]
pygame.display.set_caption('Algoritmo A*')


def draw():
    for x in range(0, largura, 15):
        for y in range(0, altura, 15):
            pos_x = x
            pos_y = y
            cor = cores[randint(0, 2)]
    return x, y

class Ponto:
    def __init__(self, cor, valor):
        self.grid = self
        self.cor = cor
        self.valor = valor

    def get_pos(self):
        return self.x, self.y

    def caminho_update(self, grid):
            neighbors = []
            neighbors.extend(self)

            if self[0] < largura and not grid[1]: # DOWN
                # print(grid)
                neighbors.append(grid[(self[0])][(self[1])])

            if self[0] > 0 and not grid[1]: # UP
                neighbors.append(grid[self[0] - 1][self[1]])

            if self[1] < largura - 1 and not grid[0]: # RIGHT
                neighbors.append(grid[self[0]][self[1] + 1])

            if self[1] > 0 and not grid[0]: # LEFT
                neighbors.append(grid[self[0]][self[1] - 1])


# Cria os quadrados coloridos
def mapa():
    posicoes = []

    for x in range(0, largura, 15):
        for y in range(0, altura, 15):
            posicoes.append((x, y))
            pos_x = x
            pos_y = y
            cor = cores[randint(0, 2)]

            ponto = pygame.draw.rect(tela, cor, (pos_x, pos_y, 15, 15))

            if ponto == 0:
                value = 1
                ponto.append(value)
                return ponto
            elif ponto == 1:
                value = 10
                ponto.append(value)
                return ponto
            elif ponto == 2:
                value = 60
                ponto.append(value)
                return ponto

            print(ponto)

    
            
    pygame.draw.rect(tela, vermelho[0], (315, 315, 15, 15))

    return posicoes

# Busca heuristica
def heuristica(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
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
    g_score = {spot: float("inf") for pos_x in mapa for spot in pos_x}
    g_score[start] = 0
    f_score = {spot: float("inf") for pos_x in mapa for spot in pos_x}
    f_score[start] = heuristica((start[0], start[1]), (end[0], end[1]))
    print(f_score[start])
    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end = pygame.Color(0,0,0)
            return True

        for neighbor in current:
            temp_g_score = g_score[current] + 1
            

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristica(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor = pygame.Color((0, 255, 0))

        draw()

        if current != start:
            current = pygame.Color(vermelho[0])

    return False


def main():

    mapa()
    esferas = []
    while True:

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                # posicao_esfera = pygame.mouse.get_pressed()
                pos_x, pos_y = evento.pos

                for x in range(0, largura):
                    for y in range(0, altura):
                        x = pos_x
                        y = pos_y

                cor_esfera = pygame.Color(laranja)
                if len(esferas) < 7:
                    pygame.draw.rect(tela, cor_esfera, ((15 * round(x/15)), (15 * round(y/15)), 15, 15), 0, 10, 10, 10, 10)
                    esferas.append((x, y))
                    print(esferas)


                #print(x,y)

            if evento.type == pygame.KEYDOWN and esferas:
                for x in range(0, largura, 15):
                    for y in range(0, altura, 15):
                        pos_x = x
                        pos_y = y
                        final = esferas[0]
                        Ponto.caminho_update(esferas[1], final)

            if evento.type == pygame.KEYDOWN and final:
                inicio = (315, 315, 15, 15)
                grid = draw()
                # print(grid)
                tamanho = (630, 630)

                # print(tela)
                algorithm(lambda: tamanho, grid, inicio, final)
        
        
        # tamanho do radar
        for i in range(0, largura, 15):
            cor_vermelho = vermelho[0]
            pygame.draw.rect(tela, cor_vermelho, (270, 270, 105, 105), 2)

        pygame.display.update()

main()
