from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import *


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class WorkTimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkTime
        fields = ('id', 'url', 'user', 'start', 'end')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    worktimes = WorkTimeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'worktimes')

