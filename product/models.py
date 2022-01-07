from django.db import models
from django.urls import reverse

# Create your models here.
class  Product(models.Model):
    title          = models.CharField( max_length=150)
    description    = models.TextField(blank=True, null=True)
    price          = models.DecimalField(max_digits=1000, decimal_places=2)
    summery        = models.TextField()
    #added data(when adding another field and you want that field to be in the existing one when runing a migration press one to add a one default  then press True)
    featured       = models.BooleanField(default=False)
    
    
    def get_absolute_url(self):
        return reverse("detailview", kwargs={"id": self.id})
    #product in line 15 is the name of the app we are using and the detailview is the name of the urls in that app
    