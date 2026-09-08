batas_nilai = (65, 100) 
nilai_masuk = []
lulus = []
remedi = []
print("INPUT NILAI MAHASISWA")
print("Ketik 'selesai' jika sudah cukup memasukkan nilai.\n")
while True:
    input_user = input("Masukkan nilai ujian (atau ketik 'selesai'): ").strip()
    if input_user.lower() == 'selesai':
        if len(nilai_masuk) < 5:
            print(f"Maaf, minimal harus memasukkan 5 nilai. Saat ini baru ada {len(nilai_masuk)} nilai.")
            continue
        ada_lulus = any(n >= batas_nilai[0] for n in nilai_masuk)
        ada_remedi = any(n < batas_nilai[0] for n in nilai_masuk)
        if not ada_lulus or not ada_remedi:
            print(f"Harus ada minimal satu nilai Lulus(>= {batas_nilai[0]}) dan satu nilai Remedi (< {batas_nilai[0]})!")
            continue
        break
    if input_user.isdigit():
        nilai = int(input_user)
        if nilai > batas_nilai[1]: 
            print(f"Nilai tidak boleh lebih dari {batas_nilai[1]}!")
        else:
            nilai_masuk.append(nilai)
            print(f"Nilai {nilai} berhasil ditambahkan.")
    else:
        print("Input tidak valid! Masukkan angka atau ketik 'selesai'.")
for n in nilai_masuk:
    if n >= batas_nilai[0]:
        lulus.append(n)
    else:
        remedi.append(n)
print("\nSISTEM KOREKSI DATA")
print("Daftar nilai saat ini:", nilai_masuk)
pilihan_hapus = input("Apakah ada nilai yang salah dan ingin dihapus? (ya/tidak): ").strip().lower()
if pilihan_hapus == 'ya':
    hapus_nilai = input("Masukkan nilai yang ingin dihapus: ").strip()
    if hapus_nilai.isdigit():
        nilai_target = int(hapus_nilai)
        if nilai_target in nilai_masuk:
            nilai_masuk.remove(nilai_target)
            if nilai_target >= batas_nilai[0]:
                lulus.remove(nilai_target)
            else:
                remedi.remove(nilai_target)
            print(f" Nilai {nilai_target} berhasil dihapus dari sistem.")
        else:
            print("Nilai tidak ditemukan pada daftar.")
    else:
        print("Input tidak valid!")
print("HASIL AKHIR")
print("Semua nilai masuk :", nilai_masuk)
print("Daftar nilai lulus:", lulus)
print("Daftar nilai remedi:", remedi)