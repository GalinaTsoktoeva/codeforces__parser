import pytest

from task.services import Codeforces


@pytest.fixture()
def some_api_codeforces():
    con = Codeforces()
    return con


# @pytest.fixture()
# def some_task():
#     new_task = Task.objects.create(
#         name="Diamond Theft",
#         tags=['bitmasks', 'dp', 'greedy', 'math', 'sortings', 'two pointers'],
#         count_solutions=502,
#         numbers="1886E",
#         index="E",
#         complexity="1000",
#         number_contest='1886'
#     )
#     return new_task
