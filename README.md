python3 -m pytest tests/test_power_management.py

# Sonnen Storage Power Management

This project simulates power management for a Sonnen battery storage system based on different system setups and energy
inputs.

## Table of Contents

- [Introduction](#introduction)
- [Scenario Description](#scenario-description)
- [Components](#components)
- [Python Assessment Goal](#python-assessment-goal)
- [Running Tests](#running-tests)
- [Fibonacci Sequence Generator](#fibonacci-sequence-generator)
- [Advantages of Using Pytest Fixtures](#advantages-of-using-pytest-fixtures)
- [Integrating Machine Learning](#integrating-machine-learning)

## Introduction

Sonnen is a market leader in battery storage systems in Europe, known for its product, the sonnenBatterie (SB). This
project focuses on implementing a power management algorithm for the SB under different system setups.

## Scenario Description

The sonnenBatterie (SB) consists of three main components: an inverter, battery modules, and a controller. The project's
goal is to manage power flow based on photovoltaic (PV) input and household consumption. Key aspects of the scenario
include:

- Three system setups: Basic, Standard, and Pro, each with varying numbers of inverters, battery modules, and
  controllers.
- Prioritizing energy flow:
    - Charging the battery with surplus PV production.
    - Supplying power to the house.
    - Selling surplus power to the grid.
- Components include Photovoltaic Panels, Grid, House, Inverter, Battery Module (BMS), Storage, and EM Controller.

## Components

- **Photovoltaic Panel (PV):** Generates energy from sunlight, with properties like power, voltage, and current.
- **Grid:** Represents the connection between the house and the utility provider grid, with power, voltage, and
  frequency properties.
- **House:** Monitors power consumption, voltage, frequency, and current.
- **Inverter:** Controls power flow to the batteries, with properties like maximum power, battery voltage, and more.
- **Battery Module (BMS):** Represents battery packs with temperature, voltage, and maximum power properties.
- **Storage:** The sonnenBatterie storage system, with power command capabilities and access to internal component
  properties.
- **EM Controller:** Manages energy logic and issues commands to devices.

## Python Assessment Goal

The Python assessment goal is to implement a pytest test case to cover the power management algorithm for different
system setups (Basic, Standard, and Pro) using the provided components and specifications. The test cases ensure that
the power management logic follows the scenario description correctly.

## Running Tests

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/sonnen-storage-power-management.git

2. Run the Tests use the following command::

   ```bash
   python3 -m pytest tests/test_power_management.py
   

### Fibonacci sequence Generator
- Refer to the [Fibonacci](tests/fibonacci.py) for details.

   ```bash
   python3 -m pytest tests/fibonacci.py


### Advantages of Using Pytest Fixtures
Refer to the [Pytest advantages of fixtures](docs/pytest_advantages_of_fixtures.md) for details.

### Integrating Machine Learning
Refer to the [Integrating ML](docs/integrating_ml.md) for details.