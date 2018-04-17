from django.forms import ModelForm
from django import forms
from .models import JobPosting

class NewJobListing(ModelForm):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = JobPosting
        fields = ['title', 'body']
