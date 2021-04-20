import json
import asyncio

from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.parse import urlencode

from .jobs import get_content
from .serializers import OptionsSerializer

# Create your views here.
class CarbonView(APIView):
    def post(self, request):
        options = OptionsSerializer(data=request.data)
        if options.is_valid():
            urlencoded = urlencode(options.data)
            image = asyncio.run(get_content(urlencoded))
            print(image)
            return Response({"status": image})
        return Response({"message": options.errors}, status=status.HTTP_400_BAD_REQUEST)
