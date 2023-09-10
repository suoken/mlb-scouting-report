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

    tool_fields = [
        (label, value)
        for stat in hitter_stats
        for label, value in [
            ('Hit', stat.hit),
            ('Hit FV', stat.hit_future_value),
            ('Hit Comment', stat.hit_comments),
            ('Power', stat.power),
            ('Power FV', stat.power_future_value),
            ('Power Comment', stat.power_comments),
            ('Field', stat.fielding),
            ('Field FV', stat.fielding_future_value),
            ('Field Comment', stat.fielding_comments),
            ('Throw', stat.throwing),
            ('Throw FV', stat.throwing_future_value),
            ('Throw Comment', stat.throwing_comments),
            ('Run', stat.run),
            ('Run FV', stat.run_future_value),
            ('Run Comment', stat.run_comments),
        ]
    ]

    print(tool_fields)

    return render(request, 'player/player-hitting-report.html', {'player': player, 'stat_fields': stat_fields, 'latest_hitter_record': latest_hitter_record, 'tool_fields': tool_fields})

def playerPitchingReport(request, slug):
    player = get_object_or_404(Player, slug=slug)
    return render(request, 'player/player-pitching-report.html', {'player': player})



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

def createPitchingReport(request):
    form = PitchingReportForm()
    return render(request, 'player/create-pitching-report.html', {'form': form})