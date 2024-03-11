import pygame
import math

pygame.init()
width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zadanie 1")

# deklarowanie kolorów
ZIELONY = (0, 255, 0)

#Funkcja rysująca 12-stokąt 1
def draw1(surface, x, y, radius):
    win.fill("black")
    n = 12
    points = []
    for i in range(n):
        angle = math.radians(360 / n * i)
        point = (x + radius * math.cos(angle), y + radius * math.sin(angle))
        points.append(point)
    pygame.draw.polygon(surface, ZIELONY, points, 0)

def draw2(surface, x, y, radius):
    draw1(surface, x, y, radius)
    surface_new = pygame.transform.rotate(surface, 45)
    scalled = pygame.transform.scale_by(surface_new,2)

    offset_x = (surface.get_width() - scalled.get_width()) // 2
    offset_y = (surface.get_height() - scalled.get_height()) // 2

    surface.blit(scalled, (offset_x,offset_y))

# Współrzędne środka i promień
center_x, center_y = width // 2, height // 2
radius = 150

draw1(win, center_x, center_y, radius)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        draw1(win, center_x, center_y, radius)
    if keys[pygame.K_2]:
        draw2(win, center_x, center_y, radius)
        

    pygame.display.update()
pygame.quit()