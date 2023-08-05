import openai
import os
from LLM_functions.set_up_story import set_up_story_func
from LLM_functions.write_timeline import write_timeline_func
from old.write_accounts import create_suspect_prompt, create_suspect_prompt_dict, generate_suspect_prompt
from suspect_init import write_suspect_account
from make_save import make_save
from story_init import initialize_story
from templates import author_template, write_timeline_template
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

def fix_trailing_commas(json_string):
    json_string = re.sub(",\s*}", "}", json_string)
    json_string = re.sub(",\s*\]", "]", json_string)
    return json.loads(json_string)


openai.api_key = os.getenv("OPENAI_API_KEY")

# initialize save directory, get path
save_path = make_save()

initialize_story(save_path)

# story_skeleton = openai.ChatCompletion.create(
#     model = 'gpt-3.5-turbo-16k-0613',
#     messages = [{'role': 'system', 'content': author_template}],
#     functions = set_up_story_func,
#     function_call = {'name': 'set_up_story'},
# )

# story_schema = story_skeleton.get('choices', [{}])[0].get('message', {}).get('function_call', {}).get('arguments')

# print(story_schema)

# plot, suspects = parse_story(fix_trailing_commas(story_schema))

# story_timeline = openai.ChatCompletion.create(
#     model = 'gpt-3.5-turbo-16k-0613',
#     messages = [{'role': 'system', 'content': write_timeline_template.format(story_schema=story_schema)}],
#     functions = write_timeline_func,
#     function_call = {'name': 'write_timeline'},
# )


# print(story_timeline)

# story_timeline_args = story_timeline.get('choices', [{}])[0].get('message', {}).get('function_call', {}).get('arguments')

# timeline = parse_timeline(fix_trailing_commas(story_timeline_args))

# for i in range(4):
#     write_suspect_account(plot, suspects, timeline, i+1)