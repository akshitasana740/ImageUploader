from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class ImageModel(models.Model):
 photo = models.ImageField(upload_to="myimage")
 status=models.CharField(max_length=200)
 posted_on = models.DateTimeField(auto_now_add=True)