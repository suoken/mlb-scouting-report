from django.shortcuts import render

def playerHittingReport(request):
    return render(request, 'player/playerHittingReport.html')

def playerPitchingReport(request):
    return render(request, 'player/playerPitchingReport.html')