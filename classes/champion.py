from utils.constants import NEW_LINE as NL, TAB
from classes.ability import Ability


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

        name = "Yasuo"

        passive = Ability(
            name="Way of the Wanderer",
            cooldown=0.0,
            description="Yasuo passively creates a shield while walking or dashing. Blocks the next incoming damage."
        )

        q = Ability(
            name="Steel Tempest",
            cooldown=5.0,
            description="Pierces forward using sword, damaging all enemies in a line."
        )

        w = Ability(
            name="Wind Wall",
            cooldown=15.0,
            description="Creates a wall that blocks all projectiles that touch it."
        )

        e = Ability(
            name="Sweeping Blade",
            cooldown=1.5,
            description="Yasuo dashes to target enemy unit, dealing damage and allowing for alternate Q use."
        )

        r = Ability(
            name="Last Breath",
            cooldown=36.0,
            description="Yasuo teleports to target airborne enemy units, holding them in place and dealing damage."
        )

        hp = 100

        level = 1
        xp = 0
        xp_bar = int()

        melee = True
        attack_range = 1
        attack_damage = 40
        attack_speed = 1.0
        ability_power = 0
        cooldown_reduction = 0.0
        movement_speed = 1.0

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
