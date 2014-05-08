#!/usr/bin/python
#!encoding: UTF-8

import pylab as dibujo 
import sys
import modulo
import time

argumentos = sys.argv[1:]
if (len(argumentos) == 8):
  n = int (argumentos[0])
  aproximaciones = int (argumentos[1])
  umbral = []
  for i in range (2,7):
    umbral.append(float (argumentos[i]))
  nombre_fichero = argumentos[7]
else:
  print "Introduzca el nº de intervalos (n > 0):"
  n = int (raw_input())
  print "Introduzca el nº de aproximaciones:"
  aproximaciones = int (raw_input())
  print "Introduzca 5 umbrales de error: "
  umbral = []
  for i in range (5):
    print "Introduzca el umbral", i, ":"
    umbral.append (float (raw_input ()))
  l = []
if (n>0):
  for i in range (5):
    start =time.time()
    porcentaje = modulo.error (n, aproximaciones, umbral[i])
    finish = time.time()-start
    l.append (finish)
  x = [1,2,3,4,5]
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
  dibujo.show()
else:
  print "El valor de los intervalos debe ser mayor que 0"
    