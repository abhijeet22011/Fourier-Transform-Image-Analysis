# Image Analysis Using Fourier Transform: Magnitude–Phase Swapping

## 📌 Project Overview

This project demonstrates image analysis using the **2D Fast Fourier Transform (FFT)**. Two grayscale images, a Dog image and the Lena image, are transformed from the spatial domain into the frequency domain.

The Fourier representation is separated into:

* **Magnitude** — represents the strength of frequency components.
* **Phase** — contains important spatial and structural information.

The magnitude and phase components of the two images are then swapped and the images are reconstructed using the **Inverse Fourier Transform (IFFT)**.

---

## 🎯 Objectives

* Understand the Fourier Transform of digital images.
* Analyze magnitude and phase components.
* Visualize frequency-domain representations.
* Perform magnitude–phase swapping.
* Reconstruct images using the Inverse FFT.
* Study the contribution of magnitude and phase to image structure.

---

## 🧠 Theory

For a grayscale image (f(x,y)) of size (M \times N), the **2D Discrete Fourier Transform (DFT)** is:

$$
F(u,v)=
\sum_{x=0}^{M-1}
\sum_{y=0}^{N-1}
f(x,y)
e^{-j2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}
$$

The Fourier Transform produces complex values:

$$
F(u,v)=|F(u,v)|e^{j\phi(u,v)}
$$

where:

* ( |F(u,v)| ) = **Magnitude**
* ( \phi(u,v) ) = **Phase**

### Magnitude

The magnitude of the Fourier Transform is:

$$
|F(u,v)| = \sqrt{Re(F)^2 + Im(F)^2}
$$

Magnitude represents the **strength of each frequency component**.

### Phase

The phase is the angle of the complex Fourier coefficient:

$$
\phi(u,v) = \tan^{-1}\left(\frac{Im(F)}{Re(F)}\right)
$$

Phase contains important **spatial and structural information** about the image.

### Inverse Fourier Transform

The original image can be reconstructed using the inverse DFT:

$$
f(x,y)=
\frac{1}{MN}
\sum_{u=0}^{M-1}
\sum_{v=0}^{N-1}
F(u,v)
e^{j2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}
$$


## 🔄 Methodology

The project follows these steps:

1. Load the Dog and Lena images.
2. Convert images to grayscale.
3. Resize the images to the same dimensions.
4. Compute the 2D FFT.
5. Shift the zero-frequency component to the center.
6. Extract magnitude and phase.
7. Swap the phase components.
8. Reconstruct the complex Fourier spectra.
9. Apply the inverse FFT.
10. Normalize and save the reconstructed images.
11. Visualize the results.

---

## 🔬 Magnitude–Phase Swapping

Let:

* Dog magnitude = (M_D)
* Dog phase = (P_D)
* Lena magnitude = (M_L)
* Lena phase = (P_L)

### Reconstruction 1

[
F_1=M_D e^{jP_L}
]

**Dog Magnitude + Lena Phase**

### Reconstruction 2

[
F_2=M_L e^{jP_D}
]

**Lena Magnitude + Dog Phase**

Both reconstructed spectra are converted back into images using the inverse FFT.

---

## 📁 Project Structure

```text
Fourier-Transform-Image-Analysis/
│
├── images/
│   ├── dog.png
│   └── Lena.png
│
├── output/
│   ├── dog_magnitude_lena_phase.png
│   └── lena_magnitude_dog_phase.png
│
├── results/
│   ├── magnitude_phase.png
│   └── reconstructed_images.png
│
├── src/
│   └── fourier_transform.py
│
├── README.md
└── requirements.txt
```

---

## 🛠️ Technologies Used

* **Python**
* **NumPy** — Fourier Transform and numerical computation
* **OpenCV** — image reading, resizing and normalization
* **Matplotlib** — visualization

---

## ⚙️ Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

From the project root directory:

```bash
python src/fourier_transform.py
```

The generated results are automatically stored in the `output/` and `results/` folders.

---

## 📊 Results

The project produces:

### Fourier Magnitude and Phase

The `magnitude_phase.png` file shows:

* Dog Fourier Magnitude
* Dog Fourier Phase
* Lena Fourier Magnitude
* Lena Fourier Phase

### Reconstructed Images

The `reconstructed_images.png` file shows:

* Dog Magnitude + Lena Phase
* Lena Magnitude + Dog Phase

The swapped images demonstrate that changing the phase can significantly alter the spatial structure and recognizable features of the reconstructed image.

---

## 🔍 Key Observations

1. Fourier Transform represents an image using frequency components.
2. Magnitude describes the strength of different frequencies.
3. Phase contains important spatial and structural information.
4. `fftshift()` places the low-frequency components at the center for visualization.
5. Phase swapping produces reconstructed images with characteristics from both input images.
6. The experiment demonstrates the significant role of phase in image structure.

---

## 📝 Conclusion

This project demonstrates how the **2D Fourier Transform** can be used to analyze images in the frequency domain. By separating magnitude and phase and swapping these components between two images, we can study their individual contributions to image formation.

The experiment shows that although magnitude represents the strength of frequency components, **phase plays a crucial role in preserving spatial structure and recognizable image information**.

---

## 📚 References

* NumPy FFT documentation
* OpenCV documentation
* Matplotlib documentation
* Digital Image Processing concepts related to Fourier Transform
