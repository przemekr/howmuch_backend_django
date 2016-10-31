from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from django.db import models

# Create your models here.
#

class WorkTime(models.Model):
    """ A work time unit... """

    def __str__(self):
        return "Work Time %s,%s,%s" % (self.user, str(self.start), str(self.end))

    start = models.DateTimeField()
    end = models.DateTimeField()
    user = models.ForeignKey(User, related_name='worktimes')
