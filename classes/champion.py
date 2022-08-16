from utils.constants import NEW_LINE as NL, TAB


class Ability:
    name: str
    cooldown: int

    def __init__(self, name: str):
        self.name = name


class Champion:
    name: str
    passive: Ability
    q: Ability
    w: Ability
    e: Ability
    r: Ability

    def __init__(self, name, passive, q, w, e, r):
        self.name = name
        self.passive = passive
        self.q = q
        self.w = w
        self.e = e
        self.r = r

    @classmethod
    def create_yasuo(cls):

        name = "Yasuo"
        passive = Ability("Way of the Wanderer")
        q = Ability("Steel Tempest")
        w = Ability("Wind Wall")
        e = Ability("Sweeping Blade")
        r = Ability("Last Breath")

        return cls(name, passive, q, w, e, r)

    def display_info(self) -> str:

        name = f"{NL}{self.name}"
        show_passive = f"{NL}{TAB}Passive: {self.passive.name}"
        show_q = f"{NL}{TAB}Q: {self.q.name}"
        show_w = f"{NL}{TAB}W: {self.w.name}"
        show_e = f"{NL}{TAB}E: {self.e.name}"
        show_r = f"{NL}{TAB}R: {self.r.name}"

        return name + show_passive + show_q + show_w + show_e + show_r
