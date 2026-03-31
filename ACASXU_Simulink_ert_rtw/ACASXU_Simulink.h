/*
 * Prerelease License - for engineering feedback and testing purposes
 * only. Not for sale.
 *
 * File: ACASXU_Simulink.h
 *
 * Code generated for Simulink model 'ACASXU_Simulink'.
 *
 * Model version                  : 1.2
 * Simulink Coder version         : 26.1 (R2026a) 20-Nov-2025
 * C/C++ source code generated on : Mon Mar 30 22:45:16 2026
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef ACASXU_Simulink_h_
#define ACASXU_Simulink_h_
#ifndef ACASXU_Simulink_COMMON_INCLUDES_
#define ACASXU_Simulink_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "math.h"
#endif                                 /* ACASXU_Simulink_COMMON_INCLUDES_ */

#include "ACASXU_Simulink_types.h"

/* Macros for accessing real-time model data structure */
#ifndef rtmGetErrorStatus
#define rtmGetErrorStatus(rtm)         ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
#define rtmSetErrorStatus(rtm, val)    ((rtm)->errorStatus = (val))
#endif

/* Constant parameters (default storage) */
typedef struct {
  /* Computed Parameter: Bias_Value
   * Referenced by: '<S2>/Bias'
   */
  int32_T Bias_Value[50];

  /* Computed Parameter: Bias_Value_g
   * Referenced by: '<S8>/Bias'
   */
  int32_T Bias_Value_g[5];

  /* Computed Parameter: Bias_Value_f
   * Referenced by: '<S7>/Bias'
   */
  int32_T Bias_Value_f[50];

  /* Computed Parameter: Bias_Value_a
   * Referenced by: '<S6>/Bias'
   */
  int32_T Bias_Value_a[50];

  /* Computed Parameter: Bias_Value_gu
   * Referenced by: '<S5>/Bias'
   */
  int32_T Bias_Value_gu[50];

  /* Computed Parameter: Bias_Value_m
   * Referenced by: '<S3>/Bias'
   */
  int32_T Bias_Value_m[50];

  /* Computed Parameter: Bias_Value_h
   * Referenced by: '<S4>/Bias'
   */
  int32_T Bias_Value_h[50];

  /* Computed Parameter: Weights_Value
   * Referenced by: '<S8>/Weights'
   */
  int8_T Weights_Value[250];

  /* Computed Parameter: Weights_Value_d
   * Referenced by: '<S7>/Weights'
   */
  int8_T Weights_Value_d[2500];

  /* Computed Parameter: Weights_Value_c
   * Referenced by: '<S3>/Weights'
   */
  int8_T Weights_Value_c[2500];

  /* Computed Parameter: Weights_Value_i
   * Referenced by: '<S4>/Weights'
   */
  int8_T Weights_Value_i[2500];

  /* Computed Parameter: Weights_Value_d3
   * Referenced by: '<S5>/Weights'
   */
  int8_T Weights_Value_d3[2500];

  /* Computed Parameter: Weights_Value_d3t
   * Referenced by: '<S6>/Weights'
   */
  int8_T Weights_Value_d3t[2500];

  /* Computed Parameter: Weights_Value_f
   * Referenced by: '<S2>/Weights'
   */
  int8_T Weights_Value_f[250];
} ConstP_ACASXU_Simulink_T;

/* External inputs (root inport signals with default storage) */
typedef struct {
  int8_T input[5];                     /* '<Root>/input' */
} ExtU_ACASXU_Simulink_T;

/* External outputs (root outports fed by signals with default storage) */
typedef struct {
  real32_T fc7_out[5];                 /* '<Root>/fc7_out' */
} ExtY_ACASXU_Simulink_T;

/* Real-time Model Data Structure */
struct tag_RTM_ACASXU_Simulink_T {
  const char_T * volatile errorStatus;
};

/* External inputs (root inport signals with default storage) */
extern ExtU_ACASXU_Simulink_T ACASXU_Simulink_U;

/* External outputs (root outports fed by signals with default storage) */
extern ExtY_ACASXU_Simulink_T ACASXU_Simulink_Y;

/* Constant parameters (default storage) */
extern const ConstP_ACASXU_Simulink_T ACASXU_Simulink_ConstP;

/* Model entry point functions */
extern void ACASXU_Simulink_initialize(void);
extern void ACASXU_Simulink_step(void);
extern void ACASXU_Simulink_terminate(void);

