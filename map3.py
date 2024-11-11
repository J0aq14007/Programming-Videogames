import pygame
import os

pygame.init()

alto = 1200
ancho = 900


#MAPA
ventana = pygame.display.set_mode((alto,ancho))
muro = pygame.image.load(os.path.join('Muro3.png'))
muro2 = pygame.image.load(os.path.join('Pared.png'))
piso = pygame.image.load(os.path.join('PISO3.png'))
character = pygame.image.load('PER.png').convert_alpha()

m = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
]

casilla = 75

muro = pygame.transform.scale(muro,(casilla,casilla))
piso = pygame.transform.scale(piso,(casilla,casilla))
muro2 = pygame.transform.scale(muro2,(casilla,casilla))


def dibujar(ventana):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                ventana.blit(piso, (j*casilla, i*casilla))
            elif m[i][j] == 1:
                ventana.blit(muro, (j*casilla, i*casilla)) 
            else:
                ventana.blit(muro2, (j*casilla, i*casilla)) 

run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
     
    dibujar(ventana)
    

    pygame.display.flip()

pygame.quit()