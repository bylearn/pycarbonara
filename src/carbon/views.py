from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import OptionsSerializer

# Create your views here.
class CarbonView(APIView):
    def post(self, request):
        serializers = OptionsSerializer(request.data)
        return Response({"status": serializers})
