# Aplikasi Simulasi Algoritma Page Replacement LRU

## Introduction

Kode python ini menggunakan library `customtkinter` dan menyediakan antarmuka pengguna grafis (GUI) untuk mensimulasikan algoritma penggantian halaman Least Recently Used (LRU). Aplikasi ini dibangun menggunakan library Tkinter, dan hasil simulasi LRU ditampilkan dalam sebuah tabel.

## Opening Page

Halaman awal (`page_intro`) dari aplikasi ini berisi informasi tentang proyek akhir untuk mata kuliah Sistem Operasi. Ini mencakup detail tentang anggota kelompok proyek. Informasi anggota kelompok ditampilkan menggunakan widget `CTkLabel` dengan jenis huruf, warna, dan sudut sudut tertentu.

### Features
- Label judul (`intro_label`) dengan detail proyek.
- Informasi anggota kelompok (`kelompok`) ditampilkan menggunakan `CTkLabel`.
- Tombol mulai (`navigate_button`) untuk berpindah ke halaman simulasi LRU.

## LRU Simulation Page

Halaman simulasi LRU (`simulation_frame`) memungkinkan pengguna memasukkan string referensi dan jumlah frame untuk mensimulasikan algoritma LRU. Hasil simulasi ditampilkan dalam tabel dinamis (`Treeview`). Simulasi LRU dijalankan oleh kelas `AlgoritmaLRU`, dan hasilnya diperbarui pada GUI.

### Features
- Label judul (`title_label`) untuk simulasi LRU.
- Widget entri (`references` dan `frames`) untuk memasukkan string referensi dan jumlah frame.
- Tombol (`add_button`) untuk memulai simulasi LRU.
- Label (`label`) untuk menampilkan informasi tambahan atau pesan.
- Grip dapat diubah ukuran (`sizegrip`) untuk merubah ukuran jendela.

### Styling
- Elemen GUI diatur dengan menggunakan library `customtkinter`, dengan efek hover dan penyesuaian batas untuk tombol.

## Execution Flow

1. Pengguna memulai aplikasi di halaman awal dengan detail proyek.
2. Pengguna mengklik tombol "Mulai" untuk beralih ke halaman simulasi LRU.
3. Pada halaman simulasi LRU, pengguna memasukkan string referensi dan jumlah frame.
4. Pengguna mengklik tombol "Simulasi Jadwal" untuk menjalankan simulasi LRU.
5. Hasil simulasi LRU ditampilkan dalam tabel di halaman yang sama.
6. Pengguna dapat merubah ukuran jendela menggunakan grip yang dapat diubah ukuran.

## Dependencies

- `customtkinter`: Library Tkinter kustom yang digunakan untuk penyesuaian dan peningkatan tata letak.
- `script.AlgoritmaLRU`: Script yang berisi implementasi algoritma simulasi LRU.

## Usage

1. Jalankan gui.py atau guiNotebook.py berdasarkan preferensi.
2. Masukkan string referensi dan jumlah frame pada halaman simulasi LRU.
3. Klik tombol "Simulasi Jadwal" untuk menjalankan simulasi LRU.
4. Lihat hasil simulasi dalam tabel di halaman yang sama.

