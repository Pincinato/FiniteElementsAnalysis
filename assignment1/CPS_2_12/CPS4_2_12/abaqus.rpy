# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Thu Apr 12 18:10:08 2018
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
a = mdb.models['Assignment1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
o3 = session.openOdb(name='/home/fe1/CPS4_2_12.odb')
#: Model: /home/fe1/CPS4_2_12.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
odb = session.odbs['/home/fe1/CPS4_2_12.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL), ), nodePick=(('PARTASSIGNMENT1-1', 1, ('[#4000000 ]', )), ), )
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/Assignment1.cae".
odb = session.odbs['/home/fe1/CPS4_2_12.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL), ))
a = mdb.models['Assignment1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
xyp = session.xyPlots['XYPlot-1']
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['/home/fe1/CPS4_2_12.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
odb = session.odbs['/home/fe1/CPS4_2_12.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL), ))
a = mdb.models['Assignment1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Assignment1'].parts['PartAssignment1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Assignment1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['Assignment1'].rootAssembly
v1 = a.instances['PartAssignment1-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
region = a.Set(vertices=verts1, name='Set-3')
mdb.models['Assignment1'].ConcentratedForce(name='Load-2', 
    createStepName='Load', region=region, cf2=-25.0, distributionType=UNIFORM, 
    field='', localCsys=None)
mdb.models['Assignment1'].loads['Load-1'].setValues(cf2=-25.0, 
    distributionType=UNIFORM, field='')
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Assignment1'].parts['PartAssignment1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Assignment1'].materials['steel'].elastic.setValues(table=((90000.0, 
    0.3), ))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/Assignment1.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/Assignment1.cae".
a = mdb.models['Assignment1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['CPS4_2_12'].submit(consistencyChecking=OFF)
#: The job input file "CPS4_2_12.inp" has been submitted for analysis.
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment1/Assignment1.cae".
#: Job CPS4_2_12: Analysis Input File Processor completed successfully.
#: Job CPS4_2_12: Abaqus/Standard completed successfully.
#: Job CPS4_2_12 completed successfully. 
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Assignment1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='/home/fe1/CPS4_2_12.odb')
#: Model: /home/fe1/CPS4_2_12.odb
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
odb = session.odbs['/home/fe1/CPS4_2_12.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL), ))
odb = session.odbs['/home/fe1/CPS4_2_12.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL), ))
