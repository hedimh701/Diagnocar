from rest_framework import serializers



class UserSubSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)