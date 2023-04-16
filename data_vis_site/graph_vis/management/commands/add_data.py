import sqlite3

import pandas as pd
from django.core.management.base import BaseCommand
from graph_vis.import_data import construct_df
from graph_vis.models import GraphVisRefugeeData


class Command(BaseCommand):
    '''
    python manage.py add_data "file_path"
    '''

    help = "Add pandas dataframe to our existing database"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args: any, **options: any):
        file_path = options['file_path']
        pop_df = construct_df(file_path)
        with sqlite3.connect('db.sqlite3') as con:
            pop_df.to_sql(GraphVisRefugeeData._meta.db_table,
                          con=con, if_exists="replace", index=False, dtype={'id': 'INTEGER PRIMARY KEY', 'total_refugees': 'INT'})
