# Generated by Django 4.2.4 on 2023-09-09 20:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion

def populate_teams(apps, schema_editor):
    Team = apps.get_model("player", "Team")
    TEAMS = [
        ("ari", "Arizona Diamondbacks"),
        ("atl", "Atlanta Braves"),
        ("bal", "Baltimore Orioles"),
        ("bos", "Boston Red Sox"),
        ("chc", "Chicago Cubs"),
        ("cws", "Chicago White Sox"),
        ("cin", "Cincinnati Reds"),
        ("cle", "Cleveland Guardians"),
        ("col", "Colorado Rockies"),
        ("det", "Detroit Tigers"),
        ("hou", "Houston Astros"),
        ("kc", "Kansas City Royals"),
        ("laa", "Los Angeles Angels"),
        ("lad", "Los Angeles Dodgers"),
        ("mia", "Miami Marlins"),
        ("mil", "Milwaukee Brewers"),
        ("min", "Minnesota Twins"),
        ("nym", "New York Mets"),
        ("nyy", "New York Yankees"),
        ("oak", "Oakland Athletics"),
        ("phi", "Philadelphia Phillies"),
        ("pit", "Pittsburgh Pirates"),
        ("sd", "San Diego Padres"),
        ("sf", "San Francisco Giants"),
        ("sea", "Seattle Mariners"),
        ("stl", "St. Louis Cardinals"),
        ("tb", "Tampa Bay Rays"),
        ("tex", "Texas Rangers"),
        ("tor", "Toronto Blue Jays"),
        ("was", "Washington Nationals"),
    ]

    for code, name in TEAMS:
        Team.objects.create(code=code, name=name)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='player.team')),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Pitcher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField(auto_now_add=True)),
                ('declarative_statement', models.TextField(blank=True, max_length=1024, null=True)),
                ('position', models.CharField(choices=[('SP', 'Starting Pitcher'), ('RP', 'Relief Pitcher'), ('CL', 'Closing Pitcher')], max_length=10)),
                ('throwing_arm', models.CharField(choices=[('R', 'Right'), ('L', 'Left')], max_length=20)),
                ('overall_grade', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('future_grade', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pitchers', to='player.player')),
            ],
            options={
                'ordering': ('-report_date',),
            },
        ),
        migrations.CreateModel(
            name='Pitch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pitch_type', models.CharField(choices=[('Four-seam Fastball', 'Four Seam Fastball'), ('Two-seam Fastball', 'Two Seam Fastball'), ('Cutter', 'Cutter'), ('Splitter', 'Splitter'), ('Slider', 'Slider'), ('Curveball', 'Curveball'), ('Forkball', 'Forkball'), ('Slurve', 'Slurve'), ('Screwball', 'Screwball'), ('Changeup', 'Changeup'), ('Palmball', 'Palmball'), ('Circle Changeup', 'Circle Changeup'), ('Kunckleball', 'Knuckleball'), ('Eephus', 'Eephus'), ('Knuckle Curve', 'Knuckle Curve'), ('Sinker', 'Sinker'), ('Sweeper', 'Sweeper')], max_length=20)),
                ('velocity_low', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)])),
                ('velocity_high', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)])),
                ('grade', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('pitch_future_value', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('comments', models.TextField(max_length=1024)),
                ('pitcher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pitches', to='player.pitcher')),
            ],
        ),
        migrations.CreateModel(
            name='Hitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField(auto_now_add=True)),
                ('declarative_statement', models.TextField(blank=True, null=True)),
                ('field_position', models.CharField(choices=[('P', 'Pitcher'), ('C', 'Catcher'), ('1B', 'First Baseman'), ('2B', 'Second Baseman'), ('3B', 'Third Baseman'), ('SS', 'Shortstop'), ('LF', 'Left Field'), ('CF', 'Center Field'), ('RF', 'Right Field'), ('DH', 'Designated Hitter')], max_length=10)),
                ('batting_position', models.CharField(choices=[('R', 'Right'), ('L', 'Left'), ('Switch', 'Switch')], max_length=10)),
                ('throwing_arm', models.CharField(choices=[('R', 'Right'), ('L', 'Left')], max_length=10)),
                ('hit', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('hit_future_value', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('hit_comments', models.TextField(blank=True, max_length=255, null=True)),
                ('power', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('power_future_value', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('power_comments', models.TextField(blank=True, max_length=255, null=True)),
                ('fielding', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('fielding_future_value', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('fielding_comments', models.TextField(blank=True, max_length=255, null=True)),
                ('throwing', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('throwing_future_value', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('throwing_comments', models.TextField(blank=True, max_length=255, null=True)),
                ('run', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('run_future_value', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('run_comments', models.TextField(blank=True, max_length=255, null=True)),
                ('overall_grade', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('future_grade', models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')])),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hitters', to='player.player')),
            ],
            options={
                'ordering': ('-report_date',),
            },
        ),
        migrations.RunPython(populate_teams),
    ]
