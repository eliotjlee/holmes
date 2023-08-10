class Timestamp:
    def __init__(self, time, suspect_actions):
        self.time = time
        self.suspect_actions = suspect_actions  # This is a list where indices 0-3 correspond to suspects 1-4

    def get_time(self):
        return self.time

    def get_suspect_actions(self):
        return self.suspect_actions