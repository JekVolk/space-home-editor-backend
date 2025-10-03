from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authtoken.models import Token

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import RegisterSerializer, TokenResponseSerializer, LogoutResponseSerializer


# -------------------------- Auth ------------------------------------------
class RegisterView(APIView):
    permission_classes = [AllowAny]  # <-- доступ без авторизації

    @extend_schema(
        request=RegisterSerializer,
        responses={201: TokenResponseSerializer},
        description="Реєстрація нового користувача і отримання токена"
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        if User.objects.filter(username=username).exists():
            return Response({"error": "Користувач вже існує"}, status=400)

        user = User.objects.create_user(username=username, password=password)
        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status=status.HTTP_201_CREATED)


class LogoutView(APIView):
    @extend_schema(
        request=None,
        responses={200: LogoutResponseSerializer},
        description="Видаляє токен поточного користувача (логаут)"
    )
    def post(self, request):
        try:
            request.user.auth_token.delete()
        except Exception:
            return Response({"error": "Ви не авторизовані"}, status=400)
        return Response({"message": "Вихід успішний"}, status=200)

