from django.db import models

class Tashriflar(models.Model):
    ip_address = models.GenericIPAddressField()  
    visit_date = models.DateField(auto_now_add=True)

class Murojatlar(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    message = models.TextField()
