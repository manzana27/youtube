from django.db import models


class Idea(models.Model):
    title - models.CharField(max_length=255)
    description - models.TextField()


class Vote(models.Model):
    Idea = models.ForeignKey(Idea, on_delete=models.CASCADE)

