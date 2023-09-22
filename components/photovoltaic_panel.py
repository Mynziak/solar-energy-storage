class PhotovoltaicPanel:
    def __init__(self, initial_power=0.0, voltage=0.0, current=0.0):
        """
        Initialize a PhotovoltaicPanel with default or provided parameters.

        :param initial_power: The initial amount of power the PV panel is producing in Watts (default is 0.0W).
        :param voltage: The voltage that the PV panel is producing in Volts (default is 0.0V).
        :param current: The current that the PV panel is producing in Amps (default is 0.0A).
        """
        self.power = initial_power
        self.voltage = voltage
        self.current = current

    def get_power(self):
        """
        Get the amount of power the PV panel is producing.

        :return: The power produced in Watts.
        """
        return self.power

    def get_voltage(self):
        """
        Get the voltage produced by the PV panel.

        :return: The voltage in Volts.
        """
        return self.voltage

    def get_current(self):
        """
        Get the current produced by the PV panel.

        :return: The current in Amps.
        """
        return self.current

    def set_power(self, power):
        """
        Set the amount of power produced by the PV panel.

        :param power: The new power produced in Watts.
        """
        self.power = power

    def set_voltage(self, voltage):
        """
        Set the voltage produced by the PV panel.

        :param voltage: The new voltage in Volts.
        """
        self.voltage = voltage

    def set_current(self, current):
        """
        Set the current produced by the PV panel.

        :param current: The new current in Amps.
        """
        self.current = current
