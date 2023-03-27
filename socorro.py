import pygame
import random
import math

# Define as dimensões da grade
ROWS = 42
COLS = 42

# Define as dimensões das células
CELL_WIDTH = 20
CELL_HEIGHT = 20

# Define as dimensões da janela do Pygame
WINDOW_WIDTH = COLS * CELL_WIDTH
WINDOW_HEIGHT = ROWS * CELL_HEIGHT

# Define os possíveis valores da matriz (1, 10, 60) e as cores correspondentes
VALUES = [0, 1, 10, 60]
COLORS = {
    0: (255, 255, 255),  # Branco para as células vazias
    1: (0, 0, 255),      # Azul para as células com valor 1
    10: (0, 255, 0),     # Verde para as células com valor 10
    60: (255, 0, 0)      # Vermelho para as células com valor 60
}

# Define a classe Node para representar cada nó na grade
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y
            

# Define a função de heurística para o algoritmo A*
def heuristic(node, goal):
    return math.sqrt((node.x - goal.x) ** 2 + (node.y - goal.y) ** 2)

# Define a função para encontrar o caminho usando o algoritmo A*
def a_star(start, end, grid):
    # Inicializa a lista aberta e a lista fechada
    open_list = []
    closed_list = []

    
    # Adiciona o ponto de partida à lista aberta
    open_list.append(start)
    
    # Loop principal do algoritmo
    while open_list:
        
        # Encontra o nó com o menor valor f na lista aberta
        current_node = open_list[0]
        for node in open_list:
            if node < current_node:
                current_node = node
        
        # Remove o nó atual da lista aberta e adiciona à lista fechada
        open_list.remove(current_node)
        closed_list.append(current_node)
        
        # Verifica se chegamos ao ponto final
        if current_node == end:
            
            # Reconstrói o caminho
            path = []
            node = current_node
            while node is not None:
                path.append((node.x, node.y))
                node = node.parent
            return path[::-1]
        
        # Expande os nós vizinhos do nó atual
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            
            # Calcula as coordenadas do nó vizinho
            if isinstance(current_node, Node):
                x = current_node.x + i
                y = current_node.y + j
                return x, y
            
            # Verifica se o nó vizinho está dentro dos limites da grade
            if x < 0 or y < 0 or x >= ROWS or y >= COLS:
                continue
            
            # Verifica se o nó vizinho não é um obstáculo (valor 0 na matriz)
            if grid[x][y] == 0:
                continue
                       # Cria um objeto Node para representar o nó vizinho
            neighbor = Node(x, y)
            
            # Verifica se o nó vizinho já está na lista fechada
            if neighbor in closed_list:
                continue
            
            # Calcula o custo g do nó vizinho
            neighbor.g = current_node.g + grid[x][y]
            
            # Calcula o custo h do nó vizinho usando a função de heurística
            neighbor.h = heuristic(neighbor, end)
            
            # Calcula o custo f do nó vizinho
            neighbor.f = neighbor.g + neighbor.h
            
            # Verifica se o nó vizinho já está na lista aberta e se tem um custo f menor
            for node in open_list:
                if neighbor == node and neighbor.f > node.f:
                    break
            else:
                # Adiciona o nó vizinho à lista aberta
                open_list.append(neighbor)
                
                # Define o nó atual como pai do nó vizinho
                neighbor.parent = current_node

# Define a função principal do programa
def main():
    # Inicializa o Pygame
    pygame.init()
    
    # Cria a janela do Pygame
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    # Define o título da janela
    pygame.display.set_caption("A* Algorithm")
    
    # Cria a matriz aleatória
    grid = [[random.choice(VALUES) for _ in range(COLS)] for _ in range(ROWS)]
    
    # Define o ponto de partida e o ponto final
    start = Node(19, 19)
    end = Node(random.randint(0, ROWS-1), random.randint(0, COLS-1))
    
    # Loop principal do programa
    running = True
    while running:
        # Desenha a matriz na tela
        for row in range(ROWS):
            for col in range(COLS):
                color = COLORS[grid[row][col]]
                pygame.draw.rect(screen, color, (col*CELL_WIDTH, row*CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
        
        # Desenha o ponto de partida e o ponto final
        pygame.draw.circle(screen, (255, 165, 0), (start.y*CELL_WIDTH+CELL_WIDTH//2, start.x*CELL_HEIGHT+CELL_HEIGHT//2), CELL_WIDTH//2)
        pygame.draw.circle(screen, (255, 0, 0), (end.y*CELL_WIDTH+CELL_WIDTH//2, end.x*CELL_HEIGHT+CELL_HEIGHT//2), CELL_WIDTH//2)
        
        # Executa o algoritmo A* para encontrar o caminho
        path = a_star(grid, start, end)

        # Desenha o caminho encontrado
        if path is not None:
            for node in path:
                pygame.draw.circle(screen, (0, 0, 255), (node.y*CELL_WIDTH+CELL_WIDTH//2, node.x*CELL_HEIGHT+CELL_HEIGHT//2), CELL_WIDTH//4)
        
        # Atualiza a tela
        pygame.display.flip()

        # Verifica eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                # Define o ponto final a partir do clique do mouse
                x, y = event.pos
                row, col = x // CELL_WIDTH, y // CELL_HEIGHT
                end = Node(row, col)

    # Encerra o Pygame
    pygame.quit()
    
main()