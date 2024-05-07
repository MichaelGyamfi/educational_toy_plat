from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)
    # Add fields related to the topic
    # Example:
    # description = models.TextField()

class Lesson(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Add fields for lesson details
    # Example:
    # duration = models.DurationField()
    # difficulty_level = models.CharField(max_length=20)

class Quiz(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    # Add fields for quiz
    # Example:
    # questions = models.ManyToManyField(Question)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    # Add fields for question options, correct answer, etc.
    # Example:
    # options = models.JSONField()
    # correct_answer = models.CharField(max_length=100)
