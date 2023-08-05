import json
import re

def create_suspect_prompt(api_response_story, api_response_timeline, suspect_number):
    function_call_story = api_response_story.get('choices', [{}])[0].get('message', {}).get('function_call', {})
    arguments_story = function_call_story.get('arguments')

    function_call_timeline = api_response_timeline.get('choices', [{}])[0].get('message', {}).get('function_call', {})
    arguments_timeline = function_call_timeline.get('arguments')

    # Remove trailing commas
    arguments_story = re.sub(",\s*}", "}", arguments_story)
    arguments_story = re.sub(",\s*\]", "]", arguments_story)

    arguments_timeline = re.sub(",\s*}", "}", arguments_timeline)
    arguments_timeline = re.sub(",\s*\]", "]", arguments_timeline)

    story_dict = json.loads(arguments_story)
    timeline_dict = json.loads(arguments_timeline)

    plot_details = story_dict["plot_details"]
    suspect_key = f"suspect_{suspect_number}"
    suspect = story_dict[suspect_key]

    prompt_lines = []

    # Append plot details
    prompt_lines.append(f"Plot Summary: {plot_details['summary']}")
    prompt_lines.append(f"Victim: {plot_details['victim']['name']}")
    prompt_lines.append(f"Victim Bio: {plot_details['victim']['bio']}")
    prompt_lines.append(f"Murder Details: {plot_details['murder_details']['murder_description']}")
    prompt_lines.append(f"Murder Setting: {plot_details['murder_details']['murder_setting']}")
    prompt_lines.append(f"Murder Weapon: {plot_details['murder_details']['murder_weapon']}")

    # Append suspect details
    prompt_lines.append(f"Suspect Name: {suspect['name']}")
    if bool(suspect['guilty']):
        prompt_lines.append("THIS SUSPECT IS THE MURDERER [GUILTY]")
    else:
        prompt_lines.append("THIS SUSPECT IS INNOCENT")
    prompt_lines.append(f"Suspect Bio: {suspect['bio']}")
    prompt_lines.append(f"Suspect Tags: {', '.join([suspect[tag] for tag in ['tag_1', 'tag_2', 'tag_3', 'tag_4', 'tag_5'] if tag in suspect])}")
    prompt_lines.append(f"Connection to Victim: {suspect['victim_connection']}")

    # Append timeline events
    for timestamp_key, timestamp_event in timeline_dict.items():
        if timestamp_key.startswith("timestamp_"):
            suspect_action = timestamp_event[f"{suspect_key}_action"]
            time = timestamp_event["time"]
            prompt_lines.append(f"At {time}, {suspect_action}")

    # Combine all prompt lines into a single string with newline separators
    prompt = "\n".join(prompt_lines)
    return prompt

def create_suspect_prompt_dict(api_response_story, api_response_timeline, suspect_number):
    function_call_story = api_response_story.get('choices', [{}])[0].get('message', {}).get('function_call', {})
    arguments_story = function_call_story.get('arguments')

    function_call_timeline = api_response_timeline.get('choices', [{}])[0].get('message', {}).get('function_call', {})
    arguments_timeline = function_call_timeline.get('arguments')

    # Remove trailing commas
    arguments_story = re.sub(",\s*}", "}", arguments_story)
    arguments_story = re.sub(",\s*\]", "]", arguments_story)

    arguments_timeline = re.sub(",\s*}", "}", arguments_timeline)
    arguments_timeline = re.sub(",\s*\]", "]", arguments_timeline)

    story_dict = json.loads(arguments_story)
    timeline_dict = json.loads(arguments_timeline)

    plot_details = story_dict["plot_details"]
    suspect_key = f"suspect_{suspect_number}"
    suspect = story_dict[suspect_key]

    prompt_lines = []

    # Append plot details
    prompt_lines.append(f"Plot Summary: {plot_details['summary']}")
    prompt_lines.append(f"Victim: {plot_details['victim']['name']}")
    prompt_lines.append(f"Victim Bio: {plot_details['victim']['bio']}")
    prompt_lines.append(f"Murder Details: {plot_details['murder_details']['murder_description']}")
    prompt_lines.append(f"Murder Setting: {plot_details['murder_details']['murder_setting']}")
    prompt_lines.append(f"Murder Weapon: {plot_details['murder_details']['murder_weapon']}")

    # Append suspect details
    prompt_lines.append(f"Suspect Name: {suspect['name']}")
    if bool(suspect['guilty']):
        prompt_lines.append("THIS SUSPECT IS THE MURDERER [GUILTY]")
    else:
        prompt_lines.append("THIS SUSPECT IS INNOCENT")
    prompt_lines.append(f"Suspect Bio: {suspect['bio']}")
    prompt_lines.append(f"Suspect Tags: {', '.join([suspect[tag] for tag in ['tag_1', 'tag_2', 'tag_3', 'tag_4', 'tag_5'] if tag in suspect])}")
    prompt_lines.append(f"Connection to Victim: {suspect['victim_connection']}")

    # Prepare timeline events
    timeline_events = {}
    for timestamp_key, timestamp_event in timeline_dict.items():
        if timestamp_key.startswith("timestamp_"):
            suspect_action = timestamp_event[f"{suspect_key}_action"]
            time = timestamp_event["time"]
            timeline_events[time] = suspect_action

    # Combine all prompt lines into a single string with newline separators
    summary = "\n".join(prompt_lines)

    # Return dictionary with summary and timeline events
    return {"summary": summary, "timeline_events": timeline_events}


def generate_suspect_prompt(story_json_string, suspect_key):
    # Remove trailing commas
    cleaned_story_json = re.sub(",\s*}", "}", story_json_string)
    cleaned_story_json = re.sub(",\s*\]", "]", cleaned_story_json)

    # Convert the cleaned JSON string into a Python dictionary
    story_json = json.loads(cleaned_story_json)

    # Extract plot details
    plot_details = story_json['plot_details']

    prompt_lines = []

    suspect_key = f"suspect_{suspect_key}"

    # Append plot details
    prompt_lines.append(f"Case details: {plot_details['summary']}")
    prompt_lines.append(f"The victim of the crime is {plot_details['victim']['name']}, {plot_details['victim']['bio']}")

    # Append murder details
    prompt_lines.append(f"The murder took place {plot_details['murder_details']['murder_setting']}. The details of the murder are as follows: {plot_details['murder_details']['murder_description']} The murder weapon was {plot_details['murder_details']['murder_weapon']}.")

    # Append other suspects' details
    for key, value in story_json.items():
        if key.startswith('suspect') and key != suspect_key:
            prompt_lines.append(f"Suspect {value['name']} is described as {value['bio']}. Their traits are {value['tag_1']}, {value['tag_2']}, {value['tag_3']}, {value['tag_4']}, {value['tag_5']}. They knew the victim in the following way: {value['victim_connection']}.")

    # Append current suspect details
    suspect = story_json[suspect_key]
    prompt_lines.append(f"You are suspect {suspect['name']}. You are described as {suspect['bio']}. Your traits are {suspect['tag_1']}, {suspect['tag_2']}, {suspect['tag_3']}, {suspect['tag_4']}, {suspect['tag_5']}. You knew the victim in the following way: {suspect['victim_connection']}.")
    if suspect['guilty']:
        prompt_lines.append("You are the guilty party.")
    else:
        prompt_lines.append("You are not the guilty party.")

    # Combine all prompt lines into a single string with newline separators
    prompt = "\n".join(prompt_lines)
    return prompt
