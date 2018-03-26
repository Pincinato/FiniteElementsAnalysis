# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Mon Mar 26 15:34:20 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=274.631500244141, 
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
openMdb(pathName='/home/fe1/Desktop/FiniteElementsAnalysis/Connecting_Lug.cae')
#: The model database "/home/fe1/Desktop/FiniteElementsAnalysis/Connecting_Lug.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Connecting_Lug'].parts['Connecting Lug']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.241608, 
    farPlane=0.347529, width=0.216836, height=0.0853434, cameraPosition=(
    -0.00736197, 0.158542, 0.249769), cameraUpVector=(-0.083557, 0.57735, 
    -0.81221), cameraTarget=(-0.0322314, -0.0132965, 0.00802787))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237862, 
    farPlane=0.351967, width=0.213474, height=0.0840204, cameraPosition=(
    0.0101316, 0.155075, 0.249769), cameraUpVector=(-0.02327, 0.582901, 
    -0.81221), cameraTarget=(-0.0324134, -0.0132604, 0.00802787))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238119, 
    farPlane=0.351651, width=0.213705, height=0.0841112, cameraPosition=(
    0.00992394, 0.155075, 0.249769), cameraTarget=(-0.0326211, -0.0132604, 
    0.00802787))
elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
p = mdb.models['Connecting_Lug'].parts['Connecting Lug']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
p = mdb.models['Connecting_Lug'].parts['Connecting Lug']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
p = mdb.models['Connecting_Lug'].parts['Connecting Lug']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.222084, 
    farPlane=0.370788, width=0.199976, height=0.0784473, cameraPosition=(
    0.0983817, 0.155075, 0.2154), cameraUpVector=(-0.332355, 0.582901, 
    -0.741462), cameraTarget=(-0.0334456, -0.0132604, 0.0083482))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.231612, 
    farPlane=0.362824, width=0.208556, height=0.081813, cameraPosition=(
    0.0983817, 0.0487407, 0.267783), cameraUpVector=(-0.332355, 0.847294, 
    -0.414284), cameraTarget=(-0.0334456, -0.0128309, 0.00813663))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.232342, 
    farPlane=0.361816, width=0.209213, height=0.0820707, cameraPosition=(
    0.0900473, 0.0487407, 0.271849), cameraUpVector=(-0.318976, 0.847294, 
    -0.424671), cameraTarget=(-0.033434, -0.0128309, 0.00813095))
p = mdb.models['Connecting_Lug'].parts['Connecting Lug']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
v, e, d = p.vertices, p.edges, p.datums
p.PartitionCellByPlaneThreePoints(point1=v[14], point2=v[8], point3=v[15], 
    cells=pickedCells)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/Connecting_Lug.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/Connecting_Lug.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/Connecting_Lug.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/Connecting_Lug.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/Connecting_Lug.cae".
