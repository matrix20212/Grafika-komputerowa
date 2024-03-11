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
    scalled = pygame.transform.scale_by(surface_new,1.5)

    offset_x = (surface.get_width() - scalled.get_width()) // 2
    offset_y = (surface.get_height() - scalled.get_height()) // 2

    surface.blit(scalled, (offset_x,offset_y))

def draw3(surface, x, y, radius):
    draw1(surface, x, y, radius)
    surface_new = pygame.transform.rotate(surface, 180)
    scalled = pygame.transform.smoothscale_by(surface_new, (1,1.5))

    offset_x = (surface.get_width() - scalled.get_width()) // 2
    offset_y = (surface.get_height() - scalled.get_height()) // 2

    surface.blit(scalled, (offset_x,offset_y))

def draw4(surface, x, y, radius):
    draw1(surface, x, y, radius)

def draw5(surface, x, y, radius):
    draw1(surface, x, y, radius)
    scalled = pygame.transform.smoothscale_by(surface, (1.5,0.5))
    surface.fill("black")

    offset_x = (surface.get_width() - scalled.get_width()) // 2
    offset_y = (surface.get_height() - scalled.get_height()) // 2

    surface.blit(scalled, (offset_x,offset_y-220))

def draw6(surface, x, y, radius):
    draw1(surface, x, y, radius)

def draw7(surface, x, y, radius):
    draw1(surface, x, y, radius)
    surface_new = pygame.transform.rotate(surface, 180)
    scalled = pygame.transform.smoothscale_by(surface_new, (1,1.5))
    flipped = pygame.transform.flip(scalled,False,True)

    offset_x = (surface.get_width() - flipped.get_width()) // 2
    offset_y = (surface.get_height() - flipped.get_height()) // 2

    surface.blit(flipped, (offset_x,offset_y))

def draw8(surface, x, y, radius):
    draw1(surface, x, y, radius)
    scalled = pygame.transform.smoothscale_by(surface, (1.5,0.5))
    surface_new = pygame.transform.rotate(scalled, -30)
    surface.fill("black")

    offset_x = (surface.get_width() - surface_new.get_width()) // 2
    offset_y = (surface.get_height() - surface_new.get_height()) // 2

    surface.blit(surface_new, (offset_x-50,offset_y+130))

def draw9(surface, x, y, radius):
    draw1(surface, x, y, radius)

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
    if keys[pygame.K_3]:
        draw3(win, center_x, center_y, radius)
    if keys[pygame.K_4]:
        draw4(win, center_x, center_y, radius)
    if keys[pygame.K_5]:
        draw5(win, center_x, center_y, radius)
    if keys[pygame.K_6]:
        draw6(win, center_x, center_y, radius)
    if keys[pygame.K_7]:
        draw7(win, center_x, center_y, radius)
    if keys[pygame.K_8]:
        draw8(win, center_x, center_y, radius)
    if keys[pygame.K_9]:
        draw9(win, center_x, center_y, radius)
            

    pygame.display.update()
pygame.quit()