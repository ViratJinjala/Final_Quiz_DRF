from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=100, unique=True, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.username

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='chapters')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject.name} - {self.name}"

class Quiz(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='quizzes')
    date_of_quiz = models.DateField(blank=True, null=True)
    time_duration = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

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

    def __str__(self):
        return f"Q: {self.question_statement[:50]}..."

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='scores')
    time_stamp = models.DateTimeField(blank=True, null=True)
    total_score = models.IntegerField(blank=True, null=True)
    correct_answers = models.IntegerField(blank=True, null=True)
    total_questions = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.quiz} - {self.total_score}"
