from django.db import models
from django import forms


class AccountType(models.Model):
    AccountId = models.AutoField(primary_key=True)
    AccountKind = models.CharField(max_length= 100)

class ClientInfo(models.Model):
    clientId = models.AutoField(primary_key=True)
    ClientName = models.CharField(max_length= 100)
    ClientSurname = models.CharField(max_length= 100)
    ClientEmail = models.CharField(max_length= 100)
    ClientNumber = models.CharField(max_length= 15)
    ClientIdNumber = models.CharField(max_length= 13)
    ClientPassword = models.CharField(max_length= 100)
    Account        = models.CharField(max_length= 100)
# Create your models here.
