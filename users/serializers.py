from rest_framework import serializers
from .models import User, Subject, Chapter, Quiz, Question, Score

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'qualification', 'dob']
        extra_kwargs = {'password': {'write_only': True}}

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'description']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'subject', 'name', 'description']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'chapter', 'date_of_quiz', 'time_duration', 'remarks']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'question_statement', 'option1', 'option2', 'option3', 'option4', 'correct_option', 'weightage']

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'user', 'quiz', 'time_stamp', 'total_score', 'correct_answers', 'total_questions']