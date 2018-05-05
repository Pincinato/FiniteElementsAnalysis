1

   Abaqus 3DEXPERIENCE R2016x                                  Date 02-May-2018   Time 21:14:29
   For use at UNIVERSITAET BERN under license from Dassault Systemes or its subsidiary.

                                                                                 
                                                                                 
 STEP    1     INCREMENT     1     STEP TIME    0.00    


                        S T E P       1     S T A T I C   A N A L Y S I S


                                                                                          

     AUTOMATIC TIME CONTROL WITH -
          A SUGGESTED INITIAL TIME INCREMENT OF                 1.00    
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

     THE MAXIMUM NUMBER OF INCREMENTS IN THIS STEP IS                    2000

          LARGE DISPLACEMENT THEORY WILL BE USED

     LINEAR EXTRAPOLATION WILL BE USED

     CHARACTERISTIC ELEMENT LENGTH      19.3    

     DETAILS REGARDING ACTUAL SOLUTION WAVEFRONT REQUESTED

     DETAILED OUTPUT OF DIAGNOSTICS TO DATABASE REQUESTED

     PRINT OF INCREMENT NUMBER, TIME, ETC., TO THE MESSAGE FILE EVERY     1  INCREMENTS

     COLLECTING MODEL CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS

     COLLECTING STEP CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS


  INCREMENT     1 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT   1.00    

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

 ***WARNING: THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE 
             FIRST YIELD AT 300 POINTS

 ***WARNING: THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT 
             THE PLASTICITY CALCULATION AT 196 POINTS
 

 ***NOTE: MATERIAL CALCULATIONS FAILED TO CONVERGE OR WERE NOT ATTEMPTED AT ONE 
          OR MORE POINTS. CONVERGENCE IS JUDGED UNLIKELY.


  INCREMENT     1 STARTS. ATTEMPT NUMBER  2, TIME INCREMENT  0.250    

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

 ***WARNING: THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE 
             FIRST YIELD AT 246 POINTS

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      1.706E+07   TIME AVG. FORCE       1.706E+07
 LARGEST RESIDUAL FORCE            -2.341E+08   AT NODE         15   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -8.90       AT NODE         63   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        -8.90       AT NODE         63   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     6.812E+09   TIME AVG. MOMENT      6.812E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -1.430E-32   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -1.430E-32   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

 ***WARNING: THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE 
             FIRST YIELD AT 216 POINTS

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      3.402E+06   TIME AVG. FORCE       3.402E+06
 LARGEST RESIDUAL FORCE            -7.104E+07   AT NODE        146   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.          20.2       AT NODE        121   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.         13.2       AT NODE        121   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     6.839E+08   TIME AVG. MOMENT      6.839E+08
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION      1.076E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION     1.537E-32   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

 ***WARNING: THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE 
             FIRST YIELD AT 262 POINTS

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     3


 AVERAGE FORCE                      2.490E+06   TIME AVG. FORCE       2.490E+06
 LARGEST RESIDUAL FORCE            -3.608E+07   AT NODE         15   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.          23.3       AT NODE         75   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.         5.83       AT NODE        122   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     4.793E+08   TIME AVG. MOMENT      4.793E+08
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION      7.508E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -3.247E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

 ***WARNING: THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE 
             FIRST YIELD AT 250 POINTS

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     4


 AVERAGE FORCE                      2.380E+06   TIME AVG. FORCE       2.380E+06
 LARGEST RESIDUAL FORCE             7.401E+07   AT NODE        146   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.          20.8       AT NODE        264   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        -4.02       AT NODE         75   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     5.267E+08   TIME AVG. MOMENT      5.267E+08
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION      3.946E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -7.114E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
 

 ***NOTE: THE SOLUTION APPEARS TO BE DIVERGING. CONVERGENCE IS JUDGED UNLIKELY.


  INCREMENT     1 STARTS. ATTEMPT NUMBER  3, TIME INCREMENT  6.250E-02

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

 ***WARNING: THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE 
             FIRST YIELD AT 168 POINTS

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      4.300E+06   TIME AVG. FORCE       4.300E+06
 LARGEST RESIDUAL FORCE            -5.070E+07   AT NODE         15   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -2.22       AT NODE         63   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        -2.22       AT NODE         63   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     1.643E+09   TIME AVG. MOMENT      1.643E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -3.575E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -3.575E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

 ***WARNING: THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE 
             FIRST YIELD AT 38 POINTS

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      1.299E+06   TIME AVG. FORCE       1.299E+06
 LARGEST RESIDUAL FORCE            -5.100E+06   AT NODE         17   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -4.32       AT NODE         16   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        -2.57       AT NODE         16   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     3.461E+08   TIME AVG. MOMENT      3.461E+08
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -1.703E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION     3.405E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

 ***WARNING: THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE 
             FIRST YIELD AT 44 POINTS

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     3


 AVERAGE FORCE                      1.233E+06   TIME AVG. FORCE       1.233E+06
 LARGEST RESIDUAL FORCE             4.899E+05   AT NODE         16   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -4.42       AT NODE         63   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.       -0.105       AT NODE         62   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     3.298E+08   TIME AVG. MOMENT      3.298E+08
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -4.521E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION     1.251E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

 ***WARNING: THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE 
             FIRST YIELD AT 44 POINTS

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     4


 AVERAGE FORCE                      1.234E+06   TIME AVG. FORCE       1.234E+06
 LARGEST RESIDUAL FORCE             1.406E+04   AT NODE        121   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -4.42       AT NODE         63   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        8.684E-03   AT NODE         16   DOF  2
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     3.298E+08   TIME AVG. MOMENT      3.298E+08
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -3.811E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION     7.099E-36   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

 ***WARNING: THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE 
             FIRST YIELD AT 44 POINTS

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     5


 AVERAGE FORCE                      1.234E+06   TIME AVG. FORCE       1.234E+06
 LARGEST RESIDUAL FORCE              41.0       AT NODE        145   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -4.42       AT NODE         63   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        2.549E-04   AT NODE        121   DOF  2
   INSTANCE: PLATE-1                                                                         
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                     3.298E+08   TIME AVG. MOMENT      3.298E+08
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -4.001E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -1.903E-36   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

 ITERATION SUMMARY FOR THE INCREMENT:   5 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  5 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  6.250E-02,  FRACTION OF STEP COMPLETED  6.250E-02
 STEP TIME COMPLETED       6.250E-02,  TOTAL TIME COMPLETED        6.250E-02


  INCREMENT     2 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  6.250E-02

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      2.959E+06   TIME AVG. FORCE       2.097E+06
 LARGEST RESIDUAL FORCE            -8.031E+05   AT NODE         17   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.          5.23       AT NODE        121   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        0.895       AT NODE        121   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     2.234E+09   TIME AVG. MOMENT      1.282E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -5.064E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -1.063E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      2.909E+06   TIME AVG. FORCE       2.072E+06
 LARGEST RESIDUAL FORCE            -1.080E+04   AT NODE        121   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.          5.23       AT NODE        255   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        7.117E-03   AT NODE        122   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     2.242E+09   TIME AVG. MOMENT      1.286E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -3.784E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION     1.280E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     3


 AVERAGE FORCE                      2.909E+06   TIME AVG. FORCE       2.072E+06
 LARGEST RESIDUAL FORCE             -31.3       AT NODE        146   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.          5.23       AT NODE        255   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.       -3.204E-04   AT NODE        121   DOF  1
   INSTANCE: PLATE-1                                                                         
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                     2.242E+09   TIME AVG. MOMENT      1.286E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -3.969E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -1.846E-36   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

 ITERATION SUMMARY FOR THE INCREMENT:   3 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  3 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  6.250E-02,  FRACTION OF STEP COMPLETED  0.125    
 STEP TIME COMPLETED       0.125    ,  TOTAL TIME COMPLETED        0.125    


  INCREMENT     3 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  6.250E-02

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      3.223E+06   TIME AVG. FORCE       2.455E+06
 LARGEST RESIDUAL FORCE             8.811E+04   AT NODE         12   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.          5.59       AT NODE        255   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.       -0.370       AT NODE        149   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     2.557E+09   TIME AVG. MOMENT      1.710E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -6.265E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -2.296E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =  1.00000E-02
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      3.232E+06   TIME AVG. FORCE       2.459E+06
 LARGEST RESIDUAL FORCE              621.       AT NODE          8   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.          5.60       AT NODE        255   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        2.711E-03   AT NODE          8   DOF  2
   INSTANCE: PLATE-1                                                                         
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                     2.562E+09   TIME AVG. MOMENT      1.711E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -6.382E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -1.171E-36   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
          TIME INCREMENT MAY NOW INCREASE TO    9.375E-02

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  6.250E-02,  FRACTION OF STEP COMPLETED  0.188    
 STEP TIME COMPLETED       0.188    ,  TOTAL TIME COMPLETED        0.188    


  INCREMENT     4 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  9.375E-02

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      3.612E+06   TIME AVG. FORCE       2.747E+06
 LARGEST RESIDUAL FORCE             2.137E+05   AT NODE         12   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.          9.12       AT NODE        256   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.       -0.745       AT NODE         15   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     3.037E+09   TIME AVG. MOMENT      2.043E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -1.164E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -2.064E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =  1.00000E-02
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      3.604E+06   TIME AVG. FORCE       2.745E+06
 LARGEST RESIDUAL FORCE             2.080E+03   AT NODE          8   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.          9.12       AT NODE        256   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        7.753E-03   AT NODE          8   DOF  2
   INSTANCE: PLATE-1                                                                         
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                     3.048E+09   TIME AVG. MOMENT      2.045E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -1.247E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -8.350E-36   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
          TIME INCREMENT MAY NOW INCREASE TO    0.141    

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  9.375E-02,  FRACTION OF STEP COMPLETED  0.281    
 STEP TIME COMPLETED       0.281    ,  TOTAL TIME COMPLETED        0.281    


  INCREMENT     5 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.141    

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1

   MAX. PENETRATION ERROR -14.2109E-15  AT NODE PLATE-1.122 OF CONTACT PAIR 
   (ASSEMBLY_S_SURF-1,ASSEMBLY_RIGID_PRESS-1_SURF-3)
   MAX. CONTACT FORCE ERROR -1.51825E-09 AT NODE PLATE-1.122 OF CONTACT PAIR 
   (ASSEMBLY_S_SURF-1,ASSEMBLY_RIGID_PRESS-1_SURF-3)
          THE CONTACT CONSTRAINTS HAVE CONVERGED.

 AVERAGE FORCE                      4.221E+06   TIME AVG. FORCE       3.040E+06
 LARGEST RESIDUAL FORCE             7.679E+05   AT NODE         12   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -15.6       AT NODE        149   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        -1.95       AT NODE         15   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     3.844E+09   TIME AVG. MOMENT      2.405E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.372E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -5.008E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =  1.00000E-02
       ELAPSED TOTAL CPU TIME (SEC) =  2.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      4.210E+06   TIME AVG. FORCE       3.038E+06
 LARGEST RESIDUAL FORCE            -6.946E+03   AT NODE        133   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -15.6       AT NODE        149   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.       -2.625E-02   AT NODE         66   DOF  1
   INSTANCE: PLATE-1                                                                         
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                     3.877E+09   TIME AVG. MOMENT      2.412E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.605E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -2.331E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
          TIME INCREMENT MAY NOW INCREASE TO    0.211    

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.141    ,  FRACTION OF STEP COMPLETED  0.422    
 STEP TIME COMPLETED       0.422    ,  TOTAL TIME COMPLETED        0.422    


  INCREMENT     6 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.211    

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      5.387E+06   TIME AVG. FORCE       3.430E+06
 LARGEST RESIDUAL FORCE             3.643E+06   AT NODE        125   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -29.0       AT NODE        149   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        -5.71       AT NODE         15   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     5.442E+09   TIME AVG. MOMENT      2.917E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -5.563E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -1.656E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      5.262E+06   TIME AVG. FORCE       3.409E+06
 LARGEST RESIDUAL FORCE             6.618E+04   AT NODE        146   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -29.1       AT NODE        149   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.       -0.148       AT NODE        146   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     5.562E+09   TIME AVG. MOMENT      2.937E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -6.200E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -6.372E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     3


 AVERAGE FORCE                      5.269E+06   TIME AVG. FORCE       3.410E+06
 LARGEST RESIDUAL FORCE            -1.204E+04   AT NODE        146   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -29.1       AT NODE        149   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.       -1.108E-02   AT NODE         68   DOF  1
   INSTANCE: PLATE-1                                                                         
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                     5.564E+09   TIME AVG. MOMENT      2.937E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -6.247E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -4.687E-36   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
          TIME INCREMENT MAY NOW INCREASE TO    0.316    

 ITERATION SUMMARY FOR THE INCREMENT:   3 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  3 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.211    ,  FRACTION OF STEP COMPLETED  0.633    
 STEP TIME COMPLETED       0.633    ,  TOTAL TIME COMPLETED        0.633    


  INCREMENT     7 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.316    

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      8.874E+06   TIME AVG. FORCE       4.190E+06
 LARGEST RESIDUAL FORCE             2.746E+07   AT NODE        125   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -63.6       AT NODE        148   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        -20.3       AT NODE         15   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     9.587E+09   TIME AVG. MOMENT      3.887E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -1.576E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -6.393E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      7.369E+06   TIME AVG. FORCE       3.976E+06
 LARGEST RESIDUAL FORCE             1.359E+06   AT NODE        146   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -64.6       AT NODE        148   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        -1.24       AT NODE        146   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     1.022E+10   TIME AVG. MOMENT      3.978E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.103E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -5.262E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     3


 AVERAGE FORCE                      7.392E+06   TIME AVG. FORCE       3.979E+06
 LARGEST RESIDUAL FORCE            -6.311E+05   AT NODE        146   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -64.6       AT NODE        147   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        0.125       AT NODE        123   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     1.025E+10   TIME AVG. MOMENT      3.981E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.283E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -1.800E-34   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     4


 AVERAGE FORCE                      7.348E+06   TIME AVG. FORCE       3.973E+06
 LARGEST RESIDUAL FORCE             3.341E+05   AT NODE        146   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -64.6       AT NODE        147   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        7.845E-02   AT NODE         14   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     1.025E+10   TIME AVG. MOMENT      3.981E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.280E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION     2.303E-36   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     5


 AVERAGE FORCE                      7.392E+06   TIME AVG. FORCE       3.979E+06
 LARGEST RESIDUAL FORCE             1.871E+05   AT NODE         15   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -64.6       AT NODE        147   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.       -5.456E-02   AT NODE         14   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     1.025E+10   TIME AVG. MOMENT      3.981E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.289E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -9.183E-36   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     6


 AVERAGE FORCE                      7.393E+06   TIME AVG. FORCE       3.979E+06
 LARGEST RESIDUAL FORCE            -1.139E+05   AT NODE         15   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -64.6       AT NODE        147   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        3.689E-02   AT NODE         14   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     1.025E+10   TIME AVG. MOMENT      3.981E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.278E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION     1.139E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     7


 AVERAGE FORCE                      7.393E+06   TIME AVG. FORCE       3.979E+06
 LARGEST RESIDUAL FORCE             7.174E+04   AT NODE         15   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -64.6       AT NODE        147   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.       -2.475E-02   AT NODE         14   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     1.025E+10   TIME AVG. MOMENT      3.981E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.280E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -2.035E-36   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     8


 AVERAGE FORCE                      7.393E+06   TIME AVG. FORCE       3.979E+06
 LARGEST RESIDUAL FORCE            -4.534E+04   AT NODE         15   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -64.6       AT NODE        147   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        1.670E-02   AT NODE         14   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     1.025E+10   TIME AVG. MOMENT      3.981E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.278E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION     2.117E-36   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     9


 AVERAGE FORCE                      7.393E+06   TIME AVG. FORCE       3.979E+06
 LARGEST RESIDUAL FORCE             2.926E+04   AT NODE         15   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -64.6       AT NODE        147   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.       -1.136E-02   AT NODE         14   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     1.025E+10   TIME AVG. MOMENT      3.981E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.280E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -1.861E-36   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION    10


 AVERAGE FORCE                      7.393E+06   TIME AVG. FORCE       3.979E+06
 LARGEST RESIDUAL FORCE            -1.901E+04   AT NODE         15   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -64.6       AT NODE        147   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.       -8.169E-03   AT NODE         65   DOF  1
   INSTANCE: PLATE-1                                                                         
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED BASED ON ALTERNATIVE
          RESIDUAL CRITERION

 AVERAGE MOMENT                     1.025E+10   TIME AVG. MOMENT      3.981E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.278E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION     1.769E-36   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

 ITERATION SUMMARY FOR THE INCREMENT:  10 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND 10 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.316    ,  FRACTION OF STEP COMPLETED  0.949    
 STEP TIME COMPLETED       0.949    ,  TOTAL TIME COMPLETED        0.949    


  INCREMENT     8 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  5.078E-02

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      8.116E+06   TIME AVG. FORCE       4.496E+06
 LARGEST RESIDUAL FORCE             1.573E+06   AT NODE        125   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -14.0       AT NODE         63   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.        -3.63       AT NODE         63   DOF  1
   INSTANCE: PLATE-1                                                                         
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     1.134E+10   TIME AVG. MOMENT      4.902E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.761E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -2.396E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

  NUMBER OF EQUATIONS =       698     NUMBER OF FLOATING PT. OPERATIONS =  3.84E+05

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      8.050E+06   TIME AVG. FORCE       4.488E+06
 LARGEST RESIDUAL FORCE             1.252E+04   AT NODE        125   DOF  2
   INSTANCE: PLATE-1                                                                         
 LARGEST INCREMENT OF DISP.         -14.0       AT NODE         63   DOF  1
   INSTANCE: PLATE-1                                                                         
 LARGEST CORRECTION TO DISP.       -4.373E-02   AT NODE         63   DOF  1
   INSTANCE: PLATE-1                                                                         
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                     1.144E+10   TIME AVG. MOMENT      4.914E+09
 ALL MOMENT    RESIDUALS ARE ZERO
 LARGEST INCREMENT OF ROTATION     -2.830E-33   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
 LARGEST CORRECTION TO ROTATION    -6.838E-35   AT NODE          1   DOF  6
   INSTANCE: RIGID_PRESS-1                                                                   
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  5.078E-02,  FRACTION OF STEP COMPLETED   1.00    
 STEP TIME COMPLETED        1.00    ,  TOTAL TIME COMPLETED         1.00    


          THE ANALYSIS HAS BEEN COMPLETED



     ANALYSIS SUMMARY:
     TOTAL OF          8  INCREMENTS
                       2  CUTBACKS IN AUTOMATIC INCREMENTATION
                      34  ITERATIONS INCLUDING CONTACT ITERATIONS IF PRESENT
                      34  PASSES THROUGH THE EQUATION SOLVER OF WHICH 
                      34  INVOLVE MATRIX DECOMPOSITION, INCLUDING
                       0  DECOMPOSITION(S) OF THE MASS MATRIX
                       1  REORDERING OF EQUATIONS TO MINIMIZE WAVEFRONT
                       0  ADDITIONAL RESIDUAL EVALUATIONS FOR LINE SEARCHES
                       0  ADDITIONAL OPERATOR EVALUATIONS FOR LINE SEARCHES
                       1  WARNING MESSAGES DURING USER INPUT PROCESSING
                      11  WARNING MESSAGES DURING ANALYSIS
                       0  ANALYSIS WARNINGS ARE NUMERICAL PROBLEM MESSAGES
                       0  ANALYSIS WARNINGS ARE NEGATIVE EIGENVALUE MESSAGES
                       0  ERROR MESSAGES



     JOB TIME SUMMARY
       USER TIME (SEC)      =   1.3800    
       SYSTEM TIME (SEC)    =  0.13000    
       TOTAL CPU TIME (SEC) =   1.5100    
       WALLCLOCK TIME (SEC) =          2
