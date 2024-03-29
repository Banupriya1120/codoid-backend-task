from rest_framework import serializers
from .models import User,Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','password']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','no_of_pages','publish_date','quantity']

    title= serializers.CharField()
    no_of_pages=serializers.IntegerField()
    publish_date=serializers.DateField()
    quantity = serializers.IntegerField()
   

    def create(self,data):
        return Book.objects.create(**data)
    