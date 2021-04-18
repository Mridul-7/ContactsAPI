from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated
class ContactLC(ListCreateAPIView):
    serializer_class=ContactSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

class ContactRUD(RetrieveUpdateDestroyAPIView):
    serializer_class=ContactSerializer
    permission_classes=[IsAuthenticated]
    lookup_field="id"
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
