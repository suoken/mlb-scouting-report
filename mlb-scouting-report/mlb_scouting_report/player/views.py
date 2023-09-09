from django.shortcuts import render, get_object_or_404

from .models import Player

def playerHittingReport(request, slug):
    player = get_object_or_404(Player, slug=slug)
    return render(request, 'player/playerHittingReport.html', {'player': player})

def playerPitchingReport(request, slug):
    return render(request, 'player/playerPitchingReport.html')