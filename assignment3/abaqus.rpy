# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Mon Apr 30 13:57:09 2018
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
    pathName='/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/assignment3.cae')
#: The model database "/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/assignment3.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].materials['Material-plate'].plastic.setValues(table=((
    50.0, 0.0), (220.0, 0.003142857), (240.0, 3.41071e-05), (260.0, 
    0.00031343), (280.0, 0.001147183), (300.0, 0.002880294), (320.0, 
    0.005882323), (340.0, 0.010542141), (360.0, 0.017264681), (380.0, 
    0.026468711), (400.0, 0.03858521), (420.0, 0.054056115), (440.0, 
    0.073333333), (460.0, 0.096877923), (480.0, 0.125159425), (500.0, 
    0.158655287), (520.0, 0.197850368), (540.0, 0.243236518), (560.0, 
    0.295312195), (580.0, 0.354582134), (600.0, 0.42155705), (620.0, 
    0.496753367), (640.0, 0.580692981), (660.0, 0.673903035), (680.0, 
    0.77691572), (700.0, 0.87)))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Error in job Job-2: THE INDEPENDENT VARIABLES MUST BE ARRANGED IN ASCENDING ORDER
#: Job Job-2: Analysis Input File Processor aborted due to errors.
#: Error in job Job-2: Analysis Input File Processor exited with an error.
#: Job Job-2 aborted due to errors.
p1 = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].materials['Material-plate'].plastic.setValues(table=((
    50.0, 0.0), (220.0, 3.01071e-05), (240.0, 3.41071e-05), (260.0, 
    0.00031343), (280.0, 0.001147183), (300.0, 0.002880294), (320.0, 
    0.005882323), (340.0, 0.010542141), (360.0, 0.017264681), (380.0, 
    0.026468711), (400.0, 0.03858521), (420.0, 0.054056115), (440.0, 
    0.073333333), (460.0, 0.096877923), (480.0, 0.125159425), (500.0, 
    0.158655287), (520.0, 0.197850368), (540.0, 0.243236518), (560.0, 
    0.295312195), (580.0, 0.354582134), (600.0, 0.42155705), (620.0, 
    0.496753367), (640.0, 0.580692981), (660.0, 0.673903035), (680.0, 
    0.77691572), (700.0, 0.87)))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Error in job Job-2: Time increment required is less than the minimum specified
#: Error in job Job-2: Too many attempts made for this increment
#: Error in job Job-2: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.
#: Job Job-2: Abaqus/Standard aborted due to errors.
#: Error in job Job-2: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='My_Step')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].steps['My_Step'].setValues(maxNumInc=5000)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Error in job Job-2: Time increment required is less than the minimum specified
#: Error in job Job-2: Too many attempts made for this increment
#: Error in job Job-2: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.
#: Job Job-2: Abaqus/Standard aborted due to errors.
#: Error in job Job-2: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/Job-2.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment3/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
mdb.models['Model-1'].interactions['Int-1'].setValues(initialClearance=OMIT, 
    surfaceSmoothing=NONE, adjustMethod=NONE, sliding=SMALL, 
    enforcement=NODE_TO_SURFACE, thickness=ON, supplementaryContact=SELECTIVE, 
    smooth=0.2, bondingSet=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Job Job-2: Abaqus/Standard completed successfully.
#: Job Job-2 completed successfully. 
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/Job-2.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment3/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.printToPrinter(printCommand='lpr', numCopies=1, canvasObjects=(
    session.viewports['Viewport: 1'], ))
#* PrintError: invalid print command
session.printToFile(fileName='CPe4_node_to_surface_small_slide', format=PNG, 
    canvasObjects=(session.viewports['Viewport: 1'], ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs.changeKey(fromName='Job-2', toName='cpe4_node_surface_small_sliding')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
mdb.models['Model-1'].interactions['Int-1'].setValues(initialClearance=OMIT, 
    adjustMethod=NONE, sliding=FINITE, enforcement=NODE_TO_SURFACE, 
    thickness=OFF, supplementaryContact=SELECTIVE, smooth=0.2, bondingSet=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.Job(name='cpe4_node_surface_finite_slide', model='Model-1', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['cpe4_node_surface_finite_slide'].submit(consistencyChecking=OFF)
#: The job input file "cpe4_node_surface_finite_slide.inp" has been submitted for analysis.
#: Job cpe4_node_surface_finite_slide: Analysis Input File Processor completed successfully.
#: Error in job cpe4_node_surface_finite_slide: Time increment required is less than the minimum specified
#: Error in job cpe4_node_surface_finite_slide: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.
#: Job cpe4_node_surface_finite_slide: Abaqus/Standard aborted due to errors.
#: Error in job cpe4_node_surface_finite_slide: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job cpe4_node_surface_finite_slide aborted due to errors.
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/Job-2.odb'])
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_finite_slide.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_finite_slide.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.printToFile(fileName='CPe4_node_to_surface_finite_slide', format=PNG, 
    canvasObjects=(session.viewports['Viewport: 1'], ))
