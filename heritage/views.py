from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Monastery, Event

# Home page: list all monasteries
def home(request):
    monasteries = Monastery.objects.all()
    return render(request, "heritage/home.html", {"monasteries": monasteries})

# Monastery detail page
def monastery_detail(request, monastery_id):
    monastery = get_object_or_404(Monastery, id=monastery_id)
    return render(request, "heritage/detail.html", {"monastery": monastery})

# Events page: show upcoming events
def events(request):
    upcoming_events = Event.objects.filter(date__gte=timezone.now())
    return render(request, "heritage/events.html", {"events": upcoming_events})
