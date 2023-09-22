class Grid:
    def __init__(self, power_sold=0.0, power_bought=0.0, voltage=0.0, frequency=60.0):
        """
        Initialize a Grid connection with default or provided parameters.

        :param power_sold: The amount of power sold to the utility provider in Watts (default is 0.0W).
        :param power_bought: The amount of power bought from the utility provider in Watts (default is 0.0W).
        :param voltage: The grid voltage in Volts (default is 0.0V).
        :param frequency: The grid frequency in Hertz (default is 60.0Hz).
        """
        self.power_sold = power_sold
        self.power_bought = power_bought
        self.voltage = voltage
        self.frequency = frequency

    def get_power_sold(self):
        """
        Get the amount of power sold to the utility provider.

        :return: The power sold in Watts.
        """
        return self.power_sold

    def get_power_bought(self):
        """
        Get the amount of power bought from the utility provider.

        :return: The power bought in Watts.
        """
        return self.power_bought

    def get_voltage(self):
        """
        Get the grid voltage.

        :return: The grid voltage in Volts.
        """
        return self.voltage

    def get_frequency(self):
        """
        Get the grid frequency.

        :return: The grid frequency in Hertz.
        """
        return self.frequency

    def set_power_sold(self, power_sold):
        """
        Set the amount of power sold to the utility provider.

        :param power_sold: The new power sold in Watts.
        """
        self.power_sold = power_sold

    def set_power_bought(self, power_bought):
        """
        Set the amount of power bought from the utility provider.

        :param power_bought: The new power bought in Watts.
        """
        self.power_bought = power_bought

    def set_voltage(self, voltage):
        """
        Set the grid voltage.

        :param voltage: The new grid voltage in Volts.
        """
        self.voltage = voltage

    def set_frequency(self, frequency):
        """
        Set the grid frequency.

        :param frequency: The new grid frequency in Hertz.
        """
        self.frequency = frequency
