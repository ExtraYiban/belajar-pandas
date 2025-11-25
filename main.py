import os
os.system("cls || clear")
# ===============================================================
# 1. APA ITU PANDAS?
# ---------------------------------------------------------------
# Pandas adalah pustaka (library) Python yang dirancang untuk ANALISIS DATA dan PENGELOLAAN DATA.
#
# Apa arti analisis data pada level dasar?
# - Memuat data ke dalam Python
# - Memeriksa bentuk datanya
# - Membersihkan nilai yang salah atau hilang (missing values)
# - Memilih bagian data yang ingin digunakan
# - Menyimpan kembali data yang telah diproses ke dalam file
#
# Nama "Pandas" berasal dari:
#   PANel DAta = data berbentuk tabel (seperti spreadsheet)
#
# Pandas merupakan salah satu alat paling umum digunakan untuk:
#   - Ilmu data (data science)
#   - Pengganti database untuk proyek kecil
#   - Analitik bisnis
#   - Otomatisasi tugas-tugas Excel
#
# Untuk menggunakan Pandas, Anda harus menginstalnya (cukup sekali):
#   pip install pandas
# ===============================================================

from colorama import init, Fore, Style
init(autoreset=True)

# Variabel warna untuk teks penjelasan saja
Judul = Fore.CYAN + Style.BRIGHT
Info = Fore.BLUE
Success = Fore.GREEN + Style.BRIGHT
Warning = Fore.YELLOW + Style.BRIGHT
Error = Fore.RED + Style.BRIGHT
ACTION = Fore.MAGENTA + Style.BRIGHT

print(Judul + "Bagian 1: Apa itu Pandas?")
print(Info + """
Pandas adalah pustaka Python untuk analisis dan pengelolaan data.
Nama 'Pandas' berasal dari 'Panel Data' — struktur data berbentuk tabel.
""")
input(ACTION + "Tekan Enter untuk melanjutkan ke bagian: Mengimpor Pandas...")

# ===============================================================
# 2. MENGIMPOR PANDAS
# ---------------------------------------------------------------
import pandas as pd

print(Success + "Pandas berhasil diimpor sebagai 'pd'.")
input(ACTION + "Tekan Enter untuk melanjutkan ke bagian: Struktur Data Utama...")

# ===============================================================
# 3. STRUKTUR DATA UTAMA DI PANDAS
# ---------------------------------------------------------------
print(Info + "Pandas memiliki dua struktur utama: Series (1D) dan DataFrame (2D).")
input(ACTION + "Tekan Enter untuk melanjutkan ke bagian: Membuat Series...")

# ===============================================================
# 4. MEMBUAT SERIES
# ---------------------------------------------------------------
data = [100, 102, 103]
another_data = [100.1, 102.3, 103.5]
non_number = ["A", "B", "C"]
what_about_this = [True, False, True]

# ubah variabel what_about_this ke salah satu 4 variabel yang ada di atas
my_series = pd.Series(what_about_this)

print(Judul + "=== Contoh Series ===")
print(my_series)
print()

print(Judul + "=== Series dengan Indeks Kustom ===")
my_series = pd.Series(data, index=["a", "b", "c"])
so_we_can_do_this = pd.Series(data, index=["Apartment #1", "Apartment #2", "Apartment #3"])
print(my_series)
print()

print(Judul + "=== Akses Nilai dengan `.loc` ===")
print(my_series.loc["a"])
print()

print(Info + "Ubah Nilai pada indeks 'c'")
my_series.loc["c"] = 200
print(my_series)
print()

print(Info + "Akses Nilai dengan `.iloc` (posisi ke-1)")
print(my_series.iloc[1])
print()

data = [100, 102, 104, 200, 202]
my_series = pd.Series(data, index=["a", "b", "c", "d", "e"])
print(Info + "Anda harus memastikan jumlah label sesuai dengan jumlah data")
print(my_series)
print()

print(Judul + "=== Filtering Series dengan Kondisi Logika ===")
print(my_series[my_series >= 200])
print()

print(Judul + "=== Series dari Dictionary ===")
calories = {
    "Day 1": 1750,
    "Day 2": 2100,
    "Day 3": 1700,
}
series = pd.Series(calories)
print(series)
print()

