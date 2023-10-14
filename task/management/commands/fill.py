
from django.core.management.base import BaseCommand

from task.services import Codeforces


class Command(BaseCommand):

    def handle(self, *args, **options):
        new_conn = Codeforces()
        new_conn.get_tasks('https://codeforces.com/api/problemset.problems/')
