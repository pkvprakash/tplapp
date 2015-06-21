from django.db import models

# Create your models here.

class Role(models.Model):
    role_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length = 20)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.role_id

class User(models.Model) :
    user_id = models.CharField(max_length = 20, primary_key=True)
    name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 100);
    role_id = models.ForeignKey(Role)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.user_id
