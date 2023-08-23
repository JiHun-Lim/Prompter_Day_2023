from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    pass

class Answer(models.Model):
    answer_1 = models.CharField("Answer1", blank=True, null=True, max_length=200)
    answer_2 = models.CharField("Answer2", blank=True, null=True, max_length=200)
    answer_3 = models.CharField("Answer3", blank=True, null=True, max_length=200)
    answer_4 = models.CharField("Answer4", blank=True, null=True, max_length=200)
    answer_5 = models.CharField("Answer5", blank=True, null=True, max_length=200)
    answer_6 = models.CharField("Answer6", blank=True, null=True, max_length=200)
    answer_7 = models.CharField("Answer7", blank=True, null=True, max_length=200)
    answer_8 = models.CharField("Answer8", blank=True, null=True, max_length=200)
    answer_9 = models.CharField("Answer9", blank=True, null=True, max_length=200)
    answer_10 = models.CharField("Answer10", blank=True, null=True, max_length=200)
