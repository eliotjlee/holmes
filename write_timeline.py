import openai
import langchain
import os
from story_elements.timestamp import Timestamp
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from LLM_functions.write_timestamp import write_timestamp_func
import json
import threading
from langchain.schema.output_parser import StrOutputParser

openai.api_key = os.getenv("OPENAI_API_KEY")

def correct_json_thread(i, timestamp, results):
    prompt = "You fix JSON strings if they are not correctly formatted. If the string you receive is already formatted, you just returnthe string again. You only return JSON, no words.\n\n"
    prompt += f"{timestamp}\n\n"

    corrected_timestamp = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-16k-0613',
        messages=[{'role': 'system', 'content': prompt}],
    )

    corrected_timestamp = corrected_timestamp.choices[0].message['content']
    results[i] = corrected_timestamp


def fix_json(timestamps):
    threads = []
    results = [None] * len(timestamps)

    for i, timestamp in enumerate(timestamps):
        thread = threading.Thread(target=correct_json_thread, args=(i, timestamp, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results
    

def parse_timeline(timestamps, plot):
    # PARSE TO 10-ELEMENT LIST OF 4-ELEMENT LISTS
    # THEN PROCESS INTO TIMESTAMP OBJECTS
    for timestamp in timestamps:
        timestamp_dict = json.loads(timestamp)
        time = timestamp_dict["time"]
        suspect_1_action = timestamp_dict["suspect_1_action"]
        suspect_2_action = timestamp_dict["suspect_2_action"]
        suspect_3_action = timestamp_dict["suspect_3_action"]
        suspect_4_action = timestamp_dict["suspect_4_action"]
        timestamp_obj = Timestamp(time, [suspect_1_action, suspect_2_action, suspect_3_action, suspect_4_action])
        plot.add_timestamp_to_timeline(timestamp_obj)




def write_timeline_template(timestamp_number, background_info, shared_events, previous_timestamp, response_format):
        
    timeline_base = "You generate full timelines in 15 minute intervals. These timeline will detail the actions and experiences of each of the four suspects during the event.\n\n"

    timeline_base += f"You are currently writing timestamp {timestamp_number} out of 10.\n\n"

    timeline_base += "BACKGROUND INFO:\n\n"
    timeline_base += f"{background_info}\n\n"

    if shared_events.interaction_id != None:
        shared_interaction = shared_events.get_interaction_pair()

        timeline_base += f"THE FOLLOWING SUSPECTS MUST INTERACT AND ACKNOWLEDGE EACHOTHER AT THIS TIMESTAMP ({timestamp_number}/10). Their actions must contain each other's names:\n"
        timeline_base += f"{shared_interaction}\n\n"

    if previous_timestamp != None:
        timeline_base += f"PREVIOUS TIMESTAMP (Yours must be 15 minutes after this):\n"
        timeline_base += f"{previous_timestamp}\n\n"

    timeline_base += "Fill in all the details, weaving a convincing, continuous narrative, otherwise you die.\n ALL SUSPECTS MUST HAVE AN ACTION AT EACH TIMESTAMP.\n Detail how the murderer plots and carries out their crime; do not write about the investigation. \n\n"

    timeline_base += f"TIMESTAMP {timestamp_number} OUT OF 10 (YOU MUST RETURN YOUR ANSWER USING write_single_timestamp()):"
    return timeline_base


def write_timeline(plot, response_format):

    timestamps = []
    
    # 1. Open a new file in append mode
    with open("timestamps.txt", "a") as file:
        

        template = write_timeline_template(1, plot.get_summary(), plot.shared_interactions[0], None, response_format)

        print(template)

        last_timestamp = openai.ChatCompletion.create(
            model='gpt-3.5-turbo-16k-0613',
            messages=[{'role': 'system', 'content': template}],
            functions=write_timestamp_func,
            function_call={'name': 'write_single_timestamp'},
        )

        last_timestamp = last_timestamp.choices[0].message.function_call.arguments
        timestamps.append(last_timestamp)

        # 2. Write the prompt and its generated timestamp to the file
        file.write(f"Prompt:\n{template}\nGenerated Timestamp:\n{last_timestamp}\n\n")

        for i in range(3, 11):
            template = write_timeline_template(i, plot.get_summary(), plot.shared_interactions[i-1], last_timestamp, response_format)
            print(template)

            last_timestamp = openai.ChatCompletion.create(
                model='gpt-3.5-turbo-16k-0613',
                messages=[{'role': 'system', 'content': template}],
                functions=write_timestamp_func,
                function_call={'name': 'write_single_timestamp'},
            )

            last_timestamp = last_timestamp.choices[0].message.function_call.arguments
            timestamps.append(last_timestamp)
            
            # 2. Write the prompt and its generated timestamp to the file
            file.write(f"Prompt:\n{template}\nGenerated Timestamp:\n{last_timestamp}\n\n")
            
            print(last_timestamp)

    timestamps = fix_json(timestamps)

    for timestamp in timestamps:
        print(timestamp)
    parse_timeline(timestamps, plot)


