#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:42:31 2018
@author: mathilde
"""
import numpy as np
import os

#====== VARIABLES INITIALIZATION =====
pb_data=dict()  #Dictionnary that contains number of flights N and gates M
A=list()
A_h=list()
A_m=list()
D=list()
D_h=list()
D_m=list()
P = np.zeros(shape=(25,5), dtype=int)
n=0
s=0

#====== Data File reading ======
while s==0:
    name = input("Quel est le nom du fichier que vous souhaitez utiliser ? \n")
    if os.path.exists(name) is False :
        print("Le fichier n'est pas présent dans le répertoire courant")
        s=0
    else :
        s+=1
    
        
with open(name, 'r') as file:
    allData = file.read()

#====== Data formating ======    
line = allData.split("\n")  #corresponds to each line of the data file


for i in range(len(line)):
    if i==0 or i==1 :
        temp = line[i].split(" ")
        pb_data[temp[0]]= temp[1]
    else:                           #contruction of vectors A, D and matrix P
        temp = line[i].split(" ")
        if len(temp) > 1:
            A.append(temp[1])
            D.append(temp[2])
            for j in range(3, len(temp)-1):
                P[n,int(temp[j])]=1
            n+=1
                
#print(A)
#print(D)
#print(P)


#====== Discrete time ======            
for i in range(len(A)):
    A_split = str(A[i]).split(":")
    D_split = str(D[i]).split(":")
    A_h.append(A_split[0])
    A_m.append(A_split[1])
    D_h.append(D_split[0])
    D_m.append(D_split[1])
    A[i]= int(A_h[i])*12 + int(int(A_m[i])/5) 
    D[i]= int(D_h[i])*12 + int(int(D_m[i])/5) 
#print(A)
#print(D)

#====== Writing data on file GAP ======
with open('GAP_test.dat', 'w') as formated_file:
    for cle, val in pb_data.items():
        formated_file.write(str(cle) + ": " + str(val) + "\n" )
    
    formated_file.write("\n FLIGHTSTIME: [")
    for n in range(len(A)):
        formated_file.write(" (" + str(n+1) + ")  [" + str(A[n]) + " " + str(D[n]) + "] \n")
    formated_file.write("] \n")
    
    formated_file.write("\n GATESALLOWED: [")
    for n in range(P.shape[0]):
        for m in range(P.shape[1]):
            formated_file.write(" (" + str(n+1) + " " + str(m+1) + ") " + str(P[n,m]) + " ")
        formated_file.write("\n")
    formated_file.write("]")