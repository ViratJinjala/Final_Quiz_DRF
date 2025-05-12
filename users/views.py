from rest_framework import generics, permissions, status
from rest_framework.response import Response
from users.models import User, Subject, Chapter, Quiz, Question, Score
from users.serializers import UserSerializer, SubjectSerializer, ChapterSerializer, QuizSerializer, QuestionSerializer, ScoreSerializer, QuizAttemptSerializer, QuizResultSerializer
from users.tasks import send_email_task
from adminz.permissions import IsAdmin, IsUser
from django.template.loader import render_to_string
from django.utils import timezone
from django.db import transaction


class UserRegistrationView(generics.CreateAPIView):
    """
    API view to handle user registration.

    - POST: Creates a new user account with the provided registration data.
      On successful registration, sends a welcome email asynchronously using Celery.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Send email to registered user via celery
        email = [serializer.validated_data.get('email')]
        subject="Welcome to Quiz app"
        message="It's pleasure seeing you here."
        username = [serializer.validated_data.get('username')][0]
        data_username = {
            'username': username
        }
        html_message = render_to_string('email_template.html', data_username)

        # Celery called here
        send_email_task.delay(email,subject,message,html_message)
        return Response(serializer.data)


class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    API view to retrieve or update a user's profile.

    - GET: Retrieve the profile of the currently authenticated user.
    - PUT/PATCH: Update the profile of the currently authenticated user.
    """
    serializer_class = UserSerializer
    permission_classes = [IsUser,IsAdmin]

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        serializer.save()


class UserScoreView(generics.ListAPIView):
    """
    API view to list all scores associated with a specific user.

    - GET: Retrieves all scores for a particular user, identified by their user ID.
    """
    serializer_class = ScoreSerializer
    permission_classes = [IsUser,IsAdmin]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Score.objects.filter(user_id=user_id)


class SubjectListView(generics.ListAPIView):
    """
    API view to list all subjects.

    - GET: Retrieves a list of all subjects in the system.
    """
    
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdmin,IsUser]


class ChapterListBySubjectView(generics.ListAPIView):
    """
    API view to list all chapters associated with a specific subject.

    - GET: Retrieves all chapters associated with a given subject, identified by the subject ID.
    """
    serializer_class = ChapterSerializer
    permission_classes = [IsAdmin,IsUser]

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return Chapter.objects.filter(subject_id=subject_id)


class QuizListByChapterView(generics.ListAPIView):
    """
    API view to list all quizzes associated with a specific chapter.

    - GET: Retrieves all quizzes associated with a given chapter, identified by the chapter ID.
    """
    serializer_class = QuizSerializer
    permission_classes = [IsAdmin,IsUser]

    def get_queryset(self):
        chapter_id = self.kwargs['chapter_id']
        return Quiz.objects.filter(chapter_id=chapter_id)


class QuestionListByQuizView(generics.ListAPIView):
    """
    API view to list all questions associated with a specific quiz.

    - GET: Retrieves all questions associated with a given quiz, identified by the quiz ID.
    """
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        return Question.objects.filter(quiz_id=quiz_id)

class QuizAttemptView(generics.CreateAPIView):
    """    
    API view to handle the submission of a quiz attempt.

    - POST: Submits a user's answers for a quiz and calculates the score based on the provided answers.
      The result includes the total score, number of correct answers, and individual question results.
    """
    serializer_class = QuizAttemptSerializer
    permission_classes = [permissions.AllowAny]
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        quiz_id = serializer.validated_data['quiz_id']
        answers = serializer.validated_data['answers']
        quiz = Quiz.objects.get(id=quiz_id)
        questions = Question.objects.filter(quiz=quiz)
        
        correct_answers = 0
        total_score = 0
        question_results = []
        
        for question in questions:
            answer = next((a for a in answers if int(a.get('question_id')) == question.id), None)
            
            if not answer:
                continue
                
            selected_option = answer.get('selected_option')
            is_correct = int(selected_option) == question.correct_option
            
            if is_correct:
                correct_answers += 1
                total_score += question.weightage or 1
            
            question_results.append({
                'question_id': question.id,
                'question': question.question_statement,
                'selected_option': selected_option,
                'correct_option': question.correct_option,
                'is_correct': is_correct
            })
    
        score = Score.objects.create(
            user=request.user,
            quiz=quiz,
            time_stamp=timezone.now(),
            total_score=total_score,
            correct_answers=correct_answers,
            total_questions=len(questions)
        )
        
        result_data = {
            'quiz_id': quiz_id,
            'total_questions': len(questions),
            'correct_answers': correct_answers,
            'total_score': total_score,
            'question_results': question_results
        }
        
        result_serializer = QuizResultSerializer(data=result_data)
        result_serializer.is_valid(raise_exception=True)
        
        return Response(result_serializer.data, status=status.HTTP_201_CREATED)


