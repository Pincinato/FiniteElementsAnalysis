1

   Abaqus 3DEXPERIENCE R2016x                                  Date 11-May-2018   Time 09:05:57
   For use at UNIVERSITAET BERN under license from Dassault Systemes or its subsidiary.

                                                                                 
                                                                                 
 STEP    1     INCREMENT     1     STEP TIME    0.00    


                        S T E P       1     S T A T I C   A N A L Y S I S


                                                                                          

     AUTOMATIC TIME CONTROL WITH -
          A SUGGESTED INITIAL TIME INCREMENT OF                0.100    
          AND A TOTAL TIME PERIOD OF                            1.00    
          THE MINIMUM TIME INCREMENT ALLOWED IS                1.000E-05
          THE MAXIMUM TIME INCREMENT ALLOWED IS                0.100    

     LINEAR EQUATION SOLVER TYPE         DIRECT SPARSE

 CONVERGENCE TOLERANCE PARAMETERS FOR FORCE    
     CRITERION FOR RESIDUAL FORCE     FOR A NONLINEAR PROBLEM          5.000E-03
     CRITERION FOR DISP.    CORRECTION IN A NONLINEAR PROBLEM          1.000E-02
     INITIAL VALUE OF TIME AVERAGE FORCE                               1.000E-02
     AVERAGE FORCE     IS TIME AVERAGE FORCE    
     ALTERNATE CRIT. FOR RESIDUAL FORCE     FOR A NONLINEAR PROBLEM    2.000E-02
     CRITERION FOR ZERO FORCE     RELATIVE TO TIME AVRG. FORCE         1.000E-05
     CRITERION FOR RESIDUAL FORCE     WHEN THERE IS ZERO FLUX          1.000E-05
     CRITERION FOR DISP.    CORRECTION WHEN THERE IS ZERO FLUX         1.000E-03
     CRITERION FOR RESIDUAL FORCE     FOR A LINEAR INCREMENT           1.000E-08
     FIELD CONVERSION RATIO                                             1.00    
     CRITERION FOR ZERO FORCE     REL. TO TIME AVRG. MAX. FORCE        1.000E-05
     CRITERION FOR ZERO DISP.    RELATIVE TO CHARACTERISTIC LENGTH     1.000E-08

 CONVERGENCE TOLERANCE PARAMETERS FOR MOMENT   
     CRITERION FOR RESIDUAL MOMENT    FOR A NONLINEAR PROBLEM          5.000E-03
     CRITERION FOR ROTATION CORRECTION IN A NONLINEAR PROBLEM          1.000E-02
     INITIAL VALUE OF TIME AVERAGE MOMENT                              1.000E-02
     AVERAGE MOMENT    IS TIME AVERAGE MOMENT   
     ALTERNATE CRIT. FOR RESIDUAL MOMENT    FOR A NONLINEAR PROBLEM    2.000E-02
     CRITERION FOR ZERO MOMENT    RELATIVE TO TIME AVRG. MOMENT        1.000E-05
     CRITERION FOR RESIDUAL MOMENT    WHEN THERE IS ZERO FLUX          1.000E-05
     CRITERION FOR ROTATION CORRECTION WHEN THERE IS ZERO FLUX         1.000E-03
     CRITERION FOR RESIDUAL MOMENT    FOR A LINEAR INCREMENT           1.000E-08
     FIELD CONVERSION RATIO                                             1.00    
     CRITERION FOR ZERO MOMENT    REL. TO TIME AVRG. MAX. MOMENT       1.000E-05

     VOLUMETRIC STRAIN COMPATIBILITY TOLERANCE FOR HYBRID SOLIDS       1.000E-05
     AXIAL STRAIN COMPATIBILITY TOLERANCE FOR HYBRID BEAMS             1.000E-05
     TRANS. SHEAR STRAIN COMPATIBILITY TOLERANCE FOR HYBRID BEAMS      1.000E-05
     SOFT CONTACT CONSTRAINT COMPATIBILITY TOLERANCE FOR P>P0          5.000E-03
     SOFT CONTACT CONSTRAINT COMPATIBILITY TOLERANCE FOR P=0.0         0.100    
     CONTACT FORCE ERROR TOLERANCE FOR CONVERT SDI=YES                 1.00    
     DISPLACEMENT COMPATIBILITY TOLERANCE FOR DCOUP ELEMENTS           1.000E-05
     ROTATION COMPATIBILITY TOLERANCE FOR DCOUP ELEMENTS               1.000E-05

 EQUILIBRIUM WILL BE CHECKED FOR SEVERE DISCONTINUITY ITERATIONS

 TIME INCREMENTATION CONTROL PARAMETERS:
     FIRST EQUILIBRIUM ITERATION FOR CONSECUTIVE DIVERGENCE CHECK              4
     EQUILIBRIUM ITERATION AT WHICH LOG. CONVERGENCE RATE CHECK BEGINS         8
     EQUILIBRIUM ITERATION AFTER WHICH ALTERNATE RESIDUAL IS USED              9
     MAXIMUM EQUILIBRIUM ITERATIONS ALLOWED                                   16
     EQUILIBRIUM ITERATION COUNT FOR CUT-BACK IN NEXT INCREMENT               10
     MAXIMUM EQUILIB. ITERS IN TWO INCREMENTS FOR TIME INCREMENT INCREASE      4
     MAXIMUM ITERATIONS FOR SEVERE DISCONTINUITIES                            50
     MAXIMUM CUT-BACKS ALLOWED IN AN INCREMENT                                 5
     MAXIMUM DISCON. ITERS IN TWO INCREMENTS FOR TIME INCREMENT INCREASE      50
     MAXIMUM CONTACT AUGMENTATIONS FOR *SURFACE BEHAVIOR,AUGMENTED LAGRANGE   50
     CUT-BACK FACTOR AFTER DIVERGENCE                                 0.2500    
     CUT-BACK FACTOR FOR TOO SLOW CONVERGENCE                         0.5000    
     CUT-BACK FACTOR AFTER TOO MANY EQUILIBRIUM ITERATIONS            0.7500    
     CUT-BACK FACTOR AFTER TOO MANY SEVERE DISCONTINUITY ITERATIONS   0.2500    
     CUT-BACK FACTOR AFTER PROBLEMS IN ELEMENT ASSEMBLY               0.2500    
     INCREASE FACTOR AFTER TWO INCREMENTS THAT CONVERGE QUICKLY        1.500    
     MAX. TIME INCREMENT INCREASE FACTOR ALLOWED                       1.500    
     MAX. TIME INCREMENT INCREASE FACTOR ALLOWED (DYNAMICS)            1.250    
     MAX. TIME INCREMENT INCREASE FACTOR ALLOWED (DIFFUSION)           2.000    
     MINIMUM TIME INCREMENT RATIO FOR EXTRAPOLATION TO OCCUR          0.1000    
     MAX. RATIO OF TIME INCREMENT TO STABILITY LIMIT                   1.000    
     FRACTION OF STABILITY LIMIT FOR NEW TIME INCREMENT               0.9500    
     TIME INCREMENT INCREASE FACTOR BEFORE A TIME POINT                1.000    
     GLOBAL STABILIZATION CONTROL IS NOT USED

          PRINT OF INCREMENT NUMBER, TIME, ETC., EVERY    1  INCREMENTS

     THE MAXIMUM NUMBER OF INCREMENTS IN THIS STEP IS                     100

          LARGE DISPLACEMENT THEORY WILL BE USED

     LINEAR EXTRAPOLATION WILL BE USED

     CHARACTERISTIC ELEMENT LENGTH     0.954    

     DETAILS REGARDING ACTUAL SOLUTION WAVEFRONT REQUESTED

     DETAILED OUTPUT OF DIAGNOSTICS TO DATABASE REQUESTED

     PRINT OF INCREMENT NUMBER, TIME, ETC., TO THE MESSAGE FILE EVERY     1  INCREMENTS

     COLLECTING MODEL CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS

     COLLECTING STEP CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS


  INCREMENT     1 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      3.304E-03   TIME AVG. FORCE       3.304E-03
 LARGEST RESIDUAL FORCE            -9.058E-04   AT NODE         83   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.         2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -4.840E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -4.840E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  2.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  2.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      3.287E-03   TIME AVG. FORCE       3.287E-03
 LARGEST RESIDUAL FORCE             1.932E-05   AT NODE        166   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.        7.204E-02   AT NODE        334   DOF  1
   INSTANCE: PART-1-4                                                                        
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -8.770E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -3.930E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  2.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  2.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     3


 AVERAGE FORCE                      3.286E-03   TIME AVG. FORCE       3.286E-03
 LARGEST RESIDUAL FORCE             4.018E-09   AT NODE         10   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.       -9.075E-04   AT NODE        335   DOF  1
   INSTANCE: PART-1-4                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -8.868E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -9.856E-40   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   3 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  3 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.100    
 STEP TIME COMPLETED       0.100    ,  TOTAL TIME COMPLETED        0.100    


  INCREMENT     2 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  2.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  2.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      6.300E-03   TIME AVG. FORCE       4.793E-03
 LARGEST RESIDUAL FORCE             1.498E-05   AT NODE        167   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.        7.376E-02   AT NODE         95   DOF  1
   INSTANCE: PART-1-4                                                                        
 ESTIMATE OF DISP.    CORRECTION   -6.844E-04
 FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -1.599E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -7.120E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.200    
 STEP TIME COMPLETED       0.200    ,  TOTAL TIME COMPLETED        0.200    


  INCREMENT     3 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      9.073E-03   TIME AVG. FORCE       6.220E-03
 LARGEST RESIDUAL FORCE            -6.287E-06   AT NODE         83   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.        2.946E-02   AT NODE         95   DOF  1
   INSTANCE: PART-1-4                                                                        
 ESTIMATE OF DISP.    CORRECTION    1.178E-04
 FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.212E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -6.132E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.300    
 STEP TIME COMPLETED       0.300    ,  TOTAL TIME COMPLETED        0.300    


  INCREMENT     4 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =  7.00000E-02
       ELAPSED TOTAL CPU TIME (SEC) =  8.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          1

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      1.165E-02   TIME AVG. FORCE       7.577E-03
 LARGEST RESIDUAL FORCE            -5.560E-06   AT NODE        166   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.        1.858E-02   AT NODE         95   DOF  1
   INSTANCE: PART-1-4                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.740E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -5.281E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.400    
 STEP TIME COMPLETED       0.400    ,  TOTAL TIME COMPLETED        0.400    


  INCREMENT     5 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  2.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  2.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      1.406E-02   TIME AVG. FORCE       8.873E-03
 LARGEST RESIDUAL FORCE            -4.780E-06   AT NODE        166   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.        1.178E-02   AT NODE         95   DOF  1
   INSTANCE: PART-1-4                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -3.210E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -4.698E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.500    
 STEP TIME COMPLETED       0.500    ,  TOTAL TIME COMPLETED        0.500    


  INCREMENT     6 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  2.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =  1.00000E-02
       ELAPSED TOTAL CPU TIME (SEC) =  3.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      1.633E-02   TIME AVG. FORCE       1.012E-02
 LARGEST RESIDUAL FORCE            -3.961E-06   AT NODE        166   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.       -9.028E-03   AT NODE        473   DOF  2
   INSTANCE: PART-1-4                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -3.635E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -4.254E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.600    
 STEP TIME COMPLETED       0.600    ,  TOTAL TIME COMPLETED        0.600    


  INCREMENT     7 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  2.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  2.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      1.846E-02   TIME AVG. FORCE       1.131E-02
 LARGEST RESIDUAL FORCE            -3.257E-06   AT NODE        166   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.       -7.424E-03   AT NODE        473   DOF  2
   INSTANCE: PART-1-4                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -4.026E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -3.904E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.700    
 STEP TIME COMPLETED       0.700    ,  TOTAL TIME COMPLETED        0.700    


  INCREMENT     8 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  2.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  2.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      2.050E-02   TIME AVG. FORCE       1.246E-02
 LARGEST RESIDUAL FORCE            -2.677E-06   AT NODE        166   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.       -6.063E-03   AT NODE        463   DOF  2
   INSTANCE: PART-1-4                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.079E-02
                                                (FROM FORCE     FIELD)
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -4.388E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -3.620E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.800    
 STEP TIME COMPLETED       0.800    ,  TOTAL TIME COMPLETED        0.800    


  INCREMENT     9 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  2.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  2.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      2.244E-02   TIME AVG. FORCE       1.357E-02
 LARGEST RESIDUAL FORCE            -2.205E-06   AT NODE        166   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.       -4.901E-03   AT NODE        463   DOF  2
   INSTANCE: PART-1-4                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.189E-02
                                                (FROM FORCE     FIELD)
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -4.726E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -3.387E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.900    
 STEP TIME COMPLETED       0.900    ,  TOTAL TIME COMPLETED        0.900    


  INCREMENT    10 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  2.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  2.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      2.431E-02   TIME AVG. FORCE       1.464E-02
 LARGEST RESIDUAL FORCE            -1.821E-06   AT NODE        166   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.       -3.912E-03   AT NODE        464   DOF  2
   INSTANCE: PART-1-4                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.295E-02
                                                (FROM FORCE     FIELD)
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -5.046E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -3.191E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED   1.00    
 STEP TIME COMPLETED        1.00    ,  TOTAL TIME COMPLETED         1.00    


          THE ANALYSIS HAS BEEN COMPLETED



     ANALYSIS SUMMARY:
     TOTAL OF         10  INCREMENTS
                       0  CUTBACKS IN AUTOMATIC INCREMENTATION
                      12  ITERATIONS INCLUDING CONTACT ITERATIONS IF PRESENT
                      12  PASSES THROUGH THE EQUATION SOLVER OF WHICH 
                      12  INVOLVE MATRIX DECOMPOSITION, INCLUDING
                       0  DECOMPOSITION(S) OF THE MASS MATRIX
                       1  REORDERING OF EQUATIONS TO MINIMIZE WAVEFRONT
                       0  ADDITIONAL RESIDUAL EVALUATIONS FOR LINE SEARCHES
                       0  ADDITIONAL OPERATOR EVALUATIONS FOR LINE SEARCHES
                       3  WARNING MESSAGES DURING USER INPUT PROCESSING
                       0  WARNING MESSAGES DURING ANALYSIS
                       0  ANALYSIS WARNINGS ARE NUMERICAL PROBLEM MESSAGES
                       0  ANALYSIS WARNINGS ARE NEGATIVE EIGENVALUE MESSAGES
                       0  ERROR MESSAGES



     JOB TIME SUMMARY
       USER TIME (SEC)      =   2.2400    
       SYSTEM TIME (SEC)    =   1.1100    
       TOTAL CPU TIME (SEC) =   3.3500    
       WALLCLOCK TIME (SEC) =          5
