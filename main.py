"""
This module is the entry point of the game. It includes functions to create a new game, load a saved game,
and run the game. It also handles the initial interaction with the user to decide whether to start a new
game or load a saved one.

Functions:
    new_game() -> object:
        Creates a new game, including the story, suspects, and their accounts, and returns the Plot object.

    load_game() -> object:
        Loads a game from a saved directory by deserializing the Plot object from a pickle file.

    main() -> None:
        The main function to run the game. It interacts with the user to decide whether to start a new game
        or load a saved one, and then builds and runs the suspect agents to commence the game.

Execution:
    If this script is run as the main module, it calls the main() function to start the game.
"""


import openai
import os
import time
import traceback
from modules.make_save import make_save  # Import function to create a save directory and return its path
from modules.story_init import initialize_story  # Import function to initialize a story
from story_elements.pickle_plot import save_plot, load_plot  # Import functions to save and load the plot
from modules.load_save import get_latest_saves  # Import function to get the path of the latest saves
from suspect_agents.run_game import build_and_run_agents  # Import function to build and run agents in the game

# Set the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    exit(1)


def new_game():
    """
    Generates a new game, including the story, suspects, and their accounts.
    It tries to initialize a new story, and if an error occurs, it retries up to three times.

    Returns:
        plot (object): The Plot object containing the story, suspects, and their accounts.
    """
    retries = 0
    max_retries = 3
    while retries < max_retries:
        save_path = None
        try:
            save_path = make_save()
            plot = initialize_story(save_path) # Dynamically create a story, including plot, suspects, etc.
            save_plot(plot, save_path)
            return plot
        except Exception as e:
            # Inevitably, sometimes the story generation will error; LLM-outputted text is not always 100% valid.
            retries += 1
            print(f"Error occurred in story generation: {e}")
            traceback.print_exc()  # Print traceback to understand the error
            if retries < max_retries:
                print("RETRYING...")
                time.sleep(3)
                if save_path is not None:
                    os.rmdir(save_path)
            else:
                print("Max retries reached. Exiting...")
                break


def load_game():
    """
    Loads a game from a saved directory by deserializing the Plot object from a pickle file.

    Returns:
        plot (object): The Plot object containing the story, suspects, and their accounts.
    """
    try:
        save_path = get_latest_saves()
        plot = load_plot(save_path)
        return plot
    except Exception as e:
        print(f"Error occurred while loading the game: {e}")
        traceback.print_exc()


def main():
    """
    The main function to run the game. It first interacts with the user to decide whether to
    start a new game or load a saved one. Then, it generates or loads a Plot object accordingly.
    Finally, it builds and runs the suspect agents to commence the game.

    Returns:
        None
    """
    while True:
        try:
            load_or_save = int(input('''
            Welcome!

            Would you like to:
            1. Generate a new game
            2. Load a save
            '''))
            if not (1 <= load_or_save <= 2):
                print('Invalid input! Please select option 1 or 2')
            else:
                break
        except ValueError:
            print('Invalid input! Please enter a number (1 or 2)')

    # Generate or load a Plot object
    plot = None
    if load_or_save == 1:
        print("Generating new game...")
        plot = new_game()
    elif load_or_save == 2:
        plot = load_game()

    # Uses the Plot object to build and run the suspect agents, commences the game
    build_and_run_agents(plot=plot)


if __name__ == "__main__":
    main()
