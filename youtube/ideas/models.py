from django.db import models


class Idea(models.Model):
    title - models.CharField(max_length=255)
    description - models.TextField()
    youtube_url = models.URLField()

    class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    reason = models.TextField()

