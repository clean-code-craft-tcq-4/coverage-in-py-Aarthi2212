import constants as const
class Battery:
    def __init__(self) -> None:
        self.set_cooling_type(const.PASSIVE_COOLING)
    
    def set_cooling_type(self, cooling_type):
        self.__setattr__(const.COOLING_TYPE, cooling_type)
    
    def to_dictionary(self):
        return self.__dict__