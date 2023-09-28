class SharedInteraction:
    def __init__(self, timestamp: str, suspect_a: str, suspect_b: str, interaction_id: int):
        """
        Initializes a SharedInteraction instance.

        :param timestamp: The time the interaction occurred.
        :param suspect_a: The name of suspect A involved in the interaction.
        :param suspect_b: The name of suspect B involved in the interaction.
        :param interaction_id: The ID of the interaction.
        """
        self.time = timestamp
        self.suspect_a = suspect_a  # name
        self.suspect_b = suspect_b  # name
        self.interaction_id = interaction_id
        self.interaction_content = None

    def __str__(self) -> str:
        """
        Returns a string representation of the interaction.
        """
        return f"{self.time} {self.suspect_a}-{self.suspect_b}:{self.interaction_id}"

    def get_text(self) -> str:
        """
        Returns the text content of the interaction.
        """
        return self.interaction_content

    def set_text(self, text: str) -> None:
        """
        Sets the text content of the interaction.

        :param text: The text content to set.
        """
        self.interaction_content = text

    def get_summary(self) -> str:
        """
        Returns a summary of the interaction.
        """
        if self.interaction_id is not None:
            summary = f"Time: {self.time}\n"
            summary += f"Suspect A: {self.suspect_a}\n"
            summary += f"Suspect B: {self.suspect_b}\n"
            summary += f"Interaction ID: {self.interaction_id}\n"
            summary += f"Interaction content: \n{self.interaction_content}\n"
            return summary
        else:
            return "No interaction"

    def get_interaction_pair(self) -> str:
        """
        Returns a string containing the pair of suspects involved in the interaction along with the time.
        """
        info = f"Time: {self.time}\n"
        info += f"Suspect A: {self.suspect_a}\n"
        info += f"Suspect B: {self.suspect_b}\n"
        return info

    def get_interaction_id(self) -> int:
        """
        Returns the ID of the interaction.
        """
        return self.interaction_id

    def __getstate__(self) -> dict:
        """
        Returns the object's state as a dictionary for serialization.
        """
        return {
            'time': self.time,
            'suspect_a': self.suspect_a,
            'suspect_b': self.suspect_b,
            'interaction_id': self.interaction_id,
            'interaction_content': self.interaction_content
        }

    def __setstate__(self, state: dict) -> None:
        """
        Restores the object's state from the given dictionary.

        :param state: The dictionary containing the object's state.
        """
        self.time = state['time']
        self.suspect_a = state['suspect_a']
        self.suspect_b = state['suspect_b']
        self.interaction_id = state['interaction_id']
        self.interaction_content = state['interaction_content']
