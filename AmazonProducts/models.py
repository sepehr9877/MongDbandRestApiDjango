from django.db import models
class CategoryManger(models.Manager):
    def get_category_id(self,name):
        selected_element=Category.objects.get(Title__exact=name)
        selected_id=selected_element.id
        return selected_id
class Category(models.Model):
    Title=models.CharField(max_length=150)
    objects=CategoryManger()
    def __str__(self):
        return self.Title
class Products(models.Model):
    Title=models.CharField(max_length=150)
    Image=models.CharField(max_length=150,null=True)
    Price=models.CharField(max_length=150)
    Reviews=models.CharField(max_length=150)
    Rate=models.CharField(max_length=150)
    Categories=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.Title


# Create your models here.
