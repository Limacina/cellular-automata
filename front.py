import copy
import random

import pygame


class Game:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    FPS = 100

    def __init__(self, w, h, r):
        pygame.init()
        self.width = w*20
        self.height = h*20
        self.rule = r
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Lab1Alg")
        self.clock = pygame.time.Clock()
        self.cells = [[0 for i in range(self.width)] for i in range(self.height)]

    def run(self, man):
        # Заполняем экран белым цветом
        self.screen.fill(self.WHITE)
        # Рисуем сетку
        for i in range(0, self.screen.get_height() // 20):
            pygame.draw.line(self.screen, self.BLACK, (0, i * 20), (self.screen.get_width(), i * 20))
        for j in range(0, self.screen.get_width() // 20):
            pygame.draw.line(self.screen, self.BLACK, (j * 20, 0), (j * 20, self.screen.get_height()))
        pygame.display.update()
        running = True
        if man:
            while running:
                self.clock.tick(self.FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                    elif event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        self.cells[pos[1]//20][pos[0]//20] = 1
                        pygame.draw.rect(self.screen, self.BLACK, (pos[0]//20 * 20, pos[1]//20 * 20, 20, 20))
                        pygame.display.flip()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            running = False
        else:
            for i in range(self.height):
                for j in range(self.width):
                    self.cells[i][j] = random.randint(0, 1)
                    if self.cells[i][j] == 1:
                        pygame.draw.rect(self.screen, self.BLACK, (j * 20, i * 20, 20, 20))
            pygame.display.flip()
            while running:
                self.clock.tick(self.FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            running = False

            # number: base, up, down, left, right
        while True:
            self.clock.tick(self.FPS)
            newcells = copy.deepcopy(self.cells)
            for i in range(self.height//20):
                for j in range(self.width//20):
                    base = (i, j)
                    up = (i-1, j) if i != 0 else (self.height-1, j)
                    down = (i+1, j) if i != self.height-1 else (0, j)
                    left = (i, j-1) if j != 0 else (i, self.width-1)
                    right = (i, j+1) if j != self.width-1 else (i, 0)
                    cond = self.rule.calculate_res([
                        self.cells[base[0]][base[1]],
                        self.cells[up[0]][up[1]],
                        self.cells[down[0]][down[1]],
                        self.cells[left[0]][left[1]],
                        self.cells[right[0]][right[1]]
                    ])
                    if cond:
                        pygame.draw.rect(self.screen, self.BLACK, (j * 20, i * 20, 20, 20))
                        newcells[i][j] = 1
                    if not cond and self.cells[i][j] == 1:
                        pygame.draw.rect(self.screen, self.WHITE, (j * 20 + 1, i * 20 + 1, 19, 19))
                        newcells[i][j] = 0
                    pygame.display.flip()
            self.cells = newcells.copy()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
