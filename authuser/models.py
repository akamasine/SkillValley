# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=254)
    phone_no =models.CharField(max_length=15)
    title = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    booked =  models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['booked']