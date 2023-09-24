import logging


class SonnenStorage:
    def __init__(self, system_setup="Basic"):
        """
        Initialize a SonnenStorage system with default or provided system setup.

        :param system_setup: The system setup ("Basic", "Standard", or "Pro") based on customer requirements (default is "Basic").
        """
        self.inverter = self.Inverter()
        self.controller = self.Controller()

        # Set inverter max power and battery module max power
        self.battery_modules = [self.BatteryModule() for _ in range(self.get_max_battery_modules(system_setup))]
        self.power_command = 0.0

        self.logger = logging.getLogger("SonnenStorage")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())

        self.logger.info(f"Initializing SonnenStorage with system setup: {system_setup}")

    def get_max_battery_modules(self, system_setup):
        if system_setup == "Basic":
            return 2
        elif system_setup == "Standard":
            return 3
        elif system_setup == "Pro":
            return 5
        else:
            raise ValueError("Invalid system setup")

    def manage_power(self, pv_panel, house, grid):

        surplus_pv = pv_panel.power - house.power_in

        if surplus_pv > 0:
            # Charge the battery if there is surplus PV production
            max_charge_power = min(surplus_pv, self.inverter.get_max_power())
            self.controller.charge_battery(max_charge_power)

            # Update the inverter's power output
            self.inverter.power_inverter = max_charge_power

            # Remaining surplus power after charging the battery
            remaining_surplus = surplus_pv - max_charge_power

            # If there's still surplus power, it can be sold to the provider
            if remaining_surplus > 0:
                grid.sold_power(remaining_surplus)

        else:
            # Discharge the battery to supply power to the house
            max_discharge_power = min(-surplus_pv, self.inverter.get_max_power())
            self.controller.discharge_battery(max_discharge_power)

            # Update the inverter's power output
            self.inverter.power_inverter = -max_discharge_power

            # Remaining power needed after discharging the battery
            remaining_power_needed = house.power_in - pv_panel.power - max_discharge_power

            # If power is still needed, get it from the grid
            if remaining_power_needed > 0:
                max_grid_power = min(remaining_power_needed, self.inverter.get_max_power())
                grid.bought_power(max_grid_power)

    class Inverter:
        def __init__(self, max_power=5000.0, battery_voltage=48.0, battery_current=0.0, power_inverter=0.0,
                     grid_frequency=60.0, grid_voltage=120.0):
            self.max_power = max_power
            self.battery_voltage = battery_voltage
            self.battery_current = battery_current
            self.power_inverter = power_inverter
            self.grid_frequency = grid_frequency
            self.grid_voltage = grid_voltage

        def get_max_power(self):
            return self.max_power

        def get_battery_voltage(self):
            return self.battery_voltage

        def get_battery_current(self):
            return self.battery_current

        def get_power_inverter(self):
            return self.power_inverter

        def get_grid_frequency(self):
            return self.grid_frequency

        def get_grid_voltage(self):
            return self.grid_voltage

    class BatteryModule:
        def __init__(self, temperature=25.0, voltage=48.0, max_power=5000.0):
            self.temperature = temperature
            self.voltage = voltage
            self.max_power = max_power

        def get_temperature(self):
            return self.temperature

        def get_voltage(self):
            return self.voltage

        def get_max_power(self):
            return self.max_power

    class Controller:
        def __init__(self):
            self.battery_command = 0.0

        def charge_battery(self, power):
            self.battery_command = power

        def discharge_battery(self, power):
            self.battery_command = -power

        def get_power_from_grid(self, power):
            self.battery_command = -power

        def get_battery_command(self):
            return self.battery_command

    def set_power_command(self, command):
        self.power_command = command

    def get_power_command(self):
        return self.power_command

    def get_state(self):
        state = {
            "Inverter": {
                "Max Power": self.inverter.get_max_power(),
                "Battery Voltage": self.inverter.get_battery_voltage(),
                "Battery Current": self.inverter.get_battery_current(),
                "Power Inverter": self.inverter.get_power_inverter(),
                "Grid Frequency": self.inverter.get_grid_frequency(),
                "Grid Voltage": self.inverter.get_grid_voltage(),
            },
            "Battery Modules": [],
            "Controller": {},  # Remove "SomeValue" as it doesn't exist
            "Power Command": self.get_power_command(),
        }

        for module in self.battery_modules:
            state["Battery Modules"].append({
                "Temperature": module.get_temperature(),
                "Voltage": module.get_voltage(),
                "Max Power": module.get_max_power(),
            })

        return state

    def reset_state(self):
        # Reset the states of components to their initial values
        self.inverter = self.Inverter()
        self.controller = self.Controller()
        self.battery_modules = [self.BatteryModule() for _ in range(len(self.battery_modules))]
        self.power_command = 0.0
