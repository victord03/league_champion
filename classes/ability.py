

class Ability:
    """Main class for abilities of Champions"""
    name: str
    cooldown: float
    description: str

    def __init__(self, info_dict: dict):
        self.name = info_dict["name"]
        self.cooldown = info_dict["cooldown"]
        self.description = info_dict["description"]
