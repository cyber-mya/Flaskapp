from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host="db",
            database="devops_db",
            user="devops_user",
            password="devops_pass"
        )
        return "Connected to PostgreSQL successfully!"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
