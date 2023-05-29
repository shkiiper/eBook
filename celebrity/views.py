from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# from celebrity.permissions import IsReadOnly
from .models import Celebrity
from .serializers import CelebritySerializer


class CelebrityViewSet(viewsets.ModelViewSet):
    queryset = Celebrity.objects.all()
    serializer_class = CelebritySerializer
    permission_classes = [AllowAny]
