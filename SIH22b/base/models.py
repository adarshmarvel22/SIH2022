from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# from shop.views import index
from django.db import models

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=200)
    # price=models.FloatField()
    # discounted_price=models.FloatField()
    cateegory=models.CharField(max_length=200)
    description=models.TextField()
    # image=models.CharField(max_length=300)
    
    def __str__(self):
        return self.title

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'

class News(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    geeks_field = models.URLField(max_length = 200, 
        db_index=True, 
        unique=True, 
        blank=True)
    def __str__(self):
        return self.title