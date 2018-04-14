# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Thu Apr 12 23:21:45 2018
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
openMdb(
    pathName='/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/Assignment1.cae')
#: The model database "/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/Assignment1.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Assignment1'].parts['PartAssignment1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
elemType1 = mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
p = mdb.models['Assignment1'].parts['PartAssignment1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Assignment1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.Job(name='CPS8R_2_12', model='Assignment1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['CPS8R_2_12'].submit(consistencyChecking=OFF)
#: The job input file "CPS8R_2_12.inp" has been submitted for analysis.
#: Job CPS8R_2_12: Analysis Input File Processor completed successfully.
#: Job CPS8R_2_12: Abaqus/Standard completed successfully.
#: Job CPS8R_2_12 completed successfully. 
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS8R_2_12/CPS8R_2_12.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS8R_2_12/CPS8R_2_12.odb
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
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS8R_2_12/CPS8R_2_12.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL), ))
p1 = mdb.models['Assignment1'].parts['PartAssignment1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=567.401, 
    farPlane=633.266, width=291.766, height=110.436, viewOffsetX=-2.35437, 
    viewOffsetY=-0.807182)
p = mdb.models['Assignment1'].parts['PartAssignment1']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Assignment1'].parts['PartAssignment1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#a ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=4, constraint=FIXED)
p = mdb.models['Assignment1'].parts['PartAssignment1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#5 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=24, constraint=FIXED)
elemType1 = mesh.ElemType(elemCode=CPS4, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=STANDARD)
p = mdb.models['Assignment1'].parts['PartAssignment1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
p = mdb.models['Assignment1'].parts['PartAssignment1']
p.seedPart(size=15.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Assignment1'].parts['PartAssignment1']
p.generateMesh()
elemType1 = mesh.ElemType(elemCode=CPS4, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=STANDARD)
p = mdb.models['Assignment1'].parts['PartAssignment1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Assignment1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='CPS4_4_24', model='Assignment1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['CPS4_4_24'].submit(consistencyChecking=OFF)
#: The job input file "CPS4_4_24.inp" has been submitted for analysis.
#: Job CPS4_4_24: Analysis Input File Processor completed successfully.
#: Job CPS4_4_24: Abaqus/Standard completed successfully.
#: Job CPS4_4_24 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS8R_2_12/CPS8R_2_12.odb'])
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS4_4_24.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS4_4_24.odb
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
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS4_4_24.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL), ))
p1 = mdb.models['Assignment1'].parts['PartAssignment1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
elemType1 = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=STANDARD)
p = mdb.models['Assignment1'].parts['PartAssignment1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
session.viewports['Viewport: 1'].view.setValues(nearPlane=567.477, 
    farPlane=633.189, width=280.25, height=106.077, viewOffsetX=-7.82808, 
    viewOffsetY=-1.61474)
a = mdb.models['Assignment1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='CPS4R_4_24', model='Assignment1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS4_4_24.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['Assignment1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['CPS4R_4_24'].submit(consistencyChecking=OFF)
#: The job input file "CPS4R_4_24.inp" has been submitted for analysis.
#: Job CPS4R_4_24: Analysis Input File Processor completed successfully.
#: Job CPS4R_4_24: Abaqus/Standard completed successfully.
#: Job CPS4R_4_24 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS4_4_24.odb'])
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS4R_4_24.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS4R_4_24.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS4R_4_24.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL), ))
p1 = mdb.models['Assignment1'].parts['PartAssignment1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=558.265, 
    farPlane=642.401, width=358.962, height=135.87, viewOffsetX=-33.63, 
    viewOffsetY=-5.68109)
elemType1 = mesh.ElemType(elemCode=CPS8, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
p = mdb.models['Assignment1'].parts['PartAssignment1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Assignment1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='CPS8_4_24', model='Assignment1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['CPS8_4_24'].submit(consistencyChecking=OFF)
#: The job input file "CPS8_4_24.inp" has been submitted for analysis.
#: Job CPS8_4_24: Analysis Input File Processor completed successfully.
#: Job CPS8_4_24: Abaqus/Standard completed successfully.
#: Job CPS8_4_24 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS4R_4_24.odb'])
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS8_4_24.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS8_4_24.odb
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
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS8_4_24.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL), ))
p1 = mdb.models['Assignment1'].parts['PartAssignment1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
elemType1 = mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
p = mdb.models['Assignment1'].parts['PartAssignment1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Assignment1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='CPS8R_4_24', model='Assignment1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['CPS8R_4_24'].submit(consistencyChecking=OFF)
#: The job input file "CPS8R_4_24.inp" has been submitted for analysis.
#: Job CPS8R_4_24: Analysis Input File Processor completed successfully.
#: Job CPS8R_4_24: Abaqus/Standard completed successfully.
#: Job CPS8R_4_24 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS8_4_24.odb'])
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS8R_4_24.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS8R_4_24.odb
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
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/CPS_2_12/CPS8R_2_12/CPS8R_4_24.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL), ))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/Assignment1.cae".
