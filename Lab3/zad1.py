import pygame
import math

pygame.init()
width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zadanie 1")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

#Funkcja rysująca 12-stokąt 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

def draw_dodecagon(surface, x, y, radius):
    n = 12
    points = []
    for i in range(n):
        angle = math.radians(360 / n * i)
        point = (x + radius * math.cos(angle), y + radius * math.sin(angle))
        points.append(point)
    pygame.draw.polygon(surface, ZIELONY, points, 2)


# Współrzędne środka i promień
center_x, center_y = width // 2, height // 2
radius = 50

# Narysowanie 12-sto kąta
draw_dodecagon(win, center_x, center_y, radius)

pygame.display.flip()
