from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class receipe(models.Model):
    name = models.CharField(max_length=122,null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    image= models.ImageField(blank=True,null=True)
    time= models.IntegerField(null=True, blank=True)

    
    

    