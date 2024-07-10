from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, JournalPostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import JournalPost
import datetime
from django.utils.timezone import now
from rest_framework.response import Response



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
    


class JournalPostSummaryView(generics.ListAPIView):
    serializer_class = JournalPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        period = self.request.query_params.get('period', 'daily').lower()
        
        if period == 'daily':
            start_date = now().date()
        elif period == 'weekly':
            start_date = now().date() - datetime.timedelta(days=now().date().weekday())
        elif period == 'monthly':
            start_date = now().date().replace(day=1)
        else:
            start_date = now().date()  # Default to daily if period is invalid

        return JournalPost.objects.filter(author=user, date__gte=start_date).order_by('-date')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'period': self.request.query_params.get('period', 'daily').lower(),
            'count': queryset.count(),
            'entries': serializer.data
        }
        return Response(data)