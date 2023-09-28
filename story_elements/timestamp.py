from typing import List, Dict


class Timestamp:
    def __init__(self, time: str, suspect_actions: List[str]):
        """
        Initializes a Timestamp instance with a specified time and a list of suspect actions.

        :param time: A string representing the time of the timestamp.
        :param suspect_actions: A list of strings where each string represents an action of a suspect.
                                Indices 0-3 correspond to suspects 1-4.
        """
        self.time = time
        self.suspect_actions = suspect_actions  # This is a list where indices 0-3 correspond to suspects 1-4

    def get_time(self) -> str:
        """
        Returns the time of the timestamp.

        :return: A string representing the time of the timestamp.
        """
        return self.time

    def get_suspect_actions(self) -> List[str]:
        """
        Returns the list of suspect actions.

        :return: A list of strings where each string represents an action of a suspect.
        """
        return self.suspect_actions

    def __getstate__(self) -> Dict[str, str]:
        """
        Returns the object's state as a dictionary for serialization.

        :return: A dictionary containing the object's state.
        """
        return {
            'time': self.time,
            'suspect_actions': self.suspect_actions
        }

    def __setstate__(self, state: Dict[str, str]) -> None:
        """
        Restores the object's state from the given dictionary.

        :param state: The dictionary containing the object's state.
        """
        self.time = state['time']
        self.suspect_actions = state['suspect_actions']
