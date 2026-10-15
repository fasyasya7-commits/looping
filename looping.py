import random

print("=== TEBAK ANGKA ===")

rahasia = random.randint(1, 100)
riwayat = []

# REPEAT ... UNTIL: ulangi terus sampai tebakan benar
while True:
    tebakan = input("Tebak angka (1-100): ")

    # WHILE: ulangi sampai yang dimasukkan berupa angka
    while not tebakan.isdigit():
        tebakan = input("Harus berupa angka! Coba lagi: ")

    tebakan = int(tebakan)
    riwayat.append(tebakan)

    if tebakan < rahasia:
        print("Terlalu kecil!")
    elif tebakan > rahasia:
        print("Terlalu besar!")

    if tebakan == rahasia:  # UNTIL tebakan benar
        break

print(f"Benar! Angkanya adalah {rahasia}.")

# FOR: tampilkan semua tebakan
print("Riwayat tebakanmu:")
for nomor, angka in enumerate(riwayat, start=1):
    print(f"  {nomor}. {angka}")  