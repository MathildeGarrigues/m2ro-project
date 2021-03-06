#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:42:31 2018
@author: mathilde
"""
import numpy as np
import os

# This file takes as an input the filename(.txt) to convert to (.dat)
#====== VARIABLES INITIALIZATION =====
pb_data=dict()  #Dictionnary that contains number of flights N and gates M
A=list()
A_h=list()
A_m=list()
D=list()
D_h=list()
D_m=list()
L0 = 0
LNP1 = 0
P = np.zeros(shape=(25,5), dtype=int) # change shape of P according to N and M
n=0
s=0

#====== Data File reading ======

filename = 'GAP5_25'  
        
with open(filename+'.txt', 'r') as file:
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


#====== Discrete time computation ======            
for i in range(len(A)):
    A_split = str(A[i]).split(":")
    D_split = str(D[i]).split(":")
    A_h.append(A_split[0])
    A_m.append(A_split[1])
    D_h.append(D_split[0])
    D_m.append(D_split[1])
    A[i]= int(A_h[i])*12 + int(int(A_m[i])/5) 
    D[i]= int(D_h[i])*12 + int(int(D_m[i])/5) 

L0 = int(A_h[0])*12
LNP1 = (int(D_h[len(D)-1])+1) *12
#print(A)
#print(D)

#====== Writing data on file GAP ======
with open(filename+'.dat', 'w') as formated_file:

    # n (flights) , m (gates) lines
    
    formated_file.write("n : " + pb_data.get('Flights') + "\n" )
    formated_file.write("m : " + pb_data.get('Gates') + "\n" )

    # L0 and LNP1 lines
    formated_file.write("L0 : " + str(L0) + "\n" )
    formated_file.write("LNP1 : " + str(LNP1) + "\n" )	    

    # A vector line
    formated_file.write("\n A : [")
    for n in range(len(A)):
        formated_file.write(" (" + str(n+1) + ") " + str(A[n]) + "\n")
    formated_file.write("] \n")

    # D vector line
    formated_file.write("\n D : [")
    for n in range(len(D)):
        formated_file.write(" (" + str(n+1) + ") " + str(D[n]) + "\n")
    formated_file.write("] \n")
    
    # P vector line
    formated_file.write("\n P : [")
    for n in range(P.shape[0]):
        for m in range(P.shape[1]):
            formated_file.write(" (" + str(n+1) + " " + str(m+1) + ") " + str(P[n,m]) + " ")
        formated_file.write("\n")

    formated_file.write("]")
