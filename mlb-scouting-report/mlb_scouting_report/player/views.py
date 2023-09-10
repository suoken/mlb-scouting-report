from django.shortcuts import render, get_object_or_404, redirect

from .models import Player
from .models import Hitter, Pitcher, Player
from .forms import HittingReportForm, PitchingReportForm

def playerHittingReport(request, slug):
    player = get_object_or_404(Player, slug=slug)
    return render(request, 'player/playerHittingReport.html', {'player': player})

def createHittingReport(request):
    tools = ["Hit", "Power", "Fielding", "Throwing", "Run"]
    if request.method == 'POST':
        form = HittingReportForm(request.POST)

        print(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form = HittingReportForm()

    return render(request, 'player/create-hitting-report.html', {'form': form, 'tools': tools})

def playerPitchingReport(request, slug):
    return render(request, 'player/playerPitchingReport.html')

def createPitchingReport(request):
    form = PitchingReportForm()
    return render(request, 'player/create-pitching-report.html', {'form': form})