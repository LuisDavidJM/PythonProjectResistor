from turtle import *
import math

def res():
 listacolores=[A,B,C]

 adigitoval1=str(listacolores[0])
 adigitoval2=str(listacolores[1])
 
 if C==3:
  rest=int(adigitoval1+adigitoval2)
  resu=str(rest)+str(" K")+str("ohm")
 elif C==6:
  rest=int(adigitoval1+adigitoval2)
  resu=str(rest)+str(" M")+str("ohm")
 elif C==9:
  rest=int(adigitoval1+adigitoval2)
  resu=str(rest)+str(" G")+str("ohm")
 else:
  exp=10**listacolores[2]
  rest=int(adigitoval1+adigitoval2)*exp
  resu=str(rest)+str(" ohm")
 
 print(resu)
 t.goto(0,-150)
 t.color("black")
 t.begin_fill()
 t.write(resu,True,"center",("Arial",32,"bold"))
 t.end_fill()

col=['negro','cafe','rojo','naranja','amarillo','verde','azul','morado','gris','blanco']

for i in range(3):
 
 X=input("Dame el primer color: ")
 x=X.lower()
 if(x not in col):
  print("Caracter no valido")
 if(x in col):
  break
  
for i in range(3):
 
 Y=input("Dame el segundo color: ")
 y=Y.lower()
 if(y not in col):
  print("Caracter no valido")
 if(y in col):
  break
  
for i in range(3):
 
 Z=input("Dame el tercer color: ")
 z=Z.lower()
 if(z not in col):
  print("Caracter no valido")
 if(z in col):
  break
datos=[]
with open('res.txt','r') as archivo:
 lineas=archivo.read().splitlines()
 for l in lineas:
  linea=l.split(' ')
  datos.append([(linea[0]),(linea[2]),int(linea[1])]) 
    
if x=='negro':
 x=datos[0][1]
 A=datos[0][2]
if x=='cafe':
 x=datos[1][1]
 A=datos[1][2]
if x=='rojo':
 x=datos[2][1]
 A=datos[2][2]
if x=='naranja':
 x=datos[3][1]
 A=datos[3][2]
if x=='amarillo':
 x=datos[4][1]
 A=datos[4][2]
if x=='verde':
 x=datos[5][1]
 A=datos[5][2]
if x=='azul':
 x=datos[6][1]
 A=datos[6][2]
if x=='morado':
 x=datos[7][1]
 A=datos[7][2]
if x=='gris':
 x=datos[8][1]
 A=datos[8][2]
if x=='blanco':
 x=datos[9][1]
 A=datos[9][2]

if y=='negro':
 y=datos[0][1]
 B=datos[0][2]
if y=='cafe':
 y=datos[1][1]
 B=datos[1][2]
if y=='rojo':
 y=datos[2][1]
 B=datos[2][2]
if y=='naranja':
 y=datos[3][1]
 B=datos[3][2]
if y=='amarillo':
 y=datos[4][1]
 B=datos[4][2]
if y=='verde':
 y=datos[5][1]
 B=datos[5][2]
if y=='azul':
 y=datos[6][1]
 B=datos[6][2]
if y=='morado':
 y=datos[7][1]
 B=datos[7][2]
if y=='gris':
 y=datos[8][1]
 B=datos[8][2]
if y=='blanco':
 y=datos[9][1]
 B=datos[9][2]

if z=='negro':
 z=datos[0][1]
 C=datos[0][2]
if z=='cafe':
 z=datos[1][1]
 C=datos[1][2]
if z=='rojo':
 z=datos[2][1]
 C=datos[2][2]
if z=='naranja':
 z=datos[3][1]
 C=datos[3][2]
if z=='amarillo':
 z=datos[4][1]
 C=datos[4][2]
if z=='verde':
 z=datos[5][1]
 C=datos[5][2]
if z=='azul':
 z=datos[6][1]
 C=datos[6][2]
if z=='morado':
 z=datos[7][1]
 C=datos[7][2]
if z=='gris':
 z=datos[8][1]
 C=datos[8][2]
if z=='blanco':
 z=datos[9][1]
 C=datos[9][2]
 
t=Turtle()
a=Turtle()
screen=t.getscreen()
setup(800,700,0,0)
screensize(800,700)

colormode(255)
t.penup()
a.penup()
t.goto(300,0)
a.goto(-300,0)
t.rt(180)
t.pendown()
a.pendown()
t.pensize(4)
a.pensize(4)
s=1
t.color("gray")
a.color("gray")
for i in range(16):
 t.fd(s)
 a.fd(s)
 s=s+1
t.color("brown")
a.color("brown") 
t.pensize(1)
a.pensize(1)
t.rt(90)
a.rt(90)
colormode(255)
s=0
t.speed(0)
a.speed(0)
t.fillcolor(210,105,30)
a.fillcolor(210,105,30)
t.begin_fill()
a.begin_fill()
for i in range(17):
 t.circle(50,s)
 a.circle(50,s)
 s=s+1
s=0
t.rt(46)
a.rt(46)
for i in range(18):
 t.fd(s)
 a.fd(s)
 s=s+1
t.fd(3)
a.fd(3)
t.rt(46)
a.rt(46)
s=0
for i in range(17):
 t.circle(50,s)
 a.circle(50,s)
 s=s+1
t.end_fill()
a.end_fill()
t.penup()
a.penup()
t.goto(-78,34)
a.goto(70,-34)
t.lt(90)
a.lt(90)
t.pendown()
a.pendown()
s=0
t.pencolor(x)
a.pencolor(z)
t.fillcolor(x)
a.fillcolor(z)
t.begin_fill()
a.begin_fill()
for i in range(8):
 t.fd(s)
 a.fd(s)
 s=s+1
t.rt(90)
a.rt(90)
s=0
for i in range(12):
 t.fd(s)
 a.fd(s)
 s=s+1
t.fd(2)
a.fd(2) 
t.rt(90)
a.rt(90)
s=0
for i in range(8):
 t.fd(s)
 a.fd(s)
 s=s+1
t.rt(90)
a.rt(90)
s=0
for i in range(12):
 t.fd(s)
 a.fd(s)
 s=s+1
t.fd(2)
a.fd(2)
t.end_fill()
a.end_fill()
t.rt(90)
t.penup()
a.penup()
a.goto(103,-49)
t.fd(60)
a.lt(90)
t.pendown()
a.pendown()
s=0
S=-0.8
t.pencolor(y)
a.pencolor(188,140,40)
t.fillcolor(y)
a.fillcolor(188,140,40)
t.begin_fill()
a.begin_fill()
for i in range(8):
 t.fd(s)
 a.fd(S)
 s=s+1
 S=S+1
t.rt(90)
a.lt(90)
s=0
S=2.7
for i in range(12):
 t.fd(s)
 a.fd(S)
 s=s+1
 S=S+1
t.fd(2) 
t.rt(90)
a.lt(90)
s=0
S=-0.8
for i in range(8):
 t.fd(s)
 a.fd(S)
 s=s+1
 S=S+1
t.rt(90)
a.lt(90)
s=0
S=2.7
for i in range(12):
 t.fd(s)
 a.fd(S)
 s=s+1
 S=S+1
t.fd(2)
t.end_fill()
a.end_fill()
t.penup()
a.penup()

res()
t.lt(90)
a.lt(90)
t.color("gray")
a.color("gray")
t.goto(-300,0)
a.goto(300,0)

screen.exitonclick()