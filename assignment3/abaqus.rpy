# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Wed May  2 20:47:23 2018
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
#--- Recover file: 'assignment3.rec' ---
# -*- coding: mbcs -*- 
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].interactionProperties['IntProp-1'].tangentialBehavior.setValues(
    formulation=FRICTIONLESS)
mdb.models['Model-1'].interactionProperties['IntProp-1'].normalBehavior.setValues(
    allowSeparation=OFF, constraintEnforcementMethod=DEFAULT, 
    pressureOverclosure=HARD)
mdb.jobs['cpe4_surfaceToSurface_finite_sliding'].submit(
    consistencyChecking=OFF)
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STARTED, {
    'phase': BATCHPRE_PHASE, 'clientHost': 'localhost.localdomain', 
    'handle': 0, 'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(WARNING, {
    'phase': BATCHPRE_PHASE, 
    'message': 'FOR TWO-DIMENSIONAL MODELS, IF A NON-UNITY THICKNESS IS SPECIFIED FOR TWO-DIMENSIONAL SOLID ELEMENTS AND THESE ELEMENTS ARE INVOLVED IN AN INTERACTION SUCH AS CONTACT, THE SAME THICKNESS SHOULD BE SPECIFIED FOR THE OUT-OF-PLANE THICKNESS OF THE CORRESPONDING SURFACE UNDER *SURFACE INTERACTION.', 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(WARNING, {
    'phase': BATCHPRE_PHASE, 
    'message': 'PATH BASED TRACKING IS DEFINED IN CONTACT PAIR (ASSEMBLY_S_SURF-1,ASSEMBLY_RIGID_PRESS-1_SURF-3). PATH BASED TRACKING CANNOT BE USED WITH ANALYTICAL RIGID MASTER SURFACES, THE STATE BASED TRACKING ALGORITHM WILL BE USED INSTEAD.', 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': '/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_surfaceToSurface_finite_sliding.odb', 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STARTED, {
    'phase': STANDARD_PHASE, 'clientHost': 'localhost.localdomain', 
    'handle': 0, 'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'cpe4_surfaceToSurface_finite_sliding', 
    'memory': 24.0})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 168 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 174 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 172 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 176 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 158 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STATUS, {
    'totalTime': 0.0, 'attempts': ' 1U', 'timeIncrement': 0.1, 'increment': 1, 
    'stepTime': 0.0, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding', 'severe': 1, 
    'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STATUS, {
    'totalTime': 0.025, 'attempts': 2, 'timeIncrement': 0.025, 'increment': 1, 
    'stepTime': 0.025, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding', 'severe': 1, 
    'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 2, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STATUS, {
    'totalTime': 0.05, 'attempts': 1, 'timeIncrement': 0.025, 'increment': 2, 
    'stepTime': 0.05, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding', 'severe': 0, 
    'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'FORCE equilibrium accepted using the alternate tolerance.', 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 3, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STATUS, {
    'totalTime': 0.0875, 'attempts': 1, 'timeIncrement': 0.0375, 
    'increment': 3, 'stepTime': 0.0875, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding', 'severe': 0, 
    'iterations': 13, 'phase': STANDARD_PHASE, 'equilibrium': 13})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STATUS, {
    'totalTime': 0.0875, 'attempts': ' 1U', 'timeIncrement': 0.0125, 
    'increment': 4, 'stepTime': 0.0875, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 4, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STATUS, {
    'totalTime': 0.090625, 'attempts': 2, 'timeIncrement': 0.003125, 
    'increment': 4, 'stepTime': 0.090625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 5, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STATUS, {
    'totalTime': 0.09375, 'attempts': 1, 'timeIncrement': 0.003125, 
    'increment': 5, 'stepTime': 0.09375, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 6, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STATUS, {
    'totalTime': 0.0984375, 'attempts': 1, 'timeIncrement': 0.0046875, 
    'increment': 6, 'stepTime': 0.0984375, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding', 'severe': 0, 
    'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STATUS, {
    'totalTime': 0.0984375, 'attempts': ' 1U', 
    'timeIncrement': 0.00156249999999999, 'increment': 7, 
    'stepTime': 0.0984375, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding', 'severe': 0, 
    'iterations': 9, 'phase': STANDARD_PHASE, 'equilibrium': 9})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 7, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STATUS, {
    'totalTime': 0.09921875, 'attempts': 2, 
    'timeIncrement': 0.000781249999999997, 'increment': 7, 
    'stepTime': 0.09921875, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding', 'severe': 0, 
    'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 8, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(STATUS, {
    'totalTime': 0.1, 'attempts': 1, 'timeIncrement': 0.000781249999999997, 
    'increment': 8, 'stepTime': 0.1, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding', 'severe': 0, 
    'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.jobs['cpe4_surfaceToSurface_finite_sliding']._Message(JOB_COMPLETED, {
    'time': 'Mon Apr 30 23:23:28 2018', 
    'jobName': 'cpe4_surfaceToSurface_finite_sliding'})
mdb.models['Model-1'].interactionProperties['IntProp-1'].tangentialBehavior.setValues(
    formulation=FRICTIONLESS)
mdb.models['Model-1'].interactionProperties['IntProp-1'].normalBehavior.setValues(
    allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
    pressureOverclosure=HARD)
mdb.models['Model-1'].interactions['Int-1'].setValues(adjustMethod=NONE, 
    bondingSet=None, enforcement=SURFACE_TO_SURFACE, initialClearance=OMIT, 
    sliding=SMALL, supplementaryContact=SELECTIVE, thickness=ON)
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='cpe4_surfaceToSurface_smal_sliding', 
    nodalOutputPrecision=SINGLE, numCpus=1, numGPUs=0, queue=None, 
    resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='', 
    waitHours=0, waitMinutes=0)
