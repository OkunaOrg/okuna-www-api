from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    subject = serializers.CharField(required=True, min_length=3, max_length=64)
    message = serializers.CharField(min_length=10, max_length=1000, required=True)
    email = serializers.EmailField(required=True)
