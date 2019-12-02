#from django.shortcuts import render
import csv
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.decorators import action
from api.serializers import MemberSerializer, GroupSerializer
from api.models import Member,Phonenumber,ClientId
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from .bulkmanager import BulkCreateManager
from django.core.files.storage import FileSystemStorage



class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('id')
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        number = Phonenumber.objects.get(pk=self.request.data['phone_number'])
        serializer.save(phone_number=number)

        client_id = ClientId.objects.get(pk=self.request.data['client_member_id'])
        serializer.save(client_member_id=client_id)

    @action(detail=True)
    def phonenumber(self, request, *args, **kwargs):
        member = self.get_object()
        return Response(member.phone_number)

    @action(detail=True)
    def clientid(self, request, *args, **kwargs):
        member = self.get_object()
        return Response(member.client_member_id )


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class FileUploadView(APIView):
    """
        API endpoint that allows csv files to be uploaded.
    """
    parser_classes = (MultiPartParser,)

    def post(self, request,format='csv'):
        file_obj = request.data['filename']
        if file_obj.name[-4:] != '.csv':
            return Response("Unsupported file type")
        storage = FileSystemStorage()
        try:
            storage.save(file_obj.name,file_obj)
            with storage.open(file_obj.name,mode='r') as opened_file:
                bulk_mgr = BulkCreateManager(chunk_size=1000)
                reader = csv.reader(opened_file)
                next(reader)
                for row in reader:
                    bulk_mgr.add(Member(id=row[0],
                                                        first_name = row[1],
                                                        last_name = row[2],
                                                        phone_number = Phonenumber.objects.create(phone_number = row[3]),
                                                        client_member_id = ClientId.objects.create(client_member_id = row[4]),
                                                        account_id = row[5]))
                bulk_mgr.done()
        except  Exception as e:
            raise e
            return Response("could not open file or invalid csv file")
        return Response({file_obj.name:storage.location()},status=204)
