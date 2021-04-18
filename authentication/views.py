from django.contrib import auth
from .serializers import UserSerializers,LoginSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
import jwt

class RegisterView(GenericAPIView):
    serializer_class=UserSerializers

    def post(self,request):
        serial=UserSerializers(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response({'Response':'Registered','Details':serial.data},status=status.HTTP_200_OK)
        return Response({'Error':serial.errors},status=status.HTTP_403_FORBIDDEN)

class LoginView(GenericAPIView):
    serializer_class=LoginSerializers
    def post(self,request):
        data=request.data
        username=data.get('username','')
        password=data.get('password','')
        user=auth.authenticate(username=username,password=password)

        #generate jwt token
        if user:
                                             #enter your key before using
            auth_token=jwt.encode({'username':user.username},key=<yourkey>)
            #returning logged in user details and authorization token
            return Response({'Success':'Logged in','details':UserSerializers(user).data,'token':auth_token},status=status.HTTP_200_OK)
        return Response({'error':'invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)
        
