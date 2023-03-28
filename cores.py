import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 630
altura = 630

verde = (0, 255, 0)
azul = (0, 0, 255)
marrom = (92, 51, 23)
vermelho = (255, 0, 0)
amarelo = (217, 217, 25)
cores = [verde, azul, marrom]


for x in range(0, largura, 15):
    for y in range(0, altura, 15):
        pos_x = x
        pos_y = y
        cor = cores[randint(0, 2)]

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')

# Cria os quadrados coloridos
posicoes = []
for x in range(0, largura, 15):
    for y in range(0, altura, 15):
        posicoes.append((x, y))
        pos_x = x
        pos_y = y
        cor = cores[randint(0, 2)]
        pygame.draw.rect(tela, cor, (pos_x, pos_y, 15, 15))
        
pygame.draw.rect(tela, vermelho, (315, 315, 15, 15))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()
    
    
    # for i in range(0, largura, 15):
    #     pygame.draw.rect(tela, marrom, (i, 0, 15, 15))
    pygame.display.update()
