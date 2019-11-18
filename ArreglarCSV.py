# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:02:28 2019

@author: (╯°□°)╯︵ ┻━┻
"""
import pandas as pd
import numpy as np
EFelicidad = pd.read_excel('Final_Felicidad_Dicotomizadas(7_11_2019).xlsx',
                       sheet_name='112 Muestras original').drop(['Marca temporal',
                                'Dirección de correo electrónico'],axis=1)
EFelicidad=EFelicidad.replace(["Totalmente en desacuerdo", "Algo en desacuerdo",
                               "Ni en acuerdo ni desacuerdo", "Algo de acuerdo",
                               "Totalmente de acuerdo"],
                                [1, 2, 3, 4, 5])
def invertirColumnas(matriz):
    matrizEfelicidadPD=pd.DataFrame(matriz).copy()    
    for i in range(len(matriz)):
        if i==0 or i==4   or i==5  or i==9  or i==12  or i==13  or i==18  or i==22 or i==23 or i==26 or i==27 or i==28 :
        #if corre[i]<0:
            matrizEfelicidadPD.loc[matrizEfelicidadPD[i] == 1, i] = -5
            matrizEfelicidadPD.loc[matrizEfelicidadPD[i] == 2, i] = -4
            matrizEfelicidadPD.loc[matrizEfelicidadPD[i] == 4, i] = 2
            matrizEfelicidadPD.loc[matrizEfelicidadPD[i] == 5, i] = 1
    matrizEfelicidadPD=abs(matrizEfelicidadPD)    
    return matrizEfelicidadPD.to_numpy()
 
def generarClase(vector,med):    
    salida=[]
    for  x in vector:       
        if (x < med):
            salida.append(0)
        else:
            salida.append(1)   
    return salida

    


EFelicidad=EFelicidad.replace(['20 o menos','más de 20'],[0,1])
EFelicidad=EFelicidad.replace(['Hombre','Mujer'],[0,1])
EFelicidad=EFelicidad.replace(['1 a 5','6 a 10'],[0,1])
EFelicidad=EFelicidad.replace(['1 y 2','3 o más'],[0,1])
EFelicidad=EFelicidad.replace(['Soltero','Otro'],[0,1])
EFelicidad=EFelicidad.replace(['Si','No'],[1,0])
EFelicidad=EFelicidad.replace(['Bajo','Suficiente'],[0,1])
EFelicidad=EFelicidad.replace(['Inferior o igual a 3.5','Superior a 3.5'],[0,1])
EFelicidad=EFelicidad.replace(['No','Si','SI'],[0,1,0])
EFelicidad=EFelicidad.replace(['Familiar u otro','Usted mismo'],[0,1])
EFelicidad=EFelicidad.replace(['Propia','Arriendo'],[0,1])
EFelicidad=EFelicidad.replace(['0 - 120 min','Mayor de 120 min'],[0,1])
EFelicidad=EFelicidad.replace(['0 - 60 min','más de 60 min'],[0,1])
EFelicidadCSV=EFelicidad.to_numpy()
creaTablaNumericarCSV=invertirColumnas(EFelicidadCSV)
EFelicidadcsv=creaTablaNumericarCSV
EFelicidadcsv2=EFelicidadcsv[:,0:29]
sumaMuestras=EFelicidadcsv2.sum(axis=1)/29
media=sumaMuestras.mean()
claseGenerada=np.array(generarClase(sumaMuestras.copy(),media))
crearCSV=pd.DataFrame(creaTablaNumericarCSV,columns=EFelicidad.columns)
crearCSV['clase']=claseGenerada.reshape(len(claseGenerada),1)
#np.hstack((EFelicidadcsv,claseGenerada.reshape(len(claseGenerada),1)))
#lo anterior agrega una columan en numpy
#'tablaCon29REguntasInvertidas.csv', mode='a', index=False, header=False,sep=';',decimal=','
crearCSV.to_csv('DFnumericoInvertido.csv', index=False, sep=',')


