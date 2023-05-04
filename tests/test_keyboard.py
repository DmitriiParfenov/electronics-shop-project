import pytest


def test_keyboard_repr(keyboard_example):
    assert repr(keyboard_example) == "Keyboard('Dark Project KD87A', 9600, 5)"


@pytest.mark.parametrize("index, expected", [(0, 'Класс Keyboard:'),
                                             (1, 'Name = Dark Project KD87A'),
                                             (2, 'price = 9600'),
                                             (3, 'quantity = 5'),
                                             (4, 'total_price = 48000'),
                                             (5, 'Language = EN')])
def test_keyboard_str(keyboard_example, index, expected):
    result = []
    list_str_phone = str(keyboard_example).split('\n')
    for elem in list_str_phone:
        result.append(elem)
    assert result[index] == expected


def test_keyboard_getter(keyboard_example):
    assert keyboard_example.language == 'EN'


def test_keyboard_setter(keyboard_example):
    with pytest.raises(AttributeError):
        keyboard_example.language = 'JA'


def test_keyboard_change_lang(keyboard_example):
    keyboard_example.change_lang()
    keyboard_example.change_lang().change_lang().change_lang().change_lang()
    assert keyboard_example.language == 'RU'
