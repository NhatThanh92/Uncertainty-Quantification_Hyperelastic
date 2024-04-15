# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 00:28:00 2022

@author: thanh
"""
from abaqus import *
from abaqusConstants import *
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import random
from array import *
from odbAccess import openOdb
import odbAccess
import math
import numpy    as np
import os        
import shutil    

Limit = 10000
somefloats1 = []
C10_txt = np.loadtxt("C10.txt")
C10_list= []
C10_list= C10_txt[:]

C01_txt = np.loadtxt("C01.txt")
C01_list= []
C01_list= C01_txt[:]

D1_txt = np.loadtxt("D1.txt")
D1_list= []
D1_list= D1_txt[:]


    # create Material-uterus
for ic in range(1,Limit,1):
    myString="Job-"+str(ic)
    myString_result = "GNA"
    p = mdb.models['GNA'].parts['baby_lateral_position']
    mdb.models['GNA'].materials['Material-uterus'].hyperelastic.setValues(table=((C10_list[ic], C01_list[ic], D1_list[ic]), )) 
       
    # create job
    
    myJob = mdb.Job(name=myString, model='GNA', description='', type=ANALYSIS,atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1,numGPUs=0)
    myJob.submit()
    myJob.waitForCompletion()
    
    #open ODB file and extract values for reaction forces
    odb = session.openOdb(str(myString)+'.odb')
    Mises_stress_list = []
    lastStep=odb.steps['Step-1']
    
    for x in range(len(lastStep.frames)):
        lastFrame = lastStep.frames [x]
        All_points = lastStep.frames[x].fieldOutputs['S'].values  
        for q in range (1,len(All_points)):
            Mises_stress = [All_points[q].mises]    # S11 = data[0]
            #Mises_stress_list.#append(Mises_stress)
            Mises_stress_list = Mises_stress_list + Mises_stress
            
    #Max_Mises_stress = max(Mises_stress_list)
    Max_Mises = np.max(Mises_stress_list)
    somefloats = [Max_Mises]
    somefloats1 = somefloats1 + somefloats
    #sortie.write('Maximum Mises stress is %f \n'%Max_Mises_stress)
    #np.savetxt('s_'+str(myString)+'.txt',Mises_stress_list)
    
    np.savetxt('sm_'+str(myString_result)+'.txt',somefloats1)
            

odb.close()
     
sortie.close()     
    
    
    
    