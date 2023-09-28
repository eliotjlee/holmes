class MurderDetails:
    def __init__(self, murder_description, murder_setting, murder_weapon, murder_action):
        """
        Initializes a MurderDetails instance with a description, setting, weapon, and action related to the murder.

        :param murder_description: A string describing the murder.
        :param murder_setting: A string describing the setting in which the murder occurred.
        :param murder_weapon: A string describing the weapon used in the murder.
        :param murder_action: A string describing the action that constituted the murder.
        """
        self.murder_description = murder_description
        self.murder_setting = murder_setting
        self.murder_weapon = murder_weapon
        self.murder_action = murder_action

    def __getstate__(self):
        """
        Return the object's state as a dictionary
        """
        return {
            'murder_description': self.murder_description,
            'murder_setting': self.murder_setting,
            'murder_weapon': self.murder_weapon,
            'murder_action': self.murder_action
        }

    def __setstate__(self, state):
        """
        Restore the object's state from the given dictionary
        """
        self.murder_description = state['murder_description']
        self.murder_setting = state['murder_setting']
        self.murder_weapon = state['murder_weapon']
        self.murder_action = state['murder_action']
