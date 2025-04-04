import pygame
import sys
import random, time
from pygame.locals import *

pygame.init()
FPS = pygame.time.Clock()

dw, dh = 400, 600
SPEED = 5
SCORE = 0
coin_score = 0

dy = 0  # Движение фона
ch_s = 2  # Скорость движения фона

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

game_over1 = font.render("Game Over", True, BLACK)

screen = pygame.display.set_mode((dw, dh))
pygame.display.set_caption('Racer')

game_over = pygame.image.load('gameover.jpg')
game_over = pygame.transform.scale(game_over, (dw, dh))
backg = pygame.image.load('AnimatedStreet.png')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Player.png')
        self.rect = self.image.get_rect(center=(160, 520))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT] and self.rect.right < dw:
            self.rect.move_ip(5, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect(center=(random.randint(40, dw - 40), 0))

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > dh:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, dw - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect(center=(random.randint(30, dw - 30), 0))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > dh:
            self.rect.center = (random.randint(30, dw - 30), 0)


P1 = Player()
E1 = Enemy()
C = Coin()

enemies = pygame.sprite.Group(E1)
all_sprites = pygame.sprite.Group(P1, E1)
coins = pygame.sprite.Group(C)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

is_playing, lose = True, False
while is_playing:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Движение фона
    screen.blit(pygame.transform.scale(backg, (dw, dh)), (0, dy))
    screen.blit(pygame.transform.scale(backg, (dw, dh)), (0, dy - dh))
    dy = (dy + ch_s) % dh

    P1.move()
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    for coin in coins:
        coin.move()
        screen.blit(coin.image, coin.rect)
        if pygame.sprite.collide_rect(P1, coin):
            coin.rect.center = (random.randint(30, dw - 30), 0)
            new_coin = random.randint(1, 5)
            coin_score += new_coin # добавили разнообрознасть и теперь каждя монета весит по разному
            if coin_score % SCORE == 0:
                SPEED += 0.5


    if pygame.sprite.spritecollideany(P1, enemies):
        lose = True

    if lose:
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(2)
        screen.fill(RED)
        screen.blit(game_over1, (30, 250))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    scores = font_small.render(f'Score: {SCORE}', True, BLACK)
    coin_text = font_small.render(f'Coins: {coin_score}', True, BLACK)
    screen.blit(scores, (10, 10))
    screen.blit(coin_text, (300, 10))

    pygame.display.flip()
pygame.quit()
