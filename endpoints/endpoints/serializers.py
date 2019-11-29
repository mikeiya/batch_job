from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['id','first_name','last_name', 'phone_number', 'client_member_id','account_id']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
