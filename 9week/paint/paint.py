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
            elif event.key == pygame.K_1:
                pen = "square"
            elif event.key == pygame.K_2:
                pen = "right_triangle"
            elif event.key == pygame.K_3:
                pen = "equilateral_triangle"
            elif event.key == pygame.K_4:
                pen = "rhombus"
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

        # Квадрат
        if pen == "square":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event = "press"
            elif event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.rect(screen, color, (x, y, 50, 50))  # Рисуем квадрат 50x50
                last_event = None

        # Прямоугольный треугольник
        elif pen == "right_triangle":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event = "press"
            elif event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, color, [(x, y), (x1, y1), (x, y1)])
                last_event = None

        # Равносторонний треугольник
        elif pen == "equilateral_triangle":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event = "press"
            elif event.type == pygame.MOUSEBUTTONUP:
                side = abs(x1 - x)  # Длина стороны
                height = int((3 ** 0.5 / 2) * side)  # Высота треугольника
                pygame.draw.polygon(screen, color, [(x, y), (x + side, y), (x + side // 2, y - height)])
                last_event = None

        # Ромб
        elif pen == "rhombus":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event = "press"
            elif event.type == pygame.MOUSEBUTTONUP:
                w, h = 50, 80  # Размеры ромба
                pygame.draw.polygon(screen, color, [(x, y - h // 2), (x + w // 2, y),
                                                     (x, y + h // 2), (x - w // 2, y)])
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
