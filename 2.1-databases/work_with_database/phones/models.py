from django.db import models
from django.urls import reverse
from django.utils.text import slugify



class Phone(models.Model):
    
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=1, max_digits=9)
    image = models.CharField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length= 250, editable=False, unique=True)

    def get_abs_url(self):
        return reverse('phone', kwargs={'slug':self.slug})
    
    def __str__(self) :
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)