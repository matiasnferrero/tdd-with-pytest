"""This class was made just for testing its methods with pytest"""

class Fridge(object):
    """Emulates a real fridge!"""

    max_load = 20

    def __init__(self, inverter, load, temp, base_speed):

        self.load = load
        self.temp = temp
        self._inverter = inverter
        self._base_speed = base_speed

    def get_temp(self):
        """Provides the temperature reading"""
        return self.temp

    def _fan_speed_factor(self):
        """Calculate fan speed factor"""

        _fan_speed_factor = (self.max_load + self.load) / self.max_load
        return _fan_speed_factor

    def get_fan_speed_setting(self):
        """Provides the fan speed settings"""

        _fan_speed_setting = self._base_speed * self._fan_speed_factor()
        print(_fan_speed_setting)
        return _fan_speed_setting
