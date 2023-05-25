from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response


# def home(request):
#     return render(request,'login.html')
class Registerview(APIView):
    def post(self,request):
        serializer = UserSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
 