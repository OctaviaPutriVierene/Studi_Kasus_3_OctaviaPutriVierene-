# Studi_Kasus_3_OctaviaPutriVierene-

Nama: Octavia Putri Vierene<br>
NIM: 012

Penjelasan:
Tuple(batas_nilai)=(65,100): berfungsi sebagai penyimpan data acuan tetap, karena sifat Tuple yang tidak dapat diubah. Menyimpan nilai standar kelulusan(65) dan batas maksimal (100). 

nilai_masuk = []
lulus=[]
remedi = []
Tiga list kosong tersebut digunakan untuk menampung data dinamis

while True
jika dosen mengetik 'selesai' maka program akan memeriksa apakah jumlah nilai sudah minimal 5 ( len(nilai_masuk)<5). Kemudian ada .isdigit() untuk memastikan inputnya berupa angka dan memeriksa supaya nilainya tidak melebihi 100.

List(nilai_masuk, lulus, remedi): digunakan untuk mengelola data nilai data yang dapat diubah sehingga data nilai mahasiswa dapat terus ditambahkan atau dihapus jika terjadi kesalahan input.
setelah proses input selesai program akan menggunakan perulangan (for n in nilai_masuk) untuk membaca nilai. Setiap nilai dibandingkan dengan batas_nilai (65)

Masuk ke sistem koreksi data pada bagian ini user atau dosen Bruce dapat memperbaiki data yang salah ketik atau salah input. Program akan cek keberadaan nilai dengan operator 'in' laluu jika ketemu nilai akan di hapus dari list utama menggunakan '.remove'



Output:

<img width="1193" height="605" alt="image" src="https://github.com/user-attachments/assets/34ca4ff8-5541-42d5-a34f-de78feae6ef3" />
