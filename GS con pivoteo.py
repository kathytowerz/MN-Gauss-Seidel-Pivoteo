# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:18:12 2021

@author: Kathleen Lucía Torres Mancilla 298944
         Francisco Javier Vite Mimila 299043
         
Gauss Seidel con Pivoteo

De ejemplo vamos a resolver
6x + 7y + 8z = 9   
-x + 4y + 2z = 2
-3x + 7y - 4z = -13  
X
6 7 8 = 9
-1 4 2 = 2
-3 7 -4 = -13
Y
Nota: cambiamos el orden de las ecuaciones para que se vea el funcionamiento del pivoteo.
"""


#Librerías utilizadas:
import numpy as np
import sys

#Para leer datos del archivo:
def read_inputs(text_basis):
#Hace un corte en "=" para dividirlo en dos matrices: 
#A (incógnitas) y b (constantes).
    a_temp, b_temp = text_basis.strip().split("=")
    b_temp = eval(b_temp.strip(" "))
    a_temp = a_temp[:-1]
    #Para quitar espacios del final:
    a_temp = [eval(i) for i in a_temp.split()]

    return a_temp, b_temp

def read_file(path):
    A= []
    b= []
    with open(path,"r") as f:
        flag=0
        for line in f:
#Para que empiece a considerar los valores a partir de la X en el archivo:
            if line.strip() != "X":
                pass
            else:
                flag=1
                continue
            #Para terminar la lectura del archivo en "Y":
            if line.strip() == "Y":
                flag=0
                break
            if flag==1:
                aux_1, aux_2 = read_inputs(line)
                A.append(aux_1)
                b.append(aux_2)
    return A, b

#Para guardarlos en el código:
ruta = "C:/Users/Kathy/OneDrive/Documentos/Métodos numéricos/ecGS.txt"
A, b = read_file(ruta)
#Para imprimir las matrices:
print("A = ",A)
print("b = ",b)

def matriz_cuadrada(M):
    if len(M) != len(M[0]):
        print("La matriz no es cuadrada.")
        #Esto es para que se salga del programa si la matriz no es cuadrada:
        sys.exit
    else:
        print("La matriz es cuadrada.")

matriz_cuadrada(A)
#Se definen los elementos como numpy del archivo de texto:
A_np = np.array(A)

b_np = np.array(b)

def pivoteo_filas(M, v):
#Pivoteo parcial por filas. Variables para indicar el tamaño de la matriz:
    t = np.shape(M)
    n = t[0]
    for i in range(0,n-1,1):
        colM = abs(M[i:,i])
        #Valor máximo por fila recorriendo columnas:
        maxM = np.argmax(colM)
#Método de la burbuja para intercambiar filas de mayor a menor: 
#Se hace el cambio con base en el máximo de cada fila.
        if(maxM != 0):
            aux = np.copy(M[i,:])
            M[i,:] = M[maxM+i,:]
            M[maxM+i,:] = aux
            print("A =", M)
            auxv = np.copy(v[i])
            v[i] = v[maxM+i]
            v[maxM+i] = auxv
            print("b =", v)
        return M, v
print("Matriz después del pivoteo: ")    
pivoteo_filas(A_np, b_np)  
    
def GS_NP(M_np, v_np, itmax, umb):
    #Auxiliares en el cálculo:
    x_np = np.zeros(len(M_np)) 
    aux_np = np.ones(len(M_np))

    for ite in range(itmax):
        for i in range(len(M_np)):
            aux_np[i] = 0.0
            x_np[i] = (v_np[i] - np.sum(x_np*aux_np*M_np[i,:]))/M_np[i][i]
            aux_np[i] = 1.0
            
        current_v = np.dot(M_np,x_np)
        error_np = np.sum(np.abs(current_v-v_np))
        
        if error_np < umb:
            #print(x_np)
            return x_np
        
#Para imprimir valores:
print("Soluciones: ", GS_NP(A_np, b_np, 100000, 0.00001))
