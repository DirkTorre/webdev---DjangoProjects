from django.contrib.auth.models import User
from django.db import models

from team.models import Team


class InfoTable(models.Model):
    created_at = models.DateField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Comment(InfoTable):
    """
    Because this tabe that can be used for general stuff,
    it's smart to not let it have many connections.
    """
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)


class Client(InfoTable):
    ACTIVE = 'active'
    CHOICES = {
        (ACTIVE, 'Active'),
        ('archived', 'Archived'),
    }

    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, choices=CHOICES, default=ACTIVE)
    # slug = models.SlugField()
    # image = models.ImageField(upload_to='media/articles')
    comment = models.ManyToManyField(Comment, blank=True)

    class Meta:
        ordering = ['-name']
        verbose_name = "Client - woop woop extra text"
        verbose_name_plural = "Clients - woop woop extra text"
    
    def __str__(self):
        return f'Client: {self.name}'
    
    def save(self, *args, **kwargs):
        if 'hello' in self.name:
            print("hello was in the name")
            self.name = self.name.replace('hello', 'hi')
        super(Client, self).save(*args, **kwargs)

    def number_of_comments(self):
        return self.comment.count()



class TodoList(InfoTable):
    client = models.ForeignKey(Client, related_name='todolist', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment = models.ManyToManyField(Comment, blank=True)
    created_by = models.ForeignKey(User, related_name='todolist', on_delete=models.CASCADE)
