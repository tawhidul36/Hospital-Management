# 🏥 Hospital Management System (Django + FastAPI + AI)

A full-featured **Hospital Management System** built with **Django** for web, **FastAPI** for AI-powered services, and integrated AI models for predictive healthcare analytics. The system manages patients, doctors, appointments, and hospital administration efficiently.



## Installation

# Hospital Management System (Django)

# 1️⃣ Clone the repository
git clone https://github.com/tawhidul36/Hospital-Management.git
cd Hospital-Management

# 2️⃣ Create Python virtual environment
python -m venv env

# 3️⃣ Activate virtual environment
# Linux / Mac
source env/bin/activate
# Windows
env\Scripts\activate

# 4️⃣ Install backend dependencies
pip install -r requirements.txt

# 5️⃣ Make migrations and migrate database
python manage.py makemigrations
python manage.py migrate

# 6️⃣ Create superuser (for Django admin)
python manage.py createsuperuser

# 7️⃣ Start Django backend server
python manage.py runserver 8000

# 8️⃣ Navigate to AI service folder
cd ai_service

# 9️⃣ Install AI service dependencies
pip install -r requirements.txt

# 🔟 Start FastAPI AI server
uvicorn main:app --reload --port 8001

# 1️⃣1️⃣ Open your browser to check:
# Django Admin: http://127.0.0.1:8000/admin/
# Django Frontend: http://127.0.0.1:8000/
# FastAPI AI endpoints: http://127.0.0.1:8001/docs


---

## 🚀 Features

### User Roles
- **Admin**: Full system control  
- **Doctor**: Patient management, appointments  
- **Patient**: Book appointments, view records  

### Admin Dashboard
- Manage doctors (add, approve, update)
- Manage patients (add, approve, update)
- Handle appointments (create, approve, reject)
- Generate patient discharge bills and reports
- View system analytics

### Doctor Dashboard
- View assigned patients
- Manage appointments
- Access patient discharge history
- AI-based patient insights and predictions (via FastAPI AI model)

### Patient Dashboard
- Book and manage appointments
- View medical history
- Access discharge summaries
- AI-based health recommendations

### AI/ML Integration
- **FastAPI-based endpoints** integrated with Django
- AI models for:
  - Predicting patient conditions
  - Anomaly detection in ECG or lab results
  - Intelligent suggestions for treatment planning

---
