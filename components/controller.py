class Controller:
    def __init__(self):
        # Initialize controller state and parameters as needed
        self.battery_power = 0.0  # Current battery power in Watts
        self.grid_power = 0.0  # Current power obtained from the grid in Watts

    def charge_battery(self, power):
        """
        Charge the battery with the specified power.

        :param power: The power to be used for charging in Watts.
        """
        # Implement logic to charge the battery
        self.battery_power += power

    def discharge_battery(self, power):
        """
        Discharge the battery to supply power to the house.

        :param power: The power to be discharged in Watts.
        """
        # Implement logic to discharge the battery
        if self.battery_power >= power:
            self.battery_power -= power
        else:
            # Not enough battery power, obtain from the grid
            power_from_grid = power - self.battery_power
            self.grid_power += power_from_grid
            self.battery_power = 0.0

    def get_power_from_grid(self, power):
        """
        Get power from the grid to supply to the house or charge the battery.

        :param power: The power to be obtained from the grid in Watts.
        """
        # Implement logic to get power from the grid
        self.grid_power += power

    def get_state(self):
        """
        Get the current state of the controller.

        :return: A dictionary containing the current state information.
        """
        state = {
            "BatteryPower": self.battery_power,
            "GridPower": self.grid_power,
        }
        return state

    # Add more methods for Controller functionality as needed
