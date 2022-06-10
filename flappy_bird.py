import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60


screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')


#definiendo variables del juego
ground_scroll = 0
scroll_speed = 4 #Velocidad de ground


#cargando imagenes
bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')

run = True
while run:

    clock.tick(fps)

    #Agregando el fondo
    screen.blit(bg, (0,0))

    #Agregando el suelo
    screen.blit(ground_img, (ground_scroll,768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False

    pygame.display.update()

pygame.quit()            