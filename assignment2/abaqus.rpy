# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Thu Apr 19 18:26:05 2018
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
    pathName='/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae')
#: The model database "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['assignment2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Global_Model.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Global_Model.odb
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
p = mdb.models['Model-1'].parts['assignment2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=283.397, 
    farPlane=341.423, width=257.598, height=97.1927, viewOffsetX=3.40909, 
    viewOffsetY=-0.280531)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].view.setValues(nearPlane=280.05, 
    farPlane=344.77, width=287.36, height=108.422, viewOffsetX=1.42458, 
    viewOffsetY=-0.602669)
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Global_Model.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Global_Model.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=343.813, 
    farPlane=539.816, width=129.856, height=46.1007, viewOffsetX=-20.9819, 
    viewOffsetY=-18.4696)
session.Path(name='AB_path', type=NODE_LIST, expression=(('ASSIGNMENT2-1', (6, 
    2, )), ))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
pth = session.paths['AB_path']
session.XYDataFromPath(name='XYData-AB', path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['AB_path']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
xQuantity = visualization.QuantityType(type=PATH)
yQuantity = visualization.QuantityType(type=STRESS)
session.xyDataObjects['XYData-AB'].setValues(axis1QuantityType=xQuantity, 
    axis2QuantityType=yQuantity, )
x0 = session.xyDataObjects['XYData-AB']
session.writeXYReport(fileName='abaqus.rpt', xyData=(x0, ))
mdb.Model(name='Submodel_AB_1mm', objectToCopy=mdb.models['Model-1'])
#: The model "Submodel_AB_1mm" has been created.
p1 = mdb.models['Submodel_AB_1mm'].parts['assignment2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Submodel_AB_1mm'].setValues(globalJob='Global_Model.odb')
a = mdb.models['Submodel_AB_1mm'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
del mdb.models['Submodel_AB_1mm'].boundaryConditions['BC-1']
del mdb.models['Submodel_AB_1mm'].loads['Load-1']
del mdb.models['Submodel_AB_1mm'].loads['Load-2']
a = mdb.models['Submodel_AB_1mm'].rootAssembly
del a.features['assignment2-1']
p1 = mdb.models['Submodel_AB_1mm'].parts['assignment2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
s = mdb.models['Submodel_AB_1mm'].ConstrainedSketch(name='__profile__', 
    sheetSize=312.4, gridSpacing=7.81)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.rectangle(point1=(-25.3825, 13.6675), point2=(-95.6725, 76.1475))
session.viewports['Viewport: 1'].view.setValues(nearPlane=269.848, 
    farPlane=354.972, width=378.739, height=142.9, cameraPosition=(-16.2515, 
    34.1315, 312.41), cameraTarget=(-16.2515, 34.1315, 0))
s.rectangle(point1=(-25.3825, 13.6675), point2=(64.4325, -33.1925))
session.viewports['Viewport: 1'].view.setValues(nearPlane=304.147, 
    farPlane=320.673, width=84.7766, height=31.9865, cameraPosition=(-37.4898, 
    -2.71354, 312.41), cameraTarget=(-37.4898, -2.71354, 0))
s.FilletByRadius(radius=1.0, curve1=g[13], nearPoint1=(-41.1732635498047, 
    -5.07541465759277), curve2=g[3], nearPoint2=(-49.9594650268555, 
    -2.51109600067139))
#* A fillet cannot be created at a vertex shared by more than two entities.
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
s.unsetPrimaryObject()
del mdb.models['Submodel_AB_1mm'].sketches['__profile__']
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
s1 = p.features['Shell planar-1'].sketch
mdb.models['Submodel_AB_1mm'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s1)
s2 = mdb.models['Submodel_AB_1mm'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
s2.unsetPrimaryObject()
del mdb.models['Submodel_AB_1mm'].sketches['__edit__']
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
s = p.features['Partition face-1'].sketch
mdb.models['Submodel_AB_1mm'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s1 = mdb.models['Submodel_AB_1mm'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Partition face-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=309.127, 
    farPlane=315.693, width=28.053, height=10.5845, cameraPosition=(-55.6703, 
    -2.77989, 312.41), cameraTarget=(-55.6703, -2.77989, 0))
s1.unsetPrimaryObject()
del mdb.models['Submodel_AB_1mm'].sketches['__edit__']
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
s = p.features['Shell planar-1'].sketch
mdb.models['Submodel_AB_1mm'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s2 = mdb.models['Submodel_AB_1mm'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=404.629, 
    farPlane=451.15, width=198.787, height=75.0032, cameraPosition=(-15.0232, 
    18.8474, 427.889), cameraTarget=(-15.0232, 18.8474, 0))
s2.FilletByRadius(radius=1.0, curve1=g[5], nearPoint1=(-42.0438423156738, 
    -4.88774299621582), curve2=g[6], nearPoint2=(-50.1262550354004, 
    0.650463104248047))
session.viewports['Viewport: 1'].view.setValues(nearPlane=426.733, 
    farPlane=429.046, width=10.2882, height=3.88176, cameraPosition=(-47.7382, 
    -3.33849, 427.889), cameraTarget=(-47.7382, -3.33849, 0))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
s2.unsetPrimaryObject()
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
p.features['Shell planar-1'].setValues(sketch=s2)
del mdb.models['Submodel_AB_1mm'].sketches['__edit__']
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
p.regenerate()
#: Warning: Mesh deleted in 2 regions due to geometry association failure.
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(
    -60.0, -15.0, 0.0))
s = mdb.models['Submodel_AB_1mm'].ConstrainedSketch(name='__profile__', 
    sheetSize=312.4, gridSpacing=7.81, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.delete(objectList=(g[2], ))
s.delete(objectList=(g[3], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=127.674, 
    farPlane=219.904, width=394.105, height=148.697, cameraPosition=(33.8484, 
    10.8907, 173.789), cameraTarget=(33.8484, 10.8907, 0))
s.unsetPrimaryObject()
del mdb.models['Submodel_AB_1mm'].sketches['__profile__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
del p.features['Partition face-1']
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
s1 = p.features['Shell planar-1'].sketch
mdb.models['Submodel_AB_1mm'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s1)
s2 = mdb.models['Submodel_AB_1mm'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
s2.rectangle(point1=(-30.0, 13.75), point2=(-86.25, 80.0))
s2.rectangle(point1=(-30.0, 13.75), point2=(50.0, -25.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=406.846, 
    farPlane=448.933, width=187.253, height=70.6511, cameraPosition=(19.042, 
    -5.15865, 427.889), cameraTarget=(19.042, -5.15865, 0))
s2.delete(objectList=(g[13], ))
s2.delete(objectList=(g[16], ))
s2.Line(point1=(50.0, 13.75), point2=(-15.0, 13.75))
s2.HorizontalConstraint(entity=g[17], addUndoState=False)
s2.PerpendicularConstraint(entity1=g[15], entity2=g[17], addUndoState=False)
#: Warning: Coincident point selected.
session.viewports['Viewport: 1'].view.setValues(nearPlane=407.68, 
    farPlane=448.099, width=172.716, height=65.1664, cameraPosition=(16.3995, 
    -3.72381, 427.889), cameraTarget=(16.3995, -3.72381, 0))
s2.Line(point1=(-15.0, 13.75), point2=(-15.0, -30.0))
s2.VerticalConstraint(entity=g[18], addUndoState=False)
s2.PerpendicularConstraint(entity1=g[17], entity2=g[18], addUndoState=False)
s2.Line(point1=(-15.0, -30.0), point2=(51.25, -30.0))
s2.HorizontalConstraint(entity=g[19], addUndoState=False)
s2.PerpendicularConstraint(entity1=g[18], entity2=g[19], addUndoState=False)
s2.Line(point1=(51.25, -30.0), point2=(50.0, 13.75))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=396.623, 
    farPlane=459.156, width=278.228, height=104.977, cameraPosition=(-1.76148, 
    5.35967, 427.889), cameraTarget=(-1.76148, 5.35967, 0))
s2.unsetPrimaryObject()
del mdb.models['Submodel_AB_1mm'].sketches['__edit__']
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
s = p.features['Shell planar-1'].sketch
mdb.models['Submodel_AB_1mm'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s1 = mdb.models['Submodel_AB_1mm'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
s1.unsetPrimaryObject()
del mdb.models['Submodel_AB_1mm'].sketches['__edit__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
s = p.features['Shell planar-1'].sketch
mdb.models['Submodel_AB_1mm'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s2 = mdb.models['Submodel_AB_1mm'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=391.611, 
    farPlane=464.167, height=121.802, cameraPosition=(15.6339, 30.2543, 
    427.889), cameraTarget=(15.6339, 30.2543, 0))
s2.rectangle(point1=(-91.25, 86.25), point2=(-33.75, 18.75))
session.viewports['Viewport: 1'].view.setValues(nearPlane=374.435, 
    farPlane=481.344, width=517.944, height=195.422, cameraPosition=(-2.66476, 
    45.5207, 427.889), cameraTarget=(-2.66476, 45.5207, 0))
s2.rectangle(point1=(-28.75, 13.75), point2=(57.5, -37.5))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=368.421, 
    farPlane=487.358, width=529.185, height=199.663, cameraPosition=(-1.39084, 
    47.092, 427.889), cameraTarget=(-1.39084, 47.092, 0))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=389.567, 
    farPlane=466.212, width=341.017, height=128.667, cameraPosition=(-7.3013, 
    12.5646, 427.889), cameraTarget=(-7.3013, 12.5646, 0))
s2.unsetPrimaryObject()
del mdb.models['Submodel_AB_1mm'].sketches['__edit__']
s = mdb.models['Submodel_AB_1mm'].ConstrainedSketch(name='__profile__', 
    sheetSize=312.4, gridSpacing=7.81)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.rectangle(point1=(-80.0525, 76.1475), point2=(-31.24, 15.62))
session.viewports['Viewport: 1'].view.setValues(nearPlane=263.067, 
    farPlane=361.753, width=421.691, height=159.106, cameraPosition=(-18.7305, 
    31.8334, 312.41), cameraTarget=(-18.7305, 31.8334, 0))
s.rectangle(point1=(-31.24, 7.81), point2=(54.67, -37.0975))
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
p.Cut(sketch=s)
s.unsetPrimaryObject()
del mdb.models['Submodel_AB_1mm'].sketches['__profile__']
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=290.678, 
    farPlane=334.142, width=190.799, height=71.989, viewOffsetX=0.197552, 
    viewOffsetY=-13.0488)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
a = mdb.models['Submodel_AB_1mm'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
a1 = mdb.models['Submodel_AB_1mm'].rootAssembly
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
a1.Instance(name='assignment2-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['Submodel_AB_1mm'].rootAssembly
e1 = a.instances['assignment2-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#10 ]', ), )
region = a.Set(edges=edges1, name='Set-4')
mdb.models['Submodel_AB_1mm'].SubmodelBC(name='BC-1', createStepName='Step-1', 
    region=region, globalStep='1', globalIncrement=0, timeScale=OFF, dof=(1, 
    2), globalDrivingRegion='', absoluteExteriorTolerance=None, 
    exteriorTolerance=0.05)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
a = mdb.models['Submodel_AB_1mm'].rootAssembly
s1 = a.instances['assignment2-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region = a.Surface(side1Edges=side1Edges1, name='Surf-1')
mdb.models['Submodel_AB_1mm'].SubmodelSB(name='Load-1', 
    createStepName='Step-1', region=region, globalStep='1', globalIncrement=0, 
    globalDrivingRegion='', absoluteExteriorTolerance=None, 
    exteriorTolerance=0.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=146.821, 
    farPlane=176.907, width=133.613, height=50.4127, viewOffsetX=9.45662, 
    viewOffsetY=1.77045)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=291.707, 
    farPlane=333.113, width=200.237, height=75.7914, viewOffsetX=2.59713, 
    viewOffsetY=-10.9957)
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
f1, e1, d2 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
    -53.876511, -7.946679, 0.0))
s1 = mdb.models['Submodel_AB_1mm'].ConstrainedSketch(name='__profile__', 
    sheetSize=312.4, gridSpacing=7.81, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.Line(point1=(3.876511, 3.946679), point2=(-16.1234889999516, 3.946679))
s1.HorizontalConstraint(entity=g[9], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[4], entity2=g[9], addUndoState=False)
s1.CoincidentConstraint(entity1=v[8], entity2=g[7], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=107.548, 
    farPlane=117.034, width=49.2433, height=18.5797, cameraPosition=(-50.882, 
    -4.24963, 112.291), cameraTarget=(-50.882, -4.24963, 0))
s1.Line(point1=(4.876511, 2.946679), point2=(-16.1234889999516, 2.946679))
s1.HorizontalConstraint(entity=g[10], addUndoState=False)
s1.ParallelConstraint(entity1=g[3], entity2=g[10], addUndoState=False)
s1.CoincidentConstraint(entity1=v[9], entity2=g[7], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=102.295, 
    farPlane=122.287, width=85.4302, height=32.2331, cameraPosition=(-53.5404, 
    -14.7364, 112.291), cameraTarget=(-53.5404, -14.7364, 0))
s1.Line(point1=(3.876511, 3.946679), point2=(3.876511, -17.0533209999779))
s1.VerticalConstraint(entity=g[11], addUndoState=False)
s1.TangentConstraint(entity1=g[4], entity2=g[11], addUndoState=False)
s1.CoincidentConstraint(entity1=v[10], entity2=g[8], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1073.95, 
    farPlane=1086.25, width=45.5879, height=17.2005, cameraPosition=(-51.3807, 
    -18.6554, 1080.1), cameraTarget=(-51.3807, -18.6554, 0))
s1.Line(point1=(4.876511, 2.946679), point2=(5.34882392724609, -17.053321))
s1.CoincidentConstraint(entity1=v[11], entity2=g[8], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1071.03, 
    farPlane=1089.17, width=67.2189, height=25.3619, cameraPosition=(-42.8097, 
    -15.0517, 1080.1), cameraTarget=(-42.8097, -15.0517, 0))
s1.ParallelConstraint(entity1=g[12], entity2=g[2])
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e, d1 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Submodel_AB_1mm'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=303.728, 
    farPlane=321.092, width=74.0073, height=28.0124, viewOffsetX=-27.8435, 
    viewOffsetY=-25.6123)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=299.802, 
    farPlane=325.018, width=111.748, height=42.2974, viewOffsetX=-14.8014, 
    viewOffsetY=-25.0921)
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#2008 ]', ), )
p.deleteSeeds(regions=pickedEdges)
session.viewports['Viewport: 1'].view.setValues(nearPlane=296.493, 
    farPlane=328.327, width=140.892, height=53.3289, viewOffsetX=-13.2135, 
    viewOffsetY=-23.2325)
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#fe1f ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=10, constraint=FINER)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=291.641, 
    farPlane=333.179, width=200.392, height=75.8498, viewOffsetX=14.9037, 
    viewOffsetY=-14.6912)
elemType1 = mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
p = mdb.models['Submodel_AB_1mm'].parts['assignment2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3f ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
a = mdb.models['Submodel_AB_1mm'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='Submodel_AB_1-job', model='Submodel_AB_1mm', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['Submodel_AB_1-job'].submit(consistencyChecking=OFF)
#: The job input file "Submodel_AB_1-job.inp" has been submitted for analysis.
#: Job Submodel_AB_1-job: Analysis Input File Processor completed successfully.
#: Job Submodel_AB_1-job: Abaqus/Standard completed successfully.
#: Job Submodel_AB_1-job completed successfully. 
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Submodel_AB_1-job.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Submodel_AB_1-job.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=125.636, 
    farPlane=191.971, width=30.9094, height=10.9733, viewOffsetX=5.23133, 
    viewOffsetY=0.963954)
session.Path(name='Path-2', type=NODE_LIST, expression=(('ASSIGNMENT2-1', (121, 
    291, )), ))
session.paths.changeKey(fromName='Path-2', toName='Arround_corner')
pth = session.paths['Arround_corner']
session.XYDataFromPath(name='XYData-submodel1mm-Arround_corner', path=pth, 
    includeIntersections=True, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=DEFORMED, 
    labelType=TRUE_DISTANCE)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Arround_corner']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
session.printToFile(fileName='asubmodel_1mm-ArroundCorner', format=PNG, 
    canvasObjects=(session.viewports['Viewport: 1'], ))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['XYData-submodel1mm-Arround_corner']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['XYData-submodel1mm-Arround_corner']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
mdb.Model(name='Submodel_AB_5mm', objectToCopy=mdb.models['Submodel_AB_1mm'])
#: The model "Submodel_AB_5mm" has been created.
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p1 = mdb.models['Submodel_AB_5mm'].parts['assignment2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=103.567, 
    farPlane=121.015, width=65.1903, height=23.8182, viewOffsetX=10.7417, 
    viewOffsetY=-4.4986)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
del p.features['Partition face-1']
#: Warning: Failed to attach mesh to part geometry.
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=100.339, 
    farPlane=124.243, width=90.2268, height=32.9656, viewOffsetX=8.76025, 
    viewOffsetY=-11.8177)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
s = p.features['Shell planar-1'].sketch
mdb.models['Submodel_AB_5mm'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s2 = mdb.models['Submodel_AB_5mm'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=426.997, 
    farPlane=429.961, width=10.9825, height=4.0126, cameraPosition=(-46.6253, 
    -3.69336, 428.479), cameraTarget=(-46.6253, -3.69336, 0))
s2.delete(objectList=(g[8], ))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
s2.FilletByRadius(radius=5.0, curve1=g[5], nearPoint1=(-48.8837814331055, 
    -4.97407484054565), curve2=g[6], nearPoint2=(-49.9933891296387, 
    -3.31308555603027))
session.viewports['Viewport: 1'].view.setValues(nearPlane=424.193, 
    farPlane=432.766, width=38.1431, height=13.9361, cameraPosition=(-40.4282, 
    -0.174673, 428.479), cameraTarget=(-40.4282, -0.174673, 0))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
s2.unsetPrimaryObject()
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
p.features['Shell planar-1'].setValues(sketch=s2)
del mdb.models['Submodel_AB_5mm'].sketches['__edit__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=99.4964, 
    farPlane=125.086, width=113.469, height=41.4574, viewOffsetX=16.2975, 
    viewOffsetY=-5.00375)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
p.regenerate()
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
f, e1, d2 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(
    -53.854792, -7.928974, 0.0))
s = mdb.models['Submodel_AB_5mm'].ConstrainedSketch(name='__profile__', 
    sheetSize=312.4, gridSpacing=7.81, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.Line(point1=(3.854792, 7.928974), point2=(-16.1452079999863, 7.928974))
s.HorizontalConstraint(entity=g[9], addUndoState=False)
s.PerpendicularConstraint(entity1=g[4], entity2=g[9], addUndoState=False)
s.CoincidentConstraint(entity1=v[8], entity2=g[7], addUndoState=False)
s.Line(point1=(7.81, -17.071026), point2=(8.854792, 2.928974))
s.CoincidentConstraint(entity1=v[9], entity2=g[8], addUndoState=False)
s.Line(point1=(8.854792, 2.928974), point2=(-16.1452079999863, 2.928974))
s.HorizontalConstraint(entity=g[11], addUndoState=False)
s.CoincidentConstraint(entity1=v[10], entity2=g[7], addUndoState=False)
s.Line(point1=(3.854792, 7.928974), point2=(4.67425382250977, -17.071026))
s.CoincidentConstraint(entity1=v[11], entity2=g[8], addUndoState=False)
s.PerpendicularConstraint(entity1=g[11], entity2=g[10])
s.PerpendicularConstraint(entity1=g[9], entity2=g[12])
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e, d1 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Submodel_AB_5mm'].sketches['__profile__']
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=99.9008, 
    farPlane=124.681, width=109.695, height=40.2063, viewOffsetX=15.6651, 
    viewOffsetY=-0.913798)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#11 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#6008 ]', ), )
p.deleteSeeds(regions=pickedEdges)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#2e ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1ffff ]', ), )
p.deleteSeeds(regions=pickedEdges)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#de17 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=10, constraint=FINER)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#8 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=10, constraint=FINER)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#100e0 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=2, constraint=FINER)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#100e0 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=3, constraint=FINER)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#2000 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=10, constraint=FINER)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
p.generateMesh()
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=104.628, 
    farPlane=119.954, width=101.068, height=37.0443, viewOffsetX=15.2322, 
    viewOffsetY=-1.54439)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=97.8186, 
    farPlane=126.764, width=128.043, height=46.9316, viewOffsetX=24.7594, 
    viewOffsetY=-2.62813)
elemType1 = mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
p = mdb.models['Submodel_AB_5mm'].parts['assignment2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3f ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Submodel_AB_5mm'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='Submodel_AB_5-job', model='Submodel_AB_5mm', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['Submodel_AB_5-job'].submit(consistencyChecking=OFF)
#: The job input file "Submodel_AB_5-job.inp" has been submitted for analysis.
#: Job Submodel_AB_5-job: Analysis Input File Processor completed successfully.
#: Job Submodel_AB_5-job: Abaqus/Standard completed successfully.
#: Job Submodel_AB_5-job completed successfully. 
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Submodel_AB_5-job.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Submodel_AB_5-job.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=122.164, 
    farPlane=195.443, width=60.9158, height=20.8987, viewOffsetX=0.306488, 
    viewOffsetY=-0.0749924)
session.Path(name='ArroundCorner5mm', type=NODE_LIST, expression=((
    'ASSIGNMENT2-1', (13, 321, )), ))
pth = session.paths['ArroundCorner5mm']
session.XYDataFromPath(name='XYData-ArroundCorner5mm', path=pth, 
    includeIntersections=True, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=DEFORMED, 
    labelType=TRUE_DISTANCE)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['ArroundCorner5mm']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
session.printToFile(fileName='asubmodel_5mm-ArroundCorner', format=PNG, 
    canvasObjects=(session.viewports['Viewport: 1'], ))
pth = session.paths['AB_path']
session.XYDataFromPath(name='XYData-AB_5mm', path=pth, 
    includeIntersections=True, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=DEFORMED, 
    labelType=TRUE_DISTANCE)
a = mdb.models['Submodel_AB_5mm'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Submodel_AB_1-job.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['Submodel_AB_5mm'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Submodel_AB_1-job.odb'])
pth = session.paths['AB_path']
session.XYDataFromPath(name='XYData-AB_1mm', path=pth, 
    includeIntersections=True, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=DEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=127.081, 
    farPlane=190.526, width=31.2062, height=10.7061, viewOffsetX=6.14794, 
    viewOffsetY=0.581569)
session.Path(name='Path-4', type=NODE_LIST, expression=(('ASSIGNMENT2-1', (8, 
    1046, )), ))
session.paths.changeKey(fromName='Path-4', toName='AB_1mm')
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['XYData-AB_1mm']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
del session.xyDataObjects['XYData-AB_1mm']
pth = session.paths['AB_1mm']
session.XYDataFromPath(name='XYData-AB_1mm', path=pth, 
    includeIntersections=True, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=DEFORMED, 
    labelType=TRUE_DISTANCE)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['AB_1mm']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['XYData-AB_1mm']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['XYData-AB_1mm']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
