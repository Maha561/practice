from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('soap_ai.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    soaps = conn.execute('SELECT * FROM soaps').fetchall()
    conn.close()
    return render_template('product.html', soaps=soaps)

@app.route('/sort', methods=['GET'])
def sort_soaps():
    sort_by = request.args.get('type')  # 'reviews' or 'purchases'
    conn = get_db_connection()
    soaps = conn.execute(f'SELECT * FROM soaps ORDER BY {sort_by} DESC').fetchall()
    conn.close()
    return jsonify([dict(row) for row in soaps])

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/')
def index():
    return render_template('index.html')  
@app.route('/products')
def products():
    conn = get_db_connection()
    soaps = conn.execute('SELECT * FROM soaps').fetchall()
    conn.close()
    return render_template('product.html', soaps=soaps)