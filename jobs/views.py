from django.shortcuts import render

# Create your views here.
def h3k(request):
    return render(request, 'jobs/h3k.html', {})