from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import UserCreateSerializer

# Import code to utilize our custom User model
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        """
        Post type API endpoint execution logic for creating a user when registering
        """
        # Retrieves request body information and saves it onto a variable ("data" in our case here)
        data = request.data

        # Extracts all the information we will need from the request body for creating the user
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']

        # Django's Python syntax for creating a User using our User model's definitions (See this file for our User model's definitions: `app/users/models.py`)
        user = User.objects.create_user(first_name, last_name, email, password)

        # Serializes (compiles/parse) the data for returning the response output (A Django Rest Framework process for using the tool)
        user = UserCreateSerializer(user)

        # Returns the API endpoint execution response along with status (Status is optional here)
        return Response(user.data, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    permisssion_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pass

