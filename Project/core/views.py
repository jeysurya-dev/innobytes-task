from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import Product, Order, User
from .serializers import ProductSerializer, OrderSerializer, UserSerializer


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_staff


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def view_order(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk, user=request.user)
        return Response(OrderSerializer(order).data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(self.request.data['password'])
        user.save()

    @action(detail=False, methods=['post'], permission_classes=[])
    def login(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({'access': str(refresh.access_token)})
        return Response({'error': 'Invalid credentials'}, status=400)

    @action(detail=False, methods=['post'], permission_classes=[])
    def register(self, request):
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({'message': 'User registered successfully'})
