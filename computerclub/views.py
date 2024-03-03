from rest_framework.viewsets import ModelViewSet
from .models import Director, Administrator, User, Order
from .serializers import DirectorSerializer, AdministratorSerializer, UserSerializer, OrderSerializer


class DirectorViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    http_method_names = ('get', 'post', 'put', 'delete')


class AdministratorViewSet(ModelViewSet):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    http_method_names = ('get', 'post', 'put', 'delete')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ('get', 'post', 'put', 'delete')
    
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ('get', 'post', 'put', 'delete')