mdb.jobs['cpe4_surfaceToSurface_smal_sliding'].submit(consistencyChecking=OFF)
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STARTED, {
    'phase': BATCHPRE_PHASE, 'clientHost': 'localhost.localdomain', 
    'handle': 0, 'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': BATCHPRE_PHASE, 
    'message': 'FOR TWO-DIMENSIONAL MODELS, IF A NON-UNITY THICKNESS IS SPECIFIED FOR TWO-DIMENSIONAL SOLID ELEMENTS AND THESE ELEMENTS ARE INVOLVED IN AN INTERACTION SUCH AS CONTACT, THE SAME THICKNESS SHOULD BE SPECIFIED FOR THE OUT-OF-PLANE THICKNESS OF THE CORRESPONDING SURFACE UNDER *SURFACE INTERACTION.', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': BATCHPRE_PHASE, 
    'message': '46 SLAVE NODES FOR SURFACE PAIR (ASSEMBLY_S_SURF-1,ASSEMBLY_RIGID_PRESS-1_SURF-3) ARE REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND SOME NODES TO FORM THE CONSTRAINT. SOME OF REASONS ARE: THE SLAVE IS COARSER OR LARGER THAN THE MASTER SURFACE, THE SLAVE IS NOT FLAT RELATIVE TO THE MASTER SURFACE, OR SLAVE NODES THAT ARE BEYOND THE EXTENT OF THE MASTER SURFACE.', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': '/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_surfaceToSurface_smal_sliding.odb', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STARTED, {
    'phase': STANDARD_PHASE, 'clientHost': 'localhost.localdomain', 
    'handle': 0, 'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'cpe4_surfaceToSurface_smal_sliding', 
    'memory': 24.0})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 300 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 196 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.0, 'attempts': ' 1U', 'timeIncrement': 0.1, 'increment': 1, 
    'stepTime': 0.0, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 246 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 243 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 287 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 10 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.0, 'attempts': ' 2U', 'timeIncrement': 0.025, 
    'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 1, 
    'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 168 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 99 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 145 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 160 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.0, 'attempts': ' 3U', 'timeIncrement': 0.00625, 
    'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 22 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 108 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 4 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.0, 'attempts': ' 4U', 'timeIncrement': 0.0015625, 
    'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 1, 
    'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000390625, 'attempts': 5, 'timeIncrement': 0.000390625, 
    'increment': 1, 'stepTime': 0.000390625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 1 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 36 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 3 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 12 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000390625, 'attempts': ' 1U', 'timeIncrement': 0.000390625, 
    'increment': 2, 'stepTime': 0.000390625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 2, 
    'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 2, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.00048828125, 'attempts': 2, 'timeIncrement': 9.765625e-05, 
    'increment': 2, 'stepTime': 0.00048828125, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 3, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': 1, 
    'timeIncrement': 0.000146484375, 'increment': 3, 
    'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': ' 1U', 
    'timeIncrement': 0.0002197265625, 'increment': 4, 
    'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': ' 2U', 
    'timeIncrement': 5.4931640625e-05, 'increment': 4, 
    'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': ' 3U', 
    'timeIncrement': 1.373291015625e-05, 'increment': 4, 
    'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': ' 4U', 
    'timeIncrement': 3.4332275390625e-06, 'increment': 4, 
    'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ERROR, {
    'phase': STANDARD_PHASE, 
    'message': 'Time increment required is less than the minimum specified', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': ' 5U', 'timeIncrement': 1e-06, 
    'increment': 4, 'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ERROR, {
    'phase': STANDARD_PHASE, 
    'message': 'Too many attempts made for this increment', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 4, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': 6, 'timeIncrement': 1e-35, 
    'increment': 4, 'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 1, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ERROR, {
    'phase': STANDARD_PHASE, 
    'message': 'THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ABORTED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase failed due to errors', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.models['Model-1'].steps['My_Step'].setValues(maxNumInc=20000)
