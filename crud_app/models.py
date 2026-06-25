from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    dob = models.DateField()
    image = models.ImageField(upload_to='images/',null=True)
    
    def __str__(self):
        return self.name