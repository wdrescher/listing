from django.shortcuts import render, redirect
from django import forms
from django.http import request
from django.views.generic import ListView

from .models import JobPosting
from .forms import NewJobListing
# Create your views here.

def land(request):
    template = 'jobs/landpage.html'
    context = {
        'key': JobPosting.objects.all()
    }
    if request.user.is_authenticated:
        context['auth'] = 'Validated'
    return render(request, template, context)

def new_job_listing(request):
    template = 'jobs/newjob.html'
    form = NewJobListing()
    if request.method == 'POST':
        form = NewJobListing(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.title  = request.POST['title']
            post.body = request.POST['body']
            post.owner = request.user
            post.save()
            return land(request)
    context = {'form': form}
    return render(request, template, context)
