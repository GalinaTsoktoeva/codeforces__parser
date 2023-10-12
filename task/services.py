import json
from abc import ABC, abstractmethod

import requests

from task.models import Task


class API(ABC):

    @abstractmethod
    def get_tasks(self):
        pass


class Codeforces(API):

    def __init__(self):
        self.name = 'codeforces_conn'
        self.url = 'https://codeforces.com/api/'

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"

    def __str__(self):
        return f"{self.name}"

    def get_tasks(self):

        """Парсинг задач с сайта CODEFORCES"""

        new_tasks_list = []
        request = self.get_json_from_codeforces(query='problemset.problems')
        parsed = json.loads(request.content)
        request.close()

        if parsed.get('status') == "OK":
            # данные по задаче
            tasks_data = parsed['result']['problems']
            # данные по количеству решений
            solutions = parsed['result']['problemStatistics']
            for task in tasks_data:
                if task:
                    # фильтруем данные по номеру контеста и индекса, выбираем количество решений
                    filtering = list(filter(lambda x: (task['contestId'] == x.get('contestId')) and task['index'] == x.get('index'), solutions))
                    if filtering:
                        solved = filtering[0].get('solvedCount')

                    # смотрим, чтобы задачи не было в базе данных
                    task_exists = task is not None and Task.objects.filter(name=task.get('name')).exists()
                    if task_exists:
                        continue
                        #raise Exception(f"Такая задача есть {task.get('name')} {task.get('contestId')}{task.get('index')} !!!")

                    # заполняем бд
                    new_tasks_list.append(
                        Task(
                        name=task['name'],
                        tags=task['tags'],
                        complexity=task.get('rating') if task.get('rating') is not None else 0,
                        numbers=str(task.get('contestId')) + task.get('index'),
                        count_solutions=solved if solved is not None else 0,
                        index = task.get('index'),
                        number_contest = task.get('contestId')
                    ))

            Task.objects.bulk_create(new_tasks_list)
        #print(tasks_data)

    def get_json_from_codeforces(self, params={}, query=''):
        try:
            response = requests.get(self.url + query)
            return response
        except ConnectionError:
            print('Connection Error')
        except requests.HTTPError:
            print('HTTP error')
        except TimeoutError:
            print('Timeout Error')
        return {}
