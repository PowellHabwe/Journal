from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, JournalPostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import JournalPost


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class JournalPostListCreate(generics.ListCreateAPIView):
    serializer_class = JournalPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return JournalPost.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class JournalPostDelete(generics.DestroyAPIView):
    serializer_class = JournalPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return JournalPost.objects.filter(author=user)


class JournalPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JournalPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return JournalPost.objects.filter(author=user)