import sys
import random
import pygame


pygame.init()
Win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Змейка')

def exit_menu(text):
    text_exit = text.render('Нажмите "Q" для выхода из игры', True, (255, 255, 255))
    text_restart = text.render('или нажмите "R" для начала новой игры', True, (255, 255, 255))
    Win.blit(text_exit, (8, 40))
    Win.blit(text_restart, (8, 80))

def start_menu(text):
    text_menu = text.render('Нажмите на стрелочки чтобы начать игру!', True, (255, 255, 255))
    Win.blit(text_menu, (8, 40))

def start():
    you_lose = False
    # кординаты змеи
    MovSnake_X = random.randrange(0, 800, 10)
    MovSnake_Y = random.randrange(0, 600, 10)
    # уровень змейки
    Snake_Level = 0
    # кординаты яблока
    kord_x = random.randrange(0, 800, 10)
    kord_y = random.randrange(0, 600, 10)
    # списки для сохранения предыдущих координат змеи
    bkord_x = []
    bkord_y = []
    # сохранение значений для перемещения змеи
    axis_a = 0
    axis_b = 0
    # проверочное сохранение предыдущего перемещения координат змеи
    #axis_x = 0
    #axis_y = 0
    while True:
        # табло с уровнем
        text = pygame.font.Font(None, 36)
        text_level = text.render(f'Уровень: {Snake_Level}', True, (255, 255, 255))
        Win.blit(text_level, (8, 6))
        if axis_a == 0 and axis_b == 0:
            start_menu(text)

        # создание яблока и змейки
        pygame.draw.rect(Win, (13, 185, 1), [MovSnake_X, MovSnake_Y, 10, 10])
        pygame.draw.rect(Win, (235, 8, 8), [kord_x, kord_y, 10, 10])
        pygame.display.update()

        while you_lose == True:
            exit_menu(text)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_r:
                        you_lose = False
                        start()

        Win.fill((0, 0, 0))
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # кнопки управления
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and axis_a == 0:
                    axis_x = -5
                    axis_a = -5
                    axis_b = 0
                elif event.key == pygame.K_RIGHT and axis_a == 0:
                    axis_x = 5
                    axis_a = 5
                    axis_b = 0
                elif event.key == pygame.K_UP and axis_b == 0:
                    axis_y = -5
                    axis_a = 0
                    axis_b = -5
                elif event.key == pygame.K_DOWN and axis_b == 0:
                    axis_y = 5
                    axis_a = 0
                    axis_b = 5

        # движение змеи
        if MovSnake_Y % 10 == 0:
            if axis_a == 0 and MovSnake_X % 10 != 0:
                MovSnake_X += axis_x
            MovSnake_X += axis_a
        if MovSnake_X % 10 == 0:
            if axis_b == 0 and MovSnake_Y % 10 != 0:
                MovSnake_Y += axis_y
            MovSnake_Y += axis_b

        # сохраняем предыдущие координаты для хвоста змеи
        bkord_x.insert(0, MovSnake_X)
        bkord_y.insert(0, MovSnake_Y)

        # делаем хвост змеи
        for i in range(1, Snake_Level+1):
            pygame.draw.rect(Win, (13, 185, 1), [bkord_x[i], bkord_y[i], 10, 10])
            #pygame.draw.rect(Win, (13, 185, 1), [bkord_x[i+1], bkord_y[i+1], 10, 10])
            if bkord_x[i] == MovSnake_X and bkord_y[i] == MovSnake_Y:
                you_lose = True

        if len(bkord_x) > Snake_Level+1:
            bkord_x.pop(-1)
            bkord_y.pop(-1)
        # новое создаем яблоко
        if MovSnake_X == kord_x and MovSnake_Y == kord_y:
            kord_x = random.randrange(0, 800, 10)
            kord_y = random.randrange(0, 600, 10)
            Snake_Level += 1

        # проигрышный сценарий
        if MovSnake_X > 800:
            you_lose = True
        elif MovSnake_X < 0:
            you_lose = True
        if MovSnake_Y > 600:
            you_lose = True
        elif MovSnake_Y < 0:
            you_lose = True


start()

