# finance-tracker-api
A FastAPI-based backend application for managing financial transactions with CRUD operations, filtering, summaries, and role-based access control.


# 💰 Finance Tracker API

A backend application built using FastAPI to manage and analyze financial transactions. This project demonstrates clean API design, data handling, and role-based access control.

---

## 🚀 Features

- ✅ Financial Records CRUD (Create, Read, Update, Delete)
- ✅ Record Filtering (by type, category)
- ✅ Summary & Analytics (total income, expenses, balance)
- ✅ Role-Based Access Control (Viewer, Analyst, Admin)
- ✅ Input Validation & Error Handling
- ✅ SQLite Database Integration
- ✅ RESTful API Endpoints
- ✅ Interactive API Docs (Swagger UI)

---

## 🛠️ Tech Stack

- **Framework:** FastAPI  
- **Database:** SQLite  
- **ORM:** SQLAlchemy  
- **Validation:** Pydantic  

---

## 📂 Project Structure

finance-tracker-api/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
│
├── routes/
│ ├── transactions.py
│ ├── summary.py
│
├── utils/
│ ├── role_checker.py


---

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone https://github.com/your-username/finance-tracker-api.git

cd finance-tracker-api


### 2. Create virtual environment


python -m venv venv
source venv/bin/activate # Mac/Linux


### 3. Install dependencies
pip install fastapi uvicorn sqlalchemy


### 4. Run the application


uvicorn main:app --reload


---

## 🌐 API Documentation

After running the server, open:


http://127.0.0.1:8000/docs


Swagger UI allows you to test all endpoints interactively.

---

## 🔐 Role-Based Access

Roles are passed via request headers:


role: admin


### Roles:
- **Viewer:** Can view data
- **Analyst:** Can filter and analyze data
- **Admin:** Full access (CRUD operations)

---

## 📊 Example Endpoints

### Create Transaction

POST /transactions/

### Get Transactions

GET /transactions/


### Get Summary

GET /summary/totals

---

## ⚠️ Notes

- This project is designed for demonstration purposes.
- Authentication is simplified using header-based roles.
- Data is stored locally using SQLite.

---

## 🚀 Future Improvements

- Add JWT Authentication
- Pagination & Advanced Filtering
- Deployment (Render/AWS)
- Frontend integration

---

## 📜 License

This project is licensed under the MIT License.
