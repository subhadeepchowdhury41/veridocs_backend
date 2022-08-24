from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.TextField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()
    createdBy = models.TextField(max_length=30)

    def __str__(self):
        return self.name