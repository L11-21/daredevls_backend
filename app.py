import os

import psycopg2
from flask import Flask, jsonify, render_template, request
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from sqlalchemy import create_engine

# 🔌 Import new modular utilities
from utils.c_library import use_clibrary
from utils.ml_models import run_ml_models
from utils.severity import get_dns_severity

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")  # 🔐 Secure session key

# 🗄️ SQLAlchemy Engines (for future modular queries)
engine_primary = create_engine(os.getenv("DATABASE_URL"))
engine_secondary = create_engine(os.getenv("IMAGINATION_DB_URL"))

# 🧠 psycopg2 Connection (legacy logic)
def connect_to_db():
    try:
        conn = psycopg2.connect(os.getenv("IMAGINATION_DB_URL"))
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def close_db_connection(conn):
    if conn:
        conn.close()

# 🌐 Home route
@app.route('/')
def index():
    return render_template('index.html')

# 🧠 Qiskit command processor
@app.route('/process_command', methods=['POST'])
def process_command():
    user_command = request.form.get('user_command')
    print(f"Received command: {user_command}")

    if user_command:
        db_connection = connect_to_db()
        if db_connection:
            cursor = db_connection.cursor()
            try:
                cursor.execute("""
                    SELECT database_item, similarity(%s, database_item)
                    FROM public.qiskit_implementations_profile
                    WHERE %s % database_item
                    ORDER BY similarity(%s, database_item) DESC
                    LIMIT 1;
                """, (user_command, user_command, user_command))

                if cursor.rowcount > 0:
                    result = cursor.fetchone()
                    similar_item = {"item": result[0], "similarity": result[1]}
                else:
                    similar_item = {"item": "No match found", "similarity": 0}

            except psycopg2.Error as e:
                print(f"Database error: {e}")
                similar_item = {"item": "Database error", "similarity": -1}
            except IndexError as e:
                print(f"IndexError: {e}")
                similar_item = {"item": "Query error", "similarity": -1}
            except Exception as e:
                print(f"Unexpected error: {e}")
                similar_item = {"item": "Unexpected error", "similarity": -1}
            finally:
                cursor.close()
                close_db_connection(db_connection)

            return jsonify({"command": user_command, "similar_item": similar_item})

    return jsonify({"error": "No command entered"})

# 🛫 Quantum plane simulator
@app.route('/create_plane', methods=['POST'])
def create_plane():
    plane_name = request.form.get('plane_name', 'Default Plane')
    plane_type = request.form.get('plane_type', 'Default Type')
    neural_response = simulate_neural_network_with_qiskit(plane_name, plane_type)
    return jsonify(neural_response)

def simulate_neural_network_with_qiskit(plane_name, plane_type):
    import random
    return {
        "activation_message": f"{plane_name} ({plane_type}) activated!",
        "qiskit_simulation": f"Quantum output: {random.choice(['00', '01', '10', '11'])}",
        "dynamic_content": "Trending topics in AI & Quantum Computing",
        "visualization": "<img src='https://i.imgur.com/qvodtvv.png' alt='Visualization'>",
        "instruction": "Enter commands to interact with the virtual grid..."
    }

# 🧮 Cosmos computation via C library
@app.route('/compute-cosmos', methods=['POST'])
def compute_cosmos():
    data = request.get_json()
    cosmos_value = int(data.get("value", 0))
    result = use_clibrary(cosmos_value)
    return jsonify({"result": result})

# 📊 ML predictions (Naive Bayes + KNN)
@app.route('/ml-predict', methods=['GET'])
def ml_predict():
    results = run_ml_models()
    return jsonify(results)

# 🔐 DNS severity matrix
@app.route('/dns-severity', methods=['GET'])
def dns_severity():
    severity_data = get_dns_severity()
    return jsonify(severity_data)

# 🚀 Launch app
if __name__ == '__main__':
    app.run(debug=True)
