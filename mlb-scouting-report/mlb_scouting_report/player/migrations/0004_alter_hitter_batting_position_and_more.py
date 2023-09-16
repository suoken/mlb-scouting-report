# Generated by Django 4.2.4 on 2023-09-16 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_alter_pitch_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hitter',
            name='batting_position',
            field=models.CharField(choices=[('R', 'R'), ('L', 'L'), ('S', 'S')], max_length=10),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='field_position',
            field=models.CharField(choices=[('C', 'C'), ('1B', '1B'), ('2B', '2B'), ('3B', '3B'), ('SS', 'SS'), ('LF', 'LF'), ('CF', 'CF'), ('RF', 'RF'), ('DH', 'DH')], max_length=10),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='fielding',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='fielding_future_value',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='future_grade',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='hit',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='hit_future_value',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='overall_grade',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='power',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='power_future_value',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='run',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='run_future_value',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='throwing',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='throwing_arm',
            field=models.CharField(choices=[('R', 'R'), ('L', 'L')], max_length=10),
        ),
        migrations.AlterField(
            model_name='hitter',
            name='throwing_future_value',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='pitch',
            name='grade',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='pitch',
            name='pitch_future_value',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='pitcher',
            name='future_grade',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='pitcher',
            name='overall_grade',
            field=models.IntegerField(choices=[(30, '30'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70'), (80, '80')]),
        ),
        migrations.AlterField(
            model_name='pitcher',
            name='position',
            field=models.CharField(choices=[('SP', 'SP'), ('RP', 'RF'), ('CL', 'CP')], max_length=10),
        ),
        migrations.AlterField(
            model_name='pitcher',
            name='throwing_arm',
            field=models.CharField(choices=[('R', 'R'), ('L', 'L')], max_length=20),
        ),
    ]
