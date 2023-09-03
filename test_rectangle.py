from rectangle import *
from tud_test_base import *
import pytest

# @pytest.fixture
# def radius():
#     radius = 5
#     return radius

def test_get_width_input():    
    set_keyboard_input([4])
    get_width_input()
    output = get_display_output()

    assert output == [
        "key in width: ",
    ]

def test_get_length_input():
    set_keyboard_input([5])
    get_length_input()
    output = get_display_output()

    assert output == [
        "key in length: ",
    ]

@pytest.mark.parametrize("width,length,area", [(4, 5, 20), (6, 7, 42), (6, 8, 48)])
def test_calculate(width, length, area):
    actual_area = calculate(width, length)
    assert actual_area == area

def test_main():
    set_keyboard_input([4])
    set_keyboard_input([5])
    main()
    output = get_display_output()

    assert output == [
        "key in width: ",
        "key in length: ",
        "Area: 20"
    ]
