# Programa de Franco Benassi
# Proyecto #3 Interfaces Graficas 2020
# Ejercicio 2
import pygame
from pygame.locals import *
import sys
from PIL import Image as Img

def RotaImagen(fig,nombre):
    fig = Img.open(fig).resize((116,116))
    fig.save(nombre+".png")

RotaImagen("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 3/f1.jpg","f1_py")
RotaImagen("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 3/f2.jpg","f2_py")
RotaImagen("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 3/f3.jpg","f3_py")
RotaImagen("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 3/f4.jpg","f4_py")


pygame.init()
screen = pygame.display.set_mode((759,185))
fig_1 = pygame.image.load("f1_py.png").convert_alpha()
fig_2 = pygame.image.load("f2_py.png").convert_alpha()
fig_3 = pygame.image.load("f3_py.png").convert_alpha()
fig_4 = pygame.image.load("f4_py.png").convert_alpha()
fondo = pygame.image.load("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 3/plantilla.png") 
rotar_1 = pygame.transform.rotate(fig_1,80)
rotar_2 = pygame.transform.rotate(fig_2,100)
rotar_3 = pygame.transform.rotate(fig_3,50)
rotar_4 = pygame.transform.rotate(fig_4,112)
screen.blit(fondo,(0,0))
screen.blit(rotar_1,(10,20))
screen.blit(rotar_2,(204,18))
screen.blit(rotar_3,(380,12))
screen.blit(rotar_4,(600,13))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()