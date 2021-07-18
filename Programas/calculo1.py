import math
import numpy as np
import matplotlib.pyplot as plt


# Ejercicio 1

print("Sean los puntos P1, P2 y P3 formados por los digitos de un RUT")
Rut = input("Ingrese un RUT sin puntos ni guion: ")


while not Rut.isdigit() or len(Rut) != 9:
    print("por favor ingrese un formato correcto")
    Rut = input("Ingrese un RUT sin puntos ni guion: " +'\n')

Lista = []
for numero in Rut:
    Lista.append(int(numero))

#digitos-----
d1=Lista[0]#x
d2=Lista[1]#y
d3=Lista[2]#x
d4=Lista[3]#y
d5=Lista[4]#x
d6=Lista[5]#y

#Puntos------
P1=(d1,d2)
P2=(d3,d4)
P3=(d5,d6)

#Pendiente---
m= 0
if(d3 == d1):
    m= 0
else:
    m= (d4-d2)/(d3-d1)

#------------

# Punto Circunferencia
d7 = d1 + d5
d8 = d2 + d6
P4 = (d7, d8)
# Centro------------
P5 = (d3, d4)
#-------------------

def EcuacionRecta(x):
    y = (m * (x - d1)) + d2
    return y

#Formula distancia punto a recta
distancia =abs((-m*d5)+(d6)+((m*d1)+d2))/math.sqrt((m**2)+1)

#numpy------
def grafica_recta():
    x= np.linspace(-10,10,2)
    plt.plot(x, EcuacionRecta(x))
    plt.plot(P3[0],P3[1],marker="o")

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.title("Recta P1,P2 y distancia P3")
    plt.grid()
    plt.show()

def mostrar_resultados():
    print()
    print('Ejercicio N°1: '+'\n')
    print("a) La ecuación de la recta que pasa por P1 y P2 es: ")
    print("La ecuación punto pendiente de la recta es : y - ", d2," = ", m, "*(x - ", d1,")")
    print("por lo tanto la forma principal: y"," = ",m,"*x + ", (m * d1) + d2)
    print("y la ecuación forma general es : - ", m,"* x + y +", (m*d1)+d2," = 0" +'\n')
    print("b) Calcule la distancia desde la recta encontrada en a) al punto P")
    print("La distancia del punto a la recta es: ",distancia)
    print("El centro de la Ecuaci贸n Can贸nica de la Circunferencia es:", P5)
    grafica_recta()
    print()
    print('Ejercicio N°2: '+'\n')
    centro = solicitarCentro()
    radio = solicitarRadio()
    Circ(centro,radio)
    print()
    print("Ejercicio N°3: ")
    foco()
    directriz()
    ladorecto_parabola()
    eje_simetria()
    grafica_Parabola()





# Ejercicio 2
#centro----P2(d3,d4)(h,k)
#Punto P1(d1+d5 , d2+d6)
X=d1+d5 #coordenada x de P1
Y=d2+d6 #coordenada Y de P1
rad = ((X-d3)**2)+((Y-d4)**2)# Ya esta al cuadrado
D = -(2*d2)
E = -(2*d3)
F = (d2**2)+(d3**2)-rad


#CLASE PARA GESTIONAR PUNTOS
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#SOLICITAR CENTRO DE LA CIRCUNFERENCIA
def solicitarCentro():
    while True:
        cx = P5[0]
        cy = P5[1]
        try:     
            centro = Punto(float(cx),float(cy))
            return centro
        except:
            print ('valor incorrecto')
            
#SOLICITAR RADIO DE LA CIRCUNFERENCIA      
def solicitarRadio():
    while True:
        r = rad
        try:
            radio = float(r)
            return radio
        except:
            print ('valor incorrecto')   

#CALCULAR LA ECUACIÓN DE UNA CIRCUNFERENCIA DADO EL CENTRO Y EL RADIO Y GRAFICARLA            
def Circ(centro,radio):
    xmin = -radio+centro.x
    xmax = radio+centro.x
    x = np.linspace(xmin,xmax,100)   
    y1 = np.sqrt(radio**2-(x-centro.x)**2)+centro.y
    y2 = -np.sqrt(radio**2-(x-centro.x)**2)+centro.y
    exp2 = chr(0x00B2)
    ecOrd = print("La ecuación ordinaria es: (x - "+str(centro.x)+")"+exp2
                  +" + (y - "+str(centro.y)+")"+exp2+" = "+str(radio)+exp2)
    D = -2*centro.x
    E = -2*centro.y
    F = centro.x**2+centro.y**2-radio**2
    ecGral = print("La ecuación general es: x"+exp2+" + y"+exp2+" + "+str(D)
                   +"x + "+str(E)+"y + "+str(F)+" = 0")
    plt.plot(x,y1, color = "k")
    plt.plot(x,y2, color = "k")
    plt.plot(centro.x,centro.y, color = "red", marker = "o")
    plt.axvline(0, color="k", lw=1)
    plt.axhline(0, color="k", lw=1)
    plt.grid()
    plt.title('Grafica de la circunferencia')
    plt.gca().set_aspect('equal')
    plt.show()
    return ecOrd, ecGral


# Ejercicio 3
#centro----P2(d3,d4)
vertice = P2
P = d1 + d2 + d3

def Canonica_Parabola(x,y):
    ec = (y-P2[1])**2 == 4*P(x-P2[0])
    return ec


def Ecuacion_Parabola(X1):
    y = ((X1**2)-(2*(X1*d3)) + (d3**2) + (4*(P*d4)))/4*P
    return y

def foco():
    foco = (P2[0],P2[1]+P)
    print("El foco de la parábola se ubica en el punto: " ,foco)
    return foco

def ladorecto_parabola():
    LLR = abs(4*P)
    print("El valor del lado recto de la parábola es: ",LLR)
    return LLR

def directriz():
    k = P2[1]
    directriz = k - P
    print("La directriz de la parábola es: ", directriz)  
    return directriz

def eje_simetria():
    eje_simetria = P2[0]
    print("El eje de simetria de la parábola es: ",eje_simetria)
    return eje_simetria

def grafica_Parabola():
    x= np.linspace(-50,50,100)
    plt.plot(x, Ecuacion_Parabola(x), color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.title("Parabola")
    plt.grid()
    plt.show()

mostrar_resultados()