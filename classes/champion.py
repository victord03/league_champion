from utils.constants import NEW_LINE as NL, TAB
from classes.ability import Ability
from data import champion_data


def create_champion(info_dict: dict):

    champion_variables = dict()

    champion_variables["name"] = info_dict["name"]

    champion_variables["passive"] = Ability(info_dict["abilities"]["passive"])
    champion_variables["q"] = Ability(info_dict["abilities"]["q"])
    champion_variables["w"] = Ability(info_dict["abilities"]["w"])
    champion_variables["e"] = Ability(info_dict["abilities"]["e"])
    champion_variables["r"] = Ability(info_dict["abilities"]["r"])

    champion_variables["hp"] = info_dict["hp"]

    champion_variables["level"] = info_dict["level"]
    champion_variables["xp"] = info_dict["xp"]
    champion_variables["xp_bar"] = info_dict["xp_bar"]

    champion_variables["melee"] = info_dict["melee"]
    champion_variables["attack_range"] = info_dict["attack_range"]
    champion_variables["attack_damage"] = info_dict["attack_damage"]
    champion_variables["attack_speed"] = info_dict["attack_speed"]

    champion_variables["ability_power"] = info_dict["ability_power"]

    champion_variables["cooldown_reduction"] = info_dict["cooldown_reduction"]

    champion_variables["movement_speed"] = info_dict["movement_speed"]

    return champion_variables


class Champion:
    """Main class for Champions (in-game characters)"""
    name: str

    passive: Ability
    q: Ability
    w: Ability
    e: Ability
    r: Ability

    hp_total: int
    hp_current: int

    level = int
    xp = int
    xp_bar = int

    melee: bool
    attack_range: int
    attack_damage: int
    attack_speed: int

    ability_power: int

    cooldown_reduction: float

    movement_speed: int

    def __init__(self, champion_variables: dict):

        self.name = champion_variables["name"]
        self.passive = champion_variables["passive"]
        self.q = champion_variables["q"]
        self.w = champion_variables["w"]
        self.e = champion_variables["e"]
        self.r = champion_variables["r"]

        self.hp_total = champion_variables["hp"]
        self.hp_current = self.hp_total

        self.level = champion_variables["level"]
        self.xp = champion_variables["xp"]
        self.xp_bar = champion_variables["xp_bar"]

        self.melee = champion_variables["melee"]
        self.range = champion_variables["attack_range"]
        self.attack_damage = champion_variables["attack_damage"]
        self.attack_speed = champion_variables["attack_speed"]

        self.ability_power = champion_variables["ability_power"]

        self.cooldown_reduction = champion_variables["cooldown_reduction"]

        self.movement_speed = champion_variables["movement_speed"]

    @classmethod
    def create_yasuo(cls):
        champion_variables = create_champion(champion_data.yasuo_info)
        return cls(champion_variables)

    @classmethod
    def create_vi(cls):
        champion_variables = create_champion(champion_data.vi_info)
        return cls(champion_variables)

    def display_info(self) -> str:

        name = f"{NL}{self.name}"
        show_passive = f"{NL}{TAB}Passive: {self.passive.name}"
        show_q = f"{NL}{TAB}Q: {self.q.name}"
        show_w = f"{NL}{TAB}W: {self.w.name}"
        show_e = f"{NL}{TAB}E: {self.e.name}"
        show_r = f"{NL}{TAB}R: {self.r.name}"

        show_hp = f"{NL}{TAB}HP: {self.hp_current}/{self.hp_total}"

        level = f"{NL}{TAB}Level: {self.level}"
        xp = f"{NL}{TAB}XP: {self.xp}"

        melee = f"{NL}{TAB}Melee: {self.melee}"
        attack_damage = f"{NL}{TAB}Damage: {self.attack_damage}"
        attack_speed = f"{NL}{TAB}Attack Speed: {self.attack_speed}"

        ability_power = f"{NL}{TAB}Ability Power: {self.ability_power}"

        cooldown_reduction = f"{NL}{TAB}Cooldown Reduction: {self.cooldown_reduction}"

        ms = f"{NL}{TAB}Movement Speed: {self.movement_speed}"

        show_level_related = level + xp
        show_damage_related = melee + attack_damage + attack_speed

        the_rest = show_hp + show_level_related + show_damage_related + ability_power + cooldown_reduction + ms

        return name + the_rest + show_passive + show_q + show_w + show_e + show_r
