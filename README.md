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
    git clone https://github.com/shanks28/.git](https://github.com/shanks28/Assignment.git
    cd Assignment

    ```


2.  **Build and run using Docker**:

    ```
    docker-compose up --build

    ```


3.  **Access the application**:

    -   API Documentation: `http://localhost:8000/docs`

API Endpoints
-------------

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `register/` | Register a new user |
| POST | `login/` | Login user and get token |
| GET | `/issues/filter/<str:status>/<str:assignee_username>/` | Get issues by status and assignee |
| POST | `/create_ticket/` | Create a new issue |
| PUT | `/update_ticket/` | Update an issue |

### System Design
![image](https://github.com/user-attachments/assets/04e3a84e-0c08-452d-b4d6-3c4ea8f4936d)


License
-------

This project is licensed under the **MIT License**.

* * * * *

**Happy Coding!** 🚀
