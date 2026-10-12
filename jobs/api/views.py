from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Category, Job, Comment
from .serializer import CategorySerializer, JobSerializer, CommentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAuthenticated]

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobByCategoryAPIView(generics.ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Job.objects.filter(category_id=category_id)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
