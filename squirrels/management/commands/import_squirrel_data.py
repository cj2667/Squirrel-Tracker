from django.core.management.base import BaseCommand
import csv


class Command(BaseCommand):
    help = 'Get squirrels information'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help = 'file contain squirrel details')
    
    def handle(self, *args, **options):
        file_ = options['squirrel_file']
        
        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for item in reader:
                print(item)
    

