from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from users.managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=100, unique=True, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.username
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','password']

    objects = UserManager()

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_subject')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_subject')

    def __str__(self):
        return self.name

class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='chapters')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_chapter')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_chapter')

    def __str__(self):
        return f"{self.subject.name} - {self.name}"

class Quiz(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='quizzes')
    date_of_quiz = models.DateField(blank=True, null=True)
    time_duration = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_quizzes')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_quizzes')

    def __str__(self):
        return f"Quiz for {self.chapter.name} on {self.date_of_quiz}"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_statement = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.PositiveSmallIntegerField()
    weightage = models.IntegerField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_question')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_question')

    def __str__(self):
        return f"Q: {self.question_statement[:50]}..."

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='scores')
    time_stamp = models.DateTimeField(auto_now_add=True)
    total_score = models.IntegerField(blank=True, null=True)
    correct_answers = models.IntegerField(blank=True, null=True)
    total_questions = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.quiz} - {self.total_score}"
