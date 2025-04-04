import random

import pygame as pg
from random import randrange
import time

pg.init()

# Основные параметры
WIDTH, HEIGHT = 800, 800
STEP = 40
FPS = 6
level = 0
running, game_over = True, False

# Настройки экрана
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake Game")
clock = pg.time.Clock()
font = pg.font.SysFont("Verdana", 20)

# Загрузка изображений
bg = pg.transform.scale(pg.image.load("/Users/777/PycharmProjects/pythonProject1/8week/snake/back.jpg"), (WIDTH, HEIGHT))
over_screen = pg.transform.scale(pg.image.load("/Users/777/PycharmProjects/pythonProject1/8week/snake/gameover.jpg"),
                                 (390, 390))


def load_image(path, size=None):
    img = pg.image.load(path)
    return pg.transform.scale(img, size) if size else img


class Food:
    def __init__(self):
        self.position = self.random_position()
        self.image = load_image("/Users/777/PycharmProjects/pythonProject1/8week/snake/food.png")
        self.spawn_time = time.time() # Создаем метку времени когда появляется еда
        self.weight = random.randint(1, 5) # еда имеет разный вес

    def random_position(self):
        return [randrange(0, WIDTH, STEP), randrange(0, HEIGHT, STEP)]

    def draw(self):
        screen.blit(self.image, self.position)

    def relocate(self, walls):
        while True:
            new_pos = self.random_position()
            if new_pos not in [wall.position for wall in walls]:
                self.position = new_pos
                self.spawn_time = time.time() # Создаем метку времени когда появляется еда
                self.weight = random.randint(1, 5)
                break


class Snake:
    def __init__(self):
        self.body = [[360, 360]]
        self.direction = [0, 0]
        self.speed = STEP
        self.color = 'black'
        self.score = 0

    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and self.direction[0] == 0:
                    self.direction = [-self.speed, 0]
                elif event.key == pg.K_RIGHT and self.direction[0] == 0:
                    self.direction = [self.speed, 0]
                elif event.key == pg.K_UP and self.direction[1] == 0:
                    self.direction = [0, -self.speed]
                elif event.key == pg.K_DOWN and self.direction[1] == 0:
                    self.direction = [0, self.speed]

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i - 1][:]

        self.body[0][0] += self.direction[0]
        self.body[0][1] += self.direction[1]

    def draw(self):
        for part in self.body:
            pg.draw.rect(screen, self.color, (*part, STEP, STEP))

    def eat(self, food,walls):
        if self.body[0] == food.position:
            self.score += food.weight
            self.body.append([-STEP, -STEP])
            food.relocate(walls)

    def check_collision(self):
        global game_over
        if self.body[0] in self.body[1:]:
            game_over = True


class Wall:
    def __init__(self, x, y):
        self.position = [x, y]
        self.image = load_image("/Users/777/PycharmProjects/pythonProject1/8week/snake/wall.jpg")

    def draw(self):
        screen.blit(self.image, self.position)


snake = Snake()
food = Food()

while running:
    clock.tick(FPS)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

    screen.blit(bg, (0, 0))

    try:
        with open(f'wall{level}.txt', 'r') as f:
            walls = [Wall(j * STEP, i * STEP) for i, line in enumerate(f.readlines()) for j, char in enumerate(line) if
                     char == "+"]
    except FileNotFoundError:
        walls = []

    food.draw()
    snake.draw()
    snake.move(events)
    snake.eat(food, walls)
    snake.check_collision()

    if time.time() - food.spawn_time > 5:  #Если прошло больше 5 секунд со спавна еды, то еда исчезнет и появится новая еда
        food.relocate(walls)

    for wall in walls:
        wall.draw()
        if food.position == wall.position:
            food.relocate(walls)
        if snake.body[0] == wall.position:
            game_over = True

    score_text = font.render(f'Score: {snake.score}', True, 'black')
    level_text = font.render(f'Level: {level}', True, 'black')
    screen.blit(score_text, (50, 50))
    screen.blit(level_text, (50, 80))

    if snake.score == 3:
        level = (level + 1) % 3
        FPS += 2
        snake.score = 0
        prev_dir = snake.direction[:]
        snake.direction = [0, 0]
        time.sleep(2)
        snake.direction = prev_dir

    while game_over:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running, game_over = False, False
            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                snake = Snake()
                level, FPS, game_over = 0, 6, False

        screen.blit(over_screen, (200, 200))
        final_score = font.render(f'Your score: {snake.score}', True, 'white')
        final_level = font.render(f'Your level: {level}', True, 'white')
        screen.blit(final_score, (320, 500))
        screen.blit(final_level, (322, 520))
        pg.display.flip()

    pg.display.flip()

pg.quit()
