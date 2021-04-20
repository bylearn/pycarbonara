from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import OptionsSerializer

# Create your views here.
class CarbonView(APIView):
    def post(self, request):
        serializers = OptionsSerializer(data=request.data)
        if serializers.is_valid():
            return Response({"status": serializers.data})
        return Response(
            {"message": serializers.errors}, status=status.HTTP_400_BAD_REQUEST
        )
