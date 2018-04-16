# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Mon Apr 16 08:37:15 2018
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
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=0.000745654, 
    viewOffsetY=-0.000306576)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=166.41, 
    farPlane=210.714, width=197.119, height=74.3738, cameraPosition=(4.6609, 
    1.70098, 188.562), cameraTarget=(4.6609, 1.70098, 0))
s.Spot(point=(-75.0, 25.0))
s.Spot(point=(-66.25, 65.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=167.269, 
    farPlane=209.854, width=181.968, height=68.6572, cameraPosition=(-1.02249, 
    -2.25806, 188.562), cameraTarget=(-1.02249, -2.25806, 0))
s.Spot(point=(-75.0, -20.0))
s.Spot(point=(-75.0, 25.0))
s.Spot(point=(-1.25, -17.5))
s.delete(objectList=(v[0], ))
s.delete(objectList=(v[2], ))
s.delete(objectList=(v[4], ))
s.delete(objectList=(v[3], ))
s.Line(point1=(-70.0, 20.0), point2=(-70.0, -25.0))
s.VerticalConstraint(entity=g[2], addUndoState=False)
s.Line(point1=(-70.0, -25.0), point2=(-15.0, -25.0))
s.HorizontalConstraint(entity=g[3], addUndoState=False)
s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s.Line(point1=(-15.0, -25.0), point2=(-15.0, -15.0))
s.VerticalConstraint(entity=g[4], addUndoState=False)
s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s.Line(point1=(-15.0, -15.0), point2=(-60.0, -15.0))
s.HorizontalConstraint(entity=g[5], addUndoState=False)
s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s.Line(point1=(-60.0, -15.0), point2=(-60.0, 20.0))
s.VerticalConstraint(entity=g[6], addUndoState=False)
s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
s.Line(point1=(-60.0, 20.0), point2=(-70.0, 20.0))
s.HorizontalConstraint(entity=g[7], addUndoState=False)
s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
mdb.saveAs(
    pathName='/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2')
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
s.ParallelConstraint(entity1=g[5], entity2=g[3])
s.ParallelConstraint(entity1=g[6], entity2=g[2])
s.ParallelConstraint(entity1=g[7], entity2=g[3])
s.PerpendicularConstraint(entity1=g[5], entity2=g[6])
s.PerpendicularConstraint(entity1=g[5], entity2=g[6])
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
s.VerticalDimension(vertex1=v[5], vertex2=v[6], textPoint=(100.0, 0.0), 
    value=100.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=146.225, 
    farPlane=230.899, width=384.585, height=145.105, cameraPosition=(-26.3357, 
    14.5255, 188.562), cameraTarget=(-26.3357, 14.5255, 0))
s.ObliqueDimension(vertex1=v[6], vertex2=v[7], textPoint=(-70.0264739990234, 
    -35.6797142028809), value=100.0)
s.delete(objectList=(d[1], ))
s.ObliqueDimension(vertex1=v[9], vertex2=v[8], textPoint=(30.2322731018066, 
    0.443557739257812), value=100.0)
#: Warning: Select two or more lines.
s.EqualLengthConstraint(entity1=g[4], entity2=g[7])
session.viewports['Viewport: 1'].view.setValues(nearPlane=141.686, 
    farPlane=235.438, width=425.818, height=160.663, cameraPosition=(-22.4716, 
    8.0416, 188.562), cameraTarget=(-22.4716, 8.0416, 0))
s.HorizontalDimension(vertex1=v[5], vertex2=v[10], textPoint=(
    -61.0018539428711, 84.3054962158203), value=20.0)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
p = mdb.models['Model-1'].Part(name='assignment2', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['assignment2']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['assignment2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='steel')
mdb.models['Model-1'].materials['steel'].Elastic(table=((500.0, 0.3), ))
del mdb.models['Model-1'].materials['steel'].elastic
mdb.models['Model-1'].materials['steel'].Plastic(table=((500.0, 0.0), ))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.models['Model-1'].HomogeneousSolidSection(name='Section_assignment2', 
    material='steel', thickness=2.0)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=258.741, 
    farPlane=366.079, width=387.366, height=146.154, viewOffsetX=50.2511, 
    viewOffsetY=-8.7096)
p = mdb.models['Model-1'].parts['assignment2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['assignment2']
p.SectionAssignment(region=region, sectionName='Section_assignment2', 
    offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['assignment2']
a.Instance(name='assignment2-1', part=p, dependent=ON)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=280.712, 
    farPlane=344.108, width=282.636, height=106.64, viewOffsetX=-2.21603, 
    viewOffsetY=0.0506973)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'U', 'RF', 'NFORC'))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['assignment2-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
region = a.Set(edges=edges1, name='Set-1')
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=307.605, 
    farPlane=317.215, width=41.0743, height=15.4975, viewOffsetX=-40.0099, 
    viewOffsetY=45.2384)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=284.224, 
    farPlane=340.596, width=250.363, height=94.4629, viewOffsetX=-18.5576, 
    viewOffsetY=49.0193)
