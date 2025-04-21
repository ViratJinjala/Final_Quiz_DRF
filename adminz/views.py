from rest_framework import generics
from users.models import User, Subject, Chapter, Quiz, Question
from users.serializers import UserSerializer, SubjectSerializer, ChapterSerializer, QuizSerializer, QuestionSerializer
from Quiz.permissions import IsAdmin, AdminFullUserReadOnly


# User Read, Update, Delete
class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


# Subject Read, Update, Delete
class SubjectView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AdminFullUserReadOnly]

# Subject Create
class SubjectCreate(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AdminFullUserReadOnly]



# Chapter Read, Update, Delete
class ChapterView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [AdminFullUserReadOnly]

# Chapter Create
class ChapterCreate(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [AdminFullUserReadOnly]



# Quiz Read, Update, Delete
class QuizView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AdminFullUserReadOnly]

# Quiz Create
class QuizCreate(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AdminFullUserReadOnly]



# Question Read, Update, Delete
class QuestionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AdminFullUserReadOnly]

# Question Create
class QuestionCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AdminFullUserReadOnly]