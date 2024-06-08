import pandas as pd
import time
import numpy as np
from django.core.management.base import BaseCommand

from memoflash_back.settings import BASE_DIR
from memo_cards.models import Card, Item, Topic


class Command(BaseCommand):
    help = 'Load the base information for the application'

    def handle(self, *args, **kwargs):
        init_hour = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f'Loading Cards... \n{init_hour}')
        topic = Topic.objects.get(id=1)
        df = pd.read_csv(f'{BASE_DIR}/src/word_families.csv')
        df.replace(np.nan, None, inplace=True)
        for index, row in df.iterrows():
            card = Card.objects.create(topic=topic)
            Item.objects.bulk_create(
                [
                    Item(
                        **{'title': 'noun', 'content': str(row['Nouns']).title(), 'comment': '', 'card': card}),
                    Item(**{'title': 'adjective', 'content': str(
                        row['Adjectives']).title(), 'comment': '', 'card': card}),
                    Item(
                        **{'title': 'verb', 'content': str(row['Verbs']).title(), 'comment': '', 'card': card}),
                    Item(
                        **{'title': 'adverb', 'content': str(row['Adverbs']).title(), 'comment': '', 'card': card})
                ])
        end_hour = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f'Yep... \n{end_hour}')
