Issue Management System
=======================

Overview
--------

This is an **Issue Management System** built using the **Zango framework** and **PostgreSQL**. The system allows users to **authenticate**, **create**, **assign**, and **update issues** while tracking their statuses. The application is fully **Dockerized** to ensure seamless deployment and scalability.

Features
--------

### 1\. User Authentication

-   Allows **user registration** and **login**.
-   Uses **Zango's built-in authentication system** for secure user management.

### 2\. Issue Management

-   Users can **create issues** with:
    -   **Title**
    -   **Description**
    -   **Status** (Open, In Progress, Resolved)
    -   **Assignee** (Assign issue to another user)
-   Users can **update the status** of an issue.
-   Issues include **timestamps** for creation and updates.

Technical Stack
---------------

-   **Framework**: [Zango](https://zango.dev/)
-   **Database**: PostgreSQL
-   **Containerization**: Docker
-   **API Endpoints**: RESTful API for all functionalities
-   **Validation & Error Handling**: Ensures robust request validation

Installation
------------

### Prerequisites

Ensure you have the following installed:

-   **Docker** & **Docker Compose**
-   **Python 3.x**
-   **PostgreSQL**

### Steps to Run

1.  **Clone the repository**:

    ```
    git clone https://github.com/yourusername/issue-management-system.git
    cd issue-management-system

    ```

2.  **Set up environment variables**: Create a `.env` file in the root directory and specify:

    ```
    DATABASE_URL=postgresql://user:password@db:5432/issue_db
    SECRET_KEY=your_secret_key

    ```

3.  **Build and run using Docker**:

    ```
    docker-compose up --build

    ```

4.  **Run database migrations**:

    ```
    docker-compose exec web zango migrate

    ```

5.  **Access the application**:

    -   API Documentation: `http://localhost:8000/docs`
    -   Admin Panel: `http://localhost:8000/admin`

API Endpoints
-------------

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/auth/register/` | Register a new user |
| POST | `/auth/login/` | Login user and get token |
| GET | `/issues/` | Retrieve all issues |
| POST | `/issues/` | Create a new issue |
| PUT | `/issues/{id}/` | Update an issue |
| DELETE | `/issues/{id}/` | Delete an issue |

Contributing
------------

1.  Fork the repository.
2.  Create a feature branch.
3.  Commit your changes.
4.  Push to your branch.
5.  Submit a pull request.

License
-------

This project is licensed under the **MIT License**.

* * * * *

**Happy Coding!** 🚀
