# Dietly Backend

Backend REST API for the Dietly application.

Dietly Backend is built using:

- Python
- Django
- Django REST Framework
- PostgreSQL
- Token Authentication
- Django CORS Headers

The backend provides APIs for authentication, user profiles, diet tracking, weight tracking, and prediction.

## Requirements

Before running the backend, make sure the following are installed or available:

- Git
- Python 3.10+
- pip
- PostgreSQL
- pgAdmin 4
- Access to the Dietly backend repository
- The dietly_db_shared.backup database backup file

PostgreSQL and the backend should run on the same computer for local development.

## API Documentation

Interactive API documentation is available through Postman:

https://documenter.getpostman.com/view/57559320/2sBYAyu9K1

The documentation includes the available Dietly API endpoints for:

- Authentication
- User Profile
- Diet Tracking
- Weight Tracking
- Prediction

## 1. Clone Repository

Clone the Dietly backend repository:

```bash

git clone https://github.com/bagasuy/dietly-backend.git

```

Enter the project directory:

```bash

cd dietly-backend

```

Make sure manage.py is available:

```bash

ls

```

Example project structure:

```text

dietly-backend/

├── manage.py

├── requirements.txt

├── accounts/

├── diet/

├── prediction/

└── ...

```

## 2. Create Virtual Environment

Create a Python virtual environment:

```bash

python3 -m venv .venv

```

The virtual environment keeps project dependencies isolated from the system Python installation.

### Linux / macOS

Activate the virtual environment:

```bash

source .venv/bin/activate

```

### Windows

Activate the virtual environment:

```bash

.venv\Scripts\activate

```

If the activation is successful, the terminal usually displays:

```text

(.venv)

```

at the beginning of the command line.

## 3. Install Python Dependencies

Make sure the virtual environment is activated.

Install the required dependencies:

```bash

pip install -r requirements.txt

```

This command installs all Python packages required by the Dietly backend.

## 4. Configure Environment Variables

The backend uses a .env file to store local configuration.

The .env file is not stored in GitHub because it may contain credentials and secret values.

Create a .env file in the same directory as manage.py.

Example structure:

```text

dietly-backend/

├── .env

├── manage.py

├── requirements.txt

└── ...

```

Add the following configuration:

```env

SECRET_KEY=your-secret-key

DEBUG=True

DB_NAME=dietly_db

DB_USER=postgres

DB_PASSWORD=your-postgres-password

DB_HOST=127.0.0.1

DB_PORT=5432

```

Never commit the .env file to Git.

### Generate SECRET_KEY

Generate a Django secret key using:

```bash

python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

```

If python3 is not available:

```bash

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

```

Copy the generated value into:

```env

SECRET_KEY=your-generated-secret-key

```

### Database Configuration

Configure the database connection according to your local PostgreSQL installation.

Example:

```env

DB_NAME=dietly_db

DB_USER=postgres

DB_PASSWORD=your-postgres-password

DB_HOST=127.0.0.1

DB_PORT=5432

```

Variable	Description
SECRET_KEY	Django secret key. Generate your own value.
DEBUG	Set to True for local development.
DB_NAME	PostgreSQL database name.
DB_USER	PostgreSQL username.
DB_PASSWORD	Local PostgreSQL password.
DB_HOST	PostgreSQL host.
DB_PORT	PostgreSQL port.

DB_PASSWORD and SECRET_KEY do not need to be the same for every team member.

## 5. Set Up PostgreSQL Database

Open pgAdmin 4.

Create a new PostgreSQL database named:

```text

dietly_db

```

Example:

```text

PostgreSQL

└── Databases

└── dietly_db

```

The database should use your local PostgreSQL installation.

## 6. Restore Dietly Database

To simplify the development setup, use the database backup provided by the project team:

```text

dietly_db_shared.backup

```

Do not use dietly_db_full_backup.backup. This file is the private master backup and must not be distributed to team members.

Restore Using pgAdmin
Open pgAdmin 4.
Right-click the dietly_db database.
Select Restore...
Under Format, select Custom or tar.
Under Filename, select dietly_db_shared.backup.
Click Restore.
Wait until the restore process is complete.
Refresh the database.

After the restore process, open:

```text

Schemas

└── public

└── Tables

```

You should see tables such as:

```text

accounts_user

diet_dietentry

diet_weighthistory

prediction_prediction

authtoken_token

django_migrations

...

```

The dietly_db_shared.backup file should be shared privately with team members and should not be uploaded to GitHub.

## 7. Apply Django Migrations

After restoring the database, run:

```bash

python3 manage.py migrate

```

If python3 is not available on Windows:

```bash

python manage.py migrate

```

Django will ensure that all required migrations have been applied.

## 8. Check Django Configuration

Run:

```bash

python3 manage.py check

```

If python3 is not available:

```bash

python manage.py check

```

If the configuration is correct, Django should display:

```text

System check identified no issues (0 silenced).

```

If an error occurs, check the following:

.env
PostgreSQL
Database name
PostgreSQL username
PostgreSQL password
PostgreSQL host
PostgreSQL port

## 9. Run Backend Server

Start the Django development server:

```bash

python3 manage.py runserver

```

If python3 is not available:

```bash

python manage.py runserver

```

If successful, the backend will be available at:

```text

http://127.0.0.1:8000/

```

API base URL:

```text

http://127.0.0.1:8000/api/v1/

```

The Dietly backend is now running locally.

To stop the development server:

```text

CTRL + C

```

## API Endpoints

Dietly API endpoints are documented and tested using Postman.

Authentication
Method	Endpoint
POST	/api/v1/auth/register/
POST	/api/v1/auth/login/
POST	/api/v1/auth/logout/
GET	/api/v1/auth/me/
PATCH	/api/v1/auth/me/
Diet
Method	Endpoint
GET	/api/v1/diet/
POST	/api/v1/diet/
GET	/api/v1/diet/weight/
POST	/api/v1/diet/weight/
GET	/api/v1/diet/<id>/
PATCH	/api/v1/diet/<id>/
DELETE	/api/v1/diet/<id>/
Prediction
Method	Endpoint
GET	/api/v1/prediction/
POST	/api/v1/prediction/

For detailed request parameters, authentication requirements, request bodies, and responses, see the Postman API Documentation.

## Project Structure

```text

dietly-backend/

├── accounts/

│ ├── models.py

│ ├── serializers.py

│ ├── views.py

│ └── urls.py

│

├── diet/

│ ├── models.py

│ ├── serializers.py

│ ├── views.py

│ └── urls.py

│

├── prediction/

│ ├── models.py

│ ├── serializers.py

│ ├── views.py

│ └── urls.py

│

├── api/

├── config/

├── manage.py

├── requirements.txt

└── README.md

```

## Development Notes

Authentication uses token-based authentication.
User profile information is stored in the custom User model.
Diet and weight data are persisted in PostgreSQL.
Prediction results are stored and returned through the prediction API.
The frontend communicates with this backend through REST APIs.
The backend and frontend are maintained in separate GitHub repositories.
The backend is responsible for API services, authentication, database operations, business logic, and prediction functionality.

## Repository

Backend

https://github.com/bagasuy/dietly-backend

Frontend

https://github.com/bagasuy/dietly-frontend
