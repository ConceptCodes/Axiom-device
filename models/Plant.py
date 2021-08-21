from dataclasses import dataclass

@dataclass
class Plant:
    """ object to represent a plant in garden """
    name: str
    ideal_tmp: float
    light_cycle: dict
    growth_duration: int

    def get_light_cycle(self) -> dict:
        """ returns current plants light cycle """
        return self.light_cycle

    def get_growth_duration(self) -> int:
        """ returns current plants growth duration """
        return self.growth_duration

    def get_name(self) -> str:
        """ returns current plants name """
        return self.name
