# Programa Editado de Franco Benassi
# Proyecto #2 Sistemas Inteligentes 2020
# Ejercicio 3 
import pygame, time, random as RA, serial
import pygame, serial, threading
from pygame.locals import *
import telegram as tele

#---------------------------------------------------------------------
# Carga los elementos del bot de Telegram
#---------------------------------------------------------------------

bot_TOKEN = '1204484946:AAGsbOBJFR0-HCHrghIJGMafP9TvZybQt84'
chat_ID = 883005873
bot = tele.Bot(token=bot_TOKEN)

#---------------------------------------------------------------------
# Carga imagenes y convierte formato pygame
#---------------------------------------------------------------------
def Load_Image(sFile,transp=False):
    try: image = pygame.image.load(sFile)
    except pygame.error:
           raise SystemExit
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image

#---------------------------------------------------------------------
# Pinta las Temperaturas a Pantalla
#---------------------------------------------------------------------
def Pinta_Data():
    sc.blit(Img,(0,0))
    nDX = 15; nDY = 39 ; nX = 0 ; nRGB = (0,0,0)
    for nT in aT:
     if nT < 10: nRGB = (0,0,255)
     if nT >= 10 and nT <= 25: nRGB = (0,255,0)
     if nT > 25: nRGB = (255,0,0)
     pygame.draw.line(sc,nRGB,(nX+nDX,nDY*4),(nX+nDX,(nDY-nT)*4),10)
     nX = nX + 12
    for nX in range(0,29):
     aT[nX] = aT[nX+1]
    return

#---------------------------------------------------------------------
# Imprime Cabezara del Archivo.-
#---------------------------------------------------------------------
def nFh_Head():
 nFh.write(' Data Logger de Temperaturas ' + '\n' )
 nFh.write('-----------------------------' + '\n' )
 nFh.write('Fecha: 06-04-2011'             + '\n' )
 nFh.write('Temperaturas.................' + '\n' )
 nFh.write('-----------------------------' + '\n' )
 return

 #---------------------------------------------------------------------
# Envio de Imagen a Telegram
#---------------------------------------------------------------------
def EnviandoImagen():
    threading.Timer(10.0, EnviandoImagen).start()
    # Tomar pantallazo de la ventana de pygame
    pygame.image.save(sc, "/home/franco-os/Documentos/Mis Programas Git/pantallazo.png")
    img = open("/home/franco-os/Documentos/Mis Programas Git/pantallazo.png", 'rb')
    bot.sendPhoto(chat_id=chat_ID, photo=img)
    print("Enviando a Telegram..")

#---------------------------------------------------------------------
# Main.-
#---------------------------------------------------------------------
s = serial.Serial('/dev/pts/2')
s.baudrate = 2400
nRes = (475,165)
nFh = open('tempe.txt','w')
aT = [ 0 for i in range(30) ] # 30 Samples.-
pygame.init()
sc = pygame.display.set_mode(nRes)
Img = Load_Image('/home/franco-os/Imágenes/base.jpg')
nFh_Head()
Done = True
while Done:
 Data = RA.randint(3,31)
 aT[29] = Data
 if Data > 28: pygame.image.save(sc,'/home/franco-os/Imágenes/warning.png')
 ev = pygame.event.get()
 for e in ev:
  if e.type == QUIT: Done = False
 Pinta_Data()
 nFh.write(str(Data) + '\n' )
 pygame.display.flip()
 EnviandoImagen()
 time.sleep(0.500)
nFh.write('---------[EOF]---------' + '\n' )
s.close()
nFh.close()