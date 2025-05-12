from rest_framework import serializers
from users.models import User, Subject, Chapter, Quiz, Question, QuizResult

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'qualification', 'dob']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            qualification=validated_data.get('qualification'),
            dob=validated_data.get('dob')
        )
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)

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
        fields = ['id', 'quiz', 'question_statement', 'option1', 'option2', 'option3', 'option4', 'weightage']

class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResult
        fields = ['id', 'user', 'quiz', 'time_stamp', 'total_score', 'correct_answers', 'total_questions']

class QuizAttemptSerializer(serializers.Serializer):
    quiz_id = serializers.IntegerField()
    answers = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )

class QuizResultSerializer(serializers.Serializer):
    quiz_id = serializers.IntegerField()
    total_questions = serializers.IntegerField()
    correct_answers = serializers.IntegerField()
    total_score = serializers.IntegerField()
    question_results = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )