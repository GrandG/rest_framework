from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Snippet


class SnippetSerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlighted = serializers.HyperlinkedIdentityField(view_name='snippet-highlighted', format='html')
    class Meta:
        model = Snippet
        fields = ('url', 'id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlighted')


class UserSerializer(HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')