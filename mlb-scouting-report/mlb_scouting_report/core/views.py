from django.shortcuts import render

from player.models import Player, Hitter, Pitcher

def homePage(request):
    hitters = Hitter.objects.all()[0:4]
    pitchers = Pitcher.objects.all()[0:4]
    player = Player.objects.all()[0:4]
    return render(request, 'core/homepage.html', {'hitters': hitters, 'pitchers': pitchers})