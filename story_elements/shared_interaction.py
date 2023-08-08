class SharedInteraction:
    def __init__(self, timestamp, suspect_a, suspect_b, interaction_id):
        self.timestamp = timestamp
        self.suspect_a = suspect_a
        self.suspect_b = suspect_b
        self.interaction_id = interaction_id

    def __str__(self):
        return f"{self.timestamp} {self.suspect_a}-{self.suspect_b}:{self.interaction_id}"

