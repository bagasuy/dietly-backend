# Dietly Backend

Backend REST API untuk aplikasi Dietly.

Dietly Backend dibangun menggunakan:

- Python
- Django
- Django REST Framework
- PostgreSQL
- Token Authentication
- Django CORS Headers

Backend menyediakan API untuk authentication, user profile, diet tracking, weight tracking, dan prediction.

---

## Requirements

Sebelum menjalankan backend, pastikan perangkat sudah memiliki:

- Git
- Python 3.10+
- pip
- PostgreSQL
- pgAdmin 4
- Akses ke repository backend Dietly
- File database backup `dietly_db_shared.backup`

> PostgreSQL dan backend harus berjalan pada komputer yang sama untuk local development.

---

## 1. Clone Repository

Clone repository backend:

```bash
git clone <URL-REPOSITORY-BACKEND>
```

Masuk ke folder project:

```bash
cd <NAMA-FOLDER-BACKEND>
```

Pastikan file `manage.py` tersedia:

```bash
ls
```

Contoh struktur project:

```text
dietly-backend/
├── manage.py
├── requirements.txt
├── accounts/
├── diet/
├── prediction/
└── ...
```

---

## 2. Create Virtual Environment

Buat Python virtual environment:

```bash
python3 -m venv .venv
```

Virtual environment digunakan agar dependency project terisolasi dari Python system.

### Linux / macOS

Aktifkan virtual environment:

```bash
source .venv/bin/activate
```

### Windows

Aktifkan virtual environment:

```bash
.venv\Scripts\activate
```

Jika berhasil, terminal biasanya menunjukkan:

```text
(.venv)
```

di awal command line.

---

## 3. Install Python Dependencies

Pastikan virtual environment sudah aktif.

Kemudian jalankan:

```bash
pip install -r requirements.txt
```

Perintah ini akan menginstall dependency yang dibutuhkan backend Dietly.

---

## 4. Configure Environment Variables

Backend menggunakan file `.env` untuk menyimpan konfigurasi lokal.

File `.env` tidak disimpan di GitHub karena dapat berisi credential dan secret.

Buat file `.env` di folder yang sama dengan `manage.py`.

Contoh struktur:

```text
dietly-backend/
├── .env
├── manage.py
├── requirements.txt
└── ...
```

Isi `.env`:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=dietly_db
DB_USER=postgres
DB_PASSWORD=your-postgres-password
DB_HOST=127.0.0.1
DB_PORT=5432
```

> Jangan commit file `.env` ke Git.

### Generate SECRET_KEY

Secret key dapat dibuat menggunakan Django:

```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Jika `python3` tidak tersedia:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy hasil command tersebut ke:

```env
SECRET_KEY=hasil-secret-key
```

### Database Configuration

Sesuaikan konfigurasi database dengan PostgreSQL lokal.

Contoh:

```env
DB_NAME=dietly_db
DB_USER=postgres
DB_PASSWORD=your-postgres-password
DB_HOST=127.0.0.1
DB_PORT=5432
```

| Variable | Keterangan |
|---|---|
| `SECRET_KEY` | Secret key Django, generate sendiri |
| `DEBUG` | `True` untuk local development |
| `DB_NAME` | Nama database PostgreSQL |
| `DB_USER` | PostgreSQL username |
| `DB_PASSWORD` | Password PostgreSQL lokal |
| `DB_HOST` | Host PostgreSQL lokal |
| `DB_PORT` | Port PostgreSQL |

> `DB_PASSWORD` dan `SECRET_KEY` tidak harus sama dengan milik anggota kelompok lain.

---

## 5. Setup PostgreSQL Database

Buka pgAdmin 4.

Buat database baru dengan nama:

```text
dietly_db
```

Contoh:

```text
PostgreSQL
└── Databases
    └── dietly_db
```

Database ini harus menggunakan PostgreSQL lokal.

---

## 6. Restore Dietly Database

Untuk mempermudah setup development, gunakan database backup yang diberikan oleh project team:

```text
dietly_db_shared.backup
```

> Jangan gunakan `dietly_db_full_backup.backup`. File tersebut adalah backup pribadi/master dan tidak digunakan untuk setup anggota kelompok.

### Restore menggunakan pgAdmin

1. Buka pgAdmin 4.
2. Klik kanan database `dietly_db`.
3. Pilih **Restore...**
4. Pada **Format**, pilih **Custom or tar**.
5. Pada **Filename**, pilih `dietly_db_shared.backup`.
6. Jalankan **Restore**.
7. Tunggu sampai proses selesai.
8. Refresh database.

Setelah restore, buka:

```text
Schemas
└── public
    └── Tables
```

Seharusnya terdapat tabel seperti:

```text
accounts_user
diet_dietentry
diet_weighthistory
prediction_prediction
authtoken_token
django_migrations
...
```

---

## 7. Apply Django Migrations

Setelah database selesai direstore, jalankan:

```bash
python3 manage.py migrate
```

Jika menggunakan Windows dan `python3` tidak tersedia:

```bash
python manage.py migrate
```

Django akan memastikan migration yang diperlukan sudah diterapkan.

---

## 8. Check Django Configuration

Jalankan:

```bash
python3 manage.py check
```

Jika berhasil, akan muncul:

```text
System check identified no issues (0 silenced).
```

Jika muncul error, periksa kembali:

- `.env`
- PostgreSQL
- Database name
- PostgreSQL username
- PostgreSQL password
- PostgreSQL host
- PostgreSQL port

---

## 9. Run Backend Server

Jalankan:

```bash
python3 manage.py runserver
```

Jika menggunakan Windows dan `python3` tidak tersedia:

```bash
python manage.py runserver
```

Jika berhasil, server akan berjalan pada:

```text
http://127.0.0.1:8000/
```

API base URL:

```text
http://127.0.0.1:8000/api/v1/
```

Backend sekarang sudah berjalan secara lokal.

Untuk menghentikan server:

```text
CTRL + C
```

---

## API Documentation

Dietly API endpoints are documented and tested using Postman.

### Authentication

| Method | Endpoint |
|---|---|
| POST | `/api/v1/auth/register/` |
| POST | `/api/v1/auth/login/` |
| POST | `/api/v1/auth/logout/` |
| GET | `/api/v1/auth/me/` |
| PATCH | `/api/v1/auth/me/` |

### Diet

| Method | Endpoint |
|---|---|
| GET | `/api/v1/diet/` |
| POST | `/api/v1/diet/` |
| GET | `/api/v1/diet/weight/` |
| POST | `/api/v1/diet/weight/` |
| GET | `/api/v1/diet/<id>/` |
| PATCH | `/api/v1/diet/<id>/` |
| DELETE | `/api/v1/diet/<id>/` |

### Prediction

| Method | Endpoint |
|---|---|
| GET | `/api/v1/prediction/` |
| POST | `/api/v1/prediction/` |

---

## Project Structure

```text
dietly-backend/
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── diet/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── prediction/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── api/
├── config/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Development Notes

- Authentication uses token-based authentication.
- User profile information is stored in the custom User model.
- Diet and weight data are persisted in PostgreSQL.
- Prediction results are stored and returned through the prediction API.
- The frontend communicates with this backend through REST APIs.