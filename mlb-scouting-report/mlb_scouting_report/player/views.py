from django.shortcuts import render, get_object_or_404, redirect

from .models import Player
from .models import Hitter, Pitcher, Player
from .forms import HittingReportForm, PitchingReportForm

def playerHittingReport(request, slug):
    player = get_object_or_404(Player, slug=slug)
    latest_hitter_record = player.hitters.last()
    hitter_stats = player.hitters.all()
    stat_fields = [
        (label, value)
        for stat in hitter_stats
        for label, value in [
            ('Date', stat.report_date),
            ('Team', player.team),
            ('Pos', stat.field_position),
            ('Bat', stat.batting_position),
            ('Thr', stat.throwing_arm)
        ]
    ]
    
    return render(request, 'player/player-hitting-report.html', {'player': player, 'stat_fields': stat_fields, 'latest_hitter_record': latest_hitter_record})

def playerPitchingReport(request, slug):
    player = get_object_or_404(Player, slug=slug)
    latest_pitcher_record = player.pitchers.last()
    pitcher_stats = player.pitchers.all()
    pitches = [pitch for pitch in latest_pitcher_record.pitches.all()]
    
    stat_fields = [
        (label, value)
        for stat in pitcher_stats
        for label, value in [
            ('Date', stat.report_date),
            ('Team', player.team),
            ('Pos', stat.position),
            ('Thr', stat.throwing_arm)
        ]
    ]

    return render(request, 'player/player-pitching-report.html', {
                'player': player, 
                'stat_fields': stat_fields, 
                'latest_pitcher_record': latest_pitcher_record, 
                'pitches': pitches
                })

def createHittingReport(request):
    tools = ["Hit", "Power", "Fielding", "Throwing", "Run"]
    if request.method == 'POST':
        form = HittingReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form = HittingReportForm()

    return render(request, 'player/create-hitting-report.html', {'form': form, 'tools': tools})

def createPitchingReport(request):
    form = PitchingReportForm()
    return render(request, 'player/create-pitching-report.html', {'form': form})