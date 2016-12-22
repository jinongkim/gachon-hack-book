from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    student_id = models.CharField(max_length = 128)
    user_mail = models.TextField()
    user_id = models.CharField(max_length = 128, blank = True)
    user_pw= models.CharField(max_length = 128, blank = True)
    user_hp= models.CharField(max_length = 128, blank = True)
    user_major= models.CharField(max_length = 128, blank = True)
    ignores = models.ManyToManyField(User, related_name = 'ignore_set', blank = True, null = True)

