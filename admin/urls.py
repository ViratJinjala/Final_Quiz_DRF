from django.urls import path
from .views import UserView, SubjectView,  SubjectCreate, ChapterView, ChapterCreate, QuizView, QuizCreate, QuestionView, QuestionCreate

urlpatterns = [
    path('subjects/<int:pk>/', SubjectView.as_view(), name='subject'),
    path('chapters/<int:pk>/', ChapterView.as_view(), name='chapter'),
    path('quizzes/<int:pk>/', QuizView.as_view(), name='quiz'),
    path('questions/<int:pk>/', QuestionView.as_view(), name='question'),
    path('questions/<int:pk>/', UserView.as_view(), name='user'),

    path('subjects/create/', SubjectCreate.as_view(), name='subject-create'),
    path('chapters/create/', ChapterCreate.as_view(), name='chapter-create'),
    path('quizzes/create/', QuizCreate.as_view(), name='quiz-create'),
    path('questions/create/', QuestionCreate.as_view(), name='question-create'),
]
