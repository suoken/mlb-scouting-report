from django.shortcuts import render, get_object_or_404, redirect

from .models import Player
from .models import Hitter, Pitcher, Player, Team
from .forms import HittingReportForm, PitchingReportForm, PitchFormSet, PitchFormEditSet
from datetime import date

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

    context = {
        'player': player,
        'stat_fields': stat_fields,
        'latest_hitter_record': latest_hitter_record
    }
        
    return render(request, 'player/player-hitting-report.html', context)

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

    context = {
        'player': player, 
        'stat_fields': stat_fields, 
        'latest_pitcher_record': latest_pitcher_record, 
        'pitches': pitches
    }

    return render(request, 'player/player-pitching-report.html', context)

def createHittingReport(request):
    current_date = date.today()
    formatted_date = current_date.strftime('%Y-%m-%d')

    if request.method == 'POST':
        form = HittingReportForm(request.POST)
        
        try:
            if form.is_valid():
                player_name = form.cleaned_data['player']
                team_name = form.cleaned_data['team']
                report_date_value = form.cleaned_data['report_date']
                player_instance, _ = Player.objects.get_or_create(name=player_name, team=team_name)

                hitter = form.save(commit=False)
                hitter.report_date = report_date_value
                hitter.player = player_instance
                hitter.save()

                return redirect('/')
        except Exception as e:
            print("Exception:", e)
                
    else:
        form = HittingReportForm()
    
    context = {
        'current_date': formatted_date,
        'fields_to_ignore': ["player", "team", "field_position", "batting_position", "throwing_arm", "report_date", "overall_grade", "future_grade", "declarative_statement"],
        'form': form 
    }

    return render(request, 'player/create-hitting-report.html', context)

def updateHitter(request, slug):
    hitter_instance = get_object_or_404(Hitter, player__slug=slug)
    initial_data = {
        'player': hitter_instance.player.name,
        'team': hitter_instance.player.team
    }
    current_date = date.today()
    formatted_date = current_date.strftime('%Y-%m-%d')

    if request.method == "POST":
        form = HittingReportForm(request.POST, instance=hitter_instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = HittingReportForm(instance=hitter_instance, initial=initial_data)

    context = {
        'form': form,
        'fields_to_ignore': ["player", "team", "field_position", "batting_position", "throwing_arm", "report_date", "overall_grade", "future_grade", "declarative_statement"],
        'is_editing': True if hitter_instance.id else False,
        'current_date': formatted_date,
    }
    
    return render(request, 'player/create-hitting-report.html', context)


def get_pitch_types_and_check_errors(formset):
    pitch_types = [form.cleaned_data.get('pitch_type', None) for form in formset.forms]

    if len(pitch_types) != len(set(pitch_types)):
        formset._non_form_errors = formset.error_class(["You cannot have duplicate pitch types."])
        return None
    elif "" in pitch_types:
        formset._non_form_errors = formset.error_class(["Pitch type cannot be empty."])
        return None

    return pitch_types

def createPitchingReport(request):
    form = PitchingReportForm(request.POST if request.method == "POST" else None)
    formset = PitchFormSet(request.POST if request.method == "POST" else None)

    if request.method == "POST" and form.is_valid():
        try:
            player_instance, _ = Player.objects.get_or_create(name=form.cleaned_data['player'], team=form.cleaned_data['team'])
            pitcher_instance = Pitcher(
                player=player_instance,
                position=form.cleaned_data['position'],
                throwing_arm=form.cleaned_data['throwing_arm'],
                overall_grade=form.cleaned_data['overall_grade'],
                future_grade=form.cleaned_data['future_grade'],
                report_date=form.cleaned_data['report_date'],
                declarative_statement=form.cleaned_data['declarative_statement']
            )
            formset = PitchFormSet(request.POST, instance=pitcher_instance)

            if formset.is_valid() and get_pitch_types_and_check_errors(formset):
                pitcher_instance.save()
                formset.save()
                return redirect('homePage')
        except Exception as e:
            print('Exception:', e)
        
    formatted_date = date.today().strftime('%Y-%m-%d')

    context = {
        'form': form,
        'formset': formset,
        'current_date': formatted_date
    }

    return render(request, 'player/create-pitching-report.html', context)

def extract_data_from_form(form):
    return {
        'player_name': form.cleaned_data['player'],
        'team_name': form.cleaned_data['team'],
        'report_date': form.cleaned_data['report_date'],
        'declarative_statement': form.cleaned_data['declarative_statement']
    }

def updatePitcher(request, slug):
    pitcher_instance = get_object_or_404(Pitcher, player__slug=slug)

    initial_data = {
        'player': pitcher_instance.player.name,
        'team': pitcher_instance.player.team,
        'report_date': pitcher_instance.report_date,
        'declarative_statement': pitcher_instance.declarative_statement
    }

    form = PitchingReportForm(request.POST if request.method == "POST" else None, instance=pitcher_instance, initial=initial_data)
    formset = PitchFormEditSet(request.POST if request.method == "POST" else None, instance=pitcher_instance)

    if request.method == "POST" and form.is_valid() and formset.is_valid():
        data = extract_data_from_form(form)
        pitch_types = get_pitch_types_and_check_errors(formset)
        
        if pitch_types:
            try:
                player_instance = pitcher_instance.player
                player_instance.name = data['player_name']
                player_instance.team = data['team_name']
                player_instance.save()

                pitcher_instance.player = player_instance
                pitcher_instance.report_date = data['report_date']
                pitcher_instance.declarative_statement = data['declarative_statement']
                pitcher_instance.save()
                
                form.save()
                formset.save()

                return redirect('homePage')
            except Exception as e:
                print("Exception: ", e)

    formatted_date = date.today().strftime('%Y-%m-%d')

    context = {
        'form': form,
        'fields_to_ignore': ["player", "team", "field_position", "batting_position", "throwing_arm", "report_date", "overall_grade", "future_grade", "declarative_statement"],
        'is_editing': bool(pitcher_instance.id),
        'formset': formset,
        'current_date': formatted_date
    }

    return render(request, 'player/create-pitching-report.html', context)