#from django.shortcuts import render
import csv
from django.contrib.auth.models import Group
from rest_framework import viewsets
from api.serializers import MemberSerializer, GroupSerializer
from api.models import Member
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from .bulkmanager import BulkCreateManager



class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('id')
    serializer_class = MemberSerializer


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
    parser_classes = (FileUploadParser,)

    def post(self, request,filename):
        file_obj = request.data['file']
        if file_obj[:-4] != '.csv':
            return Response(file_obj.name,"Unsupported file type")
        with open(file_obj) as opened_file:
            bulk_mgr = BulkCreateManager(chunk_size=1000)
            next(opened_file)
            for row in csv.reader(opened_file):
                bulk_mgr.add(Member(id=row[0],
                                                    first_name = row[1],
                                                    last_name = row[2],
                                                    phone_number = row[3],
                                                    client_member_id = row[4],
                                                    account_id = row[5]))
            bulk_mgr.done()
        return Response(file_obj.name,status=204)
