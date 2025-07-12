Step to steup project:

🔹 Step 1: Install Python Extension in VS Code
1. Open VS Code
2. Go to Extensions (left sidebar or Ctrl + Shift + X)
3. Search for: "Python"
4. Install the one published by Microsoft

🔹 Step 2: Create Your Django Project Folder
1. mkdir smart_service_system
2. cd smart_service_system

🔹 Step 3: Create a Virtual Environment
python -m venv venv

🔹 Step 4: Activate the Virtual Environment
venv\Scripts\activate

🔹 Step 5: Install Django
pip install django

✅ Check installation:
django-admin --version

🔹 Step 6: Create Django Project
django-admin startproject smartservice .

This will create files like:
1. manage.py
2. smartservice/settings.py

🔹 Step 7: Run the Development Server
python manage.py runserver
	
Open browser → Visit: http://127.0.0.1:8000
✅ If you see “The install worked successfully!” → Django is working.

Username (leave blank to use 'sushe'): admin
Email address: admin@gmail.com
Password: admin

Folder structure:
smart_service_system/           ← Your main project folder
│
├── manage.py                   ← Django management script
│
├── venv/                       ← Python virtual environment (optional)
│
├── smartservice/              ← Django project settings folder
│   ├── __init__.py
│   ├── settings.py             ← Project settings (DB, apps, etc.)
│   ├── urls.py                 ← Main URL router
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/                   ← Custom user (User + Provider + Admin)
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py                ← For admin panel customizations
│   ├── apps.py
│   ├── models.py               ← CustomUser model with roles
│   ├── views.py                ← Login/Register views
│   ├── urls.py                 ← Auth routes: signup, login
│   ├── forms.py                ← Signup form
│   └── templates/
│       └── accounts/
│           ├── login.html
│           └── signup.html
│
├── bookings/                   ← Booking app (user books provider)
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py               ← Booking model
│   ├── views.py                ← Booking views
│   ├── urls.py                 ← Booking URLs
│   └── templates/
│       └── bookings/
│           ├── create_booking.html
│           └── booking_list.html
│
├── reviews/                    ← Ratings & reviews module
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── reviews/
│           └── review_form.html
│
├── static/                     ← CSS, JS, Images
│   ├── css/
│   ├── js/
│   └── images/
│
└── templates/                  ← Shared templates (base.html, navbars, etc.)
    ├── base.html
    ├── user_dashboard.html
    ├── provider_dashboard.html
    └── admin_dashboard.html


SECRET_KEY - @%k*bh%125ohi%cbayu##np52^x$%scbj2s)ricg6-#+&6si!r

Admin:
Username : admin
Password : admin

User:
Username : amit
Password : Test@1234

Service Provider:
Username: reema
Password: Test@1234	

Github account:
chauhanreemaamit@gmail.com
*6352217770@Reema

gihub access token :  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

git clone https://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@github.com/devreemaamit/Find-Local-Service-And-Booking-System.git
