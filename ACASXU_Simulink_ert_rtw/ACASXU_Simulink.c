/*
 * Prerelease License - for engineering feedback and testing purposes
 * only. Not for sale.
 *
 * File: ACASXU_Simulink.c
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

#include "ACASXU_Simulink.h"
#include "rtwtypes.h"
#include "ACASXU_Simulink_private.h"

/* External inputs (root inport signals with default storage) */
ExtU_ACASXU_Simulink_T ACASXU_Simulink_U;

/* External outputs (root outports fed by signals with default storage) */
ExtY_ACASXU_Simulink_T ACASXU_Simulink_Y;

/* Real-time model */
static RT_MODEL_ACASXU_Simulink_T ACASXU_Simulink_M_;
RT_MODEL_ACASXU_Simulink_T *const ACASXU_Simulink_M = &ACASXU_Simulink_M_;

/*
 * Output and update for atomic system:
 *    '<S1>/relu1'
 *    '<S1>/relu2'
 */
void ACASXU_Simulink_relu1(const int8_T rtu_In1[50], int8_T rty_Out1[50])
{
  int32_T i;

  /* MinMax: '<S9>/Max' */
  for (i = 0; i < 50; i++) {
    int8_T u0;
    u0 = rtu_In1[i];
    if (u0 >= 0) {
      rty_Out1[i] = u0;
    } else {
      rty_Out1[i] = 0;
    }
  }

  /* End of MinMax: '<S9>/Max' */
}