session.viewports['Viewport: 1'].view.setValues(nearPlane=283.753, 
    farPlane=341.067, width=249.949, height=94.3066, cameraPosition=(-10, 
    15.2528, 312.41), cameraTarget=(-10, 15.2528, 0), viewOffsetX=-18.5269, 
    viewOffsetY=48.9381)
session.viewports['Viewport: 1'].view.setValues(nearPlane=283.749, 
    farPlane=341.071, width=249.945, height=94.3051, cameraPosition=(-10, 
    5.10606, 312.41), cameraTarget=(-10, 5.10606, 0), viewOffsetX=-18.5266, 
    viewOffsetY=48.9373)
session.viewports['Viewport: 1'].view.setValues(nearPlane=281.413, 
    farPlane=343.407, width=233.722, height=88.1842, viewOffsetX=13.9958, 
    viewOffsetY=14.2148)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['assignment2-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#10 ]', ), )
region = a.Set(vertices=verts1, name='Set-2')
mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1', 
    region=region, cf2=-250.0, distributionType=UNIFORM, field='', 
    localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=287.221, 
    farPlane=337.599, width=215.627, height=81.3567, viewOffsetX=10.438, 
    viewOffsetY=12.5592)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['assignment2-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#8 ]', ), )
region = a.Set(vertices=verts1, name='Set-3')
mdb.models['Model-1'].ConcentratedForce(name='Load-2', createStepName='Step-1', 
    region=region, cf2=-250.0, distributionType=UNIFORM, field='', 
    localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=266.601, 
    farPlane=358.219, width=392.656, height=148.15, viewOffsetX=11.7828, 
    viewOffsetY=9.44188)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
p1 = mdb.models['Model-1'].parts['assignment2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].materials['steel'].Elastic(table=((210000.0, 0.3), ))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=268.477, 
    farPlane=356.343, width=441.003, height=166.923, viewOffsetX=-69.2108, 
    viewOffsetY=35.9757)
p = mdb.models['Model-1'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#9 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=5, constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=279.245, 
    farPlane=345.575, width=283.139, height=107.17, viewOffsetX=-38.5249, 
    viewOffsetY=0.645443)
