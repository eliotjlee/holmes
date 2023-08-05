class Timestamp:
    def __init__(self, time, suspect_actions):
        self.time = time
        self.suspect_actions = suspect_actions  # This is a dictionary mapping each suspect to their action