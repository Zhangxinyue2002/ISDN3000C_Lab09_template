# Flask Guestbook Application - Lab 09

A simple yet comprehensive Flask-based guestbook web application with SQLite database integration, AJAX functionality, and Docker containerization with Nginx reverse proxy.

## Fetures

- **User Guestbook**: Submit and view messages with names and timestamps
- **Favorite Movies Display**: Shows a curated list of movies
- **AJAX Form Submission**: Asynchronous message posting without page reload
- **Input Validation**: 140-character message limit
- **Persistent Storage**: SQLite database for message persistence
- **Docker Support**: Full containerization with Docker Compose
- **Nginx Reverse Proxy**: Production-ready setup with Nginx

## Project Structure

```
/FlaskApp/                    # Main project folder
├── app.py                    # Main Flask application
├── init_db.py               # Database initialization script
├── schema.sql               # Database schema definition
├── database.db              # SQLite database file
├── templates/
│  └── index.html           # Main HTML template with AJAX
├── nginx/
│  └── nginx.conf           # Nginx reverse proxy configuration
├── Dockerfile               # Docker image definition
├── docker-compose.yml       # Multi-container orchestration
├── requirements.txt         # Python dependencies
├── questions.md             # Lab questions and answers
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── FlaskVenv/              # Virtual environment (not submitted)
```

## Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Docker and Docker Compose (for containerized deployment)
- WSL (recommended for Windows users)

### Local Development Setup

1. **Navigate to the FlaskApp directory**
   ```bash
   cd FlaskApp
   ```

2. **Create and activate virtual environment**
   ```bash
   python3.11 -m venv FlaskVenv
   source FlaskVenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install Flask
   ```

4. **Initialize the database**
   ```bash
   python init_db.py
   ```

5. **Run the Flask development server**
   ```bash
   flask --app app run
   ```

6. **Access the application**
   Open your browser and navigate to: `http://127.0.0.1:5000`

### API Endpoints

- `GET /` - Main guestbook page
- `POST /` - Submit message via traditional form
- `POST /api/messages` - Submit message via AJAX (JSON)
- `GET /health` - Health check endpoint
- `GET /about` - About page

## Docker Deployment

### Basic Docker Setup

1. **Navigate to FlaskApp directory**
   ```bash
   cd FlaskApp
   ```

2. **Build Docker image**
   ```bash
   docker buildx build --tag flask_container_image .
   ```

3. **Run container with volume mounting** (for data persistence)
   ```bash
   docker run -d -p 5000:5000 \
     -v "$(pwd)/database.db:/app/database.db" \
     --name flask-container_instance \
     flask_container_image
   ```

4. **Access the application**
   Navigate to: `http://localhost:5000`

5. **Stop and remove container**
   ```bash
   docker stop flask-container_instance
   docker rm flask-container_instance
   ```

### Production Setup with Docker Compose (Nginx + Flask)

1. **Navigate to FlaskApp directory**
   ```bash
   cd FlaskApp
   ```

2. **Build and start all services**
   ```bash
   docker-compose up -d --build
   ```

3. **Check service status**
   ```bash
   docker-compose ps
   ```

4. **Access the application**
   Navigate to: `http://localhost` (port 80)

5. **View logs**
   ```bash
   docker-compose logs -f
   ```

6. **Stop all services**
   ```bash
   docker-compose down
   ```

7. **Remove images**
   ```bash
   docker rmi flask_container_image
   ```

## Configuration

### Database Schema

The application uses SQLite with the following schema:

```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### Environment Variables

No environment variables are required for basic operation. The application uses default Flask settings.

