# 🎓 Course Enrollment System

A backend-powered Course Enrollment System built with Python and FastAPI that allows students to register, enroll in courses, and manage academic records efficiently.

---

## 🚀 Features

- Student Registration & Authentication
- Course Management
- Student Course Enrollment
- Department & Instructor Management
- RESTful API Architecture
- Database Migrations with Alembic
- Modular Project Structure
- Interactive API Documentation
- Environment Variable Configuration

---

## 🛠 Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Uvicorn
- Pydantic

---

## 📁 Project Structure

```bash
course-enrollment-system/
│
├── app/
│   ├── main.py
│   │
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── database/
│   └── config/
│
├── alembic/
├── alembic.ini
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/course-enrollment-system.git
```

```bash
cd course-enrollment-system
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 Database Configuration

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/course_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# 🔄 Alembic Migration Setup

## Initialize Alembic

```bash
alembic init alembic
```

## Generate Migration

```bash
alembic revision --autogenerate -m "Initial migration"
```

## Apply Migration

```bash
alembic upgrade head
```

## Rollback Migration

```bash
alembic downgrade -1
```

---

# ▶️ Running the Application

Start the development server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

Application runs at:

```bash
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

```bash
http://127.0.0.1:8000/docs
```

## ReDoc

```bash
http://127.0.0.1:8000/redoc
```

---

# 📌 Example API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/students/register` | Register a student |
| POST | `/students/login` | Authenticate student |
| GET | `/courses` | Retrieve all courses |
| POST | `/courses` | Create a new course |
| POST | `/enrollments` | Enroll a student in a course |

---

# 🧪 Running Tests

```bash
pytest
```

---

# 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| DATABASE_URL | PostgreSQL database connection URL |
| SECRET_KEY | JWT secret key |
| ALGORITHM | Authentication algorithm |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token expiration time |

---

# 📦 Requirements

Example dependencies:

```txt
fastapi
uvicorn
sqlalchemy
psycopg2-binary
alembic
python-dotenv
pydantic
passlib
python-jose
```

---

# 🚧 Future Improvements

- Role-Based Access Control
- Email Verification
- Docker Support
- CI/CD Pipeline
- Frontend Integration
- Payment System
- Course Prerequisite Validation

---

# 🤝 Contributing

Contributions are welcome.

## Steps

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Ataur-rahman Abdullahi

GitHub: https://github.com/AbdullahiAtaurrahman

---

# ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
