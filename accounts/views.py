from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth import get_user_model
from .serializer import UserSerializer
User = get_user_model()


class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user = UserSerializer(user)
        return Response(
            {
                "success": True,
                "message": "User Fetched.",
                "data": user.data
            },
            status=status.HTTP_200_OK
        )
