from rest_framework import serializers

from ads.models import Ad

from ads.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_image = serializers.CharField(source='author.image', read_only=True)
    ad_id = serializers.CharField(source='ad.id', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'pk', 'created_at', 'text', 'author_first_name', 'author_last_name',
            'author_id', 'author_image', 'ad_id')


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('pk', 'title', 'description', 'price', 'image')


class AdDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    phone = serializers.CharField(source='author.phone', read_only=True)

    class Meta:
        model = Ad
        fields = (
            'pk', 'title', 'description', 'price', 'image', 'author_first_name', 'author_last_name', 'author_id',
            'phone')
