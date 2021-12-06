from django.db import models

# Create your models here.
class CountryModel(models.Model):
    # id=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=100)

    class Meta:
        db_table='ajax_dropdown'