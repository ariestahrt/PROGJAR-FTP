# Tugas Progjar

## Anggota
1. 05111940000105 - I Kadek Agus Ariesta Putra
2. 05111940000161 - Timotius Wirawan

## Desc
[FTP-1] Nama dan versi FTP server

Informasi:
- Alamat FTP server: localhost
- Username: sembarang
- Password: sembarang
Cetaklah nama dan versi dari FTP server tersebut.
Contoh output yang diharapkan: `vsFTPd 3.0.2`

[FTP-2] Sistem yang diemulasikan FTP server

Cetaklah sistem yang diemulasikan oleh FTP server. Contoh rangkaian output yang diharapkan adalah sebagai berikut:
```
220 (vsFTPd 3.0.2)
331 Please specify the password.
230 Login successful.
215 UNIX Type: L8
221 Goodbye.
```

[FTP-3] Daftar file di FTP server (metode PASV)

Tampilkan semua file yang ada di home directory masing-masing pada FTP server. 
Metode pasif yang digunakan adalah PASV. Port data yang digunakan bisa didapatkan dengan rumus berikut:

`data_port = p1 * 256 + p2`

dimana respon dari server setelah perintah PASV adalah a1,a2,a3,a4,p1,p2 (a adalah address, p adalah port).
Contoh output yang diharapkan adalah sebagai berikut:
```
.bash_logout
.bashrc
.profile
```

[FTP-4] Mengunggah file

Unggahlah sebuah file ekstensi apa saja ke FTP server.
Contoh output yang diharapkan:
```
220 (vsFTPd 3.0.2)
331 Please specify the password.
230 Login successful.
200 Switching to ASCII mode.
150 Ok to send data.
226 Transfer complete.
221 Goodbye.
```

[FTP-5] Membuat direktori

Buatlah sebuah direktori dengan nama "test". 
Contoh output yang diharapkan adalah sebagai berikut:
```
220 (vsFTPd 3.0.2)
331 Please specify the password.
230 Login successful.
257 "/test" created
221 Goodbye.
```

[FTP-6] Direktori saat ini di FTP server

Informasi:
- Alamat FTP server: localhost
- Username: sembarang
- Password: sembarang
Cetaklah direktori yang aktif saat ini di home directory pada FTP server.
Contoh output yang diharapkan adalah sebagai berikut:
```
220 (vsFTPd 3.0.2)
331 Please specify the password.
230 Login successful.
257 "/"
221 Goodbye.
```

[FTP-7] Mengganti nama direktori

Gantilah nama direktori "test" yang dibuat pada soal FTP-5 dengan "test2".
Contoh output yang diharapkan adalah sebagai berikut:
```
220 (vsFTPd 3.0.2)
331 Please specify the password.
230 Login successful.
350 Ready for RNTO.
250 Rename successful.
221 Goodbye.
```

[FTP-8] Menghapus direktori

Hapuslah direktori "test2" yang diproses pada soal FTP-7.
Contoh output yang diharapkan:
```
250 Remove directory operation successful.
```
