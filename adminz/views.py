from rest_framework import generics
from users.models import User, Subject, Chapter, Quiz, Question
from users.serializers import UserSerializer, SubjectSerializer, ChapterSerializer, QuizSerializer, QuestionSerializer
from adminz.permissions import IsAdmin, AdminFullUserReadOnly


class UserView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a User instance.

    - GET: Retrieve a specific User by their ID.
    - PUT/PATCH: Update details of an existing User.
    - DELETE: Remove a User from the system.

    Only admin users are authorized to perform these operations.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class SubjectView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a Subject instance.

    - GET: Retrieve a specific Subject by its ID.
    - PUT/PATCH: Update the details of an existing Subject.
    - DELETE: Remove a Subject from the system.

    Admin users have full access to all operations.
    Regular users are limited to read-only access.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AdminFullUserReadOnly]


class SubjectCreate(generics.ListCreateAPIView):
    """
    API view to list all Subjects or create a new Subject.

    - GET: Returns a list of all Subject instances.
    - POST: Allows admin users to create a new Subject.

    Non-admin users have read-only access and cannot create new Subjects.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AdminFullUserReadOnly]


class ChapterView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a Chapter instance.

    - GET: Retrieve a Chapter instance by its ID.
    - PUT/PATCH: Update an existing Chapter instance.
    - DELETE: Delete an existing Chapter instance.

    This view allows full access (retrieve, update, delete) to admin users,
    while restricting non-admin users to read-only access.
    """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [AdminFullUserReadOnly]


class ChapterCreate(generics.ListCreateAPIView):
    """
    API view to list all Chapters or create a new Chapter.

    - GET: Returns a list of all Chapter instances.
    - POST: Allows admin users to create a new Chapter.

    Non-admin users have read-only access and cannot create new Chapters.
    """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [AdminFullUserReadOnly]


class QuizView(generics.RetrieveUpdateDestroyAPIView):
    """    
    API view to retrieve, update, or delete a Quiz instance.

    - GET: Retrieve a Quiz instance by its ID.
    - PUT/PATCH: Update an existing Quiz instance.
    - DELETE: Delete an existing Quiz instance.

    Admin users have full access to perform all operations.
    Non-admin users are restricted to read-only access.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AdminFullUserReadOnly]


class QuizCreate(generics.ListCreateAPIView):
    """    
    API view to list all Quizzes or create a new Quiz.

    - GET: Returns a list of all Quiz instances.
    - POST: Allows admin users to create a new Quiz.

    Non-admin users have read-only access and cannot create new Quizzes.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AdminFullUserReadOnly]


class QuestionView(generics.RetrieveUpdateDestroyAPIView):
    """    
    API view to retrieve, update, or delete a Question instance.

    - GET: Retrieve a Question instance by its ID.
    - PUT/PATCH: Update an existing Question instance.
    - DELETE: Delete an existing Question instance.

    Admin users have full access to perform all operations.
    Non-admin users are limited to read-only access.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AdminFullUserReadOnly]


class QuestionCreate(generics.ListCreateAPIView):
    """    
    API view to list all Questions or create a new Question.

    - GET: Returns a list of all Question instances.
    - POST: Allows admin users to create a new Question.

    Non-admin users have read-only access and are not permitted to create new Questions.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AdminFullUserReadOnly]