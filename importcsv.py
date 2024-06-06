import csv

# Data penjualan
tanggal = ['01-06-2024', '01-06-2024', '02-06-2024', '02-06-2024', '03-06-2024', '03-06-2024']
jumlah_terjual = [10, 5, 15, 7, 20, 5]

# Membuat file CSV
with open('penjualan.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tanggal', 'Jumlah Terjual'])  # Menulis header
    for i in range(len(tanggal)):
        writer.writerow([tanggal[i], jumlah_terjual[i]])  # Menulis baris data

print("File CSV 'penjualan.csv' berhasil dibuat.")
