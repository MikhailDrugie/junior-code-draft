from django.db import models


class Promo(models.Model):
    """
    - name
    - amount
    - duration
    """
    name = models.CharField(max_length=512)
    amount = models.IntegerField(default=1)
    expires_at = models.DateTimeField()


class Teacher(models.Model):
    """
    - login
    - password
    - promocode
    - fullname
    - school
    - town
    - email
    - phone
    - allow_personal_data
    """
    login = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    phone = models.CharField(max_length=64)
    fullname = models.CharField(max_length=256)
    school_name = models.CharField(max_length=256)
    town = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    promo_id = models.ForeignKey(Promo, on_delete=models.PROTECT)
    allow_personal = models.BooleanField(default=True)
