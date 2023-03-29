import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# class data() :
#     data = pd.read_csv('ecommerce_lite.csv', usecols=['InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country'])
#     print(data.head())

class Nomor2() :
    print('Nomor 2\n')
    #import dataframe
    data = pd.read_csv('ecommerce_lite.csv', usecols=['InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country'])

    #mencari data sesuai kode
    kode_barang = '22423'
    barang = data.loc[data['StockCode'] == kode_barang]

    #nama barang
    nama_barang = barang['Description'].iloc[0]
    print("Nama Barang:", nama_barang)

    #mencari mean median modus dari kolom harga
    mean = data['Quantity'].mean()
    median = data['Quantity'].median()
    modus = data['Quantity'].mode()[0]

    print("\nNilai Mean:", mean)
    print("Nilai Median:", median)
    print("Nilai Modus:", modus)

    #mencari q1-q3 dan iqr
    q1 = data['Quantity'].quantile(0.25)
    q2 = data['Quantity'].median()
    q3 = data['Quantity'].quantile(0.75)
    iqr = q3-q1
    
    print("\nNilai Q1:", q1)
    print("Nilai Q2:", q2)
    print("Nilai Q3:", q3)
    print("Nilai IQR:", iqr)

    #mencari outlier
    batas_bawah = q1 - 1.5 * iqr
    batas_atas = q3 + 1.5 * iqr

    jumlah_outlier = data.loc[(data['Quantity'] < batas_bawah) | (data['Quantity'] > batas_atas)].shape[0]

    print("Jumlah outlier:", jumlah_outlier, '\n')

    #mencari histogram
    barang['Quantity'].hist(bins=20)
    plt.xlabel('Quantity')
    plt.ylabel('Frequency')
    plt.show()

    # if not barang.empty:
    #     # Mengambil nama barang dari hasil filtering
    #     nama_barang = barang['Description'].iloc[0]
    #     print(barang)
    # else:
    #     print("Data barang tidak ditemukan.")
    # # nama_barang = barang['Description'].iloc[0]
    # # print(nama_barang)

class Nomor3() :
    print('Nomor 3\n')
    #import dataframe
    data = pd.read_csv('ecommerce_lite.csv', usecols=['InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country'])

    #mencari data sesuai kode
    kode_barang = '22423'
    barang = data.loc[data['StockCode'] == kode_barang]

    #mengelompokkan jumlah baris berdasarkan negara
    groupedData = data.groupby('Country')['Quantity'].sum()
    print(groupedData, '\n')

    #merubah jumlah menjadi persentase
    total = data['Quantity'].sum()

    # print(total)
    # if total != 0 :
    #     print('ada')
    # else :
    #     print('kosong')

    groupedData['Persentase'] = data.groupby('Country')['Quantity'].sum() / total * 100
    print(groupedData['Persentase'], '\n')

    #list data 5 barang teratas berdasarkan jumlah penjualan
    groupedByBarang = data.groupby(['StockCode','Description'])['Quantity'].sum()
    print (groupedByBarang.sort_values (ascending=False)[:5])
