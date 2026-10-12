from rest_framework import serializers
from .models import Category, Job, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at']

class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    jobs = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_jobs(self, obj):
        view = self.context.get('view')
        if view and view.action == 'retrieve':
            return JobDetailSerializer(obj.jobs.all(), many=True).data
        return [job.name for job in obj.jobs.all()]

class JobSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = '__all__'

    def get_comments(self, obj):
        view = self.context.get('view')
        if view and view.action == 'retrieve':
            return CommentSerializer(obj.comment_set.all(), many=True).data
        return []
