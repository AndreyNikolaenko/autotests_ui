import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, 4, 5, -3, 7, 8, 9, -1])
def test_numbers(number: int):
    print(f'Number: {number}')
    assert number > 0


# Параметризация с перемножением
@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9), (4, 16), (5, -3)])
def test_several_numbers(number: int, expected: int):
    print(f'Number: {number}')
    assert number ** 2 == expected



@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chrome', 'firefox', 'webkit'])
def test_multiplication_of_numbers(os: str, browser: str):
    print(f'OS: {os}')
    assert len(os + browser) > 0


# Параметризация фикстур
@pytest.fixture(params=['chrome', 'firefox', 'webkit'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')


# Параметризация класса
@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card',])
    def test_user_with_operations(self, user: str, account: str):
        print(f'User with operation: {user}')

    def test_user_without_operations(self, user: str):
        print(f'User without operation: {user}')


#Параметризация с идентификатором

users = {
    '+78008008070': 'User_1',
    '+78008008080': 'User_2',
    '+78008008090': 'User_3'
}


@pytest.mark.parametrize('phone_number',
                         users.keys(),
                         ids = lambda phone_number: f'{phone_number}: {users[phone_number]}'
                         )
def test_identifiers(phone_number: str):
    ...


@pytest.mark.parametrize(
    "value",
    [1, pytest.param(2, marks=pytest.mark.skip(reason="Not supported")), 3]
)
def test_example(value):
    pass

@pytest.mark.parametrize(
    "input_value",
    [
        pytest.param(1, marks=pytest.mark.xfail(reason="Known issue with 1")),
        2,
        pytest.param(3, marks=pytest.mark.skip(reason="Feature not implemented for 3")),
    ]
)
def test_function(input_value):
    assert input_value != 1