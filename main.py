import pygame
import os
import random
#import map2

pygame.init()

alto = 1200
ancho = 900


#MAPA
ventana = pygame.display.set_mode((alto,ancho))

#pygame.mixer.music.load(os.path.join('MUSICA/Red Salamander.mp3'))
#pygame.mixer.music.play(-1)

muro = pygame.image.load(os.path.join('MAPAS/Muro.png'))
muro2 = pygame.image.load(os.path.join('MAPAS/M2.png'))
piso = pygame.image.load(os.path.join('MAPAS/PISO.png'))
puerta = pygame.image.load(os.path.join('MAPAS/door.png'))

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

#CANGREJO
def spritcang():
    spritesc = []
    for i in range(4):
        cang_path= os.path.join('Cang_cuts/cang_'+str(i)+'.png')
        spritec = pygame.image.load(cang_path).convert_alpha()
        spritec= pygame.transform.scale(spritec,(75,75))
        spritesc.append(spritec)
    
    return spritesc
sprites_cg = spritcang()

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

#def cambiar_map():
#    map2.cargar_map2(ventana)

#VARIABLES CANGREJO
cx,cy = random.randint(0, ancho-75), random.randint(0, alto-75)
anchoc, altoc = 75, 75
speedc = 5
directc = random.choice(["up","down","left","right"])
controlc = 0

cangrejo = sprites_cg[controlc]

def actualizar_spritcang(directp):
    if directc == "down":
        controlc = 0
    if directc == "up":
        controlc = 1
    if directc == "left":
        controlc = 2
    if directc == "right":
        controlc = 3

    return sprites_cg[controlc]

run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    

    teclas = pygame.key.get_pressed()
    dx,dy = 0,0

    if teclas[pygame.K_LEFT]:
       dx =- speed
       directp = "left"
    if teclas[pygame.K_RIGHT]:
       dx = speed
       directp = "right"
    if teclas[pygame.K_UP]:
       dy =- speed
       directp = "up"
    if teclas[pygame.K_DOWN]:
       dy = speed
       directp = "down"         

    cx -= speedc

    personaje = actualizar_spritper(directp)
    cangrejo = actualizar_spritcang(directc)

    if random.randint(1,100) <= 5:
         directc = random.choice(["up","down","left","right"]) 

         if directc == "up":
            cy -= speedc
         if directc == "down":
            cy += speedc
         if directc == "left":
            cx -= speedc
         if directc == "right":
            cx += speedc

    if cx < 0 or cx > ancho - 75 or cy < 0 or cy > alto - 75:
       cx, cy =  random.randint(0, ancho - 75), random.randint(0, alto - 75) 

    """   door_x = 14*casilla
    door_y = 1*casilla
    if x >= door_x and x <= door_x + casilla and y >= door_y and y <= door_y + casilla:
       cambiar_map() """

    x += dx
    y += dy

    dibujar(ventana)
    ventana.blit(personaje,(x,y))
    ventana.blit(cangrejo,(cx,cy))
        

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()

