from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from teammanager import serializers
from teammanager.models import *

# views.
class MemberViewSet(viewsets.ModelViewSet):
    http_method_names = ['post',"get","patch","delete"]
    queryset = Member.objects.all()
    serializer_class = serializers.MemberSerializer
