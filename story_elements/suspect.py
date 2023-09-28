class Suspect:
    def __init__(self, name: str, bio: str, tags: list, victim_connection: str, guilty: bool, id: int):
        """
        Initializes a Suspect instance with a name, bio, tags, victim connection, guilt status, and ID.

        :param name: A string representing the name of the suspect.
        :param bio: A string containing biographical information about the suspect.
        :param tags: A list of strings representing tags associated with the suspect.
        :param victim_connection: A string describing the suspect's connection to the victim.
        :param guilty: A boolean indicating whether the suspect is guilty.
        :param id: An integer representing the ID of the suspect.
        """
        self.name = name
        self.bio = bio
        self.tags = tags
        self.victim_connection = victim_connection
        self.guilty = guilty
        self.id = id
        self.memory_path = ""

    def get_info(self) -> str:
        """
        Returns a string containing information about the suspect, including the guilt status.
        """
        info = f"Name: {self.name}\n"
        info += f"Bio: {self.bio}\n"
        info += f"Tags: {self.tags}\n"
        info += f"Victim connection: {self.victim_connection}\n"
        info += f"Guilty: {self.guilty}\n"
        return info

    def get_info_no_guilty(self) -> str:
        """
        Returns a string containing information about the suspect, excluding the guilt status.
        """
        info = f"Name: {self.name}\n"
        info += f"Bio: {self.bio}\n"
        info += f"Tags: {self.tags}\n"
        info += f"Victim connection: {self.victim_connection}\n"
        return info

    def __getstate__(self) -> dict:
        """
        Returns the object's state as a dictionary for serialization.
        """
        return {
            'name': self.name,
            'bio': self.bio,
            'tags': self.tags,
            'victim_connection': self.victim_connection,
            'guilty': self.guilty,
            'id': self.id,
            'memory_path': self.memory_path
        }

    def __setstate__(self, state: dict) -> None:
        """
        Restores the object's state from the given dictionary.

        :param state: The dictionary containing the object's state.
        """
        self.name = state['name']
        self.bio = state['bio']
        self.tags = state['tags']
        self.victim_connection = state['victim_connection']
        self.guilty = state['guilty']
        self.id = state['id']
        self.memory_path = state['memory_path']
