from django.test import TestCase
from task.models import Task


class TaskTestCase(TestCase):

    def setUp(self):
        Task.objects.create(
                name="Diamond Theft",
                tags=['bitmasks', 'dp', 'greedy', 'math', 'sortings', 'two pointers'],
                count_solutions=502,
                numbers="1886E",
                index="E",
                complexity="1000",
                number_contest='1886'
        )

    def test_task_name(self):
        task = Task.objects.get(name='Diamond Theft')
        self.assertEquals(task.name, 'Diamond Theft')

    
