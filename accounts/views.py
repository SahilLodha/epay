from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth import get_user_model
from .serializer import UserCreateSerializer

User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "error": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user = serializer.create(validated_data=serializer.validated_data)
        serialized_user = UserCreateSerializer(user)
        return Response(
            {
                "success": True,
                "message": "User Registration Success.",
                "data": serialized_user.data
            },
            status=status.HTTP_201_CREATED
        )


class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pass
