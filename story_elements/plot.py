from typing import List, Dict
from story_elements.murder_details import MurderDetails
from story_elements.victim import Victim
from story_elements.suspect import Suspect  # Assuming you have a Suspect class
from story_elements.shared_interaction import SharedInteraction  # Assuming you have a SharedInteraction class
from story_elements.timestamp import Timestamp  # Assuming you have a Timestamp class


class Plot:
    """
    Passable object that acts as a wrapper for all story details (timeline, victims, details, etc.)
    """
    def __init__(self, summary: str, victim: Victim, murder_details: MurderDetails, suspects: List[Suspect]):
        """
        Initializes a Plot instance with a summary, victim, murder details, and a list of suspects.

        :param summary: A string summarizing the plot.
        :param victim: A Victim instance representing the victim in the plot.
        :param murder_details: A MurderDetails instance containing details of the murder.
        :param suspects: A list of Suspect instances representing the suspects in the plot.
        """
        self.summary = summary
        self.victim = victim
        self.murder_details = murder_details
        self.suspects = suspects  # list
        self.shared_interactions = []  # list of SharedInteraction objects - 10
        self.timeline = []  # list of Timestamp objects - 10

    def get_info(self) -> str:
        """
        Return basic plot info.
        """
        info = f"Case Summary: {self.summary}\n"
        info += f"Victim: {self.victim.name}\nBio: {self.victim.bio}\n"
        info += f"Murder Details: {self.murder_details.murder_description}\n"
        info += f"Murder Setting: {self.murder_details.murder_setting}\n"
        info += f"Murder Weapon: {self.murder_details.murder_weapon}\n"
        return info

    def get_id_to_suspect_dict(self) -> Dict[int, Suspect]:
        """
        Returns dictionary mapping id to Suspect object
        """
        return {suspect.id: suspect for suspect in self.suspects}

    def get_name_to_suspect_dict(self) -> Dict[str, Suspect]:
        """
        Returns dictionary mapping suspect name to Suspect object
        """
        return {suspect.name: suspect for suspect in self.suspects}

    def get_summary(self) -> str:
        """
        Returns longer plot summary (including suspect details)
        """
        summary = self.get_info()
        id_to_suspect_dict = self.get_id_to_suspect_dict()

        summary += "\nSUSPECTS:"
        for i in range(1, 5):
            suspect = id_to_suspect_dict[i]
            summary += f"\n\nsuspect_{i}:\n"
            summary += suspect.get_info()

        return summary

    def get_this_suspect_summary(self, i: int) -> str:
        """
        Returns a summary of the plot from a specific suspect's perspective; omits whether other suspects are
        innocent/guilty.
        """
        this_suspect = self.suspects[i]
        summary = self.get_info()

        summary += "\nSUSPECTS:"
        other_suspects = "\n\nOTHER SUSPECTS:\n\n"
        for suspect in self.suspects:
            if suspect == this_suspect:
                summary += "\n\nYOU:\n"
                summary += suspect.get_info()
            else:
                other_suspects += suspect.get_info_no_guilty()
                other_suspects += "\n\n"
        summary += other_suspects

        return summary

    def add_shared_interaction(self, interaction: SharedInteraction) -> None:
        """
        Add shared interaction to list
        """
        self.shared_interactions.append(interaction)

    def add_timestamp_to_timeline(self, timestamp: Timestamp) -> None:
        """
        Add timestamp to list
        """
        self.timeline.append(timestamp)

    def get_timeline(self) -> List[Timestamp]:
        """
        Return timeline
        """
        return self.timeline

    def get_suspect_name_to_action(self) -> List[Dict[str, str]]:
        """
        Generate list of dictionaries (1 per timestamp) mapping a suspect's name to their action
        useful for shared convo generation
        """
        names_to_actions = []
        for timestamp in self.timeline:
            actions = {}
            timestamp_actions = timestamp.get_suspect_actions()
            for i, suspect in enumerate(self.suspects):
                actions[suspect.name] = timestamp_actions[i]
            names_to_actions.append(actions)

        return names_to_actions

    def get_shared_interactions(self) -> List[SharedInteraction]:
        """
        return shared interactions
        """
        return self.shared_interactions

    def __getstate__(self) -> dict:
        """
        Return the object's state as a dictionary
        """
        return {
            'summary': self.summary,
            'victim': self.victim,
            'murder_details': self.murder_details,
            'suspects': self.suspects,
            'shared_interactions': self.shared_interactions,
            'timeline': self.timeline
        }

    def __setstate__(self, state: dict) -> None:
        """
        Restore the object's state from the given dictionary
        """
        self.summary = state['summary']
        self.victim = state['victim']
        self.murder_details = state['murder_details']
        self.suspects = state['suspects']
        self.shared_interactions = state['shared_interactions']
        self.timeline = state['timeline']