p = mdb.models['Model-1'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#30 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=25, constraint=FINER)
p = mdb.models['Model-1'].parts['assignment2']
p.generateMesh()
elemType1 = mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['assignment2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
p = mdb.models['Model-1'].parts['assignment2']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['assignment2']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(
    -30.0, 5.0, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=312.4, gridSpacing=7.81, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['assignment2']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=299.107, 
    farPlane=325.713, width=113.687, height=42.8943, cameraPosition=(-31.0152, 
    -5.96943, 312.41), cameraTarget=(-31.0152, -5.96943, 0))
s1.Line(point1=(-20.0, -10.0), point2=(-20.0, -30.0))
s1.VerticalConstraint(entity=g[8], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[6], entity2=g[8], addUndoState=False)
s1.CoincidentConstraint(entity1=v[6], entity2=g[4], addUndoState=False)
s1.Line(point1=(-20.0, -30.0), point2=(-20.0, -10.0))
s1.VerticalConstraint(entity=g[9], addUndoState=False)
s1.ParallelConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s1.Line(point1=(-20.0, -10.0), point2=(-40.0, -10.0))
s1.HorizontalConstraint(entity=g[10], addUndoState=False)
s1.ParallelConstraint(entity1=g[6], entity2=g[10], addUndoState=False)
s1.CoincidentConstraint(entity1=v[7], entity2=g[3], addUndoState=False)
s1.Line(point1=(-40.0, -10.0), point2=(-20.0, -10.0))
s1.HorizontalConstraint(entity=g[11], addUndoState=False)
s1.ParallelConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
s1.Line(point1=(-20.0, -10.0), point2=(-40.0, -30.0))
p = mdb.models['Model-1'].parts['assignment2']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=276.097, 
    farPlane=348.723, width=321.355, height=121.635, viewOffsetX=19.7328, 
    viewOffsetY=-6.39558)
p = mdb.models['Model-1'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#41 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=5, constraint=FINER)
p = mdb.models['Model-1'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#108 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=25, constraint=FINER)
p = mdb.models['Model-1'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#90 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=5, constraint=FINER)
p = mdb.models['Model-1'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#20 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=5, constraint=FINER)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
p = mdb.models['Model-1'].parts['assignment2']
p.generateMesh()
p = mdb.models['Model-1'].parts['assignment2']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#f ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['assignment2']
f1, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
    -60.0, 35.0, 0.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=312.4, gridSpacing=7.81, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['assignment2']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=146.013, 
    farPlane=183.835, width=161.615, height=60.9779, cameraPosition=(-50.4252, 
    -1.24521, 164.924), cameraTarget=(-50.4252, -1.24521, 0))
s.delete(objectList=(g[8], ))
s.delete(objectList=(g[10], ))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=151.34, 
    farPlane=178.509, width=116.094, height=43.8027, cameraPosition=(-30.0025, 
    -5.39143, 164.924), cameraTarget=(-30.0025, -5.39143, 0))
s.Line(point1=(10.0, -40.0), point2=(-10.0, -60.0))
s.delete(objectList=(g[16], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=128.964, 
    farPlane=200.885, width=319.994, height=120.735, cameraPosition=(36.9739, 
    -0.174753, 164.924), cameraTarget=(36.9739, -0.174753, 0))
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['assignment2']
f, e1, d2 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(
    -60.0, 35.0, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=312.4, gridSpacing=7.81, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['assignment2']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=147.735, 
    farPlane=182.113, width=146.898, height=55.4253, cameraPosition=(-42.6697, 
    -2.45568, 164.924), cameraTarget=(-42.6697, -2.45568, 0))
s1.delete(objectList=(g[8], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=160.562, 
    farPlane=169.287, width=37.2828, height=14.0669, cameraPosition=(-54.3379, 
    -11.7733, 164.924), cameraTarget=(-54.3379, -11.7733, 0))
s1.delete(objectList=(g[10], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=129.767, 
    farPlane=200.081, width=312.848, height=118.039, cameraPosition=(11.6456, 
    20.3001, 164.924), cameraTarget=(11.6456, 20.3001, 0))
s1.delete(objectList=(g[2], ))
s1.delete(objectList=(g[6], g[9], g[9]))
s1.delete(objectList=(g[12], ))
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
p = mdb.models['Model-1'].parts['assignment2']
s = p.features['Partition face-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s2 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Partition face-1'], filter=COPLANAR_EDGES)
s2.delete(objectList=(g[12], ))
s2.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['assignment2']
p.features['Partition face-1'].setValues(sketch=s2)
del mdb.models['Model-1'].sketches['__edit__']
p = mdb.models['Model-1'].parts['assignment2']
p.regenerate()
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#80 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=25, constraint=FINER)
p = mdb.models['Model-1'].parts['assignment2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#60 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=5, constraint=FINER)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
p = mdb.models['Model-1'].parts['assignment2']
p.generateMesh()
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
elemType1 = mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['assignment2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Global_Model', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['Global_Model'].submit(consistencyChecking=OFF)
#: The job input file "Global_Model.inp" has been submitted for analysis.
#: Job Global_Model: Analysis Input File Processor completed successfully.
#: Job Global_Model: Abaqus/Standard completed successfully.
#: Job Global_Model completed successfully. 
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
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Global_Model.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL), ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=344.649, 
    farPlane=538.98, width=121.866, height=43.2642, viewOffsetX=-29.4612, 
    viewOffsetY=-19.0172)
session.Path(name='AB_line', type=NODE_LIST, expression=(('ASSIGNMENT2-1', (2, 
    6, )), ))
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['AB_line']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Global_Model.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.Path(name='ab_line2', type=NODE_LIST, expression=(('ASSIGNMENT2-1', (6, 
    2, )), ))
del session.paths['AB_line']
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['ab_line2']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
pth = session.paths['ab_line2']
session.XYDataFromPath(name='XYData-1', path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Global_Model.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL), ))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
x0 = chart.curves['_temp_2']
session.writeXYReport(fileName='AB_line.rpt', xyData=(x0, ))
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/Global_Model.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'), )), ))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
del session.viewports['Viewport: 1']
#* CanvasError: SystemError: the current viewport may not be deleted.
del session.viewports['Viewport: 1']
#* CanvasError: SystemError: the current viewport may not be deleted.
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment2/assignement2.cae".
