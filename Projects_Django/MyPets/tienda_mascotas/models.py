from django.db import models

from django.db.models.fields.related import ForeignKey

# Create your models here.

class Country(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    abrev = models.CharField(max_length=4)
    status = models.BooleanField()
    created_at = models.DateField(auto_now=True)
    updatesd_at = models.DateField()
    deleted_at = models.DateField()

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    id_identification_type = models.IntegerField()
    number_id = models.CharField(max_length=15)
    id_city = models.IntegerField()
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)    
    status = models.BooleanField()
    created_at = models.DateField(auto_now=True)
    updatesd_at = models.DateField()
    deleted_at = models.DateField()
    

class Session(models.Model):
    id_user = models.IntegerField()
    ip = models.CharField(max_length=200)
    status = models.BooleanField()
    created_at = models.DateField(auto_now=True)
    updatesd_at = models.DateField()
    deleted_at = models.DateField()

class Identification_type(models.Model):
    type = models.CharField(max_length=150)
    abrev = models.CharField(max_length=4)
    created_at = models.DateField(auto_now=True)
    updatesd_at = models.DateField()
    deleted_at = models.DateField()

class City(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    abrev = models.CharField(max_length=4)
    id_country = models.IntegerField()
    status = models.BooleanField()
    created_at = models.DateField(auto_now=True)
    updatesd_at = models.DateField()
    deleted_at = models.DateField()

class Pet(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    id_user = models.IntegerField()
    id_type = models.IntegerField()
    id_race = models.IntegerField()
    status = models.BooleanField()
    created_at = models.DateField(auto_now=True)
    updatesd_at = models.DateField()
    deleted_at = models.DateField()

class Type(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    abrev = models.CharField(max_length=4)
    status = models.BooleanField()
    created_at = models.DateField(auto_now=True)
    updatesd_at = models.DateField()
    deleted_at = models.DateField()

class Race(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    abrev = models.CharField(max_length=4)
    status = models.BooleanField()
    created_at = models.DateField(auto_now=True)
    updatesd_at = models.DateField()
    deleted_at = models.DateField()



