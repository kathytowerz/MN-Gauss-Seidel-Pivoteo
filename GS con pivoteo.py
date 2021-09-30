# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:18:12 2021

@author: Kathleen Lucía Torres Mancilla 298944
         FRancisco Javier Vite Mimila 299043
         
Gauss Seidel con Pivoteo

De ejemplo vamos a resolver
6x + 7y + 8z = 9   
-x + 4y + 2z = 2
-3x + 7y - 4z = -13  
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
print("SolucioneS: ", GS_NP(A_np, b_np, 100000, 0.00001))

n = len(A[0])
for k in range(n-1):
    s_max = 0
    for i in range(k,n):
        max_row = A[i][0]
        for j in range(k,n):
            if (A[i][j] > max_row):
                max_row = A[i][j]
        div_s = abs(A[i][k]/max_row)
        print("Primer elemento entre s_i = ", div_s)
        if (div_s > s_max):
            s_max = div_s
            row = i
    aux_A = A[k]
    A[k] = A[row]
    A[row] = aux_A
    
    aux_b = b[k]
    b[k] = b[row] 
    b[row] =aux_b

print(A, b)