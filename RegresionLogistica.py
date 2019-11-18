# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:26:03 2019

@author: (╯°□°)╯︵ ┻━┻
"""
import pandas as pd
import numpy as np
EFelicdad=pd.read_csv('DFnumericoInvertido.csv' )
Col=pd.DataFrame(EFelicdad.columns)
x=EFelicdad.iloc[:,29:42]
y=EFelicdad.iloc[:,42: 43]
import statsmodels.api as sm
modelo_logistico=sm.Logit(y,x)
#metodos del fit newton, cg posible es minimize
resultado=modelo_logistico.fit()
X=np.squeeze(np.asarray(EFelicdad.iloc[:,29:41]))
Y=np.squeeze(np.asarray(EFelicdad.iloc[:,41: 42]))
print(resultado)
result=resultado.summary()
print(result)
result=resultado.summary2()
print(result)
from sklearn.linear_model import LogisticRegression
modelo_logisticoSk=LogisticRegression()
modelo_logisyco_fit=modelo_logisticoSk.fit(x,y)
modelo_logisyco_score=modelo_logisticoSk.score(x,y)

