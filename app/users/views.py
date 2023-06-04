from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import UserCreateSerializer, UserSerializer


class RegisterView(APIView):
    def post(self, request):
        """
        Post type API endpoint execution logic for creating a user when registering
        """
        # Retrieves request body information and saves it onto a variable ("data" in our case here)
        data = request.data

        # Use the UserCreateSerializer to invoke validation and creation of the user account
        serializer = UserCreateSerializer(data=data)

        # If user input is not valid, throw an error with the serialized inforamtion
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.create(serializer.validated_data)
        user = UserSerializer(user)

        # Returns the API endpoint execution response along with status (Status is optional here)
        return Response(user.data, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    # Set requirement for this endpoint to have user be logged in providing an auth token
    permisssion_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Get the logged in users model information
        """
        # Get the user information from this endpoint request
        user = request.user
        user = UserSerializer(user)

        # Return the serialized user data information
        return Response(user.data, status=status.HTTP_200_OK)

