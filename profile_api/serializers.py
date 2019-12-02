from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """serialize name field for testing our api """

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField(max_length=10)
