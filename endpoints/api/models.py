from django.db import models
from django.contrib.auth.models import AbstractUser
class Phonenumber(models.Model):
    phone_number = models.CharField(max_length=30, help_text="Enter member's phone_number ")
    def __unicode__(self):
        return self.phone_number

class ClientId(models.Model):
    client_member_id = models.CharField(max_length=60, help_text='Enter member_id')
    def __unicode__(self):
        return self.client_member_id

class Member(AbstractUser):
    first_name = models.CharField(max_length=120, help_text='Enter member_id')
    last_name = models.CharField(max_length=120, help_text='Enter member_id')
    phone_number = models.ForeignKey(Phonenumber, on_delete=models.CASCADE)
    client_member_id = models.ForeignKey(ClientId, on_delete=models.CASCADE)
    account_id = models.IntegerField()
