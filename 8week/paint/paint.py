import pygame, sys
pygame.init()

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Текущий цвет
color = RED

# Настройки экрана
WIDTH, HEIGHT = 1001, 601
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

# Инструменты
pen = "mouse"
pre, cur = None, None
pre_e, cur_e = None, None
last_event = None

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        # Выбор инструмента
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pen = "mouse"
            elif event.key == pygame.K_w:
                pen = "rectangle"
            elif event.key == pygame.K_e:
                pen = "circle"
            elif event.key == pygame.K_r:
                pen = "Eraser"
            elif event.key == pygame.K_c:
                screen.fill(WHITE)  # Очистка экрана

            # Выбор цвета
            elif event.key == pygame.K_a:
                color = RED
            elif event.key == pygame.K_s:
                color = GREEN
            elif event.key == pygame.K_d:
                color = BLUE
            elif event.key == pygame.K_f:
                color = BLACK

        # Карандаш
        if pen == "mouse":
            if event.type == pygame.MOUSEBUTTONDOWN:
                pre = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEMOTION and pre:
                cur = pygame.mouse.get_pos()
                pygame.draw.line(screen, color, pre, cur, 2)
                pre = cur
            elif event.type == pygame.MOUSEBUTTONUP:
                pre = None

        # Прямоугольник
        elif pen == "rectangle":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event = "press"
            elif event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                pygame.draw.rect(screen, color, (x, y, x1 - x, y1 - y), 2)
                last_event = None

        # Круг
        elif pen == "circle":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event = "press"
            elif event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                radius = abs((x1 - x) // 2)
                center = ((x + x1) // 2, (y + y1) // 2)
                pygame.draw.circle(screen, color, center, radius, 2)
                last_event = None

        # Ластик
        elif pen == "Eraser":
            if event.type == pygame.MOUSEBUTTONDOWN:
                pre_e = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEMOTION and pre_e:
                cur_e = pygame.mouse.get_pos()
                pygame.draw.line(screen, WHITE, pre_e, cur_e, 10)
                pre_e = cur_e
            elif event.type == pygame.MOUSEBUTTONUP:
                pre_e = None

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
