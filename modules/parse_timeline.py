from story_elements.timestamp import Timestamp
from story_elements.timeline import Timeline


def parse_timeline(timeline_dict):
    valid_output = True
    start_time = timeline_dict.get("start_time")
    time_of_murder = timeline_dict.get("time_of_murder")

    timestamps = []
    for i in range(1, 11):
        timestamp = timeline_dict.get(f"timestamp_{i}")
        time = timestamp.get("time")
        suspect_actions = {
            "suspect_1": timestamp.get("suspect_1_action"),
            "suspect_2": timestamp.get("suspect_2_action"),
            "suspect_3": timestamp.get("suspect_3_action"),
            "suspect_4": timestamp.get("suspect_4_action")
        }
        timestamps.append(Timestamp(time, suspect_actions))

        # If any actions left blank, Timeline not valid -- retry
        for action in suspect_actions.values():
            if not action.isalpha():
                valid_output = False
                break

    return Timeline(start_time, time_of_murder, timestamps), valid_output
