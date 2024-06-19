from django.db import models


class Movie(models.Model):
    imdb_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.year})"


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['imdb_id'], name='unique_movie')
        ]
    

class Actor(models.Model):
    imdb_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birth_year = models.IntegerField()
    death_year = models.IntegerField(null=True, blank=True, default=None)
    age = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.name} ({self.birth_year})"


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['imdb_id'], name='unique_actor')
        ]


class Role(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor_id = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.actor_id.name} as {self.role} in {self.movie_id.title} ({self.movie_id.year})"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['movie_id','actor_id'], name='unique_role')
        ]