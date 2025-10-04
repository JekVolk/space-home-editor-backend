from django.contrib.auth.models import User
from django.db.models import Q
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from space_home_editor.utils import path_params
from user.models import Catalog, DefaultValueCatalog, DefaultResourceCatalog
from user.serializers import RegisterSerializer, TokenResponseSerializer, LogoutResponseSerializer, CatalogSerializer, \
    DefaultValueCatalogSerializer, DefaultResourceCatalogSerializer


# -------------------------- Auth ------------------------------------------
@path_params()
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

# -------------------------- Catalog ------------------------------------------
@path_params()
class CatalogViewSet(ModelViewSet):
    serializer_class = CatalogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Відбір по юзеру чи ті що без юзера (дефолтні) Андрюха дивись по сетуації якшо user обов'язковий в бд тільки по юзеру фільтрація без Q
        return Catalog.objects.filter(
            Q(user=self.request.user) | Q(user__isnull=True)
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @action(detail=True, methods=["get", "put", "patch"], url_path="default-value")
    def default_value(self, request, pk=None):
        #Андрюха Тобі не потрібна ця функція
        catalog = self.get_object()
        try:
            default_value = catalog.default_value
        except DefaultValueCatalog.DoesNotExist:
            # якщо не існує – створимо за замовчуванням
            default_value = DefaultValueCatalog.objects.create(catalog=catalog)

        if request.method == "GET":
            serializer = DefaultValueCatalogSerializer(default_value)
            return Response(serializer.data)

        if request.method in ["PUT", "PATCH"]:
            serializer = DefaultValueCatalogSerializer(default_value, data=request.data, partial=(request.method=="PATCH"))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@path_params("catalog_pk")
class DefaultResourceCatalogViewSet(ModelViewSet):
    serializer_class = DefaultResourceCatalogSerializer
    permission_classes = [IsAuthenticated]  # або інші права

    def get_queryset(self):
        catalog_id = self.kwargs.get('catalog_pk')
        return DefaultResourceCatalog.objects.filter(catalog_id=catalog_id)

    def perform_create(self, serializer):
        catalog_id = self.kwargs.get('catalog_pk')
        serializer.save(catalog_id=catalog_id)