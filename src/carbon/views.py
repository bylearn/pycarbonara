from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentSerializer

# Create your views here.
class CarbonView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True).data
        return Response(
            {
                "status": "OK",
                "comment": serializer,
            }
        )

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save()
            return Response(
                {
                    "status": "OK",
                    "comment": CommentSerializer(comment).data,
                }
            )
        return Response({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)
