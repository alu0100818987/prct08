#! /usr/bin/python

import ej_PI3
import sys

def error(interv, n_test, umbral):
 contador = 0 
 for i in (0, n_test):
   aprox = ej_PI3.h(interv)
   if (abs(aprox - ej_PI3.PI)> umbral):
     contador = contador + 1
 
 return (contador/float(n_test))*100.0
 
if __name__ == "__main__":
   if (len(sys.argv) != 4):
     interv= int(raw_input('Introduzca el valor intervalo: ')) 
     umbral= float(raw_input('Introduzca el valor umbral: '))
     n_test= int(raw_input('Introduzca el valor del numero de test: '))
     
   else:
     interv= int(sys.argv[1])
     umbral= float(sys.argv[2])
     n_test= int(sys.argv[3])
     
   print error(interv, n_test, umbral) 
    

 
    
    
    
   

