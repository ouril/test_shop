from django.db import models

class BaseModel(models.Model):
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