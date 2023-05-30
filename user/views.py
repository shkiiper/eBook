from django.contrib.auth import get_user_model, authenticate
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


from .serializers import UserSerializer

User = get_user_model()


# ViewSet для модели User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class TokenObtainPairView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Проверка учетных данных пользователя и генерация токенов
        # Это простой пример, и вам может потребоваться дополнительная логика для проверки учетных данных.
        # Пожалуйста, адаптируйте этот код к своим потребностям.

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            return Response({'access_token': access_token, 'refresh_token': refresh_token})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)