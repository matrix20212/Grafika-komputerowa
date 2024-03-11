import pygame

pygame.init()
width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zadanie 2")



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win.fill("White")      
    # Figura 1   
    pygame.draw.circle(win, "black", (150, 150), 100)
    pygame.draw.rect(win, "yellow", pygame.Rect(100, 100, 100, 100))

    # Figura 2
    pygame.draw.rect(win, "green", pygame.Rect(330, 50, 200, 200))
    pygame.draw.polygon(win, "white", [(330, 250), (530, 250), (430, 150)])

    # Figura 3
    pygame.draw.polygon(win, "blue", [(100, 350), (200, 350), (150, 440)])
    pygame.draw.rect(win, "blue", pygame.Rect(75, 440, 150, 80))
    pygame.draw.polygon(win, "blue", [(100, 590), (200, 590), (150, 520)])

    # Figura 4

    pygame.draw.line(win,"red",(330,350),(530,350),12)
    pygame.draw.line(win,"red",(330,580),(530,580),12)
    pygame.draw.line(win,"red",(330+3,580+3),(530-3,350-3),14)

    pygame.display.update()
pygame.quit()