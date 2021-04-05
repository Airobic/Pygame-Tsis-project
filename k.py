import pygame
import sys
import math
from math import pi, sin, cos
# Color
# ----------
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
# ---------
pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Airobic")
class Point:
    # constructed using a normal tupple
    def __init__(self, point_t=(0, 0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])

    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))

    def __mul__(self, scalar):
        return Point((self.x * scalar, self.y * scalar))

    def __div__(self, scalar):
        return Point((self.x / scalar, self.y / scalar))

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)


def draw_dashed_line(surf, color, start_pos, end_pos, width, dash_length=4):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement.__div__(length)
    for index in range(0, int(length / dash_length), 2):
        start = origin + (slope * index * dash_length)
        end = origin + (slope * (index + 1) * dash_length)
        pygame.draw.aaline(surf, color, start.get(), end.get(), width)


def draw_dashed_lines(surf, color, points, width, dash_len):
    for i in range(len(points) - 1):
        draw_dashed_line(surf, color, points[i], points[i + 1], width, dash_len)
legend = pygame.Surface((100, 50))
legend.fill(WHITE)
font_1 = pygame.font.SysFont("comicsansms", 20)
font_leg = pygame.font.SysFont("comicsansms", 15)
font_l = pygame.font.SysFont("comicsansms", 12)
text = font_leg.render("X", True, (0, 0, 0))
text_1 = font_1.render("cos x", True, (BLACK))
text_2 = font_1.render('sin x', True, BLACK)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys = exit()
    screen.fill(WHITE)
    # Borders
    # ----------
    pygame.draw.rect(screen, BLACK, (70, 10, 660, 540), 2)
    pygame.draw.line(screen, BLACK, (70, 280), (730, 280), 3)
    pygame.draw.line(screen, BLACK, (400, 10), (400, 550), 3)
    # ----------
    # Lines
    # ----------
    for y in range(40, 521, 60):
        pygame.draw.line(screen, BLACK, (70, y), (730, y))
    for y in range(40, 521, 30):
        pygame.draw.line(screen, BLACK, (70, y), (90, y))
        pygame.draw.line(screen, BLACK, (710, y), (730, y))
    for y in range(40, 521, 15):
        pygame.draw.line(screen, BLACK, (70, y), (80, y))
        pygame.draw.line(screen, BLACK, (720, y), (730, y))
    # ----------

    for x in range(100, 701, 100):
        pygame.draw.line(screen, BLACK, (x, 10), (x, 550))
    for x in range(100, 701, 50):
        pygame.draw.line(screen, BLACK, (x, 10), (x, 30))
        pygame.draw.line(screen, BLACK, (x, 550), (x, 530))
    for x in range(100, 701, 25):
        pygame.draw.line(screen, BLACK, (x, 10), (x, 20))
        pygame.draw.line(screen, BLACK, (x, 550), (x, 540))
    # -----------


    for x in range(100, 700):
        sin_y1 = 240 * sin((x - 100) / 100 * pi)
        sin_y2 = 240 * sin((x - 99) / 100 * pi)
        pygame.draw.aalines(screen, RED, False, [(x, 280 + sin_y1), ((x + 1), 280 + sin_y2)])

    for x in range(100, 700, 2):
        cos_y1 = 240 * cos((x - 100) / 100 * pi)
        cos_y2 = 240 * cos((x - 99) / 100 * pi)
        pygame.draw.aalines(screen, BLUE, False, [(x, 280 + cos_y1), ((x + 1), 280 + cos_y2)])
    a = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
    for x in range(9):
        f1 = pygame.font.SysFont('serif', 15)
        text1 = f1.render(a[x], True, (0, 0, 0))
        screen.blit(text1, (25, 32 + (x * 60)))
    nn = -3
    cnt5 = 0
    while nn <= 3:
        if nn % 1 != 0.5:
            font = pygame.font.Font(None, 20)
            text1 = font.render(str(nn) + "П", True, BLACK)
            screen.blit(text1, (90 + cnt5, 560))
        elif nn % 1 == 0.5:
            font = pygame.font.Font(None, 15)
            text1 = font.render(str(int(nn * 2)) + "/2" + "П", True, BLACK)
            screen.blit(text1, (90 + cnt5, 560))
        cnt5 += 50
        nn += 0.5
    b = ['-3', '-2', '-1']
    for x in range (3):
        f1 = pygame.font.Font(None, 20)
        text1 = f1.render(b[x], True, BLACK)
        screen.blit(text1, (-540 + cnt5, 325))
        cnt5 += 75

    screen.blit(legend, (475, 43))
    legend.blit(text_1, (5, 45 - text_1.get_width() // 2))  # cos
    p = [(60, 40), (90, 40)]
    draw_dashed_lines(legend, BLUE, p, 3, 3)

    legend.blit(text_2, (10, 25 - text_2.get_width() // 2))  # sin
    pygame.draw.line(legend, RED, (60, 20), (90, 20), 2)
    pygame.display.update()
pygame.quit()