/* Model step function */
void ACASXU_Simulink_step(void)
{
  int32_T i;
  int32_T i_0;
  int32_T tmp_0;
  int8_T rtb_DataTypeConversion_m[50];
  int8_T rtb_Max_p[50];
  int8_T tmp[50];

  /* Outputs for Atomic SubSystem: '<S1>/fc1' */
  /* DataTypeConversion: '<S19>/Data Type Conversion' incorporates:
   *  Constant: '<S2>/Bias'
   *  Constant: '<S2>/Weights'
   *  Inport: '<Root>/input'
   *  Product: '<S2>/Matrix Multiply'
   *  Sum: '<S18>/Add'
   */
  for (i = 0; i < 50; i++) {
    tmp_0 = 0;
    for (i_0 = 0; i_0 < 5; i_0++) {
      tmp_0 += ACASXU_Simulink_ConstP.Weights_Value_f[50 * i_0 + i] *
        ACASXU_Simulink_U.input[i_0];
    }

    tmp_0 += ACASXU_Simulink_ConstP.Bias_Value[i];
    tmp_0 = (((uint32_T)tmp_0 & 32U) != 0U) + (tmp_0 >> 6);
    if (tmp_0 > 127) {
      tmp_0 = 127;
    } else if (tmp_0 < -128) {
      tmp_0 = -128;
    }

    rtb_DataTypeConversion_m[i] = (int8_T)tmp_0;
  }

  /* End of DataTypeConversion: '<S19>/Data Type Conversion' */
  /* End of Outputs for SubSystem: '<S1>/fc1' */

  /* Outputs for Atomic SubSystem: '<S1>/relu1' */
  ACASXU_Simulink_relu1(rtb_DataTypeConversion_m, rtb_Max_p);

  /* End of Outputs for SubSystem: '<S1>/relu1' */

  /* Outputs for Atomic SubSystem: '<S1>/fc2' */
  /* DataTypeConversion: '<S25>/Data Type Conversion' incorporates:
   *  Constant: '<S3>/Bias'
   *  Constant: '<S3>/Weights'
   *  MinMax: '<S13>/Max'
   *  Product: '<S3>/Matrix Multiply'
   *  Sum: '<S24>/Add'
   */
  for (i = 0; i < 50; i++) {
    tmp_0 = 0;
    for (i_0 = 0; i_0 < 50; i_0++) {
      tmp_0 += ACASXU_Simulink_ConstP.Weights_Value_c[50 * i_0 + i] *
        rtb_Max_p[i_0];
    }

    tmp_0 += ACASXU_Simulink_ConstP.Bias_Value_m[i];
    tmp_0 = (((uint32_T)tmp_0 & 4U) != 0U) + (tmp_0 >> 3);
    if (tmp_0 > 127) {
      tmp_0 = 127;
    } else if (tmp_0 < -128) {
      tmp_0 = -128;
    }

    rtb_DataTypeConversion_m[i] = (int8_T)tmp_0;
  }

  /* End of DataTypeConversion: '<S25>/Data Type Conversion' */
  /* End of Outputs for SubSystem: '<S1>/fc2' */

  /* Outputs for Atomic SubSystem: '<S1>/relu2' */
  ACASXU_Simulink_relu1(rtb_DataTypeConversion_m, rtb_Max_p);

  /* End of Outputs for SubSystem: '<S1>/relu2' */

  /* Outputs for Atomic SubSystem: '<S1>/relu3' */
  /* Outputs for Atomic SubSystem: '<S1>/fc3' */
  for (i = 0; i < 50; i++) {
    /* DataTypeConversion: '<S31>/Data Type Conversion' incorporates:
     *  Constant: '<S4>/Bias'
     *  Constant: '<S4>/Weights'
     *  MinMax: '<S13>/Max'
     *  Product: '<S4>/Matrix Multiply'
     *  Sum: '<S30>/Add'
     */
    tmp_0 = 0;
    for (i_0 = 0; i_0 < 50; i_0++) {
      tmp_0 += ACASXU_Simulink_ConstP.Weights_Value_i[50 * i_0 + i] *
        rtb_Max_p[i_0];
    }

    tmp_0 += ACASXU_Simulink_ConstP.Bias_Value_h[i];
    tmp_0 = (((uint32_T)tmp_0 & 8U) != 0U) + (tmp_0 >> 4);
    if (tmp_0 > 127) {
      tmp_0 = 127;
    } else if (tmp_0 < -128) {
      tmp_0 = -128;
    }

    /* MinMax: '<S11>/Max' incorporates:
     *  DataTypeConversion: '<S31>/Data Type Conversion'
     */
    if (tmp_0 >= 0) {
      tmp[i] = (int8_T)tmp_0;
    } else {
      tmp[i] = 0;
    }

    /* End of MinMax: '<S11>/Max' */
  }

  /* End of Outputs for SubSystem: '<S1>/fc3' */
  /* End of Outputs for SubSystem: '<S1>/relu3' */

  /* Outputs for Atomic SubSystem: '<S1>/fc4' */
  /* DataTypeConversion: '<S37>/Data Type Conversion' incorporates:
   *  Constant: '<S5>/Bias'
   *  Constant: '<S5>/Weights'
   *  Product: '<S5>/Matrix Multiply'
   *  Sum: '<S36>/Add'
   */
  for (i = 0; i < 50; i++) {
    tmp_0 = 0;
    for (i_0 = 0; i_0 < 50; i_0++) {
      tmp_0 += ACASXU_Simulink_ConstP.Weights_Value_d3[50 * i_0 + i] * tmp[i_0];
    }

    tmp_0 += ACASXU_Simulink_ConstP.Bias_Value_gu[i];
    tmp_0 = (((uint32_T)tmp_0 & 32U) != 0U) + (tmp_0 >> 6);
    if (tmp_0 > 127) {
      tmp_0 = 127;
    } else if (tmp_0 < -128) {
      tmp_0 = -128;
    }

    rtb_DataTypeConversion_m[i] = (int8_T)tmp_0;
  }

  /* End of DataTypeConversion: '<S37>/Data Type Conversion' */
  /* End of Outputs for SubSystem: '<S1>/fc4' */

  /* Outputs for Atomic SubSystem: '<S1>/relu4' */
  ACASXU_Simulink_relu1(rtb_DataTypeConversion_m, rtb_Max_p);

  /* End of Outputs for SubSystem: '<S1>/relu4' */

  /* Outputs for Atomic SubSystem: '<S1>/fc5' */
  /* DataTypeConversion: '<S43>/Data Type Conversion' incorporates:
   *  Constant: '<S6>/Bias'
   *  Constant: '<S6>/Weights'
   *  MinMax: '<S13>/Max'
   *  Product: '<S6>/Matrix Multiply'
   *  Sum: '<S42>/Add'
   */
  for (i = 0; i < 50; i++) {
    tmp_0 = 0;
    for (i_0 = 0; i_0 < 50; i_0++) {
      tmp_0 += ACASXU_Simulink_ConstP.Weights_Value_d3t[50 * i_0 + i] *
        rtb_Max_p[i_0];
    }

    tmp_0 += ACASXU_Simulink_ConstP.Bias_Value_a[i];
    tmp_0 = (((uint32_T)tmp_0 & 4U) != 0U) + (tmp_0 >> 3);
    if (tmp_0 > 127) {
      tmp_0 = 127;
    } else if (tmp_0 < -128) {
      tmp_0 = -128;
    }

    rtb_DataTypeConversion_m[i] = (int8_T)tmp_0;
  }

  /* End of DataTypeConversion: '<S43>/Data Type Conversion' */
  /* End of Outputs for SubSystem: '<S1>/fc5' */

  /* Outputs for Atomic SubSystem: '<S1>/relu5' */
  ACASXU_Simulink_relu1(rtb_DataTypeConversion_m, rtb_Max_p);

  /* End of Outputs for SubSystem: '<S1>/relu5' */

  /* Outputs for Atomic SubSystem: '<S1>/relu6' */
  /* Outputs for Atomic SubSystem: '<S1>/fc6' */
  for (i = 0; i < 50; i++) {
    /* DataTypeConversion: '<S49>/Data Type Conversion' incorporates:
     *  Constant: '<S7>/Bias'
     *  Constant: '<S7>/Weights'
     *  MinMax: '<S13>/Max'
     *  Product: '<S7>/Matrix Multiply'
     *  Sum: '<S48>/Add'
     */
    tmp_0 = 0;
    for (i_0 = 0; i_0 < 50; i_0++) {
      tmp_0 += ACASXU_Simulink_ConstP.Weights_Value_d[50 * i_0 + i] *
        rtb_Max_p[i_0];
    }

    tmp_0 += ACASXU_Simulink_ConstP.Bias_Value_f[i];
    if (tmp_0 > 127) {
      tmp_0 = 127;
    } else if (tmp_0 < -128) {
      tmp_0 = -128;
    }

    /* MinMax: '<S14>/Max' incorporates:
     *  DataTypeConversion: '<S49>/Data Type Conversion'
     */
    if (tmp_0 >= 0) {
      tmp[i] = (int8_T)tmp_0;
    } else {
      tmp[i] = 0;
    }

    /* End of MinMax: '<S14>/Max' */
  }

  /* End of Outputs for SubSystem: '<S1>/fc6' */
  /* End of Outputs for SubSystem: '<S1>/relu6' */

  /* Outport: '<Root>/fc7_out' incorporates:
   *  Constant: '<S8>/Bias'
   *  Constant: '<S8>/Weights'
   *  DataTypeConversion: '<S1>/fc7_out_cast'
   *  Product: '<S8>/Matrix Multiply'
   *  Sum: '<S54>/Add'
   */
  for (i = 0; i < 5; i++) {
    tmp_0 = 0;
    for (i_0 = 0; i_0 < 50; i_0++) {
      /* Outputs for Atomic SubSystem: '<S1>/fc7' */
      tmp_0 += ACASXU_Simulink_ConstP.Weights_Value[5 * i_0 + i] * tmp[i_0];

      /* End of Outputs for SubSystem: '<S1>/fc7' */
    }

    /* Outputs for Atomic SubSystem: '<S1>/fc7' */
    ACASXU_Simulink_Y.fc7_out[i] = (real32_T)(tmp_0 +
      ACASXU_Simulink_ConstP.Bias_Value_g[i]) * 0.25F;

    /* End of Outputs for SubSystem: '<S1>/fc7' */
  }

  /* End of Outport: '<Root>/fc7_out' */
}

/* Model initialize function */
void ACASXU_Simulink_initialize(void)
{
  /* (no initialization code required) */
}

/* Model terminate function */
void ACASXU_Simulink_terminate(void)
{
  /* (no terminate code required) */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
