"""
URL configuration for mlb_scouting_report project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.views import homePage, deleteHitter, pitcherHitter
from player.views import playerHittingReport, playerPitchingReport, createHittingReport, createPitchingReport, updateHitter, updatePitcher

urlpatterns = [
    path('', homePage, name='homePage'),
    path('admin/', admin.site.urls),
    path('create-hitting-report/', createHittingReport, name='createHittingReport'),
    path('create-pitching-report/', createPitchingReport, name='createPitchingReport'),
    path('player-hitting-report/<slug:slug>', playerHittingReport, name='playerHittingReport'),
    path('player-pitching-report/<slug:slug>', playerPitchingReport, name='playerPitchingReport'),
    path('delete-hitter/<slug:slug>', deleteHitter, name='delete_hitter'),
    path('delete-pitcher/<slug:slug>', pitcherHitter, name='delete_hitter'),
    path('update-hitter/<slug:slug>/', updateHitter, name='updateHitter'),
    path('update-pitcher/<slug:slug>/', updatePitcher, name='updatePitcher'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
