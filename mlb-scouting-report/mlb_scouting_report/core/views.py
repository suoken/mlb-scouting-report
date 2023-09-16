from django.shortcuts import render, redirect
import datetime
import requests
import xml.etree.ElementTree as ET

from player.models import Hitter, Pitcher, Player

def homePage(request):
    hitters = Hitter.objects.all()[0:4]
    pitchers = Pitcher.objects.all()[0:4]

    feed_url = 'https://www.mlb.com/feeds/news/rss.xml'
    response = requests.get(feed_url)
    root = ET.fromstring(response.content)

    feed_entries = []

    for item in root.findall('.//item'):
        entry = {}
        entry['title'] = item.find('title').text
        entry['author'] = item.find('{http://purl.org/dc/elements/1.1/}creator').text
        entry['mlb_display-date-epoch'] = item.find('{https://www.mlb.com/rss/}display-date-epoch').text
        entry['link'] = item.find('link').text

        image_tag = item.find('image')
        if image_tag is not None:
            entry['image'] = image_tag.attrib['href']
        else:
            entry['image'] = None

        epoch_timestamp = int(entry['mlb_display-date-epoch'])
        date_obj = datetime.datetime.fromtimestamp(epoch_timestamp)
        entry['formatted_date'] = date_obj.strftime('%b %d %Y')

        feed_entries.append(entry)

    feed_entries = feed_entries[:4]

    return render(request, 'core/homepage.html', {'hitters': hitters, 'pitchers': pitchers, 'feed': feed_entries})

def deleteHitter(request, slug):
    hitter = Hitter.objects.get(player__slug=slug)
    player = hitter.player
    hitter.delete()
    player.delete()
    return redirect('homePage')

def pitcherHitter(request, slug):
    pitcher = Pitcher.objects.get(player__slug=slug)
    player = pitcher.player
    pitcher.delete()
    player.delete()
    return redirect('homePage')