import pygame
import math

pygame.init()
width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zadanie 1")

# deklarowanie kolorów
ZIELONY = (0, 255, 0)

#Funkcja rysująca 12-stokąt 
def draw12(surface, x, y, radius):
    n = 12
    points = []
    for i in range(n):
        angle = math.radians(360 / n * i)
        point = (x + radius * math.cos(angle), y + radius * math.sin(angle))
        points.append(point)
    pygame.draw.polygon(surface, ZIELONY, points, 2)


# Współrzędne środka i promień
center_x, center_y = width // 2, height // 2
radius = 150

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Narysowanie 12-sto kąta
    draw12(win, center_x, center_y, radius)

    pygame.display.update()
