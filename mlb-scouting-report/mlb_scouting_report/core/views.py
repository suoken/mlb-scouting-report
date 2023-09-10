from django.shortcuts import render
import feedparser
import datetime

from player.models import Hitter, Pitcher, Player

def homePage(request):
    hitters = Hitter.objects.all()[0:4]
    pitchers = Pitcher.objects.all()[0:4]


    feed_url = 'https://www.mlb.com/feeds/news/rss.xml'
    feed = feedparser.parse(feed_url)

    feed_entries = feed.entries[:4]

    for entry in feed_entries:
        epoch_timestamp = int(entry['mlb_display-date-epoch'])
        date_obj = datetime.datetime.fromtimestamp(epoch_timestamp)
        entry['formatted_date'] = date_obj.strftime('%b %d %Y')

    return render(request, 'core/homepage.html', {'hitters': hitters, 'pitchers': pitchers, 'feed': feed_entries})
