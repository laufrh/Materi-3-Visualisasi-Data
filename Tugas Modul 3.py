import numpy as np
import matplotlib.pyplot as plt

# Parameter
g = 9.8  # percepatan gravitasi (m/s^2)
h0 = 100  # ketinggian awal (m)

# 1. Tentukan waktu yang diperlukan benda untuk mencapai tanah
T = np.sqrt(2 * h0 / g)
print("Waktu yang diperlukan untuk mencapai tanah = ", T, "s")

# 2. Buat data untuk grafik kecepatan dan posisi
t = np.arange(0, T, 0.01)
v = g * t  # Kecepatan sebagai fungsi waktu
h = h0 - 0.5 * g * t**2  # Posisi sebagai fungsi waktu

# Setup GridSpec untuk mengatur layout grafik
gs = plt.GridSpec(3, 3)
fig = plt.figure(figsize=(8, 8))

# Grafik kecepatan vs waktu (plot 1)
s1 = fig.add_subplot(gs[1, :2])
s1.plot(t, v, 'r')
s1.set_title('Kecepatan vs Waktu')
s1.set_xlabel('Waktu (s)')
s1.set_ylabel('Kecepatan (m/s)')
s1.grid(True)

# Grafik posisi vs waktu (plot 2 - bar chart)
s2 = fig.add_subplot(gs[0, :2])
s2.bar(t[::20], h[::20])  # Menggunakan subset data untuk clarity
s2.set_title('Posisi vs Waktu (Bar)')
s2.set_xlabel('Waktu (s)')
s2.set_ylabel('Posisi (m)')
s2.grid(True)

# Grafik posisi vs waktu (horizontal bar chart)
s3 = fig.add_subplot(gs[2, 0])
s3.barh(t[::20], h[::20], color='g')
s3.set_title('Posisi Horizontal Bar')
s3.set_xlabel('Posisi (m)')
s3.set_ylabel('Waktu (s)')
s3.grid(True)

# Grafik kecepatan vs waktu (plot kecil - kanan atas)
s4 = fig.add_subplot(gs[:2, 2])
s4.plot(t, v, 'k')
s4.set_title('Kecepatan vs Waktu (Kecil)')
s4.set_xlabel('Waktu (s)')
s4.set_ylabel('Kecepatan (m/s)')
s4.grid(True)

# Kombinasi dua grafik (plot 5)
s5 = fig.add_subplot(gs[2, 1:])
s5.plot(t[::10], v[::10], 'b^', t[::10], h[::10], 'yo')
s5.set_title('Kecepatan & Posisi (Marker)')
s5.set_xlabel('Waktu (s)')
s5.set_ylabel('Nilai')
s5.grid(True)

plt.tight_layout()
plt.show()
