from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ticket(models.Model):
    class Status(models.TextChoices):
        OPEN="open"
        IN_PROGRESS="in progress"
        RESOLVED="resolved"
    title=models.CharField(max_length=100,primary_key=True)
    description=models.TextField()
    status=models.CharField(max_length=100,choices=Status.choices,default=Status.OPEN)
    assignee=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}:{}".format(self.title,self.status)