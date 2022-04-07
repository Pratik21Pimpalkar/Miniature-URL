from django.db import models

# Create your models here.

class LongToShort(models.Model):  
    
    long_url = models.URLField(max_length=500)
    short_url=  models.CharField(max_length=50,unique=True)
    date= models.DateField(auto_now_add=True)
    clicks= models.IntegerField(default=0)
  
class ChartData(models.Model):
    country=models.CharField(max_length=100)
    countryClicks= models.IntegerField(default=0)
    deviceClicks= models.IntegerField(default=0)

    def __str__(self):
        return f'{self.country}-{self.countryClicks}-{self.deviceClicks}'
    
