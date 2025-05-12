from django.urls import path
from users.views import (
    UserRegistrationView, UserProfileView,
    SubjectListView, ChapterListBySubjectView, QuizListByChapterView, QuestionListByQuizView, UserScoreView,
    QuizAttemptView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-create'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),

    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('subjects/<int:subject_id>/chapters/', ChapterListBySubjectView.as_view(), name='chapter-list-by-subject'),
    path('chapters/<int:chapter_id>/quizzes/', QuizListByChapterView.as_view(), name='quiz-list-by-chapter'),
    path('quizzes/<int:quiz_id>/questions/', QuestionListByQuizView.as_view(), name='question-list-by-quiz'),
    path('score/<int:user_id>/scores/', UserScoreView.as_view(), name='scores-list-for-user'),
    path('quiz/attempt/', QuizAttemptView.as_view(), name='quiz-attempt'),
]