/* Real-time Model object */
extern RT_MODEL_ACASXU_Simulink_T *const ACASXU_Simulink_M;

/*-
 * These blocks were eliminated from the model due to optimizations:
 *
 * Block '<S20>/Reshape' : Reshape block reduction
 * Block '<S1>/fc1_in_cast' : Eliminate redundant data type conversion
 * Block '<S26>/Reshape' : Reshape block reduction
 * Block '<S32>/Reshape' : Reshape block reduction
 * Block '<S38>/Reshape' : Reshape block reduction
 * Block '<S44>/Reshape' : Reshape block reduction
 * Block '<S50>/Reshape' : Reshape block reduction
 * Block '<S55>/Data Type Conversion' : Eliminate redundant data type conversion
 * Block '<S56>/Reshape' : Reshape block reduction
 */

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'ACASXU_Simulink'
 * '<S1>'   : 'ACASXU_Simulink/ACASXU_Simulink'
 * '<S2>'   : 'ACASXU_Simulink/ACASXU_Simulink/fc1'
 * '<S3>'   : 'ACASXU_Simulink/ACASXU_Simulink/fc2'
 * '<S4>'   : 'ACASXU_Simulink/ACASXU_Simulink/fc3'
 * '<S5>'   : 'ACASXU_Simulink/ACASXU_Simulink/fc4'
 * '<S6>'   : 'ACASXU_Simulink/ACASXU_Simulink/fc5'
 * '<S7>'   : 'ACASXU_Simulink/ACASXU_Simulink/fc6'
 * '<S8>'   : 'ACASXU_Simulink/ACASXU_Simulink/fc7'
 * '<S9>'   : 'ACASXU_Simulink/ACASXU_Simulink/relu1'
 * '<S10>'  : 'ACASXU_Simulink/ACASXU_Simulink/relu2'
 * '<S11>'  : 'ACASXU_Simulink/ACASXU_Simulink/relu3'
 * '<S12>'  : 'ACASXU_Simulink/ACASXU_Simulink/relu4'
 * '<S13>'  : 'ACASXU_Simulink/ACASXU_Simulink/relu5'
 * '<S14>'  : 'ACASXU_Simulink/ACASXU_Simulink/relu6'
 * '<S15>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc1/BiasAddition'
 * '<S16>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc1/OutputDataType'
 * '<S17>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc1/Reshape'
 * '<S18>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc1/BiasAddition/Add'
 * '<S19>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc1/OutputDataType/Convert'
 * '<S20>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc1/Reshape/Reshape'
 * '<S21>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc2/BiasAddition'
 * '<S22>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc2/OutputDataType'
 * '<S23>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc2/Reshape'
 * '<S24>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc2/BiasAddition/Add'
 * '<S25>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc2/OutputDataType/Convert'
 * '<S26>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc2/Reshape/Reshape'
 * '<S27>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc3/BiasAddition'
 * '<S28>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc3/OutputDataType'
 * '<S29>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc3/Reshape'
 * '<S30>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc3/BiasAddition/Add'
 * '<S31>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc3/OutputDataType/Convert'
 * '<S32>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc3/Reshape/Reshape'
 * '<S33>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc4/BiasAddition'
 * '<S34>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc4/OutputDataType'
 * '<S35>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc4/Reshape'
 * '<S36>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc4/BiasAddition/Add'
 * '<S37>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc4/OutputDataType/Convert'
 * '<S38>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc4/Reshape/Reshape'
 * '<S39>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc5/BiasAddition'
 * '<S40>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc5/OutputDataType'
 * '<S41>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc5/Reshape'
 * '<S42>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc5/BiasAddition/Add'
 * '<S43>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc5/OutputDataType/Convert'
 * '<S44>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc5/Reshape/Reshape'
 * '<S45>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc6/BiasAddition'
 * '<S46>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc6/OutputDataType'
 * '<S47>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc6/Reshape'
 * '<S48>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc6/BiasAddition/Add'
 * '<S49>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc6/OutputDataType/Convert'
 * '<S50>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc6/Reshape/Reshape'
 * '<S51>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc7/BiasAddition'
 * '<S52>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc7/OutputDataType'
 * '<S53>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc7/Reshape'
 * '<S54>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc7/BiasAddition/Add'
 * '<S55>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc7/OutputDataType/Convert'
 * '<S56>'  : 'ACASXU_Simulink/ACASXU_Simulink/fc7/Reshape/Reshape'
 */
#endif                                 /* ACASXU_Simulink_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
