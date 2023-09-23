import pytest
from components.photovoltaic_panel import PhotovoltaicPanel
from components.house import House
from components.grid import Grid


@pytest.mark.parametrize(
    "pv_power, house_power, grid_power, expected_inverter_power, expected_battery_charge, expected_grid_sold, expected_grid_bought",
    [
        # Excess PV, charges battery in Basic setup
        (6000, 4000, 0, 2000, 1000, 0, 0),
        # House needs more power, discharges battery in Basic setup
        (4000, 6000, 0, -2000, -1000, 0, 0),
        # Balance between PV and house consumption in Basic setup
        (3000, 3000, 0, 0, 0, 0, 0),
        # House needs power from grid in Basic setup
        (3000, 2000, 1000, 1000, 0, 1000, 0),
    ]
)
def test_basic_power_management(pv_power, house_power, grid_power, expected_inverter_power, expected_battery_charge,
                                expected_grid_sold, expected_grid_bought, storage_basic):
    pv_panel = PhotovoltaicPanel(pv_power)
    house = House(house_power)
    grid = Grid(grid_power)

    storage_basic.manage_power(pv_panel, house, grid)
    print("Storage State after Power Management:", storage_basic.get_state())

    # Assert the states of components match the expected values
    assert storage_basic.inverter.get_power_inverter() == expected_inverter_power
    assert grid.get_power_sold() == expected_grid_sold
    assert grid.get_power_bought() == expected_grid_bought


@pytest.mark.parametrize(
    "pv_power, house_power, grid_power, expected_inverter_power, expected_battery_charge, expected_grid_sold, expected_grid_bought",
    [
        # Excess PV, charges battery in Basic setup
        (6000, 4000, 0, 2000, 1000, 0, 0),
        # House needs more power, discharges battery in Basic setup
        (4000, 6000, 0, -2000, -1000, 0, 0),
        # Balance between PV and house consumption in Basic setup
        (3000, 3000, 0, 0, 0, 0, 0),
        # House needs power from grid in Basic setup
        (3000, 2000, 1000, 1000, 0, 1000, 0),
    ]
)
def test_standart_power_management(pv_power, house_power, grid_power, expected_inverter_power, expected_battery_charge,
                                   expected_grid_sold, expected_grid_bought, storage_standart):
    pv_panel = PhotovoltaicPanel(pv_power)
    house = House(house_power)
    grid = Grid(grid_power)

    storage_standart.manage_power(pv_panel, house, grid)
    print("Storage State after Power Management:", storage_standart.get_state())

    # Assert the states of components match the expected values
    assert storage_standart.inverter.get_power_inverter() == expected_inverter_power
    assert grid.get_power_sold() == expected_grid_sold
    assert grid.get_power_bought() == expected_grid_bought


@pytest.mark.parametrize(
    "pv_power, house_power, grid_power, expected_inverter_power, expected_battery_charge, expected_grid_sold, expected_grid_bought",
    [
        # Excess PV, charges battery in Basic setup
        (6000, 4000, 0, 2000, 1000, 0, 0),
        # House needs more power, discharges battery in Basic setup
        (4000, 6000, 0, -2000, -1000, 0, 0),
        # Balance between PV and house consumption in Basic setup
        (3000, 3000, 0, 0, 0, 0, 0),
        # House needs power from grid in Basic setup
        (3000, 2000, 1000, 1000, 0, 1000, 0),
    ]
)
def test_pro_power_management(pv_power, house_power, grid_power, expected_inverter_power, expected_battery_charge,
                              expected_grid_sold, expected_grid_bought, storage_pro):
    pv_panel = PhotovoltaicPanel(pv_power)
    house = House(house_power)
    grid = Grid(grid_power)

    storage_pro.manage_power(pv_panel, house, grid)
    print("Storage State after Power Management:", storage_pro.get_state())

    # Assert the states of components match the expected values
    assert storage_pro.inverter.get_power_inverter() == expected_inverter_power
    assert grid.get_power_sold() == expected_grid_sold
    assert grid.get_power_bought() == expected_grid_bought
