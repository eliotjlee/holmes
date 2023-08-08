from story_elements.murder_details import MurderDetails
from story_elements.victim import Victim

class Plot:
    def __init__(self, summary, victim: Victim, murder_details: MurderDetails):
        self.summary = summary
        self.victim = victim
        self.murder_details = murder_details

    def get_info(self):
        info = f"Case Summary: {self.summary}\n"
        info += f"Victim: {self.victim.name}\nBio: {self.victim.bio}\n"
        info += f"Murder Details: {self.murder_details.murder_description}\n"
        info += f"Murder Setting: {self.murder_details.murder_setting}\n"
        info += f"Murder Weapon: {self.murder_details.murder_weapon}\n"
        return info