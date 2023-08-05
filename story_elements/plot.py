from story_elements.murder_details import MurderDetails
from story_elements.victim import Victim

class Plot:
    def __init__(self, summary, victim: Victim, murder_details: MurderDetails):
        self.summary = summary
        self.victim = victim
        self.murder_details = murder_details