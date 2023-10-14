from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Task(models.Model):

    tags = models.CharField(max_length=250, verbose_name="тема")
    count_solutions = models.IntegerField(default=0, verbose_name='количество решений задач', **NULLABLE)
    name = models.CharField(max_length=250, verbose_name='название')
    numbers = models.CharField(max_length=50, unique=True, verbose_name='номер задачи')
    index = models.CharField(max_length=20, verbose_name='индекс задачи', **NULLABLE)
    complexity = models.CharField(max_length=100, verbose_name='сложность')
    number_contest = models.CharField(max_length=50, verbose_name='номер контеста', **NULLABLE)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f"{self.name} {self.numbers}"
