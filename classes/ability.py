

class Ability:
    """Main class for abilities of Champions"""
    name: str
    cooldown: float
    description: str

    def __init__(self, name: str, cooldown, description):
        self.name = name
        self.cooldown = cooldown
        self.description = description

    @classmethod
    def create_steel_tempest(cls):

        name = "Steel Tempest"
        cooldown = 4
        description = "Pierces forward using sword, damaging all enemies in a line."
        return cls(name, cooldown, description)
