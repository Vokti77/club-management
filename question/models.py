from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class QuestionPaper(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='questions/')
    pdf_file = models.FileField(upload_to='question_papers/')

    def __str__(self):
        return self.title

class Solution(models.Model):
    question_paper = models.ForeignKey(QuestionPaper, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='solutions/')