# Capstone Project - Part 1: The Idea and Planning Phase

## 1. Project Idea
**Social Media API Platform**

I have decided to build a robust and scalable backend API for a social media application. This platform will serve as the foundation for a social networking site where users can register, share multimedia content (text, images, videos, audio), and interact with each other through a follow system, likes, and comments. The project focuses on creating a clean, RESTful API using Django and Django Rest Framework (DRF), adhering to industry best practices.

## 2. Main Features
The project will include the following core functionalities:

*   **User Authentication & Management:**
    *   User Registration and Login (Token-based authentication).
    *   Profile management (Avatar, Bio).
*   **Content Management:**
    *   Create, Read, Update, and Delete (CRUD) operations for Posts.
    *   Support for multiple media types: Images, Videos, and Audio files.
*   **Social Interactions:**
    *   **Comments:** Users can comment on posts.
    *   **Likes:** Users can like/unlike posts.
    *   **Follow System:** Users can follow/unfollow other users.
*   **Feeds:**
    *   Personalized news feed displaying posts from followed users.
*   **Documentation:**
    *   Comprehensive API documentation using Swagger/OpenAPI.

## 3. External API (Optional)
Currently, the project is self-contained and focuses on building a custom API.
*   *Future Consideration:* Integration with cloud storage APIs (e.g., Cloudinary or AWS S3) for efficient media file hosting.

## 4. Project Structure
The project follows a modular Django structure to ensure maintainability and separation of concerns.

*   **Root Directory:** Contains configuration files (`manage.py`, `.env`, `requirements.txt`).
*   **`config/`:** The main project configuration directory.
    *   `settings.py`: Global settings (database, apps, middleware).
    *   `urls.py`: Main URL routing entry point.
*   **`api/`:** The core application handling the social media logic.
    *   `models.py`: Defines the database schema and relationships.
    *   `views.py`: Contains the logic for API endpoints (ViewSets and APIViews).
    *   `serializers.py`: Handles data validation and conversion to JSON.
    *   `urls.py`: Defines API-specific routes.
    *   `admin.py`: Configuration for the Django Admin interface.

## 5. Database Schema (Models)
The database is designed using a relational model with the following key entities:

### **User (Django Built-in)**
*   Standard authentication fields (username, password, email).

### **Profile**
*   **Relationship:** One-to-One with `User`.
*   **Fields:** `bio` (Text), `avatar` (Image).

### **Post**
*   **Relationship:** ForeignKey to `User` (Author).
*   **Fields:** `content` (Text), `image` (Image), `video` (File), `audio` (File), `created_at` (DateTime), `updated_at` (DateTime).

### **Comment**
*   **Relationship:** ForeignKey to `User` (Author), ForeignKey to `Post`.
*   **Fields:** `content` (Text), `created_at` (DateTime).

### **Like**
*   **Relationship:** ForeignKey to `User`, ForeignKey to `Post`.
*   **Constraint:** Unique together (`user`, `post`) to prevent multiple likes.

### **Follow**
*   **Relationship:** ForeignKey to `User` (Follower), ForeignKey to `User` (Following).
*   **Constraint:** Unique together (`follower`, `following`).

## 6. API Endpoints Plan
The API will expose the following RESTful endpoints:

*   **Auth:**
    *   `POST /api/register/` - Register a new user.
    *   `POST /api/login/` - Authenticate and retrieve a token.
*   **Users:**
    *   `GET /api/users/` - List users.
    *   `GET /api/users/{id}/` - Retrieve user profile.
    *   `POST /api/users/{id}/follow/` - Follow a user.
    *   `POST /api/users/{id}/unfollow/` - Unfollow a user.
*   **Posts:**
    *   `GET /api/posts/` - List all posts.
    *   `POST /api/posts/` - Create a new post.
    *   `GET /api/posts/feed/` - Get posts from followed users.
    *   `GET /api/posts/{id}/` - Retrieve a specific post.
    *   `POST /api/posts/{id}/like/` - Like a post.
    *   `POST /api/posts/{id}/unlike/` - Unlike a post.
*   **Comments:**
    *   `GET /api/comments/` - List comments.
    *   `POST /api/comments/` - Add a comment to a post.

## 7. Timeline (5 Weeks)

*   **Week 1: Foundation & Core Models**
    *   Set up Django project and Git repository.
    *   Configure database and environment variables.
    *   Implement basic `Post` and `Comment` models.
    *   Create initial Views and Serializers for Posts.

*   **Week 2: Authentication & Profiles**
    *   Implement User Registration and Login endpoints.
    *   Create `Profile` model and signals for auto-creation.
    *   Integrate Token Authentication (DRF Auth Token).
    *   Set up User permissions.

*   **Week 3: Advanced Features & Media**
    *   Implement file upload handling for Images, Videos, and Audio.
    *   Refine `PostSerializer` to handle media files.
    *   Implement `Follow` model and relationships.

*   **Week 4: Social Logic & Feeds**
    *   Implement `Like` functionality with unique constraints.
    *   Build the `feed` endpoint to filter posts by followed users.
    *   Add Follow/Unfollow endpoints.
    *   Implement filtering and search capabilities (e.g., search users by username).

*   **Week 5: Polish, Test & Document**
    *   Write unit tests for critical paths (Auth, Posts, Follows).
    *   Generate and refine API documentation (Swagger/Redoc).
    *   Perform final code cleanup and optimization.
    *   Prepare project for submission/deployment.
