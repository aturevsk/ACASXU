#!/usr/bin/env python3
"""
generate_report.py — Generate comprehensive PDF report for
ACAS Xu Neural Network ONNX to Quantized Simulink C Code Generation.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)
import os


# ── Colors ──────────────────────────────────────────────────────────
DARK_BLUE  = HexColor('#1a365d')
MED_BLUE   = HexColor('#2b6cb0')
LIGHT_BLUE = HexColor('#ebf4ff')
LIGHT_GRAY = HexColor('#f7fafc')
GRAY       = HexColor('#718096')
GREEN      = HexColor('#276749')
RED        = HexColor('#c53030')
ORANGE     = HexColor('#c05621')


def get_styles():
    """Create custom paragraph styles."""
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        'CustomTitle', parent=styles['Title'],
        fontSize=22, textColor=DARK_BLUE, spaceAfter=6,
        fontName='Helvetica-Bold',
    ))
    styles.add(ParagraphStyle(
        'Subtitle', parent=styles['Normal'],
        fontSize=12, textColor=GRAY, spaceAfter=20,
        alignment=TA_CENTER,
    ))
    styles.add(ParagraphStyle(
        'SectionHead', parent=styles['Heading1'],
        fontSize=16, textColor=DARK_BLUE, spaceBefore=18, spaceAfter=8,
        fontName='Helvetica-Bold',
    ))
    styles.add(ParagraphStyle(
        'SubsectionHead', parent=styles['Heading2'],
        fontSize=13, textColor=MED_BLUE, spaceBefore=12, spaceAfter=6,
        fontName='Helvetica-Bold',
    ))
    styles.add(ParagraphStyle(
        'BodyText2', parent=styles['Normal'],
        fontSize=10, leading=14, alignment=TA_JUSTIFY, spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        'BulletItem', parent=styles['Normal'],
        fontSize=10, leading=14, leftIndent=20, bulletIndent=10,
        spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        'CodeBlock', parent=styles['Code'],
        fontSize=8, leading=10, leftIndent=12,
        backColor=LIGHT_GRAY, spaceAfter=8,
        fontName='Courier',
    ))
    styles.add(ParagraphStyle(
        'TableHeader', parent=styles['Normal'],
        fontSize=9, textColor=white, fontName='Helvetica-Bold',
        alignment=TA_CENTER,
    ))
    styles.add(ParagraphStyle(
        'TableCell', parent=styles['Normal'],
        fontSize=9, alignment=TA_CENTER,
    ))
    styles.add(ParagraphStyle(
        'Recommendation', parent=styles['Normal'],
        fontSize=11, leading=15, textColor=GREEN,
        fontName='Helvetica-Bold', spaceAfter=6,
    ))
    return styles


def make_table(headers, rows, col_widths=None):
    """Create a styled table with alternating row backgrounds."""
    data = [headers] + rows
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',  (0, 0), (-1, 0), DARK_BLUE),
        ('TEXTCOLOR',   (0, 0), (-1, 0), white),
        ('FONTNAME',    (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE',    (0, 0), (-1, 0), 9),
        ('FONTSIZE',    (0, 1), (-1, -1), 9),
        ('ALIGN',       (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN',       (0, 0), (0, -1), 'LEFT'),
        ('VALIGN',      (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID',        (0, 0), (-1, -1), 0.5, GRAY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_BLUE]),
        ('TOPPADDING',  (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t


def build_report(output_path):
    """Build the complete ACAS Xu PDF report."""
    styles = get_styles()
    doc = SimpleDocTemplate(
        output_path, pagesize=letter,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
        topMargin=0.75*inch, bottomMargin=0.75*inch,
        title="ACAS Xu Neural Network — ONNX to Quantized Simulink C Code Generation",
        author="Claude Code",
    )

    story = []

    # ── TITLE PAGE ──────────────────────────────────────────────────
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph(
        "ACAS Xu Neural Network",
        styles['CustomTitle']
    ))
    story.append(Paragraph(
        "ONNX to Quantized Simulink C Code Generation",
        styles['Subtitle']
    ))
    story.append(Spacer(1, 0.5*inch))
    story.append(HRFlowable(width="60%", color=DARK_BLUE, thickness=2))
    story.append(Spacer(1, 0.3*inch))

    info_data = [
        ['Model', 'ACAS Xu (run2a_1_1_batch_2000), 7-layer MLP, 13,005 parameters'],
        ['Target', 'Embedded Real-Time (Simulink Embedded Coder, ert.tlc)'],
        ['Toolchain', 'MATLAB R2026a, Deep Learning Toolbox, Embedded Coder'],
        ['Date', 'March 2026'],
    ]
    info_table = Table(info_data, colWidths=[1.5*inch, 5.0*inch])
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (0, -1), DARK_BLUE),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (0, -1), 12),
    ]))
    story.append(info_table)
    story.append(PageBreak())

    # ── TABLE OF CONTENTS ───────────────────────────────────────────
    story.append(Paragraph("Table of Contents", styles['SectionHead']))
    story.append(Spacer(1, 12))
    toc_items = [
        "1. Executive Summary",
        "2. Model Architecture",
        "3. ONNX Import Attempt",
        "4. Native dlnetwork Rebuild",
        "5. INT8 Quantization",
        "6. Simulink Export &amp; C Code Generation",
        "7. Generated C Code Analysis",
        "Appendix A: File Inventory",
    ]
    for item in toc_items:
        story.append(Paragraph(item, styles['BodyText2']))
    story.append(PageBreak())

    # ── 1. EXECUTIVE SUMMARY ────────────────────────────────────────
    story.append(Paragraph("1. Executive Summary", styles['SectionHead']))
    story.append(Paragraph(
        "<b>Goal:</b> Import a pre-trained ACAS Xu ONNX neural network into MATLAB, "
        "quantize it to INT8 precision, export the quantized network to Simulink, and "
        "generate production-quality embedded C code via Embedded Coder.",
        styles['BodyText2']
    ))
    story.append(Paragraph(
        "<b>Key Finding:</b> The standard importONNXNetwork / importNetworkFromONNX "
        "functions produced custom autogenerated layers that are fundamentally "
        "incompatible with both dlquantizer (INT8 quantization) and "
        "exportNetworkToSimulink. The autogenerated network could not even execute "
        "predict due to internal matrix dimension mismatches in onnxMatMul.",
        styles['BodyText2']
    ))
    story.append(Paragraph(
        "<b>Solution:</b> Rebuild the network as a native dlnetwork using standard "
        "fullyConnectedLayer and reluLayer blocks. Weight matrices were extracted "
        "from the ONNX-imported autogenerated layer, transposed to match MATLAB's "
        "FC layer convention (output x input), and converted from double to single "
        "precision.",
        styles['BodyText2']
    ))
    story.append(Paragraph(
        "<b>Result:</b> The rebuilt native dlnetwork was successfully quantized to INT8 "
        "using dlquantizer, exported to Simulink via exportNetworkToSimulink, and "
        "compiled to embedded C code via Embedded Coder (ert.tlc). The generated C "
        "code uses int8_T arithmetic for all hidden layers with automatic "
        "quantization scaling via bit-shift operations.",
        styles['BodyText2']
    ))
    story.append(Spacer(1, 12))

    # ── 2. MODEL ARCHITECTURE ───────────────────────────────────────
    story.append(Paragraph("2. Model Architecture", styles['SectionHead']))
    story.append(Paragraph(
        "ACAS Xu (Airborne Collision Avoidance System for Unmanned Aircraft) is a "
        "family of neural networks that provide real-time advisory decisions for "
        "collision avoidance. Each network is a fully-connected multi-layer perceptron "
        "trained to approximate a large lookup table from the original ACAS X system.",
        styles['BodyText2']
    ))

    story.append(Paragraph("2.1 Inputs and Outputs", styles['SubsectionHead']))
    story.append(Paragraph(
        "The network takes 5 continuous inputs describing the encounter geometry "
        "and produces 5 outputs representing advisory action scores:",
        styles['BodyText2']
    ))

    io_data = [
        ['Direction', 'Index', 'Name', 'Description'],
        ['Input', '1', 'rho', 'Distance to intruder (ft)'],
        ['Input', '2', 'theta', 'Angle to intruder relative to ownship heading (rad)'],
        ['Input', '3', 'psi', 'Heading angle of intruder relative to ownship (rad)'],
        ['Input', '4', 'v_own', 'Speed of ownship (ft/s)'],
        ['Input', '5', 'v_int', 'Speed of intruder (ft/s)'],
        ['Output', '1', 'Clear of Conflict', 'No action needed'],
        ['Output', '2', 'Weak Left', 'Turn left 1.5 deg/s'],
        ['Output', '3', 'Weak Right', 'Turn right 1.5 deg/s'],
        ['Output', '4', 'Strong Left', 'Turn left 3.0 deg/s'],
        ['Output', '5', 'Strong Right', 'Turn right 3.0 deg/s'],
    ]
    story.append(Spacer(1, 6))
    story.append(make_table(io_data[0], io_data[1:],
                            col_widths=[0.8*inch, 0.6*inch, 1.5*inch, 3.6*inch]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("2.2 Network Architecture", styles['SubsectionHead']))

    arch_data = [
        ['Layer', 'Type', 'Size', 'Parameters'],
        ['Input', 'featureInputLayer', '5', '0'],
        ['FC1 + ReLU', 'fullyConnectedLayer + reluLayer', '50', '300 (W) + 50 (b)'],
        ['FC2 + ReLU', 'fullyConnectedLayer + reluLayer', '50', '2,550 (W) + 50 (b)'],
        ['FC3 + ReLU', 'fullyConnectedLayer + reluLayer', '50', '2,550 (W) + 50 (b)'],
        ['FC4 + ReLU', 'fullyConnectedLayer + reluLayer', '50', '2,550 (W) + 50 (b)'],
        ['FC5 + ReLU', 'fullyConnectedLayer + reluLayer', '50', '2,550 (W) + 50 (b)'],
        ['FC6 + ReLU', 'fullyConnectedLayer + reluLayer', '50', '2,550 (W) + 50 (b)'],
        ['FC7 (output)', 'fullyConnectedLayer', '5', '255 (W) + 5 (b)'],
    ]
    story.append(Spacer(1, 6))
    story.append(make_table(arch_data[0], arch_data[1:],
                            col_widths=[1.2*inch, 2.5*inch, 0.6*inch, 2.2*inch]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "Total: 13,005 parameters (50.8 KB float32). Architecture: "
        "Input(5) &rarr; [FC(50) + ReLU] x 6 &rarr; FC(5).",
        styles['BodyText2']
    ))
    story.append(PageBreak())

    # ── 3. ONNX IMPORT ATTEMPT ──────────────────────────────────────
    story.append(Paragraph("3. ONNX Import Attempt", styles['SectionHead']))

    story.append(Paragraph("3.1 importONNXNetwork (Legacy)", styles['SubsectionHead']))
    story.append(Paragraph(
        "The first attempt used MATLAB's importONNXNetwork function to load the "
        "ACAS Xu ONNX file (ACASXU_run2a_1_1_batch_2000.onnx). This failed with "
        "data format errors because the function does not support 1D input tensors "
        "of shape [1, 5]. The error message indicated that a 'BCSS' format was "
        "expected but a simple 1D vector was provided.",
        styles['BodyText2']
    ))

    story.append(Paragraph("3.2 importNetworkFromONNX (R2024a+)", styles['SubsectionHead']))
    story.append(Paragraph(
        "The newer importNetworkFromONNX function succeeded in loading the model "
        "but produced a network with only 3 autogenerated layers:",
        styles['BodyText2']
    ))

    onnx_layers = [
        ['#', 'Layer Name', 'Layer Type'],
        ['1', 'CustomInputLayerMultiOutput', 'Custom autogenerated input layer'],
        ['2', 'fused_MatMul_To_AddLayer1000', 'Fused MatMul + Add autogenerated layer'],
        ['3', 'PermuteLayer', 'Custom autogenerated permute layer'],
    ]
    story.append(Spacer(1, 6))
    story.append(make_table(onnx_layers[0], onnx_layers[1:],
                            col_widths=[0.5*inch, 2.5*inch, 3.5*inch]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("3.3 Incompatibilities", styles['SubsectionHead']))
    incompatibilities = [
        "<b>dlquantizer:</b> The autogenerated layers do not expose internal "
        "weight/bias learnables in the standard format required by the quantizer. "
        "Calling dlquantizer on this network fails.",
        "<b>exportNetworkToSimulink:</b> Custom autogenerated layers cannot be "
        "mapped to Simulink subsystem blocks. Export is rejected.",
        "<b>predict:</b> Even basic inference failed with a matrix dimension "
        "mismatch inside onnxMatMul, making the imported network unusable without "
        "manual intervention.",
    ]
    for item in incompatibilities:
        story.append(Paragraph(
            item, styles['BulletItem'], bulletText='\u2022'
        ))
    story.append(Spacer(1, 12))

    # ── 4. NATIVE dlnetwork REBUILD ─────────────────────────────────
    story.append(Paragraph("4. Native dlnetwork Rebuild", styles['SectionHead']))
    story.append(Paragraph(
        "Since the ONNX-imported network was incompatible with quantization and "
        "Simulink export, the solution was to construct a native dlnetwork from "
        "scratch using standard MATLAB Deep Learning Toolbox layers and transfer "
        "the trained weights from the autogenerated ONNX layer.",
        styles['BodyText2']
    ))

    story.append(Paragraph("4.1 Network Construction", styles['SubsectionHead']))
    story.append(Paragraph(
        "A 14-layer network was constructed: featureInputLayer(5) followed by "
        "6 blocks of [fullyConnectedLayer(50) + reluLayer], ending with a final "
        "fullyConnectedLayer(5) for the output. All layers use standard MATLAB "
        "Deep Learning Toolbox types with no custom or autogenerated code.",
        styles['BodyText2']
    ))

    story.append(Paragraph("4.2 Weight Transfer", styles['SubsectionHead']))
    weight_steps = [
        "Extracted weight matrices W0 through W6 and bias vectors B0 through B6 "
        "from the fused autogenerated layer's internal parameters.",
        "Transposed each weight matrix: ONNX convention stores weights as "
        "(input x output), while MATLAB fullyConnectedLayer expects "
        "(output x input).",
        "Converted all learnables from double to single precision, which is "
        "required by MATLAB Coder and Embedded Coder for code generation.",
        "Assigned transposed single-precision weights and biases to each "
        "fullyConnectedLayer in the rebuilt network.",
    ]
    for i, step in enumerate(weight_steps, 1):
        story.append(Paragraph(
            f"<b>Step {i}:</b> {step}", styles['BulletItem'], bulletText='\u2022'
        ))

    story.append(Paragraph("4.3 Verification", styles['SubsectionHead']))
    story.append(Paragraph(
        "The rebuilt network was verified against a manual forward pass "
        "(matrix multiplication + ReLU chain) using the same extracted weights. "
        "Results: maximum absolute error of 2.21e-04, cosine similarity of 1.0. "
        "The small absolute error arises from double-to-single precision conversion "
        "but has no practical impact on advisory output rankings.",
        styles['BodyText2']
    ))
    story.append(PageBreak())

    # ── 5. INT8 QUANTIZATION ────────────────────────────────────────
    story.append(Paragraph("5. INT8 Quantization", styles['SectionHead']))
    story.append(Paragraph(
        "With the native dlnetwork in place, INT8 quantization was performed "
        "using MATLAB's dlquantizer to reduce memory footprint and enable "
        "efficient integer-only inference on embedded targets.",
        styles['BodyText2']
    ))

    story.append(Paragraph("5.1 Quantization Procedure", styles['SubsectionHead']))
    quant_steps = [
        "Created dlquantizer object targeting the native dlnetwork with "
        "ExecutionEnvironment set to 'MATLAB'.",
        "Calibrated with 1,000 random input samples (5 features each) to "
        "determine activation ranges for each layer.",
        "The calibration produced 28 quantization entries: 7 weight matrices, "
        "7 bias vectors, and 14 activation ranges (input/output of each layer).",
        "Called quantize() to produce the final quantized dlnetwork with "
        "IsQuantized=true.",
    ]
    for step in quant_steps:
        story.append(Paragraph(step, styles['BulletItem'], bulletText='\u2022'))

    story.append(Paragraph("5.2 Quantized Layers", styles['SubsectionHead']))
    story.append(Paragraph(
        "All 13 active layers were quantized (7 fully-connected layers and "
        "6 ReLU layers). The featureInputLayer is not quantized as it merely "
        "defines the input format. Each FC layer's weights and biases are "
        "stored as INT8/INT32, and activation ranges are captured for dynamic "
        "fixed-point scaling during inference.",
        styles['BodyText2']
    ))

    quant_summary = [
        ['Metric', 'Value'],
        ['Quantization Type', 'INT8 (weights) / INT32 (biases)'],
        ['Calibration Samples', '1,000'],
        ['Quantization Entries', '28'],
        ['Quantized Layers', '13 (7 FC + 6 ReLU)'],
        ['IsQuantized', 'true'],
        ['Execution Environment', 'MATLAB'],
    ]
    story.append(Spacer(1, 6))
    story.append(make_table(quant_summary[0], quant_summary[1:],
                            col_widths=[2.5*inch, 4.0*inch]))
    story.append(Spacer(1, 12))

    # ── 6. SIMULINK EXPORT & C CODE GENERATION ──────────────────────
    story.append(Paragraph(
        "6. Simulink Export &amp; C Code Generation", styles['SectionHead']
    ))

    story.append(Paragraph("6.1 Export to Simulink", styles['SubsectionHead']))
    story.append(Paragraph(
        "The quantized dlnetwork was exported to Simulink using "
        "exportNetworkToSimulink. This created a Simulink model "
        "(ACASXU_Simulink.slx) containing individual subsystem blocks for "
        "each fully-connected and ReLU layer. The quantized model includes "
        "DataTypeConversion blocks (fc1_in_cast for input quantization and "
        "fc7_out_cast for output dequantization) that handle the conversion "
        "between floating-point I/O and internal INT8 computation.",
        styles['BodyText2']
    ))

    story.append(Paragraph("6.2 Code Generation Compatibility", styles['SubsectionHead']))
    story.append(Paragraph(
        "Before generating code, analyzeNetworkForCodegen was used to verify "
        "compatibility. The analysis confirmed that the quantized network is "
        "fully supported for all three target libraries: 'none' (pure C), "
        "'arm-compute' (ARM target), and 'mkldnn' (Intel target).",
        styles['BodyText2']
    ))

    story.append(Paragraph("6.3 Embedded Coder Output", styles['SubsectionHead']))
    story.append(Paragraph(
        "C code was generated via Embedded Coder using the ert.tlc system "
        "target file. The generated output includes the following key files:",
        styles['BodyText2']
    ))

    codegen_files = [
        ['File', 'Size', 'Description'],
        ['ACASXU_Simulink.c', '6.8 KB (320 lines)', 'Main step function with INT8 FC + ReLU logic'],
        ['ACASXU_Simulink_data.c', '306 KB', 'Constant data: int8 weights, int32 biases, scaling factors'],
        ['ert_main.c', '2.4 KB (105 lines)', 'Example main() with initialize/step/terminate calls'],
        ['ACASXU_Simulink.h', '~2 KB', 'Model header with type definitions and function prototypes'],
        ['ACASXU_Simulink_types.h', '~0.5 KB', 'Simulink type aliases'],
        ['rtwtypes.h', '~3 KB', 'Runtime type definitions (int8_T, real32_T, etc.)'],
    ]
    story.append(Spacer(1, 6))
    story.append(make_table(codegen_files[0], codegen_files[1:],
                            col_widths=[2.2*inch, 1.3*inch, 3.0*inch]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "Internal computation uses int8_T for all hidden-layer activations and "
        "weights. The output layer converts back to real32_T with a 0.25F "
        "scaling factor for the final advisory scores.",
        styles['BodyText2']
    ))
    story.append(PageBreak())

    # ── 7. GENERATED C CODE ANALYSIS ────────────────────────────────
    story.append(Paragraph("7. Generated C Code Analysis", styles['SectionHead']))

    story.append(Paragraph("7.1 API Structure", styles['SubsectionHead']))
    story.append(Paragraph(
        "The generated code follows the standard Embedded Coder pattern with "
        "three entry-point functions:",
        styles['BodyText2']
    ))
    api_items = [
        "<b>ACASXU_Simulink_initialize()</b> &mdash; One-time initialization of "
        "model state and I/O structures.",
        "<b>ACASXU_Simulink_step()</b> &mdash; Single inference step: reads INT8 "
        "inputs, executes 7 FC layers with ReLU activations, writes real32_T outputs.",
        "<b>ACASXU_Simulink_terminate()</b> &mdash; Cleanup (no-op for stateless "
        "networks, included for API consistency).",
    ]
    for item in api_items:
        story.append(Paragraph(item, styles['BulletItem'], bulletText='\u2022'))
    story.append(Spacer(1, 8))

    story.append(Paragraph("7.2 I/O Structures", styles['SubsectionHead']))

    io_structs = [
        ['Structure', 'Field', 'Type', 'Description'],
        ['ExtU_ACASXU_Simulink_T', 'input[5]', 'int8_T', 'Quantized 5-element input vector'],
        ['ExtY_ACASXU_Simulink_T', 'fc7_out[5]', 'real32_T', 'Dequantized 5-element output scores'],
        ['ConstP_ACASXU_Simulink_T', 'fc*_weights[]', 'int8_T', 'Quantized weight arrays per layer'],
        ['ConstP_ACASXU_Simulink_T', 'fc*_bias[]', 'int32_T', 'Quantized bias arrays per layer'],
    ]
    story.append(Spacer(1, 6))
    story.append(make_table(io_structs[0], io_structs[1:],
                            col_widths=[2.2*inch, 1.2*inch, 0.8*inch, 2.3*inch]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("7.3 Quantized Arithmetic", styles['SubsectionHead']))
    story.append(Paragraph(
        "The generated C code implements quantized inference using integer-only "
        "arithmetic. Key characteristics of the implementation:",
        styles['BodyText2']
    ))
    arith_items = [
        "All hidden-layer matrix multiplications use int8_T weights multiplied "
        "by int8_T activations, accumulated into int32_T accumulators.",
        "Quantization scaling is implemented via bit-shift operations "
        "(e.g., >> 6, >> 3, >> 4) with rounding, eliminating the need for "
        "floating-point division.",
        "ReLU activation is implemented as inline max(x, 0) comparisons "
        "on the int8_T intermediate values.",
        "The output layer applies a 0.25F scaling factor to convert from "
        "quantized int8_T back to real32_T for the final advisory scores.",
        "Bias vectors are stored as int32_T to preserve precision during "
        "the accumulation phase before re-quantization.",
    ]
    for item in arith_items:
        story.append(Paragraph(item, styles['BulletItem'], bulletText='\u2022'))
    story.append(Spacer(1, 8))

    story.append(Paragraph("7.4 Code Metrics", styles['SubsectionHead']))
    metrics_data = [
        ['Metric', 'Value'],
        ['Main source file', 'ACASXU_Simulink.c (320 lines, 6.8 KB)'],
        ['Weight data file', 'ACASXU_Simulink_data.c (306 KB)'],
        ['Weight storage type', 'int8_T (const arrays)'],
        ['Bias storage type', 'int32_T (const arrays)'],
        ['Hidden activation type', 'int8_T'],
        ['Output type', 'real32_T'],
        ['Output scaling', '0.25F'],
        ['Quantization scaling', 'Bit-shift (>> 6, >> 3, >> 4, etc.)'],
        ['ReLU implementation', 'Inline max(x, 0)'],
        ['System target file', 'ert.tlc (Embedded Real-Time)'],
    ]
    story.append(Spacer(1, 6))
    story.append(make_table(metrics_data[0], metrics_data[1:],
                            col_widths=[2.5*inch, 4.0*inch]))
    story.append(PageBreak())

    # ── APPENDIX A: FILE INVENTORY ──────────────────────────────────
    story.append(Paragraph("Appendix A: File Inventory", styles['SectionHead']))
    story.append(Paragraph(
        "Complete listing of project artifacts and generated files.",
        styles['BodyText2']
    ))

    inv_data = [
        ['File', 'Size', 'Description'],
        ['ACASXU_run2a_1_1_batch_2000.onnx', '~52 KB', 'Original ONNX model (float32)'],
        ['acasxu_native_net.mat', '~55 KB', 'Rebuilt native dlnetwork (MATLAB)'],
        ['ACASXU_Simulink.slx', '~120 KB', 'Simulink model with quantized network blocks'],
        ['ACASXU_Simulink.c', '6.8 KB', 'Generated C: step function with INT8 inference'],
        ['ACASXU_Simulink_data.c', '306 KB', 'Generated C: quantized weights and biases'],
        ['ert_main.c', '2.4 KB', 'Generated C: example main() entry point'],
        ['ACASXU_Simulink.h', '~2 KB', 'Generated C: model header and prototypes'],
        ['ACASXU_Simulink_types.h', '~0.5 KB', 'Generated C: Simulink type aliases'],
        ['rtwtypes.h', '~3 KB', 'Generated C: runtime type definitions'],
        ['ACASXU_Simulink_private.h', '~1 KB', 'Generated C: private model declarations'],
        ['ACASXU_Quantized_Simulink_CodeGen_Report.pdf', '~80 KB', 'This report'],
    ]
    story.append(Spacer(1, 6))
    story.append(make_table(inv_data[0], inv_data[1:],
                            col_widths=[2.8*inch, 0.8*inch, 3.0*inch]))
    story.append(Spacer(1, 20))

    # ── Footer ──────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", color=GRAY, thickness=0.5))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Generated by Claude Code &mdash; ACAS Xu Quantized Simulink C Code "
        "Generation Report &mdash; March 2026",
        ParagraphStyle('Footer', parent=styles['Normal'],
                       fontSize=8, textColor=GRAY, alignment=TA_CENTER)
    ))

    # ── Build ───────────────────────────────────────────────────────
    doc.build(story)
    print(f"Report saved to: {output_path}")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    output_path = os.path.join(
        project_dir, "ACASXU_Quantized_Simulink_CodeGen_Report.pdf"
    )
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    build_report(output_path)
