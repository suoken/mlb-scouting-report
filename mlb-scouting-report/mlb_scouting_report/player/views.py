from django.shortcuts import render

from .models import Player

def playerHittingReport(request, slug):
    player = Player.objects.get(slug=slug)
    return render(request, 'player/playerHittingReport.html', {'player': player})

def playerPitchingReport(request, slug):
    return render(request, 'player/playerPitchingReport.html')