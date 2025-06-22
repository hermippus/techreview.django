from django.db import models
from django.urls import reverse

class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=4096)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('review', args=[self.id])