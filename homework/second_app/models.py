from django.db import models

class Question(models.Model):

    question_text = models.CharField(max_length=100)
    pub_date = models.DateField('date published')

    def __str__(self):
        return f'Question {self.question_text} was added {self.pub_date}'

