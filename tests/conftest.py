# In conftest.py
import pytest
from components.storage import SonnenStorage


@pytest.fixture
def storage_basic():
    storage_system = SonnenStorage("Basic")
    yield storage_system
    # Reset the states of components after the test
    storage_system.reset_state()


@pytest.fixture
def storage_standart():
    storage_system = SonnenStorage("Standard")
    yield storage_system
    # Reset the states of components after the test
    storage_system.reset_state()


@pytest.fixture
def storage_pro():
    storage_system = SonnenStorage("Pro")
    yield storage_system
    # Reset the states of components after the test
    storage_system.reset_state()
