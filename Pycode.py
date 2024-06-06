import matplotlib.pyplot as plt

# Data penjualan
tanggal = ['01-06-2024', '01-06-2024', '02-06-2024', '02-06-2024', '03-06-2024', '03-06-2024']
jumlah_terjual = [10, 5, 15, 7, 20, 5]

# Membuat histogram
plt.hist(jumlah_terjual, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Jumlah Terjual')
plt.ylabel('Frekuensi Penjualan')
plt.title('Histogram Penjualan')
plt.grid(True)

# Menampilkan histogram
plt.show()

import matplotlib.pyplot as plt

# Data penjualan
tanggal = ['01-06-2024', '01-06-2024', '02-06-2024', '02-06-2024', '03-06-2024', '03-06-2024']
jumlah_terjual = [10, 5, 15, 7, 20, 5]

# Membuat pie chart
labels = ['01-06-2024', '02-06-2024', '03-06-2024']
sizes = [sum(jumlah_terjual[:2]), sum(jumlah_terjual[2:4]), sum(jumlah_terjual[4:])]
colors = ['gold', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0)  # Pisahkan potongan pertama (01-06-2024)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Pastikan pie chart bulat
plt.title('Pie Chart Penjualan')
plt.show()

import matplotlib.pyplot as plt

# Data penjualan
tanggal = ['01-06-2024', '01-06-2024', '02-06-2024', '02-06-2024', '03-06-2024', '03-06-2024']
jumlah_terjual = [10, 5, 15, 7, 20, 5]

# Membuat scatter plot
plt.scatter(tanggal, jumlah_terjual, color='blue', alpha=0.5)
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Terjual')
plt.title('Scatter Plot Penjualan')
plt.xticks(rotation=45)  # Putar label sumbu x untuk legibilitas
plt.grid(True)
plt.show()


