#!/usr/bin/python
#!encoding: UTF-8

import pylab as dibujo 


x = [1,2,3,4,5]
l = []
y1 = [0.18,0,0.53,0,5.46]
y2 = [12.50,0,4.17,4.17,0]
y3 = [11.11,44.44,11.11,22.22,55.56]
y4 = [30,10,0,30,20]
y5 = [3.33,100,20,100,20]


p1 = dibujo.subplot(211)

dibujo.plot (x, y1, marker='o', linestyle=':',color='r', label='Linea1') 
dibujo.plot (x, y2, marker='*', linestyle='--',color='b', label='Linea2')
dibujo.plot (x, y3, marker='s', linestyle='-',color='m', label='Linea3')
dibujo.plot (x, y4, marker='p', linestyle='-.',color='y', label='Linea4')
dibujo.plot (x, y5, marker='^', linestyle='-',color='g', label='Linea5')

dibujo.title ('Prcentaje de fallos')
dibujo.legend()
dibujo.xlim(0, 6)
dibujo.xticks(x)

p2 = dibujo.subplot(212)

dibujo.plot (x, l, marker='o', linestyle=':',color='r', label='Linea1')

dibujo.xlabel ('Intervalo')
dibujo.ylabel ('Tiempo en segundos')
dibujo.legend()

dibujo.show()