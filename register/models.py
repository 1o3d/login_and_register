from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PersonalQuestions(models.Model):
    choices = [
        (1, 'What is your mother\'s maiden name?'),
        (2, 'What was your first pet\'s name?'),
        (3, 'What city was your father born in?'),
    ]
    question = models.IntegerField(choices=choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=25)

    def __str__(self):
        return self.user.username


class Clipboard(models.Model):
    text1 = models.CharField(max_length=1000, null=True, blank=True)
    text2 = models.CharField(max_length=1000, null=True, blank=True)
    text3 = models.CharField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text1
