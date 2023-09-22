from story_elements.pickle_plot import load_plot
from suspect_agents.run_game import build_and_run_agents
import os


def get_latest_saves(base_path="saves"):
    # List all the folders in the saves directory
    all_saves = [dir_name for dir_name in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, dir_name))]

    # Sort the saves by timestamp
    sorted_saves = sorted(all_saves, reverse=True)

    # Retrieve the most recent saves (up to 10)
    latest_saves = sorted_saves[:10]
    num_latest_saves = len(latest_saves)

    # Display them to the user
    for i, save in enumerate(latest_saves, 1):
        print(f"{i}. {save}")

    # Prompt the user to make a choice
    while True:
        try:
            choice = int(input(f"Pick the number corresponding to the save (1-{num_latest_saves}): "))
            if 1 <= choice <= num_latest_saves:
                return os.path.join(base_path, latest_saves[choice - 1])
            else:
                print(f"Invalid choice. Please choose a number between 1 and {num_latest_saves}.")
        except ValueError:
            print("Please enter a valid number.")


