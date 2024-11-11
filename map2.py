import pygame
import os

pygame.init()

alto = 1200
ancho = 900


#MAPA
ventana = pygame.display.set_mode((alto,ancho))

#pygame.mixer.music.load(os.path.join('MUSICA/Red Salamander.mp3'))
#pygame.mixer.music.play(-1)

#PERSONAJE
def spritper():
    spritesp = []
    for i in range(16):
        per_path= os.path.join('Personaje_cuts/image_'+str(i)+'.png')
        spritep = pygame.image.load(per_path).convert_alpha()
        spritep= pygame.transform.scale(spritep,(75,150))
        spritesp.append(spritep)
    
    return spritesp
sprites_per = spritper()

muro = pygame.image.load(os.path.join('MAPAS/Muro2.png'))
muro2 = pygame.image.load(os.path.join('MAPAS/Pared2.png'))
piso = pygame.image.load(os.path.join('MAPAS/PISO2.png'))
puerta = pygame.image.load(os.path.join('MAPAS/door.png'))


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
casillap = 150

muro = pygame.transform.scale(muro,(casilla,casilla))
piso = pygame.transform.scale(piso,(casilla,casilla))
muro2 = pygame.transform.scale(muro2,(casilla,casilla))
puerta = pygame.transform.scale(puerta,(casilla,casilla))

def dibujar(ventana):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                ventana.blit(piso, (j*casilla, i*casilla))
            elif m[i][j] == 1:
                ventana.blit(muro, (j*casilla, i*casilla)) 
            else:
                ventana.blit(muro2, (j*casilla, i*casilla)) 

    door_x = 14* casilla
    door_y = 1* casilla
    ventana.blit(puerta,(door_x, door_y))

#VARIABLES PERSONAJE
x,y = 150,150
anchop, altop = 75, 150
speed = 5
directp = "down"
controlp = 0

personaje = sprites_per[controlp]

def actualizar_spritper(directp):
    if directp == "down":
        controlp = 0
    if directp == "up":
        controlp = 4
    if directp == "left":
        controlp = 8
    if directp == "right":
        controlp = 12

    return sprites_per[controlp]    


run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
     
    dibujar(ventana)
    

    pygame.display.flip()

pygame.quit()