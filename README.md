✅ 1. Clone the GitHub Repo
git clone https://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@github.com/devreemaamit/Find-Local-Service-And-Booking-System.git

✅ 2. Create a Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

✅ 3. Install Dependencies
pip install Django
pip install mysqlclient
pip install python-dotenv
pip install requests
pip install whitenoise
pip install fastapi uvicorn apscheduler requests
pip install apscheduler

✅ 4. Set Up .env File (If Required)
SECRET_KEY=your-django-secret-key
DB_NAME=smart_service_db
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306

settings.py
from dotenv import load_dotenv
load_dotenv()
import os

SECRET_KEY = os.getenv('SECRET_KEY')
✅ 5. Create MySQL Database
CREATE DATABASE smart_service_db;

✅ 6. Apply Migrations
python manage.py makemigrations
python manage.py migrate

✅ 7. Create Admin User
python manage.py createsuperuser

You'll be asked to enter:
Username
Email
Password

✅ 8. Run the Server
python manage.py runserver

✅ 9. Open in Browser
| URL                             | Purpose      |
| ------------------------------- | ------------ |
| `http://127.0.0.1:8000/`        | Project Home |
| `http://127.0.0.1:8000/login/`  | Login Page   |
| `http://127.0.0.1:8000/signup/` | Signup Page  |
| `http://127.0.0.1:8000/admin/`  | Admin Panel  |

✅ 10. Project Running Successfully 🎉
You can now:
Login as user/provider/admin
Navigate to dashboards (/user/home/, /provider/home/, etc.)
Use admin panel to manage data
