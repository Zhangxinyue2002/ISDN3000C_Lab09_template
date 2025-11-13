# Lab 09 - Questions and Answers

## Part 2: Build a Flask Server App

### Question 1
**What is the purpose of the `@app.route('/health')` decorator in the code?**

The `@app.route('/health')` decorator maps the URL path `/health` to the `health_check()` function. When a user or monitoring system visits `http://127.0.0.1:5000/health`, Flask will execute the `health_check()` function and return "Server is running!" with a 200 status code. This endpoint is commonly used for health monitoring and to verify that the server is operational.

---

### Question 2
**In Jinja2, what is the difference between `{{ my_variable }}` and `{% for item in my_list %}`?**

- `{{ my_variable }}` is used to **output/print** the value of a variable or expression directly into the HTML. It evaluates the expression and displays the result.

- `{% for item in my_list %}` is a **control flow statement** used for logic operations like loops, conditionals, and blocks. It does not directly output content but controls the structure and flow of the template. The `{% %}` syntax is used for statements like `for`, `if`, `endif`, `endfor`, etc.

---

### Question 3
**In `app.py`, why is it important to use `(?, ?)` and pass the variables as a tuple in the `conn.execute()` command instead of using f-strings to put the variables directly into the SQL string? What is this technique called?**

Using `(?, ?)` with parameters passed as a tuple is called **parameterized queries** or **prepared statements**. This technique is critical for preventing **SQL injection attacks**. 

If we used f-strings like `f"INSERT INTO messages (name, message) VALUES ('{name}', '{message}')"`, a malicious user could input SQL code (e.g., `'; DROP TABLE messages; --`) that would be executed directly against the database, potentially destroying data or compromising security. Parameterized queries ensure that user input is treated as data, not executable code, by properly escaping special characters.

---

### Question 4
**What is the purpose of `event.preventDefault()` in the JavaScript code? What would happen if you removed that line?**

`event.preventDefault()` prevents the browser's default form submission behavior, which would normally cause a full page reload and send the form data via a traditional HTTP POST request.

If you removed `event.preventDefault()`, the form would submit normally (reloading the page) AND the JavaScript fetch request would also execute, resulting in duplicate submissions to the server. The AJAX functionality would be broken because the page would reload before the JavaScript could handle the response properly.

---

## Part 3: Docker Container

### Question 5
**In the `Dockerfile`, why is the `CMD` `["flask", "run", "--host=0.0.0.0"]` necessary? Why wouldn't the default `flask run` (which uses host 127.0.0.1) work?**

By default, Flask binds to `127.0.0.1` (localhost), which only accepts connections from within the same machine/container. When running in a Docker container, we need external access from the host machine.

Using `--host=0.0.0.0` tells Flask to listen on all network interfaces, making the application accessible from outside the container. Without this flag, requests from your host machine's browser would not be able to reach the Flask app running inside the container, even with port mapping (`-p 5000:5000`).

---

### Coding 5 - Docker Volume Command
**Modified `docker run` command with volume mounting:**

```bash
docker run -d -p 5000:5000 -v "$(pwd)/database.db:/app/database.db" --name flask-container_instance flask_container_image
```

For Windows PowerShell:
```powershell
docker run -d -p 5000:5000 -v "${PWD}/database.db:/app/database.db" --name flask-container_instance flask_container_image
```

This mounts the local `database.db` file into the container at `/app/database.db`, ensuring data persists even when the container is removed and recreated.

---

## Part 4: Production Setup with Nginx & Docker Compose

### Question 6
**In the `docker-compose.yml` setup, Nginx is configured to `proxy_pass http://flask-app:5000`. How does the Nginx container know the IP address of the `flask-app` container?**

Docker Compose automatically creates a **custom bridge network** for all services defined in the `docker-compose.yml` file. Within this network, Docker provides built-in **DNS resolution** that maps service names to their container IP addresses.

When Nginx needs to connect to `http://flask-app:5000`, Docker's internal DNS server resolves the hostname `flask-app` to the actual IP address of the Flask container. This eliminates the need to manually configure IP addresses and makes the setup portable and maintainable. The service name becomes the hostname within the Docker network.

---

### Challenge Task (Optional)
**Improved `nginx.conf` with static file serving:**

```nginx
server {
    listen 80;

    # Serve static files directly from Nginx
    location /static/ {
        alias /app/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Pass all other requests to Flask
    location / {
        proxy_pass http://flask-app:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

**Corresponding `docker-compose.yml` volume addition for nginx service:**
```yaml
nginx:
  image: nginx:latest
  container_name: nginx_c
  ports:
    - "80:80"
  volumes:
    - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf
    - ./FlaskApp/static:/app/static  # Mount static files directory
  depends_on:
    - flask-app
```

This configuration allows Nginx to serve CSS, JavaScript, images, and other static files directly without involving the Flask application, improving performance and reducing load on the application server.
