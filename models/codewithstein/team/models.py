from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Team(models.Model):
    """
    User is a model that is built into Django.
    """
    name = models.CharField(max_length=225)
    users = models.ManyToManyField(User)


class Client(models.Model):
    team = models.ForeignKey(Team, verbose_name=(""), on_delete=models.CASCADE)
