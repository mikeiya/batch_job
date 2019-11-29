from django.db import models
from django.contrib.auth.models import AbstractUser
class Phonenumber(models.Model):
    phone_number = models.TextField(unique=True)

class ClientId(models.Model):
    client_member_id = models.TextField(unique=True)

class Member(AbstractUser):
    phone_number = models.ForeignKey(Phonenumber, on_delete=models.CASCADE)
    client_member_id = models.ForeignKey(ClientId, on_delete=models.CASCADE)
    account_id = models.IntegerField()
