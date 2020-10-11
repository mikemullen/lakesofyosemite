from csv import DictReader
from datetime import datetime
from decimal import Decimal

from django.core.management import BaseCommand

from lakes.models import Lake
from pytz import UTC



class Command(BaseCommand):

    def handle(self, *args, **options):
        for row in DictReader(open('./lake_data.csv')):
            lake = Lake()
            lake.name = row['Name']
            print(lake.name)
            lake.elevation = row['elevation']
            print(lake.elevation)
            lake.size = row['size']
            print(lake.size)
            lake_location_raw = row['location']
            print(lake_location_raw)
            lake_lat_lon_raw = lake_location_raw.split(",")
            print(lake_lat_lon_raw)
            lake.lat = Decimal(lake_lat_lon_raw[0])
            print(lake.lat)
            lake.lon = Decimal(lake_lat_lon_raw[1])
            print(lake.lon)
            lake.slug = row['slug']
            print(lake.slug)
            lake.save()