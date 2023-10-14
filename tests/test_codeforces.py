def test_codeforces(some_api_codeforces):
    assert some_api_codeforces.name == "codeforces_conn"
    assert some_api_codeforces.url == 'https://codeforces.com/api/'


def test_get_tasks(some_api_codeforces):
    result = some_api_codeforces.get_tasks(query="../data.json")
    print(result)
    assert result == 1
