from dataclasses import dataclass

@dataclass
class PhotovoltaicPanel:
    power: int = 0
    voltage: int = 0
    current: int = 0
