from suspect_agents.suspect_agent import SuspectAgent
import sys

def indict_suspect(agents):
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
    while True:
        print(f"""
        Please choose one of the following suspects:
        1. {agents[0].suspect.get_info()}
        2. {agents[1].suspect.get_info()}
        3. {agents[2].suspect.get_info()}
        4. {agents[3].suspect.get_info()}
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
            indicted_suspect = indict_suspect(agents) # returns player's chosen suspect object
            if indicted_suspect.guilty: #Check if selected suspect is guilty
                print("You win!")
            else:
                print("You lose!")
            sys.exit(0)
        else:
            print("Invalid choice. Please pick a number between 1 and 4.")

def build_and_run_agents(plot):

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
