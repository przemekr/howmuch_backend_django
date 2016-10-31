from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, WorkTimeSerializer
from django.shortcuts import get_object_or_404, render                                                                                                                                                         
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.staticfiles import finders
from models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class WorkTimeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows WorkTimes to be viewed or edited.
    """
    queryset = WorkTime.objects.all()
    serializer_class = WorkTimeSerializer



def user_view(request, id):
    user = User.objects.get(id)
    print user.worktimes.getAll()
    context = {
          'user': user,
          }
    return render(request, 'howmuch/user_view.html', context)

