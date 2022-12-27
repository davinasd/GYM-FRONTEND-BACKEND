from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer
# Create your views here.

class UserListApiView(APIView):

    def post(self, request, *args, **kwargs):
            '''
            Create the Todo with given todo data
            '''
            data = {
                'name': request.data.get('name'), 
                'age': request.data.get('age'), 
                'gender': request.data.get('gender'),
                'locality' : request.data.get('locality')
            }
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailApiView(APIView):

    def get_object(self, name):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return User.objects.get(name=name)
        except User.DoesNotExist:
            return None
    def get(self, request, name, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        user_instance = self.get_object(name)
        if not user_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UserSerializer(user_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)