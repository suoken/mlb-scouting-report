# Generated by Django 4.2.4 on 2023-09-16 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_alter_hitter_batting_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hitter',
            name='fielding',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='fielding_future_value',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='future_grade',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='hit',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='hit_future_value',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='overall_grade',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='power',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='power_future_value',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='report_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='run',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='run_future_value',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='throwing',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='throwing_future_value',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='pitch',
            name='grade',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='pitch',
            name='pitch_future_value',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='pitcher',
            name='future_grade',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='pitcher',
            name='overall_grade',
            field=models.IntegerField(choices=[(30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (65, '65'), (70, '70'), (75, '75'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='pitcher',
            name='report_date',
            field=models.DateField(),
        ),
    ]