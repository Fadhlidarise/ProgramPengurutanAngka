import os

# Fungsi untuk tukar data dalam array
def tukar_data(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Prosedur untuk pengurutan data menggunakan metode bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                tukar_data(arr, j, j+1)

# Prosedur untuk menulis data ke file
def tulis_ke_file(arr):
    with open("hasil_pengurutan.txt", "w") as file:
        for nilai in arr:
            file.write(str(nilai) + "\n")

# Prosedur untuk membaca data dari file
def baca_dari_file():
    with open("hasil_pengurutan.txt", "r") as file:
        lines = file.readlines()
        return [int(line.strip()) for line in lines]

# Program utama
angka = []

while True:
    print("\nMENU PILIHAN")
    print("1. Input angka")
    print("2. Tampil hasil pengurutan")
    print("3. Selesai")

    pilihan = input("Masukkan pilihan [1/2/3]: ")

    if pilihan == '1':
        jumlah_angka = int(input("Masukkan jumlah angka yang akan diinput: "))
        print("Input Angka Secara Acak")
        print("-" * 45)
        for i in range(jumlah_angka):
            nilai = int(input(f"Angka {i+1} : "))
            angka.append(nilai)

    elif pilihan == '2':
        if not angka:
            print("Belum ada data yang diinput. Silakan pilih menu 1 terlebih dahulu.")
        else:
            bubble_sort(angka)
            tulis_ke_file(angka)
            hasil_pengurutan = baca_dari_file()
            print("\nTAMPIL HASIL PENGURUTAN")
            print("Nilai tugas:", ", ".join(map(str, hasil_pengurutan)))

    elif pilihan == '3':
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

