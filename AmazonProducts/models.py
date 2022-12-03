from django.db import models
class Category(models.Model):
    Title=models.CharField(max_length=150)
class Products(models.Model):
    Title=models.CharField(max_length=150)
    Image=models.ImageField(upload_to='Procuts',null=True,blank=True)
    Price=models.IntegerField()
    Reviews=models.IntegerField()
    Rate=models.IntegerField()
    Categories=models.ForeignKey(Category,on_delete=models.CASCADE)


# Create your models here.
