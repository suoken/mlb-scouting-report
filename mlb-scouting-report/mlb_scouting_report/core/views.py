from django.shortcuts import render, redirect

from player.models import Hitter, Pitcher, Player
from .forms import CreateHittingReport

def homePage(request):
    hitters = Hitter.objects.all()[0:4]
    pitchers = Pitcher.objects.all()[0:4]
    return render(request, 'core/homepage.html', {'hitters': hitters, 'pitchers': pitchers})

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

    return render(request, 'core/create-hitting-report.html', {'form': form})

def pitchingReport(request):
    return render(request, 'core/pitchingreport.html')
