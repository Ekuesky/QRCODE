from rest_framework import serializers

class QRCodeSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)