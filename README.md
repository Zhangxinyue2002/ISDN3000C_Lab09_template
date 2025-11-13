# Flask Guestbook Application - Lab 09

A simple yet comprehensive Flask-based guestbook web application with SQLite database integration, AJAX functionality, and Docker containerization with Nginx reverse proxy.

## 📋 Features

- ✍️ **User Guestbook**: Submit and view messages with names and timestamps
- 🎬 **Favorite Movies Display**: Shows a curated list of movies
- 🔄 **AJAX Form Submission**: Asynchronous message posting without page reload
- ✅ **Input Validation**: 140-character message limit
- 💾 **Persistent Storage**: SQLite database for message persistence
- 🐳 **Docker Support**: Full containerization with Docker Compose
- 🌐 **Nginx Reverse Proxy**: Production-ready setup with Nginx

## 🗂️ Project Structure

```
/FlaskApp/                    # Main project folder
├── app.py                    # Main Flask application
├── init_db.py               # Database initialization script
├── schema.sql               # Database schema definition
├── database.db              # SQLite database file
├── templates/
│   └── index.html           # Main HTML template with AJAX
├── nginx/
│   └── nginx.conf           # Nginx reverse proxy configuration
├── Dockerfile               # Docker image definition
├── docker-compose.yml       # Multi-container orchestration
├── requirements.txt         # Python dependencies
├── questions.md             # Lab questions and answers
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── FlaskVenv/              # Virtual environment (not submitted)
```

## 🚀 Getting Started

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
   source FlaskVenv/bin/activate  # On Windows: FlaskVenv\Scripts\activate
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

## 🐳 Docker Deployment

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

## 🔧 Configuration

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

## 📝 Development Notes

### Message Validation

- Messages are limited to 140 characters
- Both name and message fields are required
- Validation occurs on both traditional form submission and AJAX requests

### AJAX Implementation

The application uses the Fetch API for asynchronous form submission:
- Prevents default form behavior
- Sends JSON data to `/api/messages`
- Clears form fields on success
- Displays error messages on failure
- Reloads page to show new message

### Docker Architecture

**Development Container:**
- Single Flask container
- Direct port mapping (5000:5000)
- Volume mounting for database persistence

**Production Setup:**
- Flask application container
- Nginx reverse proxy container
- Internal Docker network communication
- Nginx handles port 80, proxies to Flask on port 5000
- Database volume persistence

## 🛡️ Security Considerations

- **SQL Injection Prevention**: Uses parameterized queries (`?` placeholders)
- **Input Validation**: Server-side validation for message length and required fields
- **CORS**: Not configured (add if needed for cross-origin requests)

## 🧪 Testing

### Manual Testing Checklist

- [ ] Submit message via form (traditional)
- [ ] Submit message via AJAX (JavaScript-enabled)
- [ ] Verify 140-character limit enforcement
- [ ] Check database persistence after restart
- [ ] Test health endpoint: `/health`
- [ ] Test about endpoint: `/about`
- [ ] Verify favorite movies display

### Docker Testing

- [ ] Container builds successfully
- [ ] Container runs and is accessible
- [ ] Database persists after container restart
- [ ] Docker Compose orchestrates both containers
- [ ] Nginx correctly proxies requests to Flask

## 📚 Learning Objectives Covered

1. ✅ Flask web framework basics
2. ✅ Jinja2 templating engine
3. ✅ SQLite database integration
4. ✅ AJAX and Fetch API
5. ✅ Docker containerization
6. ✅ Docker Compose multi-container setup
7. ✅ Nginx reverse proxy configuration
8. ✅ Virtual environment management
9. ✅ SQL injection prevention
10. ✅ RESTful API design

## 🤝 Contributing

This is a lab assignment project. For educational purposes only.

## 📄 License

This project is part of ISDN3000C coursework. All rights reserved.

## 👥 Authors

- **Student**: xzhangfr2002
- **Course**: ISDN3000C
- **Lab**: Lab 09 - Server and Web Application

## 🔗 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)

## 📞 Support

For questions or issues related to this lab assignment, please contact your course instructor or teaching assistant.

---

**Last Updated**: November 2025  
**Version**: 1.0
