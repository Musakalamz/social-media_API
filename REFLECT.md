# Capstone Project Reflection - Part 1 & 2

## 1. What I Have Accomplished So Far
I have successfully laid the foundation for the Social Media API project.
*   **Project Planning:** Defined the core idea, features, and timeline in `GOOGLE.md`.
*   **Database Design:** Created a comprehensive Entity Relationship Diagram (ERD) in `DIAGRAM.md`, outlining the relationships between Users, Profiles, Posts, Comments, Likes, and Follows.
*   **API Architecture:** Defined the RESTful API endpoints and their HTTP methods.
*   **Documentation:** Prepared a presentation deck outline (`PRE.md`) and a demo video script (`VID.md`) to effectively communicate the project's value and technical details.
*   **Initial Setup:** Configured the Django project structure, installed dependencies, and set up the Git repository.

## 2. Challenges Faced and How I Handled Them
*   **Database Modeling:**
    *   *Challenge:* Designing the "Follow" system was tricky, specifically deciding between a separate model or a Many-to-Many field on the User model.
    *   *Solution:* I opted for a dedicated `Follow` model (linking `follower` and `following` users). This allows for storing additional metadata (like `created_at`) and makes querying "followers" vs "following" more explicit and scalable.
*   **Scope Management:**
    *   *Challenge:* I initially wanted to include real-time chat and notifications, which risked overcomplicating the MVP.
    *   *Solution:* I prioritized core social features (CRUD posts, feed, likes/comments) for the first iteration, moving advanced features to the "Future Roadmap".
*   **Tooling:**
    *   *Challenge:* Ensuring the ERD was clear and followed standard conventions.
    *   *Solution:* Used Mermaid.js syntax within Markdown to create a version-controllable and easily editable diagram directly in the codebase.

## 3. What’s Next? (Plan for the Upcoming Week)
My focus for the next week shifts from planning to active development (coding):
*   **Environment Setup:** Finalize the virtual environment and install all necessary Django/DRF packages.
*   **Model Implementation:** Translate the ERD into actual Django Models (`api/models.py`).
*   **Database Migration:** Run initial migrations to create the database schema.
*   **Basic Views & Serializers:** Implement the first set of API views for User Registration and Post creation to test the end-to-end flow.
*   **Testing:** Verify the initial endpoints using Postman/Swagger.
