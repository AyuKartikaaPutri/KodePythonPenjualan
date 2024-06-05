import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_venn import venn2, venn3

# Membaca file CSV
df_produk = pd.read_csv('produk.csv')
df_pelanggan = pd.read_csv('pelanggan.csv')
df_transaksi = pd.read_csv('transaksi.csv')

# Menampilkan DataFrame
print("DataFrame Produk:")
print(df_produk)
print("\nDataFrame Pelanggan:")
print(df_pelanggan)
print("\nDataFrame Transaksi:")
print(df_transaksi)

# Visualisasi Harga Produk (Bar Chart)
plt.figure(figsize=(10, 6))
sns.barplot(x='Nama Produk', y='Harga', data=df_produk)
plt.title('Harga Produk')
plt.xlabel('Nama Produk')
plt.ylabel('Harga')
plt.show()

# Visualisasi Distribusi Kota Pelanggan (Pie Chart)
plt.figure(figsize=(8, 8))
df_pelanggan['Kota'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Distribusi Kota Pelanggan')
plt.ylabel('')
plt.show()

# Visualisasi Jumlah Transaksi per Hari (Line Plot)
plt.figure(figsize=(10, 6))
df_transaksi['Tanggal'] = pd.to_datetime(df_transaksi['Tanggal'])
transaksi_per_hari = df_transaksi.groupby('Tanggal').sum()['Jumlah'].reset_index()
sns.lineplot(x='Tanggal', y='Jumlah', data=transaksi_per_hari, marker='o')
plt.title('Jumlah Transaksi per Hari')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah')
plt.show()

# Scatter Plot of Harga Produk vs Jumlah Transaksi
plt.figure(figsize=(10, 6))
df_scatter = pd.merge(df_transaksi, df_produk, on='ID Produk')
sns.scatterplot(x='Harga', y='Jumlah', hue='Nama Produk', data=df_scatter, s=100)
plt.title('Scatter Plot Harga Produk vs Jumlah Transaksi')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Transaksi')
plt.show()

# Histogram of Harga Produk
plt.figure(figsize=(10, 6))
sns.histplot(df_produk['Harga'], bins=10, kde=True)
plt.title('Histogram Harga Produk')
plt.xlabel('Harga Produk')
plt.ylabel('Frekuensi')
plt.show()

# Venn Diagram
plt.figure(figsize=(10, 6))
venn2(subsets=(3, 2, 1), set_labels=('Set A', 'Set B'))
plt.title('Venn Diagram 2 Sets')
plt.show()

plt.figure(figsize=(10, 6))
venn3(subsets=(3, 2, 1, 1, 1, 1, 1), set_labels=('Set A', 'Set B', 'Set C'))
plt.title('Venn Diagram 3 Sets')
plt.show()

# Pie Chart for Transaksi per Produk
plt.figure(figsize=(8, 8))
transaksi_per_produk = df_transaksi.groupby('ID Produk').sum()['Jumlah'].reset_index()
transaksi_per_produk = pd.merge(transaksi_per_produk, df_produk, on='ID Produk')
transaksi_per_produk.set_index('Nama Produk')['Jumlah'].plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Distribusi Transaksi per Produk')
plt.ylabel('')
plt.show()

# Bar Chart for Transaksi per Kota
plt.figure(figsize=(10, 6))
transaksi_per_kota = df_transaksi.merge(df_pelanggan, on='ID Pelanggan')
transaksi_per_kota = transaksi_per_kota.groupby('Kota').sum()['Jumlah'].reset_index()
sns.barplot(x='Kota', y='Jumlah', data=transaksi_per_kota)
plt.title('Jumlah Transaksi per Kota')
plt.xlabel('Kota')
plt.ylabel('Jumlah Transaksi')
plt.show()
