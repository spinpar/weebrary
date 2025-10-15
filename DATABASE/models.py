from django.db import models

class Anime(models.Model):
    mal_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    synopsis = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title

class Manga(models.Model):
    mal_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    synopsis = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title