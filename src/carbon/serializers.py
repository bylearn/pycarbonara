from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
