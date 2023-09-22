class House:
    def __init__(self, power_in=0.0, voltage=120.0, frequency=60.0, current=0.0):
        """
        Initialize a House measurement point with default or provided parameters.

        :param power_in: The amount of power going into the house in Watts (default is 0.0W).
        :param voltage: The voltage of the house grid in Volts (default is 120.0V).
        :param frequency: The frequency of the house grid in Hertz (default is 60.0Hz).
        :param current: The current flowing into the house in Amps (default is 0.0A).
        """
        self.power_in = power_in
        self.voltage = voltage
        self.frequency = frequency
        self.current = current

    def get_power_in(self):
        """
        Get the amount of power going into the house.

        :return: The power going into the house in Watts.
        """
        return self.power_in

    def get_voltage(self):
        """
        Get the voltage of the house grid.

        :return: The house grid voltage in Volts.
        """
        return self.voltage

    def get_frequency(self):
        """
        Get the frequency of the house grid.

        :return: The house grid frequency in Hertz.
        """
        return self.frequency

    def get_current(self):
        """
        Get the current flowing into the house.

        :return: The current flowing into the house in Amps.
        """
        return self.current

    def set_power_in(self, power_in):
        """
        Set the amount of power going into the house.

        :param power_in: The new power going into the house in Watts.
        """
        self.power_in = power_in

    def set_voltage(self, voltage):
        """
        Set the voltage of the house grid.

        :param voltage: The new house grid voltage in Volts.
        """
        self.voltage = voltage

    def set_frequency(self, frequency):
        """
        Set the frequency of the house grid.

        :param frequency: The new house grid frequency in Hertz.
        """
        self.frequency = frequency

    def set_current(self, current):
        """
        Set the current flowing into the house.

        :param current: The new current flowing into the house in Amps.
        """
        self.current = current
