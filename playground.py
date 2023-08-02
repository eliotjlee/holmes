import openai
import os
from LLM_functions.set_up_story import set_up_story_func
from LLM_functions.write_timeline import write_timeline_func
from write_accounts import create_suspect_prompt
from templates import author_template, write_timeline_template
import json
import re
import pprint


openai.api_key = os.getenv("OPENAI_API_KEY")

def print_function_arguments(data):
    if not isinstance(data, dict):
        raise ValueError('Input data should be a dictionary')

    try:
        function_call = data.get('choices', [{}])[0].get('message', {}).get('function_call', {})
        function_name = function_call.get('name')
        arguments = function_call.get('arguments')

        # pretty print function name
        print(f"Function: {function_name}")

        # pretty print arguments
        print("Arguments:")
        
        # Remove trailing commas
        arguments = re.sub(",\s*}", "}", arguments)
        arguments = re.sub(",\s*\]", "]", arguments)

        arguments_dict = json.loads(arguments)
        pprint.pprint(arguments_dict, indent=2)

    except Exception as e:
        print(f"Error processing data: {str(e)}")


story_skeleton = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo-16k-0613',
    messages = [{'role': 'system', 'content': author_template}],
    functions = set_up_story_func,
    function_call = {'name': 'set_up_story'},
)

print(story_skeleton)

print_function_arguments(story_skeleton)

story_schema = story_skeleton.get('choices', [{}])[0].get('message', {}).get('function_call', {}).get('arguments')

# story_timeline = openai.ChatCompletion.create(
#     model = 'gpt-3.5-turbo-16k-0613',
#     messages = [{'role': 'system', 'content': generate_plot_template}],
#     functions = set_up_story_func,
#     function_call = {'name': 'generate_plot'},
#     max_tokens = 1000,
#     temperature = 0.7,
#     top_p = 1,
#     frequency_penalty = 0.5,
#     presence_penalty = 0.5,
#     stop = ['\n', 'YOU MUST FOLLOW THESE GUIDELINES EXACTLY:']
# )



story_timeline = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo-16k-0613',
    messages = [{'role': 'system', 'content': write_timeline_template.format(story_schema=story_schema)}],
    functions = write_timeline_func,
    function_call = {'name': 'write_timeline'},
)

print(story_timeline)

print_function_arguments(story_timeline)