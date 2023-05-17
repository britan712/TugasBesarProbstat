import os
import pandas as pd

# Mendapatkan path direktori saat ini
dir_path = os.path.dirname(os.path.realpath(__file__))

# Membaca file excel
df = pd.read_excel(os.path.join(dir_path, 'datasaya.xlsx'), usecols='B', skiprows=1, nrows=40)

# Menghitung rata-rata dan variansi
mean = df.mean().values[0]
variance = df.var().values[0]

# Menghitung modus, median, maksimum, minimum, serta quartile 1, quartile 2, dan quartile 3
mode = df.mode().values[0][0]
median = df.median().values[0]
maximum = df.max().values[0]
minimum = df.min().values[0]
q1 = df.quantile(0.25).values[0]
q2 = df.quantile(0.5).values[0]
q3 = df.quantile(0.75).values[0]

# Menampilkan hasil
print('Rata-rata:', mean)
print('Variansi:', variance)
print('Modus:', mode)
print('Median:', median)
print('Maksimum:', maximum)
print('Minimum:', minimum)
print('Q1:', q1)
print('Q2:', q2)
print('Q3:', q3)

# Menyimpan hasil ke dalam file excel baru
result = pd.DataFrame({
    'Rata-rata': [mean],
    'Variansi': [variance],
    'Modus': [mode],
    'Median': [median],
    'Maksimum': [maximum],
    'Minimum': [minimum],
    'Q1': [q1],
    'Q2': [q2],
    'Q3': [q3],
})
result.to_excel(os.path.join(dir_path, 'hasil.xlsx'), index=False)
