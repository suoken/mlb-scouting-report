from django.shortcuts import render

from player.models import Hitter, Pitcher, Player

def homePage(request):
    hitters = Hitter.objects.all()[0:4]
    pitchers = Pitcher.objects.all()[0:4]
    return render(request, 'core/homepage.html', {'hitters': hitters, 'pitchers': pitchers})

def pitchingReport(request):
    return render(request, 'core/pitchingreport.html')
