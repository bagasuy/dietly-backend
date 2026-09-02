# Dietly Backend

Backend untuk aplikasi Dietly menggunakan Django REST Framework.

## Prerequisites

Pastikan sudah terinstall:

- Python 3.x
- PostgreSQL
- Git
________________________________________________________________________________________

## 1. Clone Repository

Clone repository backend:

:;bash
git clone https://github.com/bagasuy/dietly-backend


________________________________________________________________________________________


Masuk ke folder:
buka terminal 

cd dietly-backend

## 2. Buat Virtual Environment

Linux/macOS:

python3 -m venv .venv

Aktifkan:

source .venv/bin/activate

Windows:

python -m venv .venv

Aktifkan:

.venv\Scripts\activate

Jika berhasil, terminal akan menunjukkan:

(.venv)

## 3. Install Dependencies

Jalankan:

pip install -r requirements.txt

Tunggu sampai proses selesai.

## 4. Setup Environment Variables

Buat file .env di root project:

dietly-backend/
├── .env
├── manage.py
├── requirements.txt
└── ...

Isi .env sesuai konfigurasi database lokal.

Contoh:

SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=dietly
DB_USER=postgres
DB_PASSWORD=your-postgres-password
DB_HOST=127.0.0.1
DB_PORT=5432

Jangan upload .env ke GitHub.

Gunakan .env.example sebagai referensi jika tersedia.

## 5. Setup Database

Pastikan PostgreSQL sedang berjalan.

Buat database bernama:

dietly

atau gunakan nama database yang sesuai dengan konfigurasi .env.

Kemudian jalankan migration:

python manage.py migrate

Jika berhasil, Django akan membuat tabel yang dibutuhkan oleh aplikasi.

## 6. Jalankan Backend

Pastikan virtual environment masih aktif.

Jalankan:

python manage.py runserver

Jika berhasil, akan muncul:

Starting development server at http://127.0.0.1:8000/

Backend sekarang berjalan di:

http://127.0.0.1:8000/

API Dietly tersedia melalui:

http://127.0.0.1:8000/api/v1/

Biarkan terminal backend tetap berjalan.
