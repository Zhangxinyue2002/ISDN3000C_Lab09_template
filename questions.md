# Lab 09 - Questions and Answers

## Part 2: Build a Flask Server App

### Question 1
**What is the purpose of the `@app.route('/health')` decorator in the code?**

The `@app.route('/health')` part basically tells Flask "when someone goes to /health, run this function". So when you open `http://127.0.0.1:5000/health`, it shows "Server is running" to let you know everything's working. 

---

### Question 2
**In Jinja2, what is the difference between `{{ my_variable }}` and `{% for item in my_list %}`?**

- `{{ my_variable }}` - This one prints out whatever is in the variable right onto the page. Like if my_variable is "Hello", it'll show "Hello" in the HTML.

- `{% for item in my_list %}` - This is for doing loops and if statements. You need to close it with `{% endfor %}` too.

---

### Question 3
**In `app.py`, why is it important to use `(?, ?)` and pass the variables as a tuple in the `conn.execute()` command instead of using f-strings to put the variables directly into the SQL string? What is this technique called?**

If I just put the variables directly into the SQL string like `f"INSERT INTO messages (name, message) VALUES ('{name}', '{message}')"`, someone could type in weird SQL code and mess up the database. 

Using the `?` placeholders and passing values separately keeps the user input safe because it treats everything as just text data, not code that could run.

---

### Question 4
**What is the purpose of `event.preventDefault()` in the JavaScript code? What would happen if you removed that line?**

`event.preventDefault()` stops the form from doing its normal thing, which is refreshing the whole page when you click submit. If I removed it, the page would reload and my JavaScript code would also try to send the message at the same time. So the message would get sent twice, and the page would refresh so fast that my JavaScript wouldn't even get a chance to show if it worked or not. 

---

## Part 3: Docker Container

### Question 5
**In the `Dockerfile`, why is the `CMD` `["flask", "run", "--host=0.0.0.0"]` necessary? Why wouldn't the default `flask run` (which uses host 127.0.0.1) work?**

Flask only listens to connections from inside the same computer (127.0.0.1 means localhost). But when it's running in a Docker container, that's like its own little computer, and I'm trying to access it from outside the container.

The `--host=0.0.0.0` tells Flask to listen on ALL network connections, not just localhost. Without this, even though I mapped the port with `-p 5000:5000`, my browser still can't reach Flask inside the container because it's only listening internally.

---

## Part 4: Production Setup with Nginx & Docker Compose

### Question 6
**In the `docker-compose.yml` setup, Nginx is confugured to `proxy_pass http://flask-app:5000`. How does the Nginx container know the IP address of the `flask-app` container?**

Docker Compose automatically creates a network for all the containers and gives them their own internal DNS system. 

So when I use `flask-app` as the hostname, Docker's DNS finds which container and what its IP address is. Like how website names turn into IP addresses, but it happens automatically inside Docker. This is easier than figuring out IP addresses manually, especially since container IPs can change.

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

This lets Nginx handle the CSS, JavaScript, and image files directly without bothering Flask, which makes everything faster.
