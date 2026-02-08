# Demo Video Script & Guide

**Objective:** A 5-minute professional walkthrough of the Social Media API.

---

## Part 1: Introduction (0:00 - 0:45)
**Visual:** Slide Deck (Title Slide) or IDE with Project Structure.
**Script:**
"Hi, I'm [Your Name], and this is my Capstone Project: a backend API for a Social Media Platform. The goal was to build a scalable and secure RESTful API that handles user authentication, content management, and social interactions like following and liking. I built this using Python, Django, and the Django REST Framework."

## Part 2: Architecture & Data Model (0:45 - 1:30)
**Visual:** Show the ERD Diagram or `models.py` file.
**Script:**
"Before we dive into the code, let's look at the data structure. I designed a relational database schema centered around the User.
*   We have a **Profile** model linked One-to-One with the User for bio and avatar details.
*   **Posts** are the core content unit, supporting text and media.
*   **Comments** and **Likes** are related to both Users and Posts.
*   Crucially, I implemented a self-referential **Follow** system, allowing users to build their social graph. This structure ensures data integrity and efficient querying."

## Part 3: Live Demo - Authentication (1:30 - 2:15)
**Visual:** Postman / Swagger UI.
**Action:** Demonstrate Register and Login.
**Script:**
"Let's see the API in action using Postman.
First, security is paramount. I'm using Token-based authentication.
*   Here, I'm registering a new user 'JohnDoe'. [Send Request] -> We get a 201 Created response.
*   Now, I'll log in to get my authentication token. [Send Request] -> This token is required for all secure endpoints, ensuring only authorized users can modify data."

## Part 4: Core Features - Posts & Feed (2:15 - 3:30)
**Visual:** Postman.
**Action:** Create a Post, View Feed.
**Script:**
"With our token, let's create some content.
*   I'll send a POST request to `/api/posts/` with some content and an image. [Send Request]. The API validates the input and saves the file.
*   One of the most complex features is the **News Feed**. If I hit `/api/posts/feed/`, the backend filters the database to show *only* posts from users I follow, ordered chronologically. This personalized experience is key for any social platform."

## Part 5: Social Interactions (3:30 - 4:15)
**Visual:** Postman.
**Action:** Follow a user, Like a post.
**Script:**
"Interaction drives engagement.
*   I can follow another user by hitting this endpoint. [Send Request].
*   I can also 'like' a post. The backend ensures I can't like the same post twice thanks to unique constraints in the database model. If I try again, the API returns a clear error message, handling edge cases gracefully."

## Part 6: Best Practices & Conclusion (4:15 - 5:00)
**Visual:** Codebase (`views.py` or `serializers.py`) or Summary Slide.
**Script:**
"Throughout development, I adhered to industry best practices:
1.  **REST Principles:** Using proper HTTP verbs (GET, POST, DELETE) and status codes.
2.  **Clean Architecture:** Separating logic into Models, Serializers, and ViewSets for maintainability.
3.  **Validation:** Extensive error handling to ensure bad data never reaches the database.

Thank you for watching. This project represents a solid foundation for a social networking backend, ready for frontend integration."
