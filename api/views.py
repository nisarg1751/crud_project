from sub.models import User
from .serializer import UserSerializer
from rest_framework import viewsets


class CrudApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer