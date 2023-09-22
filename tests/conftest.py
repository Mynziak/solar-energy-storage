# In conftest.py
import pytest
from components.storage import SonnenStorage

@pytest.fixture
def storage(system_setup):
    storage_system = SonnenStorage(system_setup)
    yield storage_system
    # Teardown: Reset the states of components after the test
    storage_system.reset_state()
