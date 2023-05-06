import django_filters
from django_filters import filters

from ads.models import Ad


class AdFilter(django_filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Ad
        fields = ('title',)
