from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Parent(models.Model):
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )
    family = models.ForeignKey(Family,on_delete=models.CASCADE,related_name='parent_data')
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=100,choices=GENDER)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Children(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE,related_name='children_data')
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name



    def __str__(self):
        return self.name

