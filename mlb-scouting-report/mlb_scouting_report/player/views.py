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
    tools = ("Hit", "Power", "Fielding", "Throwing", "Run")    
    if request.method == 'POST':
        form = HittingReportForm(request.POST)
        try:
            if form.is_valid():
                player_name = form.cleaned_data['player']
                team_name = form.cleaned_data['team']
                player_instance, _ = Player.objects.get_or_create(name=player_name, team=team_name)

                hitter = form.save(commit=False)
                hitter.player = player_instance
                hitter.save()

                return redirect('/')
        except Exception as e:
            print("Exception:", e)
                
    else:
        form = HittingReportForm()

    groups = [
        (form['hit'], form['hit_future_value'], form['hit_comments']),
        (form['power'], form['power_future_value'], form['power_comments']),
        (form['fielding'], form['fielding_future_value'], form['fielding_comments']),
        (form['throwing'], form['throwing_future_value'], form['throwing_comments']),
        (form['run'], form['run_future_value'], form['run_comments'])
    ]

    return render(request, 'player/create-hitting-report.html', {'form': form, 'tools': tools, 'groups': groups})

def updateHitter(request, slug):
    hitter_instance = get_object_or_404(Hitter, player__slug=slug)
    if request.method == "POST":
        form = HittingReportForm(request.POST, instance=hitter_instance)
        if form.is_valid():
            form.save()
            return redirect('homePage')
    else:
        form = HittingReportForm(instance=hitter_instance)
    
    return render(request, 'player/update-hitting-report.html', {'form': form})

def createPitchingReport(request):
    form = PitchingReportForm()
    return render(request, 'player/create-pitching-report.html', {'form': form})