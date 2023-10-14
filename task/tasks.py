from celery import shared_task

from task.services import Codeforces


@shared_task
def codeforces_parser():
    new_conn = Codeforces()
    new_conn.get_tasks()
