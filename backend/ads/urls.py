from django.urls import include, path
from rest_framework_nested import routers

from ads.views import AdViewSet, CommentViewSet


ads_router = routers.SimpleRouter()
ads_router.register('ads', AdViewSet, basename='ads')
comment_router = routers.NestedSimpleRouter(ads_router, 'ads', lookup='ad')
comment_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(ads_router.urls)),
    path('', include(comment_router.urls)),
]

