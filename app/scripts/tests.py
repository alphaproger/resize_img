import pytest
from app.scripts.resizefunc import resize_picture


'''
def setup():
    print('\n ===== ScriptsTest - setup method =====\n ')


def teardown():
    print('\n ===== ScriptsTest - teardown method =====\n')
'''


def test_type_error():
    with pytest.raises(TypeError):
        resize_picture('', 1, 34)


def test_value_error():
    with pytest.raises(ValueError):
        resize_picture("It's name", 0)


def test_duplicated():
    assert resize_picture('1417265282-6037567-www.nevseoboi.com.ua.jpg', 300, 300)[0] == \
           '04a503d1dc5ce4bb4f1c2097e6929837_300x300.jpg'

