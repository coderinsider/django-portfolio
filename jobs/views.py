from django.shortcuts import render
from .models import Job

# Create your views here.
def h3k(request):
    job = Job.objects.all();
    return render(request, 'jobs/h3k.html', {'job': job})