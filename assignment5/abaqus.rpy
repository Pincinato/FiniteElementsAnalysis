# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Fri May 11 08:36:42 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=246.569549560547, 
    height=121.358612060547)
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
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
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
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=105.285, 
    farPlane=185.589, width=31.6769, height=8.76348, viewOffsetX=3.04805, 
    viewOffsetY=30.1998)
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RT', 
    NODAL), ('U', NODAL), ), nodePick=(('ASSEMBLY', 1, ('[#1 ]', )), ), )
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'RT', NODAL), ('U', NODAL), ), nodePick=(('ASSEMBLY', 1, ('[#1 ]', )), ), )
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RT', 
    NODAL, ((COMPONENT, 'RT2'), )), ('U', NODAL, ((COMPONENT, 'U2'), )), ), 
    nodePick=(('ASSEMBLY', 1, ('[#1 ]', )), ), )
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'RT', NODAL, ((COMPONENT, 'RT2'), )), ('U', NODAL, ((COMPONENT, 'U2'), )), 
    ), nodePick=(('ASSEMBLY', 1, ('[#1 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
del session.xyDataObjects['RT:Magnitude PI: ASSEMBLY N: 1']
del session.xyDataObjects['RT:RT1 PI: ASSEMBLY N: 1']
del session.xyDataObjects['RT:RT2 PI: ASSEMBLY N: 1']
del session.xyDataObjects['RT:RT2 PI: ASSEMBLY N: 1_1']
del session.xyDataObjects['U:Magnitude PI: ASSEMBLY N: 1']
del session.xyDataObjects['U:U1 PI: ASSEMBLY N: 1']
del session.xyDataObjects['U:U2 PI: ASSEMBLY N: 1']
del session.xyDataObjects['U:U2 PI: ASSEMBLY N: 1_1']
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['_RT:RT2 PI: ASSEMBLY N: 1_1']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RT', 
    NODAL, ((COMPONENT, 'RT2'), )), ('U', NODAL, ((COMPONENT, 'U2'), )), ), 
    nodePick=(('PART-1-4', 1, ('[#0:2 #1 ]', )), ), )
del session.xyDataObjects['_RT:RT2 PI: ASSEMBLY N: 1_1']
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment5/CPS4_hyperplastic.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', 
    NODAL, ((COMPONENT, 'RF2'), )), ('U', NODAL, ((COMPONENT, 'U2'), )), ), 
    nodePick=(('ASSEMBLY', 1, ('[#1 ]', )), ), )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
