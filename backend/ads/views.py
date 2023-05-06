from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets

from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer, AdDetailSerializer
from rest_framework.decorators import action


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    default_serializer_class = AdSerializer
    filterset_class = AdFilter

    serializers = {
        'retrieve': AdDetailSerializer
    }

    def get_queryset(self):
        if self.action == 'me':
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        ad = get_object_or_404(Ad, id=self.kwargs['ad__pk'])
        author = self.request.user
        serializer.save(author=author, ad=ad)
