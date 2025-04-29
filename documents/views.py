from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Document, Tag
from .serializers import DocumentSerializer, TagSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Document.objects.filter(owner=self.request.user)
        sort = self.request.query_params.get('sort')
        tag = self.request.query_params.get('tag')

        if sort == 'created':
            queryset = queryset.order_by('created')
        elif sort == 'updated':
            queryset = queryset.order_by('updated')

        if tag:
            queryset = queryset.filter(tags__id=tag)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserLoginViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def login(self, request, id=None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
