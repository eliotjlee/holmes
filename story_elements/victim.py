class Victim:
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio


    def __getstate__(self):
        # Return the object's state as a dictionary
        return {
            'name': self.name,
            'bio': self.bio
        }

    def __setstate__(self, state):
        # Restore the object's state from the given dictionary
        self.name = state['name']
        self.bio = state['bio']
