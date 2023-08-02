import json

def create_suspect_prompt(api_response_story, api_response_timeline, suspect_number):
    story_dict = json.loads(api_response_story["choices"][0]["function_call"]["arguments"])
    timeline_dict = json.loads(api_response_timeline["choices"][0]["function_call"]["arguments"])

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
    prompt_lines.append(f"Suspect Bio: {suspect['bio']}")
    prompt_lines.append(f"Suspect Tags: {', '.join([suspect[tag] for tag in ['tag_1', 'tag_2', 'tag_3', 'tag_4', 'tag_5'] if tag in suspect])}")
    prompt_lines.append(f"Connection to Victim: {suspect['victim_connection']}")

    # Append timeline events
    for timestamp_key, timestamp_event in timeline_dict.items():
        if timestamp_key.startswith("timestamp_"):
            suspect_action = timestamp_event[f"{suspect_key}_action"]
            time = timestamp_event["time"]
            prompt_lines.append(f"At {time}, {suspect['name']} {suspect_action.lower()}.")

    # Combine all prompt lines into a single string with newline separators
    prompt = "\n".join(prompt_lines)
    return prompt
