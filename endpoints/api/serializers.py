from django.contrib.auth.models import Group
from rest_framework import serializers
from api.models import Member,Phonenumber,ClientId


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    phone_number = serializers.SlugRelatedField(
         queryset= Phonenumber.objects.all(),
         slug_field='id'
     )
    client_member_id = serializers.SlugRelatedField(
         queryset= ClientId.objects.all(),
         slug_field='id'
     )
    class Meta:
        model = Member
        fields = ['id','first_name','last_name', 'phone_number', 'client_member_id','account_id']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
