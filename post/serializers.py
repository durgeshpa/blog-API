from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import (Post, Comment)

user = get_user_model()


# base_url = "http://localhost:8000"
base_url = "https://blog-1-api-test.herokuapp.com"


class PostCreateOrUpdate(serializers.ModelSerializer):
    """update or create serializer..."""

    class Meta:
        """meta class..."""

        model = Post
        fields = ["title",
                  "body",
                  "status",
                  ]

    def validate_title(self, value):
        """Validate title..."""
        if len(value) > 100:
            return serializers.ValidationError("Max title length is 100 characters")
        return value


class PostListSerializer(serializers.ModelSerializer):
    """List serilizer ...."""

    url = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField(read_only=True)
    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """Meta class.."""

        model = Post
        fields = [
            "id",
            "url",
            "title",
            "author",
            "comments",
        ]

    def get_comments(self, obj):
        """Return comment count..."""
        qs = Comment.objects.filter(parent=obj).count()
        return qs

    def get_author(self, obj):
        """Return author name ..."""
        return obj.author.username

    def get_url(self, obj):
        """Return absalute url ..."""
        return base_url + obj.get_absolute_url()


class PostDetailSerializer(serializers.ModelSerializer):
    """post details serilizers..."""

    id = serializers.SerializerMethodField(read_only=True)
    # author = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """meta class.."""

        model = Post
        fields = [
            "id",
            # "slug",
            "title",
            "body",
            "author",
            "created",
            "updated",
            "comments",
        ]

    def get_id(self, obj):
        """Return Id ...."""
        return obj.id

    def get_author(self, obj):
        """Return author name ..."""
        return obj.author.username

    def get_comments(self, obj):
        """Get comments ..."""
        qs = Comment.objects.filter(parent=obj)
        try:
            serializer = CommentSerializer(qs, many=True)
        except Exception as e:
            print(e)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    """comment serializer.."""

    class Meta:
        """Meta classs .."""

        model = Comment
        fields = [
            "id",
            "parent",
            "author",
            "body",
            "created_at",
            "updated_at",
        ]


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    """new comment .."""

    class Meta:
        """meta class.."""

        model = Comment
        fields = [
            "body",
        ]
