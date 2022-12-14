import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=50)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        #CUSTOM COMPLEX METHOD. STUDY THIS
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <=now

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=10)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text