mdb.jobs['cpe4_surfaceToSurface_smal_sliding'].submit(consistencyChecking=OFF)
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STARTED, {
    'phase': BATCHPRE_PHASE, 'clientHost': 'localhost.localdomain', 
    'handle': 0, 'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': BATCHPRE_PHASE, 
    'message': 'FOR TWO-DIMENSIONAL MODELS, IF A NON-UNITY THICKNESS IS SPECIFIED FOR TWO-DIMENSIONAL SOLID ELEMENTS AND THESE ELEMENTS ARE INVOLVED IN AN INTERACTION SUCH AS CONTACT, THE SAME THICKNESS SHOULD BE SPECIFIED FOR THE OUT-OF-PLANE THICKNESS OF THE CORRESPONDING SURFACE UNDER *SURFACE INTERACTION.', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': BATCHPRE_PHASE, 
    'message': '46 SLAVE NODES FOR SURFACE PAIR (ASSEMBLY_S_SURF-1,ASSEMBLY_RIGID_PRESS-1_SURF-3) ARE REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND SOME NODES TO FORM THE CONSTRAINT. SOME OF REASONS ARE: THE SLAVE IS COARSER OR LARGER THAN THE MASTER SURFACE, THE SLAVE IS NOT FLAT RELATIVE TO THE MASTER SURFACE, OR SLAVE NODES THAT ARE BEYOND THE EXTENT OF THE MASTER SURFACE.', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': '/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_surfaceToSurface_smal_sliding.odb', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STARTED, {
    'phase': STANDARD_PHASE, 'clientHost': 'localhost.localdomain', 
    'handle': 0, 'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'cpe4_surfaceToSurface_smal_sliding', 
    'memory': 24.0})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 300 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 196 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.0, 'attempts': ' 1U', 'timeIncrement': 0.1, 'increment': 1, 
    'stepTime': 0.0, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 246 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 243 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 287 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 10 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.0, 'attempts': ' 2U', 'timeIncrement': 0.025, 
    'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 1, 
    'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 168 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 99 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 145 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 160 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.0, 'attempts': ' 3U', 'timeIncrement': 0.00625, 
    'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 22 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 108 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 4 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.0, 'attempts': ' 4U', 'timeIncrement': 0.0015625, 
    'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 1, 
    'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000390625, 'attempts': 5, 'timeIncrement': 0.000390625, 
    'increment': 1, 'stepTime': 0.000390625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 1 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 36 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 3 POINTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(WARNING, {
    'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 12 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000390625, 'attempts': ' 1U', 'timeIncrement': 0.000390625, 
    'increment': 2, 'stepTime': 0.000390625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 2, 
    'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 2, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.00048828125, 'attempts': 2, 'timeIncrement': 9.765625e-05, 
    'increment': 2, 'stepTime': 0.00048828125, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 3, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': 1, 
    'timeIncrement': 0.000146484375, 'increment': 3, 
    'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': ' 1U', 
    'timeIncrement': 0.0002197265625, 'increment': 4, 
    'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': ' 2U', 
    'timeIncrement': 5.4931640625e-05, 'increment': 4, 
    'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': ' 3U', 
    'timeIncrement': 1.373291015625e-05, 'increment': 4, 
    'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': ' 4U', 
    'timeIncrement': 3.4332275390625e-06, 'increment': 4, 
    'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ERROR, {
    'phase': STANDARD_PHASE, 
    'message': 'Time increment required is less than the minimum specified', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': ' 5U', 'timeIncrement': 1e-06, 
    'increment': 4, 'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ERROR, {
    'phase': STANDARD_PHASE, 
    'message': 'Too many attempts made for this increment', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 4, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(STATUS, {
    'totalTime': 0.000634765625, 'attempts': 6, 'timeIncrement': 1e-35, 
    'increment': 4, 'stepTime': 0.000634765625, 'step': 1, 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding', 'severe': 1, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ERROR, {
    'phase': STANDARD_PHASE, 
    'message': 'THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ABORTED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase failed due to errors', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.jobs['cpe4_surfaceToSurface_smal_sliding']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'cpe4_surfaceToSurface_smal_sliding'})
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', 
    objectToCopy=mdb.models['Model-1'].parts['rigid_press'].features['2D Analytic rigid shell-1'].sketch)
mdb.models['Model-1'].parts['rigid_press'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=mdb.models['Model-1'].parts['rigid_press'].features['2D Analytic rigid shell-1'])
mdb.models['Model-1'].sketches['__edit__'].FilletByRadius(
    curve1=mdb.models['Model-1'].sketches['__edit__'].geometry[2], 
    curve2=mdb.models['Model-1'].sketches['__edit__'].geometry[5], nearPoint1=(
    -550.387939453125, -164.071395874023), nearPoint2=(-479.720825195312, 
    -198.682830810547), radius=3.01)
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].dimensions[3], ))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].dimensions[4], ))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].dimensions[2], ))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].constraints[21], ))
mdb.models['Model-1'].sketches['__edit__'].FilletByRadius(
    curve1=mdb.models['Model-1'].sketches['__edit__'].geometry[5], 
    curve2=mdb.models['Model-1'].sketches['__edit__'].geometry[4], nearPoint1=(
    -273.035217285156, -199.851470947266), nearPoint2=(-249.344161987305, 
    -181.967391967773), radius=3.01)
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[7], ))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[9], ))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[6], ))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[8], ))
#--- End of Recover file ------
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=3765.91, 
    farPlane=5636.21, width=197.657, height=68.1259, viewOffsetX=3.54547, 
    viewOffsetY=-145.822)
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_finite_slide.odb']
session.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('PEEQ', INTEGRATION_POINT), ('PEMAG', INTEGRATION_POINT), ('S', 
    INTEGRATION_POINT, ((INVARIANT, 'Mises'), )), ), elementPick=((
    'RIGID_PRESS-1', 1, ('[#4 ]', )), ), )
