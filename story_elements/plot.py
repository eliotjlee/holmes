from story_elements.murder_details import MurderDetails
from story_elements.victim import Victim

class Plot:
    def __init__(self, summary, victim: Victim, murder_details: MurderDetails, suspects):
        self.summary = summary
        self.victim = victim
        self.murder_details = murder_details
        self.suspects = suspects # list
        self.shared_interactions = [] #list of SharedInteraction objects - 10
        self.timeline = [] #list of Timestamp objects - 10

    def get_info(self):
        info = f"Case Summary: {self.summary}\n"
        info += f"Victim: {self.victim.name}\nBio: {self.victim.bio}\n"
        info += f"Murder Details: {self.murder_details.murder_description}\n"
        info += f"Murder Setting: {self.murder_details.murder_setting}\n"
        info += f"Murder Weapon: {self.murder_details.murder_weapon}\n"
        return info
    
    def get_id_to_suspect_dict(self):
        dict = {}
        for suspect in self.suspects:
            dict[suspect.id] = suspect
        return dict
    
    def get_name_to_suspect_dict(self):
        dict = {}
        for suspect in self.suspects:
            dict[suspect.name] = suspect
        return dict
    
    def get_summary(self):
        summary = self.get_info()
        id_to_suspect_dict = self.get_id_to_suspect_dict()

        summary += "\nSUSPECTS:"
        for i in range(1,5):
            suspect = id_to_suspect_dict[i]
            summary += f"\n\nsuspect_{i}:\n"
            summary += suspect.get_info()

        return summary
    
    def get_this_suspect_summary(self, i):
        this_suspect = self.suspects[i]
        summary = self.get_info

        summary += "\nSUSPECTS:"
        other_suspects = "\n\nOTHER SUSPECTS:\n\n"
        for suspect in self.suspects:
            if suspect == this_suspect:
                summary+= "\n\nYOU:\n"
                summary += suspect.get_info()
            else:
                other_suspects += suspect.get_info_no_guilty()
                other_suspects += "\n\n"
        summary += other_suspects

    
    def add_shared_interaction(self, interaction):
        self.shared_interactions.append(interaction)
        return
    
    def add_timestamp_to_timeline(self, timestamp):
        self.timeline.append(timestamp)
    
    def get_timeline(self):
        return self.timeline
    
    def get_suspect_name_to_action(self):
        # generate list of dictionaries (1 per timestamp) mapping a suspect's name to their action
        # useful for shared convo generation
        names_to_actions = []
        for timestamp in self.timeline:
            actions = {}
            timestamp_actions = timestamp.get_suspect_actions()
            i = 0
            for suspect in self.suspects:
                actions[suspect.name] = timestamp_actions[i]
                i += 1
            names_to_actions.append(actions)

        return names_to_actions
    
    def get_shared_interactions(self):
        return self.shared_interactions
                
  