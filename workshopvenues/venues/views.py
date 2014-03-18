from django.shortcuts import render
from venues.models import Venue
from django.http import Http404

def index(request):
    venues = Venue.objects.filter(active=True)
    context = {'venues': venues }
    return render(request, 'venues/index.html', context)

def about(request):
    return render(request, 'about.html')

def signin(request):
    return render(request, 'signin.html')

def detail(request, venue_id):
    try:
        venue = Venue.objects.get(pk=venue_id)
    except Venue.DoesNotExist:
        raise Http404
    return render(request, 'venues/detail.html', {'venue': venue})
