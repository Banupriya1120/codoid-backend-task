from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import UserSerializer,BookSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User, Book
import jwt,datetime
from rest_framework.decorators import api_view
from rest_framework import status


class Registerview(APIView):
    def post(self,request):
        serializer = UserSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        payload = {
            'id':serializer.data['id'],
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()

        }
        token = jwt.encode(payload,'secret',algorithm='HS256')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data={
            'jwt':token
        }
        return response


class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')


        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()

        }
        token = jwt.encode(payload,'secret',algorithm='HS256')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data={
            'jwt':token
        }
        return response
    

class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Not Authorized')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])        
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed
        
        user = User.objects.filter(id=payload['id']).first()
        ser = UserSerializer(user)
        return Response(ser.data)


class BookView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return JsonResponse({"message": "data created", "data": serializer.data})

class BookCreate(APIView):
    def post(self,request):
        serializer= BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"message": "data created", "data": serializer.data})

@api_view(['GET'])
def get_item(request,pk):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return JsonResponse({"message": "data found", "data": serializer.data})
    except Exception as e:
        print(e)
        return JsonResponse({"message": "No data found"})

@api_view(['PUT'])
def update_item(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        data = BookSerializer(instance=book, data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse({"message": "Data Updated", "data": data.data})
        else:
            return JsonResponse({"message": "No data found"})
    except Exception as e:
        print(e)
        return JsonResponse({"message": "No data found"})

@api_view(['DELETE'])
def delete_items(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
        return JsonResponse({"message": "Data Deleted", "status": status.HTTP_202_ACCEPTED}) 
    except Exception as e:
        print(e)
        return JsonResponse({"message": "No data found"})

        


    



 