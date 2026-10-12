from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, JobViewSet, CommentViewSet, JobByCategoryAPIView

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('jobs', JobViewSet, basename='job')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('categories/<int:category_id>/jobs/', JobByCategoryAPIView.as_view()),
]
