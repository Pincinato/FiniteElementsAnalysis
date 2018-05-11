# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Thu May 10 17:26:25 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=246.084625244141, 
    height=121.657890319824)
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
    pathName='/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/againagainagin.cae')
#: The model database "/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/againagainagin.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].view.setValues(nearPlane=95.3294, 
    farPlane=131.968, width=162.487, height=59.6254, viewOffsetX=2.29801, 
    viewOffsetY=0.0741342)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
a = mdb.models['Model-1'].rootAssembly
a.makeIndependent(instances=(a.instances['Part-1-4'], ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
elemType1 = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=STANDARD)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-1-4'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1ff ]', ), )
pickedRegions =(faces1, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=90.6198, 
    farPlane=200.255, width=165.852, height=57.1637, viewOffsetX=-2.28878, 
    viewOffsetY=1.22631)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'U', 'RF', 'RT', 'CF'))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['CPS4_hyperplastic'].submit(consistencyChecking=OFF)
#: The job input file "CPS4_hyperplastic.inp" has been submitted for analysis.
#: Job CPS4_hyperplastic: Analysis Input File Processor completed successfully.
#: Job CPS4_hyperplastic: Abaqus/Standard completed successfully.
#: Job CPS4_hyperplastic completed successfully. 
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 1'].maximize()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=97.1566, 
    farPlane=193.718, width=87.1147, height=24.2075, viewOffsetX=2.07351, 
    viewOffsetY=4.75094)
session.viewports['Viewport: 1'].view.setValues(nearPlane=105.595, 
    farPlane=185.28, width=29.5069, height=8.1994, viewOffsetX=0.110364, 
    viewOffsetY=30.2687)
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('U', 
    NODAL, ((COMPONENT, 'U2'), )), ), nodePick=(('ASSEMBLY', 1, ('[#1 ]', )), 
    ), )
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('U', 
    NODAL, ((COMPONENT, 'U2'), )), ), nodePick=(('ASSEMBLY', 1, ('[#1 ]', )), 
    ), )
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', 
    NODAL, ((COMPONENT, 'RF2'), )), ('RT', NODAL, ((COMPONENT, 'RT2'), )), (
    'U', NODAL, ((COMPONENT, 'U2'), )), ), nodePick=(('ASSEMBLY', 1, ('[#1 ]', 
    )), ), )
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'RF', NODAL, ((COMPONENT, 'RF2'), )), ('RT', NODAL, ((COMPONENT, 'RT2'), 
    )), ('U', NODAL, ((COMPONENT, 'U2'), )), ), nodePick=(('ASSEMBLY', 1, (
    '[#1 ]', )), ), )
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['_U:U2 PI: ASSEMBLY N: 1']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['RT:RT2 PI: ASSEMBLY N: 1']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['RF:RF2 PI: ASSEMBLY N: 1']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/againagainagin.cae".
