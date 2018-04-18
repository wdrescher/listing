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
        'key': JobPosting.objects.filter(active=True)
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
            post.active = True
            post.save()
            return land(request)
    context = {'form': form}
    return render(request, template, context)

def myjobs(request):
    template = "jobs/myjobs.html"
    query_result = JobPosting.objects.filter(owner=request.user).filter(active=True)
    # if query_result <= 0:
    #     query_result = 'oops'
    context = {
        'listings': query_result
    }
    return render(request, template, context)

def deletejob(request, job_posting_id):
    # deactivate instance with posting id matching job_posting_id
    job_post = JobPosting.objects.filter(pk = job_posting_id)
    for j in job_post:
        j.active = False
        j.save()
    return myjobs(request)
