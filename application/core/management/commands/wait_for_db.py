'''
Django command to wait for the db to be available
'''
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    ''' Django command to wait for database '''
    def handle(self, *args, **options):
        self.stdout.write('waiting for db')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('db unavailable waiting 1 sec')
                time.sleep(1)
        self.stdout.write('DB Available')