import json

from task.services import Codeforces


def test_codeforces():
    some_api_codeforces = Codeforces().get_tasks()
    assert some_api_codeforces.name == "codeforces_conn"
    assert some_api_codeforces.url == 'https://codeforces.com/api/'


# def test_get_tasks():
#     path_file = "../data.json"
#     with open(path_file, "r", encoding='utf-8') as file:
#         data1 = json.load(file)
#     result = some_api_codeforces.get_tasks(query="../data.json")
#
#     assert len(result) == len(data1)
