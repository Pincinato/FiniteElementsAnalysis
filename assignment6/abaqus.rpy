# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Mon May 14 09:27:26 2018
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
mdb.models.changeKey(fromName='Model-1', toName='3d-Lagrange')
session.viewports['Viewport: 1'].setValues(displayedObject=None)
mdb.Model(name='3D_lagrange', modelType=STANDARD_EXPLICIT)
#: The model "3D_lagrange" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
del mdb.models['3d-Lagrange']
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['3D_lagrange'].ConstrainedSketch(name='__profile__', 
    sheetSize=100.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(8.0, -12.0), point2=(-38.0, 2.0))
s.HorizontalDimension(vertex1=v[1], vertex2=v[2], textPoint=(-36.0826797485352, 
    7.02277565002441), value=30.0)
s.VerticalDimension(vertex1=v[2], vertex2=v[3], textPoint=(-27.5657978057861, 
    -11.2744026184082), value=20.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=81.9341, 
    farPlane=106.628, width=109.868, height=40.3167, cameraPosition=(3.91485, 
    -1.54235, 94.2809), cameraTarget=(3.91485, -1.54235, 0))
mdb.saveAs(
    pathName='/home/fe1/Desktop/FiniteElementsAnalysis/assignment6/ass6')
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment6/ass6.cae".
p = mdb.models['3D_lagrange'].Part(name='Lagrange', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['3D_lagrange'].parts['Lagrange']
p.BaseSolidExtrude(sketch=s, depth=2.0)
s.unsetPrimaryObject()
p = mdb.models['3D_lagrange'].parts['Lagrange']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['3D_lagrange'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=54.6857, 
    farPlane=99.3037, width=66.1351, height=24.2686, viewOffsetX=-0.806142, 
    viewOffsetY=0.972661)
p = mdb.models['3D_lagrange'].parts['Lagrange']
v1 = p.vertices
p.DatumPointByOffset(point=v1[6], vector=(0.0, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
p.DatumPointByCoordinate(coords=(-4.0, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
p.DatumPointByCoordinate(coords=(-4.0, 15.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
p.DatumPointByCoordinate(coords=(-19.0, 0.0, 0.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=54.1204, 
    farPlane=91.398, width=65.4514, height=24.0177, cameraPosition=(4.92594, 
    35.9959, 62.5127), cameraUpVector=(-0.120109, 0.57735, -0.807614), 
    cameraTarget=(-4.32185, -8.457, 0.330669), viewOffsetX=-0.797808, 
    viewOffsetY=0.962605)
p = mdb.models['3D_lagrange'].parts['Lagrange']
del p.features['Datum pt-1']
p = mdb.models['3D_lagrange'].parts['Lagrange']
del p.features['Datum pt-2']
p = mdb.models['3D_lagrange'].parts['Lagrange']
del p.features['Datum pt-3']
p = mdb.models['3D_lagrange'].parts['Lagrange']
del p.features['Datum pt-4']
session.viewports['Viewport: 1'].view.setValues(nearPlane=54.5406, 
    farPlane=97.0398, width=65.9596, height=24.2042, cameraPosition=(-37.4404, 
    35.9959, 54.7195), cameraUpVector=(0.424768, 0.57735, -0.697308), 
    cameraTarget=(-4.73552, -8.457, 1.03045), viewOffsetX=-0.804002, 
    viewOffsetY=0.970079)
p = mdb.models['3D_lagrange'].parts['Lagrange']
v2 = p.vertices
p.DatumPointByOffset(point=v2[3], vector=(0.0, 0.0, 0.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.7851, 
    farPlane=91.5517, width=73.5115, height=26.9754, cameraPosition=(-10.3938, 
    35.9959, 63.1263), cameraUpVector=(0.0744035, 0.57735, -0.813099), 
    cameraTarget=(-4.66512, -8.457, 0.521933), viewOffsetX=-0.896054, 
    viewOffsetY=1.08115)
p = mdb.models['3D_lagrange'].parts['Lagrange']
p.DatumPointByCoordinate(coords=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
del p.features['Datum pt-2']
p = mdb.models['3D_lagrange'].parts['Lagrange']
del p.features['Datum pt-1']
session.viewports['Viewport: 1'].view.setValues(nearPlane=53.4121, 
    farPlane=98.1015, width=64.5948, height=23.7034, cameraPosition=(-43.9987, 
    35.9959, 50.37), cameraUpVector=(0.507029, 0.57735, -0.63999), 
    cameraTarget=(-4.96014, -8.457, 1.09407), viewOffsetX=-0.787366, 
    viewOffsetY=0.95001)
p = mdb.models['3D_lagrange'].parts['Lagrange']
v1 = p.vertices
p.DatumPointByOffset(point=v1[1], vector=(0.0, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
del p.features['Datum pt-1']
p = mdb.models['3D_lagrange'].parts['Lagrange']
v2 = p.vertices
p.DatumPointByOffset(point=v2[1], vector=(0.0, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
v1, d1 = p.vertices, p.datums
p.DatumPointByOffset(point=d1[9], vector=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
d2 = p.datums
p.DatumPointByOffset(point=d2[10], vector=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
d1 = p.datums
p.DatumPointByOffset(point=d1[11], vector=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
d2 = p.datums
p.DatumPointByOffset(point=d2[9], vector=(0.0, -15.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
d1 = p.datums
p.DatumPointByOffset(point=d1[13], vector=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
d2 = p.datums
p.DatumPointByOffset(point=d2[14], vector=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
d1 = p.datums
p.DatumPointByOffset(point=d1[15], vector=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
p.deleteFeatures(('Datum pt-5', 'Datum pt-6', 'Datum pt-7', 'Datum pt-8', ))
p = mdb.models['3D_lagrange'].parts['Lagrange']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e, v2, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlaneNormalToEdge(edge=e[4], point=d2[10], cells=pickedCells)
p = mdb.models['3D_lagrange'].parts['Lagrange']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
e1, v1, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlaneNormalToEdge(edge=e1[7], point=d1[11], cells=pickedCells)
p = mdb.models['3D_lagrange'].parts['Lagrange']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#4 ]', ), )
e, v2, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlaneNormalToEdge(edge=e[19], point=d2[12], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=54.2033, 
    farPlane=97.3103, width=65.5517, height=24.0545, cameraPosition=(-42.6466, 
    35.9959, 51.4412), cameraTarget=(-3.60807, -8.457, 2.16524), 
    viewOffsetX=-0.799029, viewOffsetY=0.964083)
session.viewports['Viewport: 1'].view.setValues(width=66.6229, height=24.4476, 
    cameraPosition=(-4.62798, -6.64211, 77.411), cameraUpVector=(0, 1, 0), 
    cameraTarget=(-4.62798, -6.64211, 1.65424), viewOffsetX=0, viewOffsetY=0)
p = mdb.models['3D_lagrange'].parts['Lagrange']
v1 = p.vertices
p.DatumPointByOffset(point=v1[18], vector=(0.0, 4.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
v2, d1 = p.vertices, p.datums
p.DatumPointByOffset(point=d1[20], vector=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
v1, d2 = p.vertices, p.datums
p.DatumPointByOffset(point=d2[21], vector=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
v2, d1 = p.vertices, p.datums
p.DatumPointByOffset(point=d1[22], vector=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
v1, d2 = p.vertices, p.datums
p.DatumPointByOffset(point=d2[23], vector=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
v2, d1 = p.vertices, p.datums
p.DatumPointByOffset(point=d1[9], vector=(0.0, -1.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
v1, d2 = p.vertices, p.datums
p.DatumPointByOffset(point=d2[25], vector=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
v2, d1 = p.vertices, p.datums
p.DatumPointByOffset(point=d1[26], vector=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
v1, d2 = p.vertices, p.datums
p.DatumPointByOffset(point=d2[27], vector=(7.5, 0.0, 0.0))
p = mdb.models['3D_lagrange'].parts['Lagrange']
v2, d1 = p.vertices, p.datums
p.DatumPointByOffset(point=d1[28], vector=(7.5, 0.0, 0.0))
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment6/ass6.cae".
p = mdb.models['3D_lagrange'].parts['Lagrange']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#4 ]', ), )
e1, v1, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlaneNormalToEdge(edge=e1[32], point=d2[25], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65.862, 
    farPlane=86.96, width=80.9266, height=29.6964, cameraUpVector=(0.0314616, 
    0.999505, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.0931, 
    farPlane=86.7289, width=81.2106, height=29.8007, cameraPosition=(-4.04597, 
    -6.64211, 77.411), cameraTarget=(-4.04597, -6.64211, 1.65424))
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.0977, 
    farPlane=86.7243, width=81.2163, height=29.8028, cameraPosition=(-4.04597, 
    -6.58156, 77.411), cameraTarget=(-4.04597, -6.58156, 1.65424))
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.0978, 
    farPlane=86.7242, width=81.2165, height=29.8028, cameraUpVector=(0.0121523, 
    0.999926, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=65.5657, 
    farPlane=87.2563, width=91.098, height=33.4289, viewOffsetX=-1.09317, 
    viewOffsetY=-0.0793015)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65.0604, 
    farPlane=87.7616, width=90.396, height=33.1713, cameraPosition=(-4.04597, 
    -7.44543, 77.411), cameraTarget=(-4.04597, -7.44543, 1.65424), 
    viewOffsetX=-1.08474, viewOffsetY=-0.0786904)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.8321, 
    farPlane=96.9646, width=78.9634, height=28.976, cameraPosition=(-0.0953155, 
    56.4634, 42.4583), cameraUpVector=(0.111694, 0.534945, -0.837471), 
    cameraTarget=(-4.01253, -7.05672, 1.36159), viewOffsetX=-0.94755, 
    viewOffsetY=-0.0687382)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.6698, 
    farPlane=92.7948, width=84.2956, height=30.9327, cameraPosition=(-3.83112, 
    37.826, 62.5339), cameraUpVector=(0.0604946, 0.802217, -0.59396), 
    cameraTarget=(-4.06539, -7.24141, 1.64089), viewOffsetX=-1.01154, 
    viewOffsetY=-0.0733799)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52.9697, 
    farPlane=99.0236, width=73.597, height=27.0068, cameraPosition=(-39.1387, 
    37.826, 52.4758), cameraUpVector=(0.387272, 0.802217, -0.454388), 
    cameraTarget=(-4.73167, -7.24141, 2.23469), viewOffsetX=-0.883158, 
    viewOffsetY=-0.0640667)
p = mdb.models['3D_lagrange'].parts['Lagrange']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#4 ]', ), )
e, v2, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlaneNormalToEdge(edge=e[10], point=d1[26], cells=pickedCells)
p = mdb.models['3D_lagrange'].parts['Lagrange']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#4 ]', ), )
e1, v1, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlaneNormalToEdge(edge=e1[7], point=d2[27], cells=pickedCells)
p = mdb.models['3D_lagrange'].parts['Lagrange']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#40 ]', ), )
e, v2, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlaneNormalToEdge(edge=e[7], point=d1[28], cells=pickedCells)
p = mdb.models['3D_lagrange'].parts['Lagrange']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#8 ]', ), )
e1, v1, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlaneNormalToEdge(edge=e1[58], point=d2[20], 
    cells=pickedCells)
p = mdb.models['3D_lagrange'].parts['Lagrange']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#8 ]', ), )
e, v2, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlaneNormalToEdge(edge=e[4], point=d1[21], cells=pickedCells)
p = mdb.models['3D_lagrange'].parts['Lagrange']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#8 ]', ), )
e1, v1, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlaneNormalToEdge(edge=e1[49], point=d2[22], 
    cells=pickedCells)
p = mdb.models['3D_lagrange'].parts['Lagrange']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#400 ]', ), )
e, v2, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlaneNormalToEdge(edge=e[43], point=d1[23], cells=pickedCells)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment6/ass6.cae".
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['3D_lagrange'].Material(name='Material-lagrange')
mdb.models['3D_lagrange'].materials['Material-lagrange'].Elastic(table=((
    210000.0, 0.266), ))
mdb.models['3D_lagrange'].materials['Material-lagrange'].Density(table=((7.85, 
    ), ))
mdb.models['3D_lagrange'].materials['Material-lagrange'].Plastic(table=((300.0, 
    0.0), (450.0, 0.02), (750.0, 0.34), (1400.0, 0.35)))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
mdb.models['3D_lagrange'].parts.changeKey(fromName='Lagrange', 
    toName='Eulerian')
s1 = mdb.models['3D_lagrange'].ConstrainedSketch(name='__profile__', 
    sheetSize=100.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.unsetPrimaryObject()
del mdb.models['3D_lagrange'].sketches['__profile__']
p1 = mdb.models['3D_lagrange'].parts['Eulerian']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['3D_lagrange'].parts['Eulerian'].setValues(space=THREE_D, 
    type=EULERIAN)
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment6/ass6.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment6/ass6.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment6/ass6.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment6/ass6.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment6/ass6.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/Desktop/FiniteElementsAnalysis/assignment6/ass6.cae".
