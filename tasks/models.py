from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Collection(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tasks_edit', kwargs={'id': self.id})


class Task(models.Model):
    name = models.CharField(max_length=50)
    condition = models.TextField()
    answer = models.CharField(max_length=500)
    module = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.module.get_absolute_url()