from rest_framework import APIView
from rest_framework import permissions

class RegisterView(APIView):
    def post(self, request):
        data = request.data

        return Response({}, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    permisssion_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pass

