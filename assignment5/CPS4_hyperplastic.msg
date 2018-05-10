1

   Abaqus 3DEXPERIENCE R2016x                                  Date 10-May-2018   Time 17:40:19
   For use at UNIVERSITAET BERN under license from Dassault Systemes or its subsidiary.

                                                                                 
                                                                                 
 STEP    1     INCREMENT     1     STEP TIME    0.00    


                        S T E P       1     S T A T I C   A N A L Y S I S


                                                                                          

     AUTOMATIC TIME CONTROL WITH -
          A SUGGESTED INITIAL TIME INCREMENT OF                0.100    
          AND A TOTAL TIME PERIOD OF                            1.00    
          THE MINIMUM TIME INCREMENT ALLOWED IS                1.000E-05
          THE MAXIMUM TIME INCREMENT ALLOWED IS                 1.00    

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
       ELAPSED SYSTEM TIME (SEC)    =  1.00000E-02
       ELAPSED TOTAL CPU TIME (SEC) =  2.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      1.886E-03   TIME AVG. FORCE       1.886E-03
 LARGEST RESIDUAL FORCE            -5.180E-04   AT NODE         83   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.         2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.771E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -2.771E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      1.876E-03   TIME AVG. FORCE       1.876E-03
 LARGEST RESIDUAL FORCE             1.209E-05   AT NODE        192   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.        7.443E-02   AT NODE        334   DOF  1
   INSTANCE: PART-1-4                                                                        
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -5.021E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -2.250E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     3


 AVERAGE FORCE                      1.876E-03   TIME AVG. FORCE       1.876E-03
 LARGEST RESIDUAL FORCE             2.547E-09   AT NODE         10   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.       -9.572E-04   AT NODE        335   DOF  1
   INSTANCE: PART-1-4                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -5.071E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -4.963E-40   AT NODE          1   DOF  6
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

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      3.596E-03   TIME AVG. FORCE       2.736E-03
 LARGEST RESIDUAL FORCE             8.977E-06   AT NODE        191   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          2.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.        7.520E-02   AT NODE         95   DOF  1
   INSTANCE: PART-1-4                                                                        
 ESTIMATE OF DISP.    CORRECTION   -7.281E-04
 FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -9.157E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -4.086E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE
          TIME INCREMENT MAY NOW INCREASE TO    0.150    

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.200    
 STEP TIME COMPLETED       0.200    ,  TOTAL TIME COMPLETED        0.200    


  INCREMENT     3 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.150    

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      5.930E-03   TIME AVG. FORCE       3.801E-03
 LARGEST RESIDUAL FORCE            -1.212E-05   AT NODE         86   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          3.00       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.        5.206E-02   AT NODE         95   DOF  1
   INSTANCE: PART-1-4                                                                        
 ESTIMATE OF DISP.    CORRECTION    3.825E-04
 FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -1.428E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -5.487E-39   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE
          TIME INCREMENT MAY NOW INCREASE TO    0.225    

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.150    ,  FRACTION OF STEP COMPLETED  0.350    
 STEP TIME COMPLETED       0.350    ,  TOTAL TIME COMPLETED        0.350    


  INCREMENT     4 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.225    

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      9.005E-03   TIME AVG. FORCE       5.102E-03
 LARGEST RESIDUAL FORCE            -4.956E-05   AT NODE        166   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          4.50       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.        5.768E-02   AT NODE         95   DOF  1
   INSTANCE: PART-1-4                                                                        
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.046E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     9.635E-39   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      9.020E-03   TIME AVG. FORCE       5.106E-03
 LARGEST RESIDUAL FORCE             1.150E-08   AT NODE         95   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          4.50       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.       -1.169E-03   AT NODE         83   DOF  1
   INSTANCE: PART-1-4                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.009E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     3.742E-39   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE
          TIME INCREMENT MAY NOW INCREASE TO    0.338    

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.225    ,  FRACTION OF STEP COMPLETED  0.575    
 STEP TIME COMPLETED       0.575    ,  TOTAL TIME COMPLETED        0.575    


  INCREMENT     5 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.338    

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      1.296E-02   TIME AVG. FORCE       6.676E-03
 LARGEST RESIDUAL FORCE            -1.599E-04   AT NODE        166   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          6.75       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.       -7.089E-02   AT NODE        462   DOF  2
   INSTANCE: PART-1-4                                                                        
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.771E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     2.422E-38   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      1.297E-02   TIME AVG. FORCE       6.679E-03
 LARGEST RESIDUAL FORCE            -1.337E-07   AT NODE        166   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          6.75       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.       -1.800E-03   AT NODE         83   DOF  1
   INSTANCE: PART-1-4                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.713E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION     5.811E-39   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.338    ,  FRACTION OF STEP COMPLETED  0.913    
 STEP TIME COMPLETED       0.913    ,  TOTAL TIME COMPLETED        0.913    


  INCREMENT     6 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  8.750E-02

  NUMBER OF EQUATIONS =      1003     NUMBER OF FLOATING PT. OPERATIONS =  9.39E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      1.390E-02   TIME AVG. FORCE       7.883E-03
 LARGEST RESIDUAL FORCE            -4.724E-06   AT NODE          2   DOF  1
   INSTANCE: PART-1-4                                                                        
 LARGEST INCREMENT OF DISP.          1.75       AT NODE          1   DOF  2
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO DISP.       -1.081E-02   AT NODE        462   DOF  2
   INSTANCE: PART-1-4                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      0.00       TIME AVG. MOMENT      1.000E-02
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.882E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
 LARGEST CORRECTION TO ROTATION    -2.178E-37   AT NODE          1   DOF  6
   INSTANCE: {assembly node}                                                                 
          THERE IS ZERO MOMENT    EVERYWHERE

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  8.750E-02,  FRACTION OF STEP COMPLETED   1.00    
 STEP TIME COMPLETED        1.00    ,  TOTAL TIME COMPLETED         1.00    


          THE ANALYSIS HAS BEEN COMPLETED



     ANALYSIS SUMMARY:
     TOTAL OF          6  INCREMENTS
                       0  CUTBACKS IN AUTOMATIC INCREMENTATION
                      10  ITERATIONS INCLUDING CONTACT ITERATIONS IF PRESENT
                      10  PASSES THROUGH THE EQUATION SOLVER OF WHICH 
                      10  INVOLVE MATRIX DECOMPOSITION, INCLUDING
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
       USER TIME (SEC)      =  0.71000    
       SYSTEM TIME (SEC)    =  0.11000    
       TOTAL CPU TIME (SEC) =  0.82000    
       WALLCLOCK TIME (SEC) =          1
