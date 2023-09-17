from django.contrib import admin

from .models import Player, Hitter, Pitcher, Team, Pitch

class PitchInline(admin.TabularInline):
    model = Pitch
    extra = 4

class PitcherAdmin(admin.ModelAdmin):
    inlines = [PitchInline]

admin.site.register(Player)
admin.site.register(Hitter)
admin.site.register(Pitcher, PitcherAdmin)
admin.site.register(Team)