print(Info + "Menggunakan `.loc` untuk akses 'Day 2'")
print(series.loc["Day 2"])
print()

series.loc["Day 3"] += 500

print(Info + "Sekarang kita bisa melakukan pemeriksaan!")
print(Success + "Pada hari apa saya tidak mengikuti rencana diet?")
print(series[series >= 2000])
print(Success + "Pada hari apa saya mengikuti rencana diet?")
print(series[series < 2000])
print()

input(ACTION + "Tekan Enter untuk melanjutkan ke bagian: Membuat DataFrame...")

# ===============================================================
# 5. DATAFRAME
# ---------------------------------------------------------------
print(Judul + "Membuat DataFrame dari dictionary")
data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

df = pd.DataFrame(data)
print("\nDataFrame awal:")
print(df)
print()

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
print(Info + "DataFrame dengan indeks kustom:")
print(df)
print()

print(Info + "Mengambil baris 'Employee 1' dengan `.loc`:")
print(df.loc["Employee 1"])
print()

print(Info + "Mengambil baris pertama dengan `.iloc`:")
print(df.iloc[0])
print()

print(Info + "Menambahkan kolom 'Job':")
df["Job"] = ["Cook", "N/A", "Cashier"]
print(df)
print()

print(Info + "Menambahkan baris baru untuk 'Sandy':")
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}], index=["Employee 4"])
df = pd.concat([df, new_row])
print(df)
print()

input(ACTION + "Tekan Enter untuk melanjutkan ke bagian: Memuat Data dari File CSV...")

# ===============================================================
# 6. MEMUAT DATA DARI FILE (IMPORTING)
# ---------------------------------------------------------------
print(Judul + "Memuat data dari file 'data.csv'...")
try:
    df = pd.read_csv("data.csv")
    print(Info + "\nData yang dimuat (tampilan default terpotong):")
    print(df)
    print(Info + "\nTampilan lengkap dengan `.to_string()`:")
    print(df.to_string())
except FileNotFoundError:
    print(Error + "File 'data.csv' tidak ditemukan. Lanjutkan dengan data contoh.")
    df = pd.DataFrame({
        "nama": ["Budi", "Ani", "Cici"],
        "nim": [2511207001, 2511207002, 2511207003],
        "nilai": [85, 92, 78]
    })
    print(df.to_string())

input(ACTION + "Tekan Enter untuk melanjutkan ke bagian: Seleksi Data...")

# ===============================================================
# 7. SELEKSI DATA
# ---------------------------------------------------------------
# Memilih kolom atau baris dari DataFrame.
# ===============================================================
print(Info + "Pilih satu kolom:")
print(df["nama"])
print()

print(Info + "Pilih beberapa kolom:")
print(df[["nama","nim","nilai"]])
print()

print(Info + "Tampilan lengkap beberapa kolom:")
print(df[["nama","nim","nilai"]].to_string())
print()

print(Info + "Pilih baris dengan .loc:")
print(df.loc[0])
print()

print(Info + "Gunakan 'nim' sebagai indeks:")
df = pd.read_csv("data.csv", index_col="nim")
print(df.to_string())
print()

print(Info + "Akses baris berdasarkan nilai 'nim':")
print(df.loc[2511207002])
print()

print(Info + "Akses kolom spesifik dari baris tersebut:")
print(df.loc[2511207002, ["nama","nilai"]])
print()

print(Info +"Akses dengan .iloc (posisi):")
print(df.iloc[0:2])  # 2 baris pertama
print()

input(ACTION + "Tekan Enter untuk melanjutkan ke bagian: Filtering Data")

# ===============================================================
# 8. FILTERING
# ---------------------------------------------------------------
# Menyaring baris berdasarkan kondisi tertentu.
# Hasilnya adalah DataFrame baru yang hanya berisi baris yang memenuhi syarat.
# ===============================================================
print(Info + "Filter: mahasiswa dengan nilai >= 90")
mahasiswa_lulus = df[df["nilai"] >= 90]
print(mahasiswa_lulus)
print()

print(Success + "Selesai!")