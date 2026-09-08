# Dietly Backend

Backend REST API untuk aplikasi Dietly.

Dietly Backend dibangun menggunakan:

- Python
- Django
- Django REST Framework
- PostgreSQL
- Token Authentication

Backend menyediakan API untuk authentication, user profile, diet tracking, weight tracking, dan prediction.

---

## Requirements

Sebelum menjalankan backend, pastikan perangkat sudah memiliki:

- Git
- Python 3
- pip
- PostgreSQL
- pgAdmin 4 (disarankan untuk database setup)
- Akses ke repository backend Dietly
- File database backup `dietly_db_shared.backup`

> PostgreSQL dan backend harus berjalan pada komputer yang sama untuk local development.

---

# 1. Clone Repository

Clone repository backend:

``bash
git clone <URL-REPOSITORY-BACKEND>

Masuk ke folder project:

cd <NAMA-FOLDER-BACKEND>

Pastikan file manage.py tersedia:

ls

Contoh struktur project:

dietly-backend/
├── manage.py
├── requirements.txt
├── accounts/
├── diet/
├── prediction/
└── ...
# 2. Create Virtual Environment

Buat Python virtual environment:

python3 -m venv venv

Virtual environment digunakan agar dependency project terisolasi dari Python system.

Linux / macOS

Aktifkan virtual environment:

source venv/bin/activate
Windows
venv\Scripts\activate

Jika berhasil, terminal biasanya menunjukkan:

(venv)

di awal command line.

# 3. Install Python Dependencies

Pastikan virtual environment sudah aktif.

Kemudian jalankan:

pip install -r requirements.txt

Perintah ini akan menginstall dependency yang dibutuhkan backend Dietly.

# 4. Configure Environment Variables

Backend menggunakan file .env untuk menyimpan konfigurasi lokal.

File .env tidak disimpan di GitHub karena dapat berisi credential dan secret.

Buat file .env di folder yang sama dengan manage.py.

Contoh:

dietly-backend/
├── .env
├── manage.py
├── requirements.txt
└── ...

Isi .env:

SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=dietly_db
DB_USER=postgres
DB_PASSWORD=your-postgres-password
DB_HOST=127.0.0.1
DB_PORT=5432
Generate SECRET_KEY

Secret key dapat dibuat menggunakan Django:

python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Jika python3 tidak tersedia:

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Copy hasil command tersebut ke:

SECRET_KEY=hasil-secret-key
Database Configuration

Sesuaikan konfigurasi database dengan PostgreSQL lokal.

Contoh:

DB_NAME=dietly_db
DB_USER=postgres
DB_PASSWORD=your-postgres-password
DB_HOST=127.0.0.1
DB_PORT=5432

Keterangan:

Variable	Keterangan
SECRET_KEY	Secret key Django, generate sendiri
DEBUG	True untuk local development
DB_NAME	Nama database PostgreSQL
DB_USER	PostgreSQL username
DB_PASSWORD	Password PostgreSQL lokal
DB_HOST	Host PostgreSQL lokal
DB_PORT	Port PostgreSQL

DB_PASSWORD dan SECRET_KEY tidak harus sama dengan milik anggota kelompok lain.

# 5. Setup PostgreSQL Database

Buka pgAdmin 4.

Buat database baru dengan nama:

dietly_db

Contoh:

PostgreSQL
└── Databases
    └── dietly_db

Database ini harus menggunakan PostgreSQL lokal.

# 6. Restore Dietly Database

Untuk mempermudah setup development, gunakan database backup yang diberikan oleh project team:

dietly_db_shared.backup

Jangan gunakan dietly_db_full_backup.backup. File tersebut adalah backup pribadi/master dan tidak digunakan untuk setup anggota kelompok.

Restore menggunakan pgAdmin
Buka pgAdmin.
Klik kanan database dietly_db.
Pilih Restore...

Pada Format, pilih:

Custom or tar

Pada Filename, pilih:

dietly_db_shared.backup
Jalankan Restore.
Tunggu sampai proses selesai.
Refresh database.

Setelah restore, buka:

Schemas
└── public
    └── Tables

Seharusnya terdapat tabel seperti:

accounts_user
diet_dietentry
diet_weighthistory
prediction_prediction
authtoken_token
django_migrations
...
# 7. Apply Django Migrations

Setelah database selesai direstore, jalankan:

python3 manage.py migrate

Jika menggunakan Windows dan python3 tidak tersedia:

python manage.py migrate

Django akan memastikan migration yang diperlukan sudah diterapkan.

# 8. Check Django Configuration

Jalankan:

python3 manage.py check

Jika berhasil, akan muncul:

System check identified no issues (0 silenced).

Jika muncul error, periksa kembali:

.env
PostgreSQL
database name
PostgreSQL username
PostgreSQL password
PostgreSQL host
PostgreSQL port
9. Run Backend Server

Jalankan:

python3 manage.py runserver

Jika berhasil, server akan berjalan pada:

http://127.0.0.1:8000/

Backend sekarang sudah berjalan secara lokal.

Untuk menghentikan server:

CTRL + C
