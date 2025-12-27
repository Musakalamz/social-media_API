# Social Media API

A robust and scalable RESTful API for a social media platform, built with Django and Django REST Framework. This API provides comprehensive features for user interaction, content management, and social networking.

## 🚀 Features

- **User Authentication**: Secure registration and login using Token-based authentication.
- **User Profiles**: Manage user profiles with bios and avatars.
- **Posts (CRUD)**: Create, read, update, and delete posts with support for text, images, videos, and audio.
- **Social Graph**: Follow and unfollow other users.
- **News Feed**: Personalized feed displaying posts from followed users.
- **Interactions**: Like and unlike posts.
- **Comments**: Comment on posts.
- **Search & Filtering**: Filter posts by username and search by content.
- **Pagination**: Efficient data retrieval with pagination support.
- **Documentation**: Interactive API documentation via Swagger and ReDoc.
- **Security**: Throttling and permission classes to protect resources.

## 🛠️ Tech Stack

- **Backend**: Python, Django, Django REST Framework
- **Database**: SQLite (Development) / PostgreSQL (Production ready)
- **Authentication**: Token Authentication (DRF)
- **Documentation**: drf-yasg (Swagger/OpenAPI)
- **Media**: Pillow (Image processing)

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.8+
- Git

### Steps

1.  **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/social-media-api.git
    cd social-media-api
    ```

2.  **Create and activate a virtual environment**

    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (Admin)**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server**

    ```bash
    python manage.py runserver
    ```

    The API will be available at `http://127.0.0.1:8000/`.

## 📖 API Documentation

The API includes interactive documentation. Once the server is running, visit:

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## 🔌 Key Endpoints

| Method    | Endpoint                  | Description                 |
| :-------- | :------------------------ | :-------------------------- |
| **Auth**  |                           |                             |
| `POST`    | `/api/register/`          | Register a new user         |
| `POST`    | `/api/login/`             | Login and obtain auth token |
| **Posts** |                           |                             |
| `GET`     | `/api/posts/`             | List all posts (paginated)  |
| `POST`    | `/api/posts/`             | Create a new post           |
| `GET`     | `/api/posts/feed/`        | Get feed of followed users  |
| `POST`    | `/api/posts/{id}/like/`   | Like a post                 |
| **Users** |                           |                             |
| `GET`     | `/api/users/`             | List users                  |
| `POST`    | `/api/users/{id}/follow/` | Follow a user               |
| `PUT`     | `/api/users/{id}/`        | Update profile (Bio/Avatar) |

## 🧪 Running Tests

To run the automated test suite:

```bash
python manage.py test
```

## 🔐 Authentication & Usage

- Register:
  ```powershell
  $b = @{ username = "john"; email = "john@example.com"; password = "securepassword" } | ConvertTo-Json
  Invoke-RestMethod -Method POST -Uri http://127.0.0.1:8000/api/register/ -ContentType "application/json" -Body $b
  ```
- Login:
  ```powershell
  $b = @{ username = "john"; password = "securepassword" } | ConvertTo-Json
  $res = Invoke-RestMethod -Method POST -Uri http://127.0.0.1:8000/api/login/ -ContentType "application/json" -Body $b
  $token = $res.token; $headers = @{ Authorization = "Token $token" }
  ```
- Create Post:
  ```powershell
  $post = @{ content = "Hello world" } | ConvertTo-Json
  Invoke-RestMethod -Method POST -Uri http://127.0.0.1:8000/api/posts/ -Headers $headers -ContentType "application/json" -Body $post
  ```
- Swagger: open `http://127.0.0.1:8000/swagger/`, click "Authorize", enter `Token <your_token>`, then try endpoints.

## 🚢 Deployment

### Render (recommended PaaS)

- Environment variables:
  - `DJANGO_SETTINGS_MODULE=config.settings`
  - `SECRET_KEY=<strong-secret>`
  - `ALLOWED_HOSTS=<your-service.onrender.com>,localhost`
  - `DATABASE_URL` (if using Render Postgres)
- Build command:
  ```bash
  pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
  ```
- Start command:
  ```bash
  gunicorn config.wsgi
  ```
- Notes: static files served via WhiteNoise; database auto-configured if `DATABASE_URL` is set.

### PythonAnywhere

- Create a web app, point WSGI to `config.wsgi`.
- In a virtualenv:
  ```bash
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py collectstatic --noinput
  ```
- Set `ALLOWED_HOSTS` to your PythonAnywhere domain.

## ⚙️ Configuration

- `ALLOWED_HOSTS` is read from env (defaults to `*` for dev).
- Static files: `STATIC_URL=/static/`, `STATIC_ROOT=staticfiles`, `WhiteNoise` enabled.
- DB: falls back to SQLite; if `DATABASE_URL` exists, uses Postgres via `dj_database_url`.

## 🔒 Security & Performance

- **Throttling**:
  - Anonymous users: 100 requests/day
  - Authenticated users: 1000 requests/day
- **Permissions**:
  - `IsAuthenticatedOrReadOnly`: Read for all, write for authenticated users.

## 📄 License

This project is licensed under the MIT License.
