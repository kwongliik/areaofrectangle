from radius2 import *
from tud_test_base import *
import pytest

# @pytest.fixture
# def radius():
#     radius = 5
#     return radius

def test_read_input():    
    set_keyboard_input([4])
    read_input()
    output = get_display_output()

    assert output == [
        "key in radius: ",
    ]

@pytest.mark.parametrize("radius,area", [(4, 50.272), (5, 78.55), (6, 113.112)])
def test_calculate(radius, area):
    actual_area = calculate(radius)
    assert actual_area == area

def test_main():
    set_keyboard_input([4])
    main()
    output = get_display_output()

    assert output == [
        "key in radius: ",
        "Area: 50.272"
    ]
