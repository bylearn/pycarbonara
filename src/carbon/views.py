import json

from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.parse import urlencode

from .serializers import OptionsSerializer

# Create your views here.
class CarbonView(APIView):
    def post(self, request):
        options = OptionsSerializer(data=request.data)
        if options.is_valid():
            urlencoded = urlencode(options.data)
            return Response({"status": "https://carbon.now.sh/?" + urlencoded})
        return Response({"message": options.errors}, status=status.HTTP_400_BAD_REQUEST)
