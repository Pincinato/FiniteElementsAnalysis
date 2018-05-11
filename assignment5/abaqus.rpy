# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Fri May 11 12:16:00 2018
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
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.jobs['CPSR4_without_Optimization'].submit(consistencyChecking=OFF)
#: The job input file "CPSR4_without_Optimization.inp" has been submitted for analysis.
#: Error in job CPSR4_without_Optimization: The executable pre aborted with system error "Illegal memory reference" (signal 11). Please check the .dat, .msg, and .sta files for error messages if the files exist.  If there are no error messages and you cannot resolve the problem, please run the command "abaqus job=support information=support" to report and save your system information.  Use the same command to run Abaqus that you used when the problem occurred.  Please contact your local Abaqus support office and send them the input file, the file support.log which you just created, the executable name, and the error code.
#: Job CPSR4_without_Optimization aborted due to errors.
