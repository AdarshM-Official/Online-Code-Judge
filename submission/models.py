from django.db import models
from django.contrib.auth.models import User
from problem.models import Problem

class Submission(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Wrong Answer', 'Wrong Answer'),
        ('TLE', 'Time Limit Exceeded'),
        ('Error', 'Runtime Error'),
    ]

    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('cpp', 'C++'),
        ('java', 'Java'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="submissions"
    )

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="submissions"
    )

    code = models.TextField()

    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    execution_time = models.FloatField(null=True, blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.problem.title}"