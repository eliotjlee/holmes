from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain, LLMChain
from langchain.prompts import PromptTemplate
from templates import generate_perspective_template, new_perspective
from assemble_suspect_context import assemble_suspect_context
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a memory object
memory = ConversationBufferMemory()

llm = ChatOpenAI(
    temperature=0.45,
    model="gpt-3.5-turbo-16k-0613",
)

prompt = PromptTemplate.from_template(new_perspective)

# Create a chain object
chain = LLMChain(
    llm=llm,
    memory=memory,
    verbose=True,
    prompt=prompt,
)

info_template = """Here is some background information about the case:
{character_description}

Here is the part of the event you are currently living out again in your dream:
{event}"""

def get_narrative_header(suspects, suspect_id):
    # Get the desired suspect
    print(suspects)
    print(f"ID: {suspect_id}")

    suspect = suspects[suspect_id-1]

    # Create an empty string
    output_str = ""

    # Add each line of output to the string, using the 'suspect' variable
    output_str += f"Suspect name: {suspect.name}\n"
    output_str += f"Suspect bio: {suspect.bio}\n"
    output_str += f"Suspect tags: {suspect.tags}\n"
    output_str += f"Suspect victim connection: {suspect.victim_connection}\n"
    output_str += f"Guilty?: {suspect.guilty}\n"
    output_str += f"Suspect ID: {suspect.id}\n"

    # Return the string
    return output_str



def write_suspect_account(plot, suspects, timeline, suspect_id, save_path):
    # Create 'accounts' folder if it does not exist
    accounts_path = os.path.join(save_path, "accounts")
    if not os.path.exists(accounts_path):
        os.mkdir(accounts_path)

    # Write a suspect account
    with open(f"{accounts_path}/suspect_{suspect_id}", "w") as f:
        suspect_context = assemble_suspect_context(plot, suspects, suspect_id)
        header = get_narrative_header(suspects, suspect_id)
        f.write(header)
        f.write("\nTIMELINE:\n\n")
        for timestamp in timeline.timestamps:
            action = timestamp.suspect_actions[f"suspect_{suspect_id}"]
            time_and_action = f"At {timestamp.time}, {action}"
            
            info = info_template.format(character_description=suspect_context, event=time_and_action)

            entry = chain(info)
            f.write(f"\n\nTIME: {timestamp.time}\n")
            f.write(entry['text'])

    
