# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Thu Apr 12 20:22:02 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=262.208312988281, 
    height=131.972366333008)
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
openMdb(
    pathName='/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/Assignment1.cae')
#: The model database "/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/Assignment1.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Assignment1'].parts['PartAssignment1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p1 = mdb.models['Assignment1'].parts['PartAssignment1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=566.088, 
    farPlane=634.578, width=309.279, height=111.63, viewOffsetX=4.08248, 
    viewOffsetY=-0.289107)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
elemType1 = mesh.ElemType(elemCode=CPS8, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
p = mdb.models['Assignment1'].parts['PartAssignment1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
session.viewports['Viewport: 1'].view.setValues(nearPlane=565.548, 
    farPlane=635.118, width=296.748, height=112.321, viewOffsetX=-1.92212, 
    viewOffsetY=-1.11915)
p = mdb.models['Assignment1'].parts['PartAssignment1']
p.generateMesh()
a = mdb.models['Assignment1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='CPS8_2_12', model='Assignment1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['CPS8_2_12'].submit(consistencyChecking=OFF)
#: The job input file "CPS8_2_12.inp" has been submitted for analysis.
#: Job CPS8_2_12: Analysis Input File Processor completed successfully.
#: Job CPS8_2_12: Abaqus/Standard completed successfully.
#: Job CPS8_2_12 completed successfully. 
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS8_2_12/CPS8_2_12.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS8_2_12/CPS8_2_12.odb
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
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS8_2_12/CPS8_2_12.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL), ))
