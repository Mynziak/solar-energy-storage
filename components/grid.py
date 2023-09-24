from dataclasses import dataclass

@dataclass
class Grid:
    sold_power: int = 0
    bought_power: int = 0
    voltage: int = 0
    frequency: float = 60.0
