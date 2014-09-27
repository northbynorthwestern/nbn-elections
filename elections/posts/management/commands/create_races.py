from django.core.management.base import BaseCommand, CommandError
from posts.models import Race
import requests


class Command(BaseCommand):
    HOUSE_URL= 'http://elections.huffingtonpost.com/pollster/api/charts?topic=2014-house'
    SENATE_URL = 'http://elections.huffingtonpost.com/pollster/api/charts?topic=2014-senate'
    GOVERNOR_URL = 'http://elections.huffingtonpost.com/pollster/api/charts?topic=2014-governor'

    house = requests.get(HOUSE_URL)
    senate = requests.get(SENATE_URL)
    governor = requests.get(GOVERNOR_URL)

    races = house.json() + senate.json() + governor.json()

    Race.objects.all().delete()

    for race in races:
        r = Race(
            title=race['title'],
            slug=race['slug'],
            poll_count=race['poll_count'],
            url=race['url'],
            last_updated=race['last_updated'],
            estimates=race['estimates']
            )
        r.save()
