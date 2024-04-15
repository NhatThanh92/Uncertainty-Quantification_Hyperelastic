# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:56:27 2023

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
import sys
Limit = 10

for ic in range(1,Limit,1):
    myString="Job-"+str(ic)
    o1 = session.openOdb(str(myString)+'.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)
    
    ##Stress##
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 'Max. Principal'))
    
    ## displacement##
    #session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 'Magnitude'), )
    #######
    
    pth = session.Path(name='Path-2', type=NODE_LIST, expression=(('UTERUS', (4095, 4102, 4085, 4086, 4067, 4077, 4078, 4079, 4080, 4088, 4107, 4091, 4092, 4071, )), ))
    session.XYDataFromPath(name='S'+myString, path=pth, includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, removeDuplicateXYPairs=True, includeAllElements=False)
    x0 = session.xyDataObjects['S'+myString]
    
    #session.writeXYReport(fileName='your_file_name.csv', xyData=(x0))
    y0 = np.savetxt(str(ic)+'.csv',x0 , delimiter = ",")
   
    