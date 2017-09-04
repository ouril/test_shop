from django.db import models

class BaseModel(models.Model):
    '''
    Base model for different Products
    Add date creation and update for model
    '''

    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name ='Creation_date'
    )
    updated = models.DateTimeField(
        auto_now_add = True,
        verbose_name ='Updated_date'
    )

    class Meta:
        abstract = True

