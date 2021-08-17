from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from faker import Faker


fake = Faker()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, default=1, choices=range(1, 11),
                            help='Define amount of users you`d like to create from 1 to 10')

    def handle(self, *args, **kwargs):
        User = get_user_model()
        amount = kwargs['amount']
        upd = []
        for i in range(amount):
            upd.append(User(username=fake.name(), email=fake.email(), password=fake.password()))
        User.objects.bulk_create(upd)
