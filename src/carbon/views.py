from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.parse import urlencode

from .serializers import OptionsSerializer

# Create your views here.
class CarbonView(APIView):
    def post(self, request):
        serializers = OptionsSerializer(data=request.data)
        if serializers.is_valid():
            url_pronta = urlencode(serializers.data)
            return Response({"status": "https://carbon.now.sh/?" + url_pronta})
        return Response(
            {"message": serializers.errors}, status=status.HTTP_400_BAD_REQUEST
        )
