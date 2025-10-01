from django.db import models

class SignUpRegistration(models.Model):    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=12, default="")
    date_registered = models.DateTimeField(auto_now_add=True)

   
    def __str__(self):
        return f"{self.first_name}{self.last_name}"
