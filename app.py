import sqlite3
# Add request, url_for, redirect, and jsonify to imports
from flask import Flask, render_template, request, url_for, redirect, jsonify

# Create an instance of the Flask class
app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row # This allows us to access columns by name
    return conn


@app.route('/', methods=('GET', 'POST'))

def index():

    conn = get_db_connection()

    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        
        # Basic validation and check message length (Coding 3)
        if name and message and len(message) <= 140:
            conn.execute('INSERT INTO messages (name, message) VALUES (?, ?)',
                         (name, message))
            conn.commit()
            conn.close()
            return redirect(url_for('index')) # Redirect to prevent form resubmission
        else:
            # If validation fails, just redirect without adding
            conn.close()
            return redirect(url_for('index'))

    # This code runs for a GET request
    messages = conn.execute('SELECT * FROM messages ORDER BY created_at DESC').fetchall()
    conn.close()
    
    # Create a list of favorite movies
    favorite_movies = ["Doraemon", "Boonie bears", "Kimetsu no Yaiba"]
    
    # Pass variables to the template
    return render_template(
        'index.html',
        page_title='Guestbook Home', 
        messages=messages,
        movies=favorite_movies  # Pass the list of movies
    )

# A simple health check route
@app.route('/api/messages', methods=['POST'])
def add_message_api():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')

    if not name or not message:
        return jsonify({'status': 'error', 'message': 'Name and message are required.'}), 400
    
    if len(message) > 140:
        return jsonify({'status': 'error', 'message': 'Message must be 140 characters or less.'}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO messages (name, message) VALUES (?, ?)',
                 (name, message))
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success', 'message': 'Message added!'})

@app.route('/health')
def health_check():
    return 'Server is running!', 200

@app.route('/about')
def about():
    return 'This is a simple Flask guestbook application.'
