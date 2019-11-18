# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:30:25 2019

@author: (╯°□°)╯︵ ┻━┻
"""
import pandas as pd
import numpy as np
EFelicdad=pd.read_csv('DFnumericoInvertido.csv' )
seleccion=EFelicdad.iloc[:,29:42]
seleccion['total']=seleccion.sum(axis=1)
vector=[]
p=seleccion.drop(['total'], axis =1).mean(axis=0)
p=p.copy().T
q=1-p
pq=p*q
k=len(EFelicdad.iloc[:,29:42].T)
k2=len(seleccion.T)
sumatoria_pq=pq.sum()
varT=seleccion['total'].var(ddof=0)
result=(k/(k-1))*(1-(sumatoria_pq/varT))
def corrItemTest(matriz1):
    salida=[]
    for x in matriz1.drop(['total'], axis =1):
        b=matriz1['total']
        a=matriz1[x]
        c=np.corrcoef(a,b)[0,1]
        salida.append(c)
    return salida
rCorrItemTest=corrItemTest(seleccion)
def indicecorrelaT(matriz1):
    salida=[]
    for x in matriz1.drop(['total'], axis =1):
        b=matriz1['total']
        a=matriz1[x]
        c=np.corrcoef(a,b-a)[0,1]
        salida.append(c)
    return salida
rIndiceHCorregido=indicecorrelaT(seleccion)
"""vector=[]
for i in seleccion.drop(['total'], axis =1):
    vector.append( seleccion[i][seleccion[i]==1].value_counts()/len(seleccion))
p=pd.DataFrame(vector).T
resul2t=(k/(k-1))*((varT-sumatoria_pq)/varT)
"""