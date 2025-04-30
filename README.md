# 📝 Todo App with FastAPI and Streamlit

This is a simple Todo application built with **FastAPI** as the backend and **Streamlit** as the frontend. It allows users to:

- ✅ Add todos  
- 📋 View all todos  
- ✔️ Mark todos as completed  
- 🗑️ Delete todos  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/paulabesst/todo-fastapi-streamlit.git
cd todo-fastapi-streamlit
```
### 2. Create Virtual Environment
```bash
python3 -m venv fastapi-env
source fastapi-env/bin/activate  # On Windows: fastapi-env\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run FastAPI Backend
```bash
uvicorn main:app --reload
```
- API base URL: http://127.0.0.1:8000
- API docs: http://127.0.0.1:8000/docs

### 5. Run Streamlit Frontend
```bash
streamlit run streamlit_app.py
```
- Streamlit app URL: http://localhost:8501


## 📌 Example API Endpoints

| Method | Endpoint           | Description         |
|--------|--------------------|---------------------|
| GET    | `/api/`            | Get all todos       |
| POST   | `/api/`            | Add a new todo      |
| PUT    | `/api/{id}`        | Update a todo       |
| DELETE | `/api/{id}`        | Delete a todo       |
