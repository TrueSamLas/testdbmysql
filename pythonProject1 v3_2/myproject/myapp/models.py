# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Percent(models.Model):
    idpercent = models.AutoField(primary_key=True)
    ts = models.DateField()
    rate = models.DecimalField(max_digits=2, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'percent'


class Products(models.Model):
    idproducts = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    descriprions = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Profit(models.Model):
    idprofit = models.AutoField(primary_key=True)
    ts = models.DateTimeField(blank=True, null=True)
    idregister = models.ForeignKey('Register', models.DO_NOTHING, db_column='idregister')
    quantite = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    n_profit = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=2, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'profit'


class Register(models.Model):
    idregister = models.AutoField(primary_key=True)
    ts = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(Products, models.DO_NOTHING, db_column='product')
    quantite = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    n_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    n_quantite = models.IntegerField(blank=True, null=True)
    n_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'register'
