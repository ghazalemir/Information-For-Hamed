# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 08:10:23 2021

@author: ghaza
"""


import numpy as np
from scipy.optimize import minimize
import pandas as pd

#Call artificial Experimental Data
#To test the ability of code for parameter optimization I used a set of artificial data to back calculate the parameters
#This code takes artificial experimental data, walpha,wtetha and passes (for 206 mesh points and 1000 montecarlo iteration)
EXP_read=pd.read_csv('Result.csv')
EXP=EXP_read.values


#Call Pre-Calculated parameters by MonteCarlo simultaion

wtetha_read=pd.read_csv('wtetha.csv')
wtetha=wtetha_read.values


walpha_read=pd.read_csv('walpha.csv')
walpha=walpha_read.values


depthDetector_read=pd.read_csv('depthDetector.csv')
depthDetector=depthDetector_read.values


depthReactor_read=pd.read_csv('depthReactor.csv')
depthReactor=depthReactor_read.values





def EPSCalc(x):
    
    
    mu_d=21.477
    
    shape=np.shape(wtetha)
    
    V_psi=[]
    
    for i in range(0,shape[1]):
        
        psi=0
        
        for j in range(0,shape[0]):
            
            #psi is efficiancy 
            
            psi+=walpha[j][i]*wtetha[j][i]*(1-np.exp(-1*mu_d*depthDetector[j][i]))*np.exp(-1*x[2]*depthReactor[j][i])
        
        psi=psi/shape[0]
        V_psi.append(psi)   
    

    return(V_psi)
    


def optimization(x):
    T=1
    nui=2
    phi=0.4

    

    

    V_count=[]
    EPS=EPSCalc(x)
    
 
    for i in range(0,len(EPS)):
        
        count=(T*nui*x[0]*phi*EPS[i])/(1+(x[1]*nui*x[0]*phi*EPS[i]))
        V_count.append(count)   
        
    
    f=0
    for i in range(0,len(EXP)):
        f=f+((V_count[i]-EXP[i])/(V_count[i]+EXP[i]))**2
    
    
    return f
    
    





def finding_parameters(x0):

    

    res=minimize(optimization,x0,method='nelder-mead',options={'xatol': 1e-8, 'disp': True})
    print(res.x)
  

finding_parameters([3e6,1e-04,5])




"""
x=[2e6,1e-05,10]
Re=EPSCalc(x)

EPS_num=pd.DataFrame(Re)     
EPS_num = EPS_num.copy()
EPS_num.to_csv('Re.csv')
"""





