from django.db import models

class Proj(models.Model) :
    name = models.CharField(max_length=20)
    contents = models.CharField(max_length=300)
    githuburl = models.CharField(max_length=50)   
    credit = models.IntegerField(default=0)
    

