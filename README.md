# LAB-AP-15-2026

Harap membaca seluruh panduan berikut sebelum memulai proses pengumpulan tugas.

---

## 📌 Perhatian

> Setiap teks yang dibungkus `< >` wajib diganti sesuai dengan data masing-masing.  
> Contoh: `mkdir <NIM>` → `mkdir H071241066`

> Pastikan Git sudah terinstal dan akun GitHub sudah login sebelum melakukan proses fork, clone, commit, push, dan pull request.

---

## 📥 Panduan Pengumpulan Tugas

### 1. Fork Repository

1. Buka repositori **LAB-AP-15-2026** di GitHub.
2. Klik tombol **Fork** yang terletak di pojok kanan atas halaman repository.
3. Pilih akun GitHub pribadi sebagai tujuan fork.
4. Repositori akan tersalin secara otomatis ke akun GitHub masing-masing.
5. Setelah proses fork selesai, buka repository hasil fork pada akun GitHub pribadi.

> Contoh repository hasil fork:
>
> ```text
> https://github.com/<username>/LAB-AP-15-2026.git
> ```

---

### 2. Buat dan Pilih Folder Penyimpanan Repository

Sebelum melakukan clone, buat atau pilih terlebih dahulu folder di komputer yang akan digunakan untuk menyimpan seluruh repository tugas.

Contoh, buat folder bernama `GitHub` atau `Tugas AP` pada drive yang diinginkan.

#### Contoh melalui File Explorer

1. Buka **File Explorer**.
2. Pilih lokasi penyimpanan, misalnya `Documents` atau drive `D:`.
3. Buat folder baru, misalnya:

   ```text
   D:\GitHub
   ```

   atau:

   ```text
   D:\Tuprak AP
   ```

4. Buka terminal, PowerShell, Git Bash, atau terminal di VS Code pada folder tersebut.

#### Contoh menggunakan PowerShell

Jika ingin menyimpan repository di folder `D:\Tuprak AP`, jalankan:

```powershell
cd D:\
mkdir Tuprak AP
cd Tuprak AP
```

Jika folder `Tuprak AP` sudah pernah dibuat, cukup masuk ke folder tersebut:

```powershell
cd D:\Tuprak AP
```

> Folder ini akan menjadi lokasi penyimpanan repository hasil clone dari GitHub.

---

### 3. Clone Repository Hasil Fork

Pastikan terminal sudah berada di dalam folder penyimpanan yang telah dipilih pada langkah sebelumnya.

Kemudian jalankan perintah berikut:

```bash
git clone <url-repositori-hasil-fork>
```

Contoh:

```bash
git clone https://github.com/username/LAB-AP-15-2026.git
```

Setelah proses clone selesai, akan terbentuk folder repository:

```text
LAB-AP-15-2026
```

Contoh struktur lokasi di komputer:

```text
D:\
└── Tuprak AP\
    └── LAB-AP-15-2026\
```

---

### 4. Masuk ke Direktori Repository

Masuk ke folder repository hasil clone:

```bash
cd LAB-AP-15-2026
```

Untuk memastikan terminal sudah berada pada repository yang benar, jalankan:

```bash
git status
```

Jika benar, biasanya akan muncul informasi seperti berikut:

```text
On branch main
Your branch is up to date with 'origin/main'.
```

---

### 5. Buat Folder Sesuai NIM

Buat folder dengan nama NIM masing-masing.

```bash
mkdir <NIM>
```

Contoh:

```bash
mkdir H071241066
```

> Pastikan NIM ditulis dengan benar dan sesuai ketentuan. Jangan menggunakan nama lengkap sebagai nama folder.

---

### 6. Buat Folder Praktikum

Masuk ke folder NIM yang telah dibuat:

```bash
cd <NIM>
```

Contoh:

```bash
cd H071241066
```

Kemudian buat folder praktikum dengan format:

```text
Praktikum-<n>
```

Perintahnya:

```bash
mkdir Praktikum-<n>
```

Contoh untuk Praktikum 1:

```bash
mkdir Praktikum-1
```

Masuk ke folder praktikum tersebut:

```bash
cd Praktikum-1
```

---

### 7. Tambahkan File Tugas

Letakkan seluruh file tugas ke dalam folder praktikum yang sesuai.

Format penamaan file tugas adalah:

```text
TP<n>_<nomor soal>_<NIM>.py
```

Contoh untuk Praktikum 1:

```text
TP1_1_H071241066.py
TP1_2_H071241066.py
```

Contoh struktur repository yang diharapkan:

```text
LAB-AP-15-2026/
├── H071241066/
│   ├── Praktikum-1/
│   │   ├── TP1_1_H071241066.py
│   │   └── TP1_2_H071241066.py
│   └── Praktikum-2/
│       ├── TP2_1_H071241066.py
│       └── TP2_2_H071241066.py
└── H071241067/
    ├── Praktikum-1/
    └── Praktikum-2/
```

