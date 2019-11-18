# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:44:08 2019

@author: (╯°□°)╯︵ ┻━┻
"""
import pandas as pd
import numpy as np

EFelicidad = pd.read_csv('DFnumericoInvertido.csv').drop(['Edad:','Género:','Semestre:',
                                  'Estrato económico:','Estado civil:','Trabaja:',
                                  '¿El nivel de sus ingresos con respecto a sus gastos mensuales son?',
                                  'Promedio académico:','Es creyente','¿Quién costea sus estudios?',
                                  'Tiempo promedio diario de uso del celular:',
                                  '¿En que tipo de casa vive?','clase','Tiempo de traslado'], axis=1)
matrizCovarianza12=np.cov(EFelicidad.T)
def calcualrVarPorPregunta(matriz):
    #funcion que calcula la varianza de elemento por elemento
    vector = []
    for i in range(len(matriz.T)):
        vector.append(np.var(matriz[:,i:i+1]))
    vectorNP=np.array(vector)    
    return np.array(vector),vectorNP.sum()
#funcion de carianza total
def calcularVarTotal(matriz):
    #funcion que calcula la varianza tota
    vector = []
    for i in range(len(matriz)):
        vector.append(np.sum(matriz[i:i+1,:]))
    vectorNP=np.array(vector)    
    return np.array(vector),np.var(vectorNP)
k=len(EFelicidad.T)
def alfaCronbach(matriz1,sumVPP,varTotal):
    k=len(matriz1.T)
    alfacrombach=(k/(k-1))*(1-(sumVPP/varTotal))
    return alfacrombach
def matrizCronbacsi(matriz):
    vector=[]
    for i in range(len(matriz.T)):
        matrizSin=np.delete(matriz,[i], axis=1)
        y,sumVarPorPRegunta=calcualrVarPorPregunta(matrizSin)
        yy,VarT=calcularVarTotal(matrizSin)
        #esto es la formula de alfa cronbach
        k=len(matrizSin.T)
        alfaCrombach=(k/(k-1))*(1-(sumVarPorPRegunta/VarT))
        #va guardadno cada dato de elemento
        vector.append(alfaCrombach)
    return np.array(vector)
#indice de homogeneidad
def corrItemTest(matriz1,totalpersoa):
    salida=[]
    for x in range(len(matriz1.T)):
        b=totalpersoa
        a=matriz1[:,x:x+1].reshape(len(matriz1),)
        c=np.corrcoef(a,b)[0,1]
        salida.append(c)
    return np.array(salida)
####mejorar crombacha########################################################################
def indicecorrelaT(matriz1,totalpersoa):
    salida=[]
    
    for x in range(len(matriz1.T)):
        b=totalpersoa
        a=matriz1[:,x:x+1].reshape(len(matriz1),)
        c=np.corrcoef(a,b-a)[0,1]
        salida.append(c)
    return np.array(salida)
EFelicidad = pd.read_csv('DFnumericoInvertido.csv').drop(['Edad:','Género:','Semestre:',
                          'Estrato económico:','Estado civil:','Trabaja:',
                          '¿El nivel de sus ingresos con respecto a sus gastos mensuales son?',
                          'Promedio académico:','Es creyente','¿Quién costea sus estudios?',
                          'Tiempo promedio diario de uso del celular:',
                          '¿En que tipo de casa vive?','clase','Tiempo de traslado'], axis=1)
matrizEFelicidad=EFelicidad.to_numpy().copy()
totalporpersona,VarT=calcularVarTotal(matrizEFelicidad)
indicehomogeneidad=corrItemTest(matrizEFelicidad,totalporpersona) 
indicedeCorrelacionT=indicecorrelaT(matrizEFelicidad,totalporpersona)
matrizCorrealcioEFCorregida=np.corrcoef(matrizEFelicidad)
varPorElementoMatrizMejorada,sumVarPorPRegunta=calcualrVarPorPregunta(matrizEFelicidad)
totalporpersona_matrizMEjorVarTMatrizMejo,VarTMAtrizmejorada=calcularVarTotal(matrizEFelicidad)
alfa=alfaCronbach(matrizEFelicidad,sumVarPorPRegunta,VarTMAtrizmejorada)
siSeRetiraUnElemento=matrizCronbacsi(matrizEFelicidad);  