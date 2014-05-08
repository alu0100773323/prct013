#!/usr/bin/python
#!encoding: UTF-8
import sys
import math

PI35 = 3.1415926535897931159979634685441852 #se declara como variable global

#Función
def calcular_pi (n):
  PI35 = 3.1415926535897931159979634685441852
  ini = 0
  intervalos = 1.0 / float (n)
  sumatorio = 0.0
  for i in range(n):
    #x_i = calcular_xi (n, i+1)
    x_i = ((i+1) - 1.0/2.0) / n
    fx_i = 4.0 / (1.0 + x_i * x_i)
    ini += intervalos
    sumatorio += fx_i
  valor_pi = sumatorio / n
  return (valor_pi)

  
#Función
def error (n, aproximaciones, umbral):
  intervalo = n
  lista = []
  for i in range (aproximaciones):
    valor = calcular_pi (intervalo)
    lista.append (valor)
    intervalo += n
  pi35 = []
  for i in range (aproximaciones):
    pi35.append (PI35)
  diferencia = []
  for i in range (aproximaciones):
    dif = abs (PI35 - lista[i])
    diferencia.append (dif)
  correcto = 0
  for i in range (aproximaciones):
    if (diferencia[i] <= umbral):
      correcto = correcto + 1
  porcentaje = 100.0 * (1.0 - (float(correcto) / float(aproximaciones)))
  return (porcentaje)
      
#Programa principal
if (__name__ == "__main__"):
  argumentos = sys.argv[1:] #[1:] que empiece a visualizar desde la posición 1 hasta el final
  if (len(argumentos) == 3):
    n = int (argumentos[0])
    aproximaciones = int (argumentos[1])
  else:
    print "Introduzca el nº de intervalos (n>0):"
    n = int (raw_input())
    print "Introduzca el nº de aproximaciones:"
    aproximaciones = int (raw_input())
    print"Introduzca el umbral de error:"
    umbral = float (raw_input())
  if (n>0):
    porcentaje = error (n, aproximaciones, umbral)
    print "El porcentaje de fallos es del ", porcentaje
  else:
    print "El valor de los intervalos debe ser mayor de 0"