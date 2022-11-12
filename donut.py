import pygame
import math
import colorsys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
hue = 0

WIDTH, HEIGHT = 1000, 800

x_start, y_start = 0, 0

x_separator = 10
y_separator = 20

rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0

theta_spacing = 18
phi_spacing = 1

chars = ".,-~:;=!*#$@"

screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Donut')
font = pygame.font.SysFont('Arial', 18, bold=True)
clock = pygame.time.Clock()
FPS = 60


def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    display_surface.blit(text, (x_start, y_start))


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hls_to_rgb(h, s, v))


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 5, pygame.Color("Red"))
    return fps_text


run = True
while run:
    clock.tick(FPS)
    pygame.display.set_caption("{:.2f}".format(clock.get_fps()))
    screen.fill((black))
    z = [0] * screen_size
    b = [' '] * screen_size

    for j in range(0, 628, theta_spacing):
        for i in range(0, 628, phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d *
                         e - f * g - l * d * n))
            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if y_start == rows * y_separator - y_separator:
        y_start = 0

    for i in range(len(b)):
        A += 0.00004
        B += 0.00002
        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_separator

    pygame.display.update()
    hue += 0.005
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
