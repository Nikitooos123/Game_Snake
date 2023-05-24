import sys
import random
import pygame


class Snake:
    pygame.init()

    def __init__(self, x=800, y=600):
        self.x = x
        self.y = y
        self.Win = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption('Змейка')
        self.text = pygame.font.Font(None, 36)
        self.start()

    def start(self):
        # кординаты змеи
        self.MovSnake_X = random.randrange(0, self.x, 10)
        self.MovSnake_Y = random.randrange(0, self.y, 10)
        # уровень змейки
        self.Snake_Level = 0
        # кординаты яблока
        self.kord_x = random.randrange(0, self.x, 10)
        self.kord_y = random.randrange(0, self.y, 10)
        # списки для сохранения предыдущих координат змеи
        self.bkord_x = []
        self.bkord_y = []
        # сохранение значений для перемещения змеи
        self.axis_a = 0
        self.axis_b = 0
        self.game()

    def lose(self):
        while True:
            self.table()
            text_exit = self.text.render('Нажмите "Q" для выхода из игры', True, (255, 255, 255))
            text_restart = self.text.render('или нажмите "R" для начала новой игры', True, (255, 255, 255))
            self.Win.blit(text_exit, (8, 40))
            self.Win.blit(text_restart, (8, 80))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_r:
                        self.start()

    def table(self):
        text_level = self.text.render(f'Уровень: {self.Snake_Level}', True, (255, 255, 255))
        self.Win.blit(text_level, (8, 6))

    def game(self):
        while True:
            self.table()
            # создание яблока и змейки
            pygame.draw.rect(self.Win, (13, 185, 1), [self.MovSnake_X, self.MovSnake_Y, 10, 10])
            pygame.draw.rect(self.Win, (235, 8, 8), [self.kord_x, self.kord_y, 10, 10])
            pygame.display.update()
            self.Win.fill((0, 0, 0))
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # кнопки управления
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.axis_a == 0:
                        self.axis_x = -5
                        self.axis_a = -5
                        self.axis_b = 0
                    elif event.key == pygame.K_RIGHT and self.axis_a == 0:
                        self.axis_x = 5
                        self.axis_a = 5
                        self.axis_b = 0
                    elif event.key == pygame.K_UP and self.axis_b == 0:
                        self.axis_y = -5
                        self.axis_a = 0
                        self.axis_b = -5
                    elif event.key == pygame.K_DOWN and self.axis_b == 0:
                        self.axis_y = 5
                        self.axis_a = 0
                        self.axis_b = 5

            # движение змеи
            if self.MovSnake_Y % 10 == 0:
                if self.axis_a == 0 and self.MovSnake_X % 10 != 0:
                    self.MovSnake_X += self.axis_x
                self.MovSnake_X += self.axis_a
            if self.MovSnake_X % 10 == 0:
                if self.axis_b == 0 and self.MovSnake_Y % 10 != 0:
                    self.MovSnake_Y += self.axis_y
                self.MovSnake_Y += self.axis_b

            # сохраняем предыдущие координаты для хвоста змеи
            self.bkord_x.insert(0, self.MovSnake_X)
            self.bkord_y.insert(0, self.MovSnake_Y)

            # делаем хвост змеи
            for i in range(1, self.Snake_Level + 1):
                pygame.draw.rect(self.Win, (13, 185, 1), [self.bkord_x[i], self.bkord_y[i], 10, 10])
                if self.bkord_x[i] == self.MovSnake_X and self.bkord_y[i] == self.MovSnake_Y:
                    self.lose()

            # создаем новое яблоко
            if self.MovSnake_X == self.kord_x and self.MovSnake_Y == self.kord_y:
                self.kord_x = random.randrange(0, self.x, 10)
                self.kord_y = random.randrange(0, self.y, 10)
                self.Snake_Level += 1

            # проигрышный сценарий
            if self.MovSnake_X > self.x:
                self.lose()
            elif self.MovSnake_X < 0:
                self.lose()
            if self.MovSnake_Y > self.y:
                self.lose()
            elif self.MovSnake_Y < 0:
                self.lose()

a = Snake()
a.game()