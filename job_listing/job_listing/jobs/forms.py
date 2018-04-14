from django.forms import ModelForm
from .models import JobPosting

class NewJobListing(ModelForm):
    class Meta:
        model = JobPosting
        fields = ['title', 'body']
