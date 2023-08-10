class SharedInteraction:
    def __init__(self, timestamp, suspect_a, suspect_b, interaction_id):
        self.time = timestamp
        self.suspect_a = suspect_a #name
        self.suspect_b = suspect_b #name
        self.interaction_id = interaction_id
        self.interaction_content = None

    def __str__(self):
        return f"{self.timestamp} {self.suspect_a}-{self.suspect_b}:{self.interaction_id}"
    
    def get_text(self):
        return self.interaction_content
    
    def set_text(self, text):
        self.interaction_content = text

    def get_summary(self):
        if self.interaction_id != None:
            summary = f"Time: {self.time}\n"
            summary += f"Suspect A: {self.suspect_a}\n"
            summary += f"Suspect B: {self.suspect_b}\n"
            summary += f"Interaction ID: {self.interaction_id}\n"
            summary += f"Interaction content: \n{self.interaction_content}\n"
            return summary
        else:
            return "No interaction"
        
    def get_interaction_pair(self):
        info = f"Time: {self.time}\n"
        info += f"Suspect A: {self.suspect_a}\n"
        info += f"Suspect B: {self.suspect_b}\n"
        return info

    def get_interaction_id(self):
        return self.interaction_id