from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Snippet


class SnippetSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlighted')


class UserSerializer(ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')