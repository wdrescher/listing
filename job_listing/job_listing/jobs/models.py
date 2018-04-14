from django.db import models
from job_listing.users.models import User

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=40)
    body = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete='CASCADE')
