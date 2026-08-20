import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ==============================
# 1. Project paths
# ==============================

BASE_DIR = Path(__file__).resolve().parent.parent

DOG_PATH = BASE_DIR / "images" / "dog.png"
LENNA_PATH = BASE_DIR / "images" / "Lenna.png"

OUTPUT_DIR = BASE_DIR / "output"
RESULTS_DIR = BASE_DIR / "results"

OUTPUT_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)


# ==============================
# 2. Read images
# ==============================

dog = cv2.imread(str(DOG_PATH), cv2.IMREAD_GRAYSCALE)
lenna = cv2.imread(str(LENNA_PATH), cv2.IMREAD_GRAYSCALE)

if dog is None:
    raise FileNotFoundError(f"Dog image not found: {DOG_PATH}")

if lenna is None:
    raise FileNotFoundError(f"Lenna image not found: {LENNA_PATH}")


# ==============================
# 3. Resize Lenna to Dog size
# ==============================

lenna = cv2.resize(
    lenna,
    (dog.shape[1], dog.shape[0])
)


# ==============================
# 4. Compute 2D Fourier Transform
# ==============================

F_dog = np.fft.fft2(dog)
F_lenna = np.fft.fft2(lenna)


# ==============================
# 5. Shift zero frequency
# ==============================

F_dog_shifted = np.fft.fftshift(F_dog)
F_lenna_shifted = np.fft.fftshift(F_lenna)


# ==============================
# 6. Calculate Magnitude
# ==============================

dog_magnitude = np.abs(F_dog_shifted)
lenna_magnitude = np.abs(F_lenna_shifted)


# ==============================
# 7. Calculate Phase
# ==============================

dog_phase = np.angle(F_dog_shifted)
lenna_phase = np.angle(F_lenna_shifted)


# ==============================
# 8. Display Magnitude & Phase
# ==============================

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(np.log(1 + dog_magnitude), cmap="gray")
plt.title("Dog - Fourier Magnitude")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(dog_phase, cmap="gray")
plt.title("Dog - Fourier Phase")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(np.log(1 + lenna_magnitude), cmap="gray")
plt.title("Lenna - Fourier Magnitude")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(lenna_phase, cmap="gray")
plt.title("Lenna - Fourier Phase")
plt.axis("off")

plt.tight_layout()

plt.savefig(
    RESULTS_DIR / "magnitude_phase.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==============================
# 9. Magnitude-Phase Swapping
# ==============================

# Dog Magnitude + Lena Phase
F_swap_1 = dog_magnitude * np.exp(1j * lenna_phase)

# Lena Magnitude + Dog Phase
F_swap_2 = lenna_magnitude * np.exp(1j * dog_phase)


# ==============================
# 10. Shift back
# ==============================

F_swap_1 = np.fft.ifftshift(F_swap_1)
F_swap_2 = np.fft.ifftshift(F_swap_2)


# ==============================
# 11. Inverse Fourier Transform
# ==============================

reconstructed_1 = np.fft.ifft2(F_swap_1)
reconstructed_2 = np.fft.ifft2(F_swap_2)


# Take real part
reconstructed_1 = np.real(reconstructed_1)
reconstructed_2 = np.real(reconstructed_2)


# ==============================
# 12. Normalize images
# ==============================

reconstructed_1 = cv2.normalize(
    reconstructed_1,
    None,
    0,
    255,
    cv2.NORM_MINMAX
).astype(np.uint8)

reconstructed_2 = cv2.normalize(
    reconstructed_2,
    None,
    0,
    255,
    cv2.NORM_MINMAX
).astype(np.uint8)


# ==============================
# 13. Save reconstructed images
# ==============================

cv2.imwrite(
    str(OUTPUT_DIR / "dog_magnitude_lenna_phase.png"),
    reconstructed_1
)

cv2.imwrite(
    str(OUTPUT_DIR / "lenna_magnitude_dog_phase.png"),
    reconstructed_2
)


# ==============================
# 14. Display reconstructed images
# ==============================

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(reconstructed_1, cmap="gray")
plt.title("Dog Magnitude + Lenna Phase")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(reconstructed_2, cmap="gray")
plt.title("Lenna Magnitude + Dog Phase")
plt.axis("off")

plt.tight_layout()

plt.savefig(
    RESULTS_DIR / "reconstructed_images.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


print("Fourier Transform analysis completed successfully!")
print("Results saved in output/ and results/")