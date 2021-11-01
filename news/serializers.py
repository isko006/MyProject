from rest_framework import serializers

from news.models import News, Law, Publication
from favorite.models import FavoriteLaw, FavoritePublication, FavoriteNews


class NewsListSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = 'id image title short_description publication_date is_favorite'.split()

    def get_is_favorite(self, news):
        request = self.context['request']
        return bool(request.user.is_authenticated and FavoriteNews.objects.filter(news=news, user=request.user))


class NewFullListSerializer(serializers.ModelSerializer):
    # is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = '__all__'


class LawListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Law
        fields = 'id title short_description'.split()

    def get_is_favorite(self, law):
        request = self.context['request']
        return bool(request.user.is_authenticated and FavoriteLaw.objects.filter(law=law, user=request.user))


class LawFullListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Law
        fields = '__all__'


class PublicationListSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = '__all__'

    def get_is_favorite(self, publication):
        request = self.context['request']
        return bool(request.user.is_authenticated and FavoritePublication.objects.filter(publication=publication, user=request.user))
