"""
This module defines the game flow, facilitating user interactions with the suspect agents.
It provides a textual interface for the user to interact with the suspects, indict a suspect,
and navigate through the game.

Functions:
    indict_suspect(agents: list) -> object:
        Prompts the user to indict one of the suspects for the murder.
        Returns the indicted suspect object.

    choose_function(agents: list) -> callable:
        Prompts the user to choose a suspect to interact with or to indict a suspect.
        Returns the suspect's response function or exits the game based on the user's choice.

    build_and_run_agents(plot: object) -> None:
        Creates suspect agent instances, and manages the user interactions with these agents.
        Allows the user to query the suspects, switch between suspects, or quit the game.
"""

from suspect_agents.suspect_agent import SuspectAgent
import sys


def indict_suspect(agents):
    """
     Prompts the user to indict one of the suspects for the murder.
     The user is provided with a list of suspects to choose from.

     Args:
     agents (list): List of SuspectAgent instances.

     Returns:
     object: The indicted suspect object.
    """
    while True:
        print(f"""
        Who committed the murder?
        1. {agents[0].suspect.get_info()}
        2. {agents[1].suspect.get_info()}
        3. {agents[2].suspect.get_info()}
        4. {agents[3].suspect.get_info()}
        """)

        choice = input("Enter suspect number (1-4): ").strip()

        if choice == '1':
            return agents[0].suspect
        elif choice == '2':
            return agents[1].suspect
        elif choice == '3':
            return agents[2].suspect
        elif choice == '4':
            return agents[3].suspect
        else:
            print("Invalid choice. Please pick a number between 1 and 4.")


def choose_function(agents):
    """
    Prompts the user to choose a suspect to interact with or to indict a suspect.
    The user is provided with a list of suspects and the option to indict.

    Args:
    agents (list): List of SuspectAgent instances.

    Returns:
    callable: The function to get the suspect's response to the user's queries.
    """
    while True:
        print(f"""
        Please choose one of the following suspects:
        1. {agents[0].suspect.get_info_no_guilty()}
        2. {agents[1].suspect.get_info_no_guilty()}
        3. {agents[2].suspect.get_info_no_guilty()}
        4. {agents[3].suspect.get_info_no_guilty()}
        5. Indict a suspect
        """)

        choice = input("Enter function number (1-5): ").strip()

        if choice == '1':
            return agents[0].get_suspect_response
        elif choice == '2':
            return agents[1].get_suspect_response
        elif choice == '3':
            return agents[2].get_suspect_response
        elif choice == '4':
            return agents[3].get_suspect_response
        elif choice == '5':
            indicted_suspect = indict_suspect(agents)  # returns player's chosen suspect object
            if indicted_suspect.guilty:  # Check if selected suspect is guilty
                print("You win!")
            else:
                print("You lose!")
            sys.exit(0)
        else:
            print("Invalid choice. Please pick a number between 1 and 4.")


def build_and_run_agents(plot):
    """
        Creates suspect agent instances, and manages the user interactions with these agents.
        Allows the user to query the suspects, switch between suspects, or quit the game.

        Args:
        plot (Plot): The plot object containing the story and suspect information.

        Returns:
        None
    """
    suspect_1_agent = SuspectAgent(plot, 0)
    suspect_2_agent = SuspectAgent(plot, 1)
    suspect_3_agent = SuspectAgent(plot, 2)
    suspect_4_agent = SuspectAgent(plot, 3)

    agents = [suspect_1_agent, suspect_2_agent, suspect_3_agent, suspect_4_agent]

    current_function = choose_function(agents)

    while True:
        user_input = input("\nPlease enter your input, type 'switch' to change suspects, or 'quit' to exit: ").strip()

        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'switch':
            current_function = choose_function(agents)
            continue

        print("\nSUSPECT RESPONSE:\n")
        print(current_function(user_input))
