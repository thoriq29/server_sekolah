from django.db import models


class Province(models.Model):
    kode_provinsi = models.CharField(max_length=5)
    province_name = models.CharField(max_length=200)
    logo_provinsi = models.FileField()
