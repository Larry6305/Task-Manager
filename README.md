# TaskManager Pro 🗂️

**TaskManager Pro** is a command-line interface (CLI) application built in Python for managing users, projects, and tasks. It's designed to help developers or small teams organize their work in a structured and efficient way.

---

## 🚀 Features

- User creation and management
- Project creation linked to users
- Task management with categories, due dates, and statuses
- Database powered by SQLAlchemy ORM
- CLI interface (to be implemented) for ease of use

---

## 🧱 Tech Stack

- Python 3.x
- SQLAlchemy (ORM)
- SQLite (local database)
- Pipenv (dependency management)


## 📁 Project Structure

taskmanager/
├── cli/ # CLI interface (coming soon)
│ └── main.py
├── models/ # ORM model definitions
│ ├── base.py
│ ├── user.py
│ ├── project.py
│ ├── task.py
│ └── category.py
├── database/
│ └── setup.py # DB setup and session
├── main.py # Entry point to initialize the DB
└── Pipfile # Pipenv environment and dependencies


## 🔧 Setup Instructions

### 1. Clone the repository

```bash
    git clone https://github.com/yourusername/taskmanager-pro.git
    cd taskmanager-pro

### 2. Install dependencies with Pipenv
bash
Copy
Edit
pipenv install
pipenv shell
If you don’t have pipenv, install it with pip install pipenv.

### 3. Initialize the database
bash
Copy
Edit
python main.py
You should see:

nginx
Copy
Edit
Database initialized.
A file called taskmanager.db will be created.

🧪 Future Enhancements
Full CLI interface using Click or Argparse

Task filtering and searching

Task reminders and email notifications

User authentication

📜 License
This project is open source and available under the MIT License.

🙌 Contributing
Pull requests and feedback are welcome! Please fork the repository and open a PR with your changes.

👤 Author
Larry [larry6305]