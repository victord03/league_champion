from utils.constants import NEW_LINE as NL, TAB
from classes.ability import Ability
from data import champion_data


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

    def __init__(
        self,
        name,
        passive,
        q,
        w,
        e,
        r,
        hp,
        level,
        xp,
        xp_bar,
        melee,
        attack_range,
        attack_damage,
        attack_speed,
        ability_power,
        cooldown_reduction,
        movement_speed,
    ):

        self.name = name
        self.passive = passive
        self.q = q
        self.w = w
        self.e = e
        self.r = r

        self.hp_total = hp
        self.hp_current = hp

        self.level = level
        self.xp = xp
        self.xp_bar = xp_bar

        self.melee = melee
        self.range = attack_range
        self.attack_damage = attack_damage
        self.attack_speed = attack_speed
        self.ability_power = ability_power
        self.cooldown_reduction = cooldown_reduction

        self.movement_speed = movement_speed

    @classmethod
    def create_yasuo(cls):

        info = champion_data.yasuo_info

        name = info["name"]

        passive = Ability(info["abilities"]["passive"])
        q = Ability(info["abilities"]["q"])
        w = Ability(info["abilities"]["w"])
        e = Ability(info["abilities"]["e"])
        r = Ability(info["abilities"]["r"])

        hp = info["hp"]

        level = info["level"]
        xp = info["xp"]
        xp_bar = info["xp_bar"]

        melee = info["melee"]
        attack_range = info["attack_range"]
        attack_damage = info["attack_damage"]
        attack_speed = info["attack_speed"]

        ability_power = info["ability_power"]

        cooldown_reduction = info["cooldown_reduction"]

        movement_speed = info["movement_speed"]

        return cls(
            name,
            passive,
            q,
            w,
            e,
            r,
            hp,
            level,
            xp,
            xp_bar,
            melee,
            attack_range,
            attack_damage,
            attack_speed,
            ability_power,
            cooldown_reduction,
            movement_speed,
        )

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
