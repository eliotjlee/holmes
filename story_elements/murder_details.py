class MurderDetails:
    def __init__(self, murder_description, murder_setting, murder_weapon, murder_action):
        self.murder_description = murder_description
        self.murder_setting = murder_setting
        self.murder_weapon = murder_weapon
        self.murder_action = murder_action

    def __getstate__(self):
        # Return the object's state as a dictionary
        return {
            'murder_description': self.murder_description,
            'murder_setting': self.murder_setting,
            'murder_weapon': self.murder_weapon,
            'murder_action': self.murder_action
        }

    def __setstate__(self, state):
        # Restore the object's state from the given dictionary
        self.murder_description = state['murder_description']
        self.murder_setting = state['murder_setting']
        self.murder_weapon = state['murder_weapon']
        self.murder_action = state['murder_action']
