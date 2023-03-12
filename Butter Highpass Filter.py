import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar grayscale
img = cv2.imread('foto10.jpeg', 0)

# Lakukan transformasi Fourier pada gambar
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Buat filter Butterworth Highpass
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
d0 = 30
n = 2
butter_hp = np.zeros((rows, cols), np.float32)
for i in range(rows):
    for j in range(cols):
        d = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
        butter_hp[i, j] = 1 / (1 + (d / d0) ** (2 * n))

# Terapkan filter pada spektrum frekuensi
fshift_filtered = fshift * butter_hp

# Geser kembali nol frekuensi ke kiri atas
f_ishift = np.fft.ifftshift(fshift_filtered)

# Lakukan inverse Fourier Transform
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# Tampilkan gambar asli dan hasil filter
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title('Butterworth Highpass Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()
