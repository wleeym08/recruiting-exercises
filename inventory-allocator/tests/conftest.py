import sys
import os

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "../")))

import pytest
from src.shipments import InventoryAllocator

@pytest.fixture
def a():
    "Setting up testing fixture."
    return InventoryAllocator() 
