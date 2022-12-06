from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Account(models.Model):
    UserAccount=models.ForeignKey(User,on_delete=models.CASCADE,related_name='UserSpecification')
    ImageFile=models.ImageField(upload_to='User',null=True,blank=True)
    def __str__(self):
        return self.UserAccount.username
