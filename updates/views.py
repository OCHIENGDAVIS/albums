from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Update
from .serializers import UpdateSerializer


class UpdateModeDetaillAPIView(RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    lookup_field = 'id'


class UpdateModeListAPIView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UpdateSerializer

    queryset = Update.objects.all()


def index(request):
    return render(request, 'base.html', context={"title": "welcome"})


def about(request):
    return render(request, 'about.html', context={})




