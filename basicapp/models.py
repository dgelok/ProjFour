from django.db import models

# Create your models here.
class User(models.Model):
    user_first_name = models.CharField(max_length=64)
    user_last_name = models.CharField(max_length=64)
    user_email = models.EmailField(max_length=120, unique=True)

    def __str__(self):
        return self.user_first_name + " " + self.user_last_name + ": " + self.user_email

