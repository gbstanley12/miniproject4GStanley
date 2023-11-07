from django.shortcuts import render
from django.http import HttpResponse
from .forms import MoviePollForm

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'polls/templates/index.html')  # Make sure you have a template at 'polls/templates/polls/home.html'
