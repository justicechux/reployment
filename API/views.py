from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserRegistrationSerializer


@api_view(["POST"])
def register(request):
    if request.method == "POST":
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["response"] = "Your account has been created successfully!"
            data["email"] = user.email
            data["username"] = user.username
        else:
            data = serializer.errors
        return Response(data)
# Create your views here.
            
