from dataclasses import dataclass

@dataclass
class House:
    power_in: int = 0
    voltage: int = 120
    frequency: int = 60
    current: int = 0
