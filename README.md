# Cat_Doorbell

Vision-based Cat Doorbell using FPGA Acceleration

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Repository Structure](#repository-structure)  
3. [Key Technical Achievements](#key-technical-achievements)  
4. [Performance Analysis](#performance-analysis)  
5. [Technical Stack](#technical-stack)  
6. [Getting Started](#getting-started)  
7. [Future Work](#future-work)  
8. [Acknowledgements & References](#acknowledgements--references)

---

## Project Overview

This project develops a computer vision system—the *Cat Doorbell*—that detects cats using a CNN followed by image preprocessing, frame averaging, etc., running on an Ultra96 V2 FPGA board. The goal is to explore and benchmark AI acceleration techniques in embedded FPGA systems, integrating both off-the-shelf acceleration (DPU via Vitis AI) and custom accelerators (HLS, OpenAMP, etc.).

---

## Repository Structure

Here’s how the Cat_Doorbell repo is organized:

```
Cat_Doorbell/
├── petalinux/         # PetaLinux build files for Ultra96 V2 (device tree, config, rootfs etc.)
├── python/            # Python-side code: data preprocessing, model training, inference scripts
├── vitis/             # Vitis‐Vision custom accelerators, library integration, image processing IP cores
├── vitis_ai/          # Vitis AI toolchain work: model quantization, compilation for DPU
├── vitis_hls/         # HLS (High Level Synthesis) projects: custom IP cores (averaging, preprocessing etc.)
├── vivado/            # Vivado hardware design / block design sources (if applicable)
├── .gitignore
├── README.md
└── readme.txt         # Possibly legacy notes or supplementary information
```

- **petalinux/** contains everything needed to build, configure, and deploy the PetaLinux image on Ultra96 V2 (Linux kernel, device tree source, overlays, root filesystem modifications).  
- **python/** is where the dataset, preprocessing code (including image correction, denoising, frame handling), CNN model training (Keras/TensorFlow), inference glue code lives.  
- **vitis/** includes modules using Vitis Vision libraries, integration of OpenCV + Vitis, and custom image processing accelerators.  
- **vitis_ai/** focuses on quantization of the trained model, compilation for the DPU, architecture definitions, model to bitstream workflows.  
- **vitis_hls/** contains HLS‐based IP cores for operations like image averaging, illumination correction etc., with their testbenches.  
- **vivado/** holds the lower level RTL / block designs / wiring together of accelerators (if applicable) and constraints.

---

## Key Technical Achievements

- **Algorithm & Training**  
  - CNN model for cat detection (cats vs dogs) using Keras/TensorFlow, trained on datasets from Kaggle.  
  - Preprocessing pipeline: CLAHE (illumination correction), denoising, frame averaging etc.  

- **FPGA Platform Setup**  
  - Ultra96 V2 board setup with PetaLinux, USB webcam support, configured device trees.  
  - WiFi, file transfer (SSH/SCP), etc., all working for embedded deployment.

- **Acceleration Implementations**  
  - Vitis AI: quantization & model compilation for the DPU, custom architectures to resolve fingerprint mismatches.  
  - Vitis Vision & OpenCV: acceleration of preprocessing (CLAHE, auto-white balance etc.).  
  - Custom HLS IPs: e.g. image averaging.  
  - Exploring use of OpenAMP / R5 cores for non-critical real-time tasks.

- **System Integration & Build Infrastructure**  
  - Memory management (CMA) for hardware accelerators.  
  - Resolving toolchain / library dependency conflicts.  
  - Integrating multiple acceleration paths (software, HLS, DPU).

---

## Performance Analysis

| Component            | Time (software baseline) |
|----------------------|---------------------------|
| CNN inference        | ~ 18.664 s                |
| Preprocessing        | ~ 0.339 s                 |
| Frame averaging      | ~ 0.212 s                 |

Based on profiling:

- **Image Detection** → target to be offloaded to DPU (via Vitis AI)  
- **Preprocessing** → acceleration via Vitis Vision / custom IP cores  
- **Frame Averaging** → possibly implemented on R5 core via OpenAMP or custom IP

---

## Technical Stack

- **Hardware**: Ultra96 V2 FPGA board, USB webcam, MicroSD for storage  
- **FPGA Tooling**: Vivado, Vitis, Vitis HLS, Vitis AI  
- **OS**: PetaLinux (on Ultra96), Ubuntu (host for development)  
- **Software**: Python (training, inference), C/C++ (embedded code), device tree, Tcl, Bash  
- **Libraries**: TensorFlow, Keras, OpenCV, Vitis Vision libs, XRT, etc.  

---

## Getting Started

Here’s how to clone, build, and run the system roughly end-to-end. (Assumes you have the necessary FPGA hardware, licenses, and toolchain installed.)

1. **Clone the repo**
   ```bash
   git clone https://github.com/caccolillo/Cat_Doorbell.git
   cd Cat_Doorbell
   ```

2. **Host-side / Model Training**
   - Go to `python/` to run data preprocessing scripts, model training (if retraining needed), and evaluating baseline performance.  
   - Save model checkpoints so they are available for quantization.

3. **Quantize & Compile for DPU**
   - Switch to `vitis_ai/`  
   - Quantize the trained model (post‐training quantization)  
   - Compile for the target DPU architecture  

4. **Build FPGA Accelerators**
   - Use `vitis_hls/` to build custom IP cores (e.g. image averaging)  
   - Use `vitis/` to integrate Vision Library accelerators  

5. **Prepare the PetaLinux System**
   - Go to `petalinux/`  
   - Configure device tree, rootfs modifications, build Linux image, boot Ultra96 V2  

6. **Deploy & Run**
   - Boot board with built PetaLinux image  
   - Transfer inference code + models (over SSH/SCP)  
   - Plug in USB webcam, run inference pipeline (preprocessing, detection, averaging etc.)  

7. **Profiling & Optimization**
   - Measure timings for each component  
   - Replace software components with accelerated versions one by one  

---

## Future Work

- Finalize full deployment of CNN model quantization + DPU inference and measure speedups.  
- Optimize memory usage and bandwidth (e.g. reduce bottlenecks between DDR/CMA/dma).  
- Reduce latency to allow real-time performance.  
- Power consumption profiling and optimizations.  
- Add support for additional vision tasks (e.g., tracking, detection of multiple object classes).  

---

## Acknowledgements & References

- Thanks to the Kaggle datasets for cats vs dogs for training data  
- Tutorials, documentation of Vitis AI, Vitis Vision, etc. used heavily (see notes in `docs/` or in the Scrapbook PDFs)  
- Key references for FPGA acceleration, quantization, OpenAMP, etc.
