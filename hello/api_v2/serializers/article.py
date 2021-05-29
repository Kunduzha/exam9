from rest_framework import serializers

from webapp.models import Albom, Gallery


class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = ('id', 'title', 'content', 'author', 'created_at')
        read_only_fields = ('author', 'id')

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = ('image', 'caption', 'user', 'status')
        read_only_fields = ('user', 'id')

