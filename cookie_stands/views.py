from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CookieStandSerializer
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class CookieStandList(ListCreateAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer

class CookieStandDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer