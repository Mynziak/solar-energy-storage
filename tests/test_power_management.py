import pytest
from components.photovoltaic_panel import PhotovoltaicPanel
from components.house import House
from components.grid import Grid
from components.storage import SonnenStorage


@pytest.mark.parametrize(
    "pv_power, house_power, grid_power, expected_inverter_power, expected_battery_charge, expected_grid_sold, expected_grid_bought, system_setup",
    [
        # Excess PV, charges battery in Basic setup
        (6000, 4000, 0, 2000, 1000, 0, 0, "Basic"),
        # House needs more power, discharges battery in Basic setup
        (4000, 6000, 0, -2000, -1000, 0, 0, "Basic"),
        # Balance between PV and house consumption in Basic setup
        (3000, 3000, 0, 0, 0, 0, 0, "Basic"),
        # House needs power from grid in Basic setup
        (3000, 2000, 1000, 1000, 0, 1000, 0, "Basic"),

        # Additional test cases for other system setups:
        (6000, 4000, 0, 2000, 1000, 0, 0, "Standard"),
        (4000, 6000, 0, -2000, -1000, 0, 0, "Standard"),
        (3000, 3000, 0, 0, 0, 0, 0, "Standard"),
        (3000, 2000, 1000, 1000, 0, 1000, 0, "Standard"),

        (6000, 4000, 0, 2000, 1000, 0, 0, "Pro"),
        (4000, 6000, 0, -2000, -1000, 0, 0, "Pro"),
        (3000, 3000, 0, 0, 0, 0, 0, "Pro"),
        (3000, 2000, 1000, 1000, 0, 1000, 0, "Pro"),
    ]
)
def test_power_management(pv_power, house_power, grid_power, expected_inverter_power, expected_battery_charge,
                          expected_grid_sold, expected_grid_bought, storage, system_setup):
    pv_panel = PhotovoltaicPanel(pv_power)
    house = House(house_power)
    grid = Grid(grid_power)

    # Configure the storage system (SonnenStorage)
    storage = SonnenStorage(system_setup)
    storage.inverter.max_power = 5000  # Set inverter max power
    storage.battery_modules[0].max_power = 1000  # Set battery module max power
    storage.manage_power(pv_panel, house, grid)


    # Assert the states of components match the expected values
    assert storage.inverter.get_power_inverter() == expected_inverter_power
    assert storage.battery_modules[0].get_max_power() == 1000
    assert grid.get_power_sold() == expected_grid_sold
    assert grid.get_power_bought() == expected_grid_bought
