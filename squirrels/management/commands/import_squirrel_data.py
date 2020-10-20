from django.core.management.base import BaseCommand
import csv
from squirrels.models import Squirrel
from datetime import datetime

class Command(BaseCommand):
    help = 'Get squirrels information'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help = 'file contain squirrel details')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']
        with open(file_) as fp:
            reader = csv.DictReader(fp)
            for item in reader:
                obj = Squirrel()
                obj.Latitude = item["X"]
                obj.Longitude = item["Y"]
                obj.Unique_Squirrel_ID = item["Unique Squirrel ID"]
                obj.Shift = item["Shift"]
                obj.Date = datetime.strptime(item["Date"],'%m%d%Y').date()
                obj.Age = item["Age"]


                obj.Running = item["Running"]
                obj.Chasing = item["Chasing"]
                obj.Climbing = item["Climbing"]
                obj.Eating = item["Eating"]
                obj.Foraging = item["Foraging"]








                obj.save()
        msg = f"You are importing from {file_}"
        self.stdout.write(self.style.SUCCESS(msg))

