from django.shortcuts import render, get_object_or_404, redirect

from .models import Player
from .models import Hitter, Pitcher, Player
from .forms import CreateHittingReport

def playerHittingReport(request, slug):
    player = get_object_or_404(Player, slug=slug)
    return render(request, 'player/playerHittingReport.html', {'player': player})

def createHittingReport(request):
    if request.method == 'POST':
        form = CreateHittingReport(request.POST)

        print(request.POST)
        print(form)

        if form.is_valid():
            print("valid")
            form.save()
            return redirect('/')
        
    else:
        print("not valid")
        form = CreateHittingReport()

    return render(request, 'player/create-hitting-report.html', {'form': form})

def playerPitchingReport(request, slug):
    return render(request, 'player/playerPitchingReport.html')