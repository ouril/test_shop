from testshop.models import BaseModel
from django.db import models
from testshop import settings
import uuid
# Create your models here.


def make_upload_path(instance, filename, prefix=False):
    '''
    Create unque name for Image
    '''
    new_name = str(uuid.uuid1())
    parts = filename.split('.')
    index = parts[-1]
    filename = new_name + '.' + index
    return "{0}/{1}".format(settings.MEDIA_ROOT, filename)

class Product(BaseModel):
    name = models.CharField(
        max_length=191, 
        verbose_name='Product'
        )
    about = models.TextField() 
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        default=0.00,
        verbose_name='Price')
    image = models.ImageField(
        upload_to=make_upload_path,
        default='',
        blank=True
    )
    
    def __str__(self):
        return self.name

class Store(BaseModel):
    product = models.ForeignKey('Product')
    number = models.PositiveIntegerField(default=0)