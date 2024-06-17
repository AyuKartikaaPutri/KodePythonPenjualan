# Proyek Analisis dan Visualisasi Data

## Deskripsi Proyek
Proyek ini melibatkan analisis dan visualisasi data pelanggan, produk, dan transaksi menggunakan Python. Data yang digunakan terdiri dari informasi pelanggan, detail produk, dan catatan transaksi. Berbagai visualisasi seperti bar chart, pie chart, line plot, scatter plot, histogram, dan diagram Venn dibuat untuk mendapatkan wawasan dari data tersebut.

## Data
Proyek ini menggunakan dataset berikut:

1. **Pelanggan (`pelanggan.csv`):**
   - ID Pelanggan
   - Nama Pelanggan
   - Kota

2. **Produk (`produk.csv`):**
   - ID Produk
   - Nama Produk
   - Harga

3. **Transaksi (`transaksi.csv`):**
   - ID Transaksi
   - ID Pelanggan
   - ID Produk
   - Tanggal
   - Jumlah

## Kebutuhan
Pastikan Anda memiliki perangkat lunak berikut terinstal:
- Python 3.x
- pandas
- matplotlib
- seaborn
- matplotlib-venn

Anda dapat menginstal pustaka Python yang dibutuhkan dengan menjalankan perintah berikut:
```bash
pip install pandas matplotlib seaborn matplotlib-venn
```

## Cara Penggunaan
1. **Baca File CSV:**
    ```python
    import pandas as pd

    df_produk = pd.read_csv('produk.csv')
    df_pelanggan = pd.read_csv('pelanggan.csv')
    df_transaksi = pd.read_csv('transaksi.csv')

    print("DataFrame Produk:")
    print(df_produk)
    print("\nDataFrame Pelanggan:")
    print(df_pelanggan)
    print("\nDataFrame Transaksi:")
    print(df_transaksi)
    ```

2. **Visualisasi Harga Produk (Bar Chart):**
    ```python
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Nama Produk', y='Harga', data=df_produk)
    plt.title('Harga Produk')
    plt.xlabel('Nama Produk')
    plt.ylabel('Harga')
    plt.show()
    ```

3. **Visualisasi Distribusi Kota Pelanggan (Pie Chart):**
    ```python
    plt.figure(figsize=(8, 8))
    df_pelanggan['Kota'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title('Distribusi Kota Pelanggan')
    plt.ylabel('')
    plt.show()
    ```

4. **Visualisasi Jumlah Transaksi per Hari (Line Plot):**
    ```python
    df_transaksi['Tanggal'] = pd.to_datetime(df_transaksi['Tanggal'])
    transaksi_per_hari = df_transaksi.groupby('Tanggal').sum()['Jumlah'].reset_index()

    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Tanggal', y='Jumlah', data=transaksi_per_hari, marker='o')
    plt.title('Jumlah Transaksi per Hari')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah')
    plt.show()
    ```

5. **Scatter Plot Harga Produk vs Jumlah Transaksi:**
    ```python
    df_scatter = pd.merge(df_transaksi, df_produk, on='ID Produk')

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Harga', y='Jumlah', hue='Nama Produk', data=df_scatter, s=100)
    plt.title('Scatter Plot Harga Produk vs Jumlah Transaksi')
    plt.xlabel('Harga Produk')
    plt.ylabel('Jumlah Transaksi')
    plt.show()
    ```

6. **Histogram Harga Produk:**
    ```python
    plt.figure(figsize=(10, 6))
    sns.histplot(df_produk['Harga'], bins=10, kde=True)
    plt.title('Histogram Harga Produk')
    plt.xlabel('Harga Produk')
    plt.ylabel('Frekuensi')
    plt.show()
    ```

7. **Diagram Venn:**
    ```python
    from matplotlib_venn import venn2, venn3

    plt.figure(figsize=(10, 6))
    venn2(subsets=(3, 2, 1), set_labels=('Set A', 'Set B'))
    plt.title('Venn Diagram 2 Sets')
    plt.show()

    plt.figure(figsize=(10, 6))
    venn3(subsets=(3, 2, 1, 1, 1, 1, 1), set_labels=('Set A', 'Set B', 'Set C'))
    plt.title('Venn Diagram 3 Sets')
    plt.show()
    ```

8. **Pie Chart untuk Transaksi per Produk:**
    ```python
    transaksi_per_produk = df_transaksi.groupby('ID Produk').sum()['Jumlah'].reset_index()
    transaksi_per_produk = pd.merge(transaksi_per_produk, df_produk, on='ID Produk')

    plt.figure(figsize=(8, 8))
    transaksi_per_produk.set_index('Nama Produk')['Jumlah'].plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title('Distribusi Transaksi per Produk')
    plt.ylabel('')
    plt.show()
    ```

9. **Bar Chart untuk Transaksi per Kota:**
    ```python
    transaksi_per_kota = df_transaksi.merge(df_pelanggan, on='ID Pelanggan')
    transaksi_per_kota = transaksi_per_kota.groupby('Kota').sum()['Jumlah'].reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Kota', y='Jumlah', data=transaksi_per_kota)
    plt.title('Jumlah Transaksi per Kota')
    plt.xlabel('Kota')
    plt.ylabel('Jumlah Transaksi')
    plt.show()
    ```

## Struktur Proyek
- `pelanggan.csv`: Data pelanggan
- `produk.csv`: Data produk
- `transaksi.csv`: Data transaksi
- `visualisasi.py`: Skrip Python untuk analisis dan visualisasi data
