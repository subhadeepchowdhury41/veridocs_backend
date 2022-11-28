from django.db import models
import random
import string

# Create your models here.
class Form(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    data = models.JSONField()
    createdBy = models.TextField(max_length=30)

    def __str__(self):
        return self.name

# Create your models here.
class Template(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()
    createdBy = models.TextField(max_length=30)
    agency = models.TextField(max_length=30)
    def __str__(self):
        return self.name

def key_generator():
    key = ''.join(random.choice(string.digits) for i in range(6))
    if User.objects.filter(id=key).exists():
        key = key_generator()
    return key

class User(models.Model):
    uid = models.CharField(max_length=30, unique=True)
    id = models.CharField(max_length=6, default=key_generator,
        unique=True, editable=False, primary_key=True)