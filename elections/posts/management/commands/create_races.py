from django.core.management.base import BaseCommand, CommandError
import requests

from elections.posts.models import Race

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        HOUSE_URL= 'http://elections.huffingtonpost.com/pollster/api/charts?topic=2014-house'
        SENATE_URL = 'http://elections.huffingtonpost.com/pollster/api/charts?topic=2014-senate'
        GOVERNOR_URL = 'http://elections.huffingtonpost.com/pollster/api/charts?topic=2014-governor'

        house = requests.get(HOUSE_URL)
        senate = requests.get(SENATE_URL)
        governor = requests.get(GOVERNOR_URL)

        races = house.json() + senate.json() + governor.json()

        print "Updating %s races" % len(races)

        Race.objects.all().delete()

        for race in races:
            print race['title']

            # Remove the keys from the race dictionary that don't map to a model attribute.
            for k in ['election_date', 'short_title', 'topic', 'state']:
                del race[k]

            # It's a sneaky Python trick, but if the dictionary keys precisely match your model
            # objects, you can unpack a dictionary to keyword arguments like this:
            #
            #     Class(**dictionary)
            #
            # Awesome, right?
            Race(**race).save()
