import jwt
from rest_framework import authentication,exceptions
from django.contrib.auth.models import User
class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data=authentication.get_authorization_header(request)
        if not auth_data:   #if credentials are not supplied
            return None
        prefix,token=auth_data.decode('utf-8').split(' ')   #decoded into python native form 
        try:
            #decode the token into data
                                #enter your key before using
            payload=jwt.decode(token,key=<yourkey>,algorithms='HS256')

            #get username from payload
            user=User.objects.get(username=payload['username'])
            return (user,token)
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Invalid token')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('token expired')
        return super().authenticate(request)