from django.db import models

# Create your models here.
class Comment(models.Model):
    email = models.EmailField("Email")
    content = models.TextField("Content")
    created_at = models.DateTimeField("Created At", auto_now=True)
