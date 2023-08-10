class Timestamp:
    def __init__(self, time, suspect_actions):
        self.time = time
        self.suspect_actions = suspect_actions  # This is a list where indices 0-3 correspond to suspects 1-4

    def get_time(self):
        return self.time

    def get_suspect_actions(self):
        return self.suspect_actions

    def __getstate__(self):
        # Return the object's state as a dictionary
        return {
            'time': self.time,
            'suspect_actions': self.suspect_actions
        }

    def __setstate__(self, state):
        # Restore the object's state from the given dictionary
        self.time = state['time']
        self.suspect_actions = state['suspect_actions']