#* VisError: No xy data was extracted using the provided options.
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_finite_slide.odb']
session.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('PEEQ', INTEGRATION_POINT), ('PEMAG', INTEGRATION_POINT), ('S', 
    INTEGRATION_POINT, ((INVARIANT, 'Mises'), )), ), elementPick=((
    'RIGID_PRESS-1', 1, ('[#4 ]', )), ), )
#* VisError: No xy data was extracted using the provided options.
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_finite_slide.odb']
session.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('PEEQ', INTEGRATION_POINT), ('PEMAG', INTEGRATION_POINT), ('S', 
    INTEGRATION_POINT, ((INVARIANT, 'Mises'), )), ), elementPick=((
    'RIGID_PRESS-1', 1, ('[#4 ]', )), ), )
#* VisError: No xy data was extracted using the provided options.
session.viewports['Viewport: 1'].view.setValues(nearPlane=3777.67, 
    farPlane=5624.46, width=127.128, height=43.8168, viewOffsetX=1.09413, 
    viewOffsetY=-150.761)
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_finite_slide.odb']
session.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('PEEQ', INTEGRATION_POINT), ('PEMAG', INTEGRATION_POINT), ('S', 
    INTEGRATION_POINT, ((INVARIANT, 'Mises'), )), ), elementPick=(('PLATE-1', 
    1, ('[#0:4 #1000 ]', )), ), )
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_finite_slide.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('PEEQ', INTEGRATION_POINT), ('PEMAG', INTEGRATION_POINT), ('S', 
    INTEGRATION_POINT, ((INVARIANT, 'Mises'), )), ), elementPick=(('PLATE-1', 
    1, ('[#0:4 #1000 ]', )), ), )
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['_S:Mises PI: PLATE-1 E: 141 IP: 4']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['_S:Mises PI: PLATE-1 E: 141 IP: 4']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['PEMAG PI: PLATE-1 E: 141 IP: 1']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
xQuantity = visualization.QuantityType(type=TIME)
yQuantity = visualization.QuantityType(type=STRAIN)
session.xyDataObjects['PEEQ PI: PLATE-1 E: 141 IP: 1'].setValues(
    axis1QuantityType=xQuantity, axis2QuantityType=yQuantity, )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['S:Mises PI: PLATE-1 E: 141 IP: 3']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['PEEQ PI: PLATE-1 E: 141 IP: 1']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['PEEQ PI: PLATE-1 E: 141 IP: 3']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
