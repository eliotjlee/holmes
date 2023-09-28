from typing import List
from story_elements.timestamp import Timestamp  # Assuming you have a Timestamp class


class Timeline:
    def __init__(self, start_time: str, time_of_murder: str, timestamps: List[Timestamp]):
        """
        Initializes a Timeline instance with a start time, time of murder, and a list of timestamps.

        :param start_time: A string representing the start time of the timeline.
        :param time_of_murder: A string representing the time of murder in the timeline.
        :param timestamps: A list of Timestamp instances representing the events in the timeline.
        """
        self.start_time = start_time
        self.time_of_murder = time_of_murder
        self.timestamps = timestamps  # This is a list of Timestamp objects

    def get_times_list(self) -> List[str]:
        """
        Returns a list of times extracted from the timestamps in the timeline.

        :return: A list of strings representing the times of events in the timeline.
        """
        times_list = [timestamp.time for timestamp in self.timestamps]
        return times_list
