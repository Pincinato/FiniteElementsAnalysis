# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Thu Apr 12 22:55:54 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=246.084625244141, 
    height=125.096046447754)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
openMdb(
    pathName='/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/Assignment1.cae')
#: The model database "/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/Assignment1.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Assignment1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['Assignment1'].parts['PartAssignment1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
elemType1 = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=STANDARD)
p = mdb.models['Assignment1'].parts['PartAssignment1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Assignment1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='CPS4R_2_12', model='Assignment1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['CPS4R_2_12'].submit(consistencyChecking=OFF)
#: The job input file "CPS4R_2_12.inp" has been submitted for analysis.
#: Job CPS4R_2_12: Analysis Input File Processor completed successfully.
#: Job CPS4R_2_12: Abaqus/Standard completed successfully.
#: Job CPS4R_2_12 completed successfully. 
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS4R_2_12/CPS4R_2_12.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS4R_2_12/CPS4R_2_12.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS4R_2_12/CPS4R_2_12.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL), ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    ORIENT_ON_DEF, ))
#: Warning: Material orientation information is not available in the current frame for any elements in the current display group.  Please make sure the primary variable is element-based AND orientations had been defined in the pertinent solid/shell sections.
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=661.04, 
    farPlane=1036.96, width=310.214, height=110.131, viewOffsetX=4.00893, 
    viewOffsetY=1.36369)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/Assignment1.cae".
