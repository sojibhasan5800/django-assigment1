from django.db import models

# Create your models here.

class catagory_model(models.Model):
    cat_name = models.CharField(max_length=20)

    def __str__(self):
        return self.cat_name
   

