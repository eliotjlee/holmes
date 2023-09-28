class Victim:
    """
    The Victim class represents a victim character in the story.
    It holds the victim's name and biographical information.

    Attributes:
        name (str): The name of the victim.
        bio (str): The biographical information of the victim.

    Methods:
        __getstate__() -> dict:
            Prepares a serializable dictionary of the object's state for pickling.

        __setstate__(state: dict) -> None:
            Restores the object's state from the provided dictionary during unpickling.
    """

    def __init__(self, name, bio):
        """
        Initializes a new instance of the Victim class with the given name and bio.

        Parameters:
            name (str): The name of the victim.
            bio (str): The biographical information of the victim.
        """
        self.name = name
        self.bio = bio

    def __getstate__(self):
        """
        Prepares a serializable dictionary of the object's state for pickling.
        This method is called during the pickling process.

        Returns:
            state (dict): A dictionary containing the object's state.
        """
        return {
            'name': self.name,
            'bio': self.bio
        }

    def __setstate__(self, state):
        """
        Restores the object's state from the provided dictionary during unpickling.
        This method is called during the unpickling process.

        Parameters:
            state (dict): A dictionary containing the object's state.
        """
        self.name = state['name']
        self.bio = state['bio']
