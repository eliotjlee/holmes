import openai
import os
from LLM_functions.set_up_story import set_up_story_func
from LLM_functions.write_timeline import write_timeline_func
from LLM_functions.shared_events import shared_events_func
from LLM_functions.write_timestamp import write_timestamp_func
from shared_convo_gen import generate_shared_interactions
from old.write_accounts import create_suspect_prompt, create_suspect_prompt_dict, generate_suspect_prompt
from parse_shared_events import parse_shared_interactions
from suspect_init import write_suspect_account
from make_save import make_save
from prompt_templates.story_init import author_template
import json
import re
import pprint
from parse_story import parse_story
from story_elements.victim import Victim
from story_elements.murder_details import MurderDetails
from story_elements.plot import Plot
from story_elements.suspect import Suspect
from parse_timeline import parse_timeline
import datetime
import re
import json
import threading
from prompt_templates.shared_events import shared_events_template
from story_elements.plot import Plot
from prompt_templates.timeline import write_timeline_template
from write_timeline import write_timeline

def fix_trailing_commas(json_string):
    json_string = re.sub(",\s*}", "}", json_string)
    json_string = re.sub(",\s*\]", "]", json_string)
    return json.loads(json_string)


openai.api_key = os.getenv("OPENAI_API_KEY")

def save_schema(plot, suspects, save_path):
    with open(f"{save_path}/plot_overview.txt", "w") as f:
        f.write(f"Plot summary: {plot.summary}\n")
        f.write(f"Murder description: {plot.murder_details.murder_description}\n")
        f.write(f"Murder settting: {plot.murder_details.murder_setting}\n")
        f.write(f"Murder weapon: {plot.murder_details.murder_weapon}\n")
        f.write(f"Murder action: {plot.murder_details.murder_action}\n\n")

        f.write("Suspects:\n")
        for suspect in suspects:
            f.write(f"\nName: {suspect.name}\n")
            f.write(f"\tBio: {suspect.bio}\n")
            f.write(f"\tTags: {suspect.tags}\n")
            f.write(f"\tVictim connection: {suspect.victim_connection}\n")
            f.write(f"\tGuilty?: {suspect.guilty}\n")
            f.write(f"\tSuspect ID: {suspect.id}\n")

def save_timeline(timeline, save_path):
    with open(f"{save_path}/timeline.txt", "w") as f:
        f.write(f"TIME OF MURDER: {timeline.time_of_murder}\n\n")
        f.write("TIMELINE:\n")
        for timestamp in timeline.timestamps:
            f.write(f"\nTime: {timestamp.time}")
            for i in range(len(timestamp.suspect_actions)):
                suspect_key = f"suspect_{i+1}"
                f.write(f"\n\t{timestamp.suspect_actions[suspect_key]}\n")

def save_shared_events(shared_events, save_path):
    with open(f"{save_path}/shared_events.txt", "w") as f:
        json.dump(shared_events, f, indent=4)

def save_shared_interactions(plot, save_path):
    with open(f"{save_path}/shared_events.txt", "w") as f:
        shared_interactions = plot.shared_interactions

        for interaction in shared_interactions:
            if interaction.interaction_content != None:
                f.write(f"TIME: {interaction.time}\n\n")
                f.write(f"Suspect a: {interaction.suspect_a}\n")
                f.write(f"Suspect b: {interaction.suspect_b}\n\n")
                f.write(f"Interaction content: \n\n{interaction.interaction_content}\n\n")


def initialize_story(save_path):

    # generate base story schema
    story_skeleton = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo-16k-0613',
        messages = [{'role': 'system', 'content': author_template}],
        functions = set_up_story_func,
        function_call = {'name': 'set_up_story'},
    )

    story_schema = story_skeleton.get('choices', [{}])[0].get('message', {}).get('function_call', {}).get('arguments')

    print(story_schema)

    plot, suspects = parse_story(fix_trailing_commas(story_schema))

    save_schema(plot, suspects, save_path)

    # pre timeline events
    story_shared_events = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo-16k-0613',
        messages = [{'role': 'system', 'content': shared_events_template.format(story_schema=story_schema)}],
        functions = shared_events_func,
        function_call = {'name': 'shared_events'},
    )

    shared_events = story_shared_events.get('choices', [{}])[0].get('message', {}).get('function_call', {}).get('arguments')

    parse_shared_interactions(fix_trailing_commas(shared_events), plot)

    print(shared_events)

    save_shared_events(fix_trailing_commas(shared_events), save_path)

    write_timeline(plot, write_timestamp_func)

    generate_shared_interactions(plot)
    
    save_shared_interactions(plot, save_path)

    accounts_path = os.path.join(save_path, "accounts")
    if not os.path.exists(accounts_path):
        os.mkdir(accounts_path)

    threads = []
    for i in range(4):
        print(f"Creating thread for suspect {i+1}")
        t = threading.Thread(target=write_suspect_account, args=(plot, i, accounts_path))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    return plot