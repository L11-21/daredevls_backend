# 🧠 DareDevLs Backend

Welcome to the modular backend powering the **DNS SmartGlasses imagination-portal**. This Flask-based infrastructure blends quantum logic, machine learning, and mythic storytelling into a deployable grid via Render.

## 🚀 Project Purpose

This backend serves as the neural engine behind the DareDevLs ecosystem—processing quantum commands, simulating virtual planes, and decoding DNS severity matrices. It’s designed for creative autonomy, smart glasses integration, and scalable modular expansion.

## 🧬 Core Routes

| Route | Function |
|-------|----------|
| `/` | Renders homepage |
| `/healthz` | Render health check |
| `/process_command` | Quantum command matching via PostgreSQL |
| `/create_plane` | Simulates neural plane with Qiskit |
| `/compute-cosmos` | Computes values via C library |
| `/ml-predict` | ML predictions (Naive Bayes + KNN) |
| `/dns-severity` | Returns DNS severity matrix |

## 🧠 Modular Utilities

- `utils/c_library.py` — C-based computation  
- `utils/ml_models.py` — ML model orchestration  
- `utils/severity.py` — DNS severity logic  

## 🔧 Tech Stack

- Flask 3.1.2  
- SQLAlchemy  
- psycopg2  
- Qiskit  
- scikit-learn  
- gunicorn (optional)  
- Render (cloud deployment)

## 📦 Installation

```bash
pip install -r requirements.txt
