from django.shortcuts import render
from .models import Organization
from .serializers import OrganizationSerializer
from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission

class OrganizationAPIView(APIView):
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get(self,request):
        org_data= Organization.objects.all()
        serialize_org = OrganizationSerializer(org_data,many=True)
        return Response(serialize_org.data)
    
    def post(self,request):
        org_data = OrganizationSerializer(data = request.data)
        if org_data.is_valid():
            org_data.save()
            return Response(org_data.data,status = status.HTTP_201_CREATED)
        return Response(org_data.errors,status = status.HTTP_400_BAD_REQUEST)
    
class OrganizationDetailsBy_ID(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    def get_object(self,id):
        try:
            return Organization.objects.get(id = id)
        except Organization.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        org_data = self.get_object(id)
        serialize_org = OrganizationSerializer(org_data) 
        return Response(serialize_org.data)
    
    def put(self,request,id):
        org_data = self.get_object(id)
        serialize_org = OrganizationSerializer(org_data, data = request.data)
        if serialize_org.is_valid():
            serialize_org.save()
            return Response(serialize_org.data)
        return Response(serialize_org.errors , status = status.HTTP_404_BAD_REQUEST)
    
    def delete(self,request,id):
        org_data = self.get_object(id)
        org_data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
