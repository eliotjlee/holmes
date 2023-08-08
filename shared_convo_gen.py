import openai
import os
import threading

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_shared_convos(prompts_dict):

    shared_convo_dict = {}
        
    def simulate_convo(interaction, prompt):
        story_skeleton = openai.ChatCompletion.create(
            model='gpt-3.5-turbo-16k-0613',
            messages=[{'role': 'system', 'content': prompt}],
        )
        shared_convo_dict[interaction] = story_skeleton.get('choices', [{}])[0].get('text', {})

    threads = []
    for interaction, prompt in prompts_dict:
        thread = threading.Thread(target=simulate_convo, args=(interaction, prompt))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return shared_convo_dict



def get_prompts(shared_interactions, plot, suspects_dict):
    """
    Generate prompts for the LLM based on the shared interactions.

    :param shared_interactions: List of SharedInteraction objects
    :param plot_info: Information about the murder/plot
    :param suspect_info: Dictionary with suspect names as keys and details as values
    :return: Dictionary with SharedInteraction string as keys and prompts as values
    """
    prompts_dict = {}
    
    for interaction in shared_interactions:
        suspect_a = suspects_dict[interaction.suspect_a]
        suspect_b = suspects_dict[interaction.suspect_b]

        prompt = (f"Timestamp: {interaction.timestamp}. Context: A murder has taken place. Details: \n{plot.get_info}. "
                  f"Suspect {interaction.suspect_a} details: \n\n{suspect_a.get_info()}. "
                  f"Suspect {interaction.suspect_b} details: \n\n{suspect_b.get_info()}. "
                  f"Using the interaction ID '{interaction.interaction_id}', simulate a conversation between "
                  f"{interaction.suspect_a} and {interaction.suspect_b}.")
        
        prompts_dict[str(interaction)] = prompt
    
    return prompts_dict

def write_shared_interaction_prompts(shared_interactions, plot, suspects_dict):
    prompts_dict = get_prompts(shared_interactions, plot, suspects_dict)
    generated_convos_dict = generate_shared_convos(prompts_dict)
    return generated_convos_dict