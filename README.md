# Student-result-portal

A web-based portal built using **Django** to manage student details and results.

---

## 🚀 Features
1. Student login & logout system  
2. Admin panel to manage students & results  
3. Add, update, and delete student records  
4. View results subject-wise  
5. Secure authentication with Django  

---

## 🛠️ Technologies Used
- Python 3.x  
- Django Framework  
- SQLite / MySQL (Database)  
- HTML, CSS, Bootstrap  

---

## ⚙️ Installation & Setup (Step by Step)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ayesha-Cherukuri/Student-result-portal.git
cd Student-result-portal

2.Create Virtual Environment
python -m venv venv

3.Activate environment
venv\Scripts\activate     #On Windows
source venv/bin/activate   #On Mac/Linux

4.Install Requirements
pip install -r requirements.txt

5.Apply Migrations
python manage.py makemigrations
python manage.py migrate

6.Create Superuser
python manage.py createsuperuser

7.Run Development Server
python manage.py runserver

8.Open in Browser
http://127.0.0.1:8000/

