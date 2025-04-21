# Quiz Application

A Django REST API-based quiz application that allows users to take quizzes, track their scores, and administrators to manage quiz content.

## Features

- **User Authentication**: JWT-based authentication system
- **User Management**: Registration, profile management, and role-based permissions
- **Quiz Management**: Create and manage subjects, chapters, and quizzes
- **Quiz Taking**: Users can attempt quizzes and receive immediate feedback
- **Score Tracking**: Track and view user scores across different quizzes
- **Email Notifications**: Automated email notifications for user registration

## Technology Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: PostgreSQL
- **Task Queue**: Celery with Redis
- **Email**: SMTP (Gmail)

## Models

- **User**: Custom user model with email and username authentication
- **Subject**: Represents a subject area (e.g., Mathematics, Science)
- **Chapter**: Chapters within a subject
- **Quiz**: Quizzes associated with a chapter
- **Question**: Questions within a quiz with multiple-choice options
- **Score**: Tracks user performance on quizzes

## API Endpoints

### Authentication
- `POST /token/`: Obtain JWT access and refresh tokens
- `POST /token/refresh/`: Refresh an expired access token

### User Management
- `POST /register/`: Register a new user
- `GET/PUT /profile/`: View and update user profile

### Quiz Content
- `GET /subjects/`: List all subjects
- `GET /subjects/<subject_id>/chapters/`: List chapters by subject
- `GET /chapters/<chapter_id>/quizzes/`: List quizzes by chapter
- `GET /quizzes/<quiz_id>/questions/`: List questions by quiz

### Quiz Taking
- `POST /quiz/attempt/`: Submit quiz answers and get results
- `GET /score/<user_id>/scores/`: View user's quiz scores

## Setup and Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Quiz
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Start Celery worker (in a separate terminal):
   ```
   celery -A Quiz worker -l info
   ```

## Authentication

The application uses JWT (JSON Web Token) for authentication. To access protected endpoints:

1. Obtain a token by sending a POST request to `/token/` with your credentials:
   ```json
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

2. Include the token in subsequent requests:
   ```
   Authorization: Bearer your_access_token
   ```

## Quiz Taking Process

1. Browse available subjects, chapters, and quizzes
2. Select a quiz to attempt
3. Submit answers in the following format:
   ```json
   {
     "quiz_id": 1,
     "answers": [
       {
         "question_id": 1,
         "selected_option": "2"
       },
       {
         "question_id": 2,
         "selected_option": "4"
       }
     ]
   }
   ```
4. Receive immediate feedback with your score and which questions were correct/incorrect

## Permissions

- **Admin Users**: Full access to all endpoints
- **Regular Users**: Can take quizzes, view their scores, and access limited content


## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 