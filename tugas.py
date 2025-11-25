"""
Tugas APD

Data.csv
Nim,nama,prodi,nilai,angkatan(bisa tambah bebas)

Leng data(bebas)

Output:
grubkan berdasarkan prodi dan angkatan

Di dalam word:

Berisi file csv, codingan, penjelasan dan ss output


Kumpul dalam bentuk word(data csv dan coding)
Kirim ke awanghk@unmul.ac.id
Title = NIM + NAMA + TUGAS ALD-02
"""

import pandas as pd
from tabulate import tabulate # library untuk mendapat output rapi

# Baca CSV
df = pd.read_csv("data.csv")

# Ambil daftar unik prodi dan angkatan
daftar_prodi = df["prodi"].unique()
daftar_angkatan = df["angkatan"].unique()

# Loop untuk setiap kombinasi prodi & angkatan
for p in daftar_prodi:
    for a in daftar_angkatan:

        # Filter berdasarkan prodi dan angkatan
        subset = df[(df["prodi"] == p) & (df["angkatan"] == a)]

        if len(subset) == 0:
            continue  # Lewati jika data kosong

        # Header
        print(f"=== PRODI: {p} | ANGKATAN: {a} ===")

        # Tampilkan tabel
        print(
            tabulate(
                subset[["nim", "nama", "nilai"]],
                headers=["NIM", "Nama", "Nilai"],
                tablefmt="grid",
                showindex=False
            )
        )

        print("\n")  # Jarak antar bagian
