# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QFbD69VKhBJXKvJxNPKV-l9ydjfDHsoJ
"""

print('@@@@      @     @@@@ @     @')
print('@  @     @ @    @    @     ')
print('@ @     @   @   @@@@ @     @  ')
print('@  @   @ @@@ @  @    @     @   ')
print('@   @ @       @ @    @@@@@ @      ')
def hitung_jumlah_range(start, end):
    # Menggunakan rumus untuk menghitung jumlah rentang bilangan
    total = (end - start + 1) * (start + end) / 2
    return total

# Memasukkan rentang bilangan
start_range = int(input("Masukkan nilai awal rentang: "))
end_range = int(input("Masukkan nilai akhir rentang: "))

# Memanggil fungsi untuk menghitung jumlah rentang bilangan dan menampilkannya
hasil = hitung_jumlah_range(start_range, end_range)
print(f"Jumlah dari rentang bilangan adalah: {hasil}")