> Pastikan file `.py` berada di dalam folder `Praktikum-<n>`, bukan langsung di dalam folder NIM atau folder utama repository.

---

### 8. Cek Perubahan File

Sebelum melakukan commit, kembali ke folder utama repository jika masih berada di dalam folder praktikum.

Contoh:

```bash
cd ../..
```

Kemudian cek file yang berubah atau baru ditambahkan:

```bash
git status
```

Pastikan yang muncul hanya folder dan file milik sendiri.

> ⚠️ Jangan mengubah, memindahkan, atau menghapus folder maupun file milik praktikan lain.

---

### 9. Add, Commit, dan Push

Setelah memastikan file tugas sudah benar, jalankan perintah berikut secara berurutan:

```bash
git add .
git commit -m "<pesan commit>"
git push origin main
```

Contoh:

```bash
git add .
git commit -m "feat: menambahkan Praktikum-1 H071241066"
git push origin main
```

Jika ini adalah push pertama dari repository hasil fork, GitHub mungkin meminta autentikasi akun. Ikuti proses login atau otorisasi yang muncul.

---

## 💬 Ketentuan Pesan Commit

Pesan commit menggunakan format **Conventional Commits** agar riwayat perubahan repository tetap konsisten dan mudah dibaca.

### Format

```text
<type>: <deskripsi singkat>
```

### Daftar Type Commit

| Type | Penggunaan |
|---|---|
| `feat` | Menambahkan tugas atau file baru |
| `fix` | Memperbaiki kesalahan kode atau penulisan |
| `docs` | Memperbarui dokumentasi, seperti README |
| `refactor` | Merapikan struktur kode tanpa mengubah fungsi program |
| `style` | Menyesuaikan format atau gaya penulisan kode |
| `chore` | Perubahan lain yang tidak berdampak pada kode utama |

### Contoh Pesan Commit

```text
feat: menambahkan Praktikum-1 H071241066
```

```text
feat: menambahkan TP1_1 dan TP1_2 H071241066
```

```text
fix: memperbaiki perhitungan total pada TP1_2 H071241066
```

```text
style: merapikan format kode Praktikum-1 H071241066
```

> Gunakan pesan commit yang jelas. Hindari pesan seperti `update`, `tugas`, `coba`, atau `fix bug` tanpa penjelasan.

---

## 🔃 Membuat Pull Request

Setelah berhasil melakukan push, buat Pull Request (PR) agar tugas dapat diperiksa dan digabungkan ke repository utama.

1. Buka repository hasil fork di akun GitHub masing-masing.
2. Pastikan file tugas sudah terlihat pada repository GitHub.
3. Klik tombol **Contribute**.
4. Klik **Open Pull Request**.
5. Pastikan arah Pull Request sudah benar:
   - **Base repository**: repository utama `LAB-AP-15-2026`
   - **Head repository**: repository hasil fork milik sendiri
6. Isi judul Pull Request dengan format berikut:

   ```text
   Praktikum-<n>-<NIM>
   ```

7. Contoh judul Pull Request:

   ```text
   Praktikum-1-H071241066
   ```

   ```text
   Praktikum-2-H071241066
   ```

8. Pada bagian deskripsi Pull Request, tuliskan daftar file yang ditambahkan atau diperbarui (opsional).

Contoh deskripsi Pull Request:

```text
Praktikum-1

File yang ditambahkan:
- TP1_1_H071241066.py
- TP1_2_H071241066.py
```

9. Klik **Create Pull Request**.

---

## ✅ Checklist Sebelum Mengirim PR

Sebelum membuat Pull Request, pastikan hal-hal berikut sudah benar:

- Repository sudah di-fork ke akun GitHub pribadi.
- Repository hasil fork sudah di-clone ke komputer.
- Folder NIM sudah dibuat dengan format yang benar.
- Folder praktikum menggunakan format `Praktikum-<n>`.
- File tugas menggunakan format `TP<n>_<nomor soal>_<NIM>.py`.
- Program dapat dijalankan tanpa error.
- Perubahan sudah dicek menggunakan `git status`.
- Commit menggunakan format Conventional Commits.
- Perubahan sudah di-push ke repository hasil fork.
- Judul Pull Request menggunakan format `Praktikum-<n>-<NIM>`.
- Deskripsi Pull Request memuat daftar file yang ditambahkan atau diperbarui.
- Tidak ada folder atau file milik praktikan lain yang diubah maupun dihapus.

---

> ⚠️ Dilarang mengubah atau menghapus folder milik praktikan lain.  
> ⚠️ Pull Request yang tidak sesuai format dapat tidak diproses atau tidak di-merge.