odb = session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_finite_slide.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3567.05, 
    farPlane=5835.08, width=2004.2, height=690.783, viewOffsetX=319.357, 
    viewOffsetY=6.89388)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['cpe4_node_surface_small_sliding'].submit(consistencyChecking=OFF)
#: The job input file "cpe4_node_surface_small_sliding.inp" has been submitted for analysis.
#: Job cpe4_node_surface_small_sliding: Analysis Input File Processor completed successfully.
#: Error in job cpe4_node_surface_small_sliding: Time increment required is less than the minimum specified
#: Error in job cpe4_node_surface_small_sliding: Too many attempts made for this increment
#: Error in job cpe4_node_surface_small_sliding: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.
#: Job cpe4_node_surface_small_sliding: Abaqus/Standard aborted due to errors.
#: Error in job cpe4_node_surface_small_sliding: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job cpe4_node_surface_small_sliding aborted due to errors.
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_finite_slide.odb'])
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_small_sliding.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_small_sliding.odb
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
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.jobs['cpe4_node_surface_small_sliding'].submit(consistencyChecking=OFF)
#: The job input file "cpe4_node_surface_small_sliding.inp" has been submitted for analysis.
#: Job cpe4_node_surface_small_sliding: Analysis Input File Processor completed successfully.
#: Error in job cpe4_node_surface_small_sliding: Time increment required is less than the minimum specified
#: Error in job cpe4_node_surface_small_sliding: Too many attempts made for this increment
#: Error in job cpe4_node_surface_small_sliding: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.
#: Job cpe4_node_surface_small_sliding: Abaqus/Standard aborted due to errors.
#: Error in job cpe4_node_surface_small_sliding: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job cpe4_node_surface_small_sliding aborted due to errors.
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_small_sliding.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_small_sliding.odb
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
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='My_Step')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].steps['My_Step'].setValues(timePeriod=1.0, 
    maxNumInc=2000, initialInc=1.0, minInc=1e-05, maxInc=1.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['cpe4_node_surface_small_sliding'].submit(consistencyChecking=OFF)
#: The job input file "cpe4_node_surface_small_sliding.inp" has been submitted for analysis.
#: Job cpe4_node_surface_small_sliding: Analysis Input File Processor completed successfully.
#: Error in job cpe4_node_surface_small_sliding: Time increment required is less than the minimum specified
#: Error in job cpe4_node_surface_small_sliding: Too many attempts made for this increment
#: Error in job cpe4_node_surface_small_sliding: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.
#: Job cpe4_node_surface_small_sliding: Abaqus/Standard aborted due to errors.
#: Error in job cpe4_node_surface_small_sliding: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job cpe4_node_surface_small_sliding aborted due to errors.
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_small_sliding.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_small_sliding.odb
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
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
mdb.models['Model-1'].interactions['Int-1'].setValues(initialClearance=OMIT, 
    surfaceSmoothing=NONE, adjustMethod=NONE, sliding=SMALL, 
    enforcement=NODE_TO_SURFACE, thickness=OFF, supplementaryContact=SELECTIVE, 
    smooth=0.2, bondingSet=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.Job(name='Job-6', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['Job-6'].submit(consistencyChecking=OFF)
#: The job input file "Job-6.inp" has been submitted for analysis.
#: Job Job-6: Analysis Input File Processor completed successfully.
#: Job Job-6: Abaqus/Standard completed successfully.
#: Job Job-6 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/cpe4_node_surface_small_sliding.odb'])
o3 = session.openOdb(
    name='/home/fe1/Desktop/FiniteElementsAnalysis/assignment3/Job-6.odb')
#: Model: /home/fe1/Desktop/FiniteElementsAnalysis/assignment3/Job-6.odb
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
