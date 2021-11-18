from django.db import models
from django.contrib.auth import authenticate
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.contrib.auth.models import User

# Create your models here.
status_choices=[
    ('C', 'Completed'),
    ('P', 'Pending'),
    ('I', 'In-Progress')
]

priority_choices =[
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),
    ('6', '6️⃣'),
    ('7', '7️⃣'),
    ('8', '8️⃣'),
    ('9', '9️⃣'),
    ('10', '🔟'),
]
class Todo(models.Model):
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=30, choices=status_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=2, choices=priority_choices)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title + " " + str(self.user)