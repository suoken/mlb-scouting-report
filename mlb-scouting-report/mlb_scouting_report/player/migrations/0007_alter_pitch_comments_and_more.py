# Generated by Django 4.2.4 on 2023-09-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0006_alter_hitter_field_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitch',
            name='comments',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='pitcher',
            name='declarative_statement',
            field=models.TextField(blank=True, null=True),
        ),
    ]
