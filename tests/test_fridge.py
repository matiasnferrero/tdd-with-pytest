""" Tests certain methods in the Fridge class"""

import pytest
from app.fridge import Fridge


@pytest.fixture(scope="function")
def loaded_fridge() -> Fridge:
    """Setup a loaded fridge (fix state) for running the tests"""
    return Fridge(inverter="my_fridge", load=10, temp=5, base_speed=500)


def test_get_temp(loaded_fridge):
    """Tests that get_temp actually fetches the property 'temp' (temp can be any value)"""
    assert loaded_fridge.get_temp() == loaded_fridge.temp


def test_get_fan_speed_setting(loaded_fridge):
    """Tests that the interface get_fan_speed_settings works as intended"""
    assert loaded_fridge.get_fan_speed_setting() == 750


