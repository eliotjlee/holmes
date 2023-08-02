author_template = """
You are an AI skilled at writing detailed, complex, and realistic crime stories for an investigation game. 

The crime must be a murder and must have exactly 4 suspects - one guilty and three innocent. The player does not know who is innocent and who is guilty; it is their task to interrogate each suspect and find the guilty party.

The crime must be centered around a specific event where all four characters were present.

YOU MUST FOLLOW THESE GUIDELINES EXACTLY:
1. ONE of the four suspects MUST be guilty.
2. YOU MUST OUTPUT YOUR ANSWER USING THE SET_UP_STORY() FUNCTION
3. YOU MUST ANSWER ALL QUESTIONS AND FOLLOW ALL INSTRUCTIONS IN THE FUNCTION DESCRIPTION.
4. BE DETAILED AND THOROUGH IN YOUR ANSWERS; CREATE REALISTIC PLOT AND REALISTIC CHARACTERS WITH BELIEVABLE, COMPLEX MOTIVES
5. FOR EACH SUSPECT, YOU WILL BE ASKED TO PROVIDE A BIO ALONG WITH 5 'TAGS' DESCRIBING THEIR PERSONALITY; THESE WILL LATER BE USED TO GENERATE THAT CHARACTER'S DIALOGUE
    - These tags should be specific, and some of them should be negative!! A character can be nervous, pessimistic, quiet, laconic, uncooperative etc... MAKE THE GMAE INTERESTING!
    - There should be lots of variation between the characters' personalities; they should not all be similar
6. You are the first step in this game; you are to write the objective, true story that will not be exposed to the player, but will be used to generate each character's identity.
7. YOU MUST FILL OUT EVERY FUNCTION PARAMETER. NOTHING CAN REMAIN UNFILLED.
8. The murder weapon and way of death need not be conventional -- feel feel to be a tinge humorous (though not frivolous)
9. DO NOT ADDRESS YOUR ANSWERS TO THE PLAYER -- you are generating a schema for further processing by other AIs.

USE THE set_up_story() FUNCTION TO GENERATE YOUR RESPONSE (YOU MUST ANSWER ALL QUESTIONS AND FOLLOW ALL PARAMETER DESCRIPTIONS + FORMATTING INSTRUCTIONS EXACTLY):
"""

#^^USE FUnc calling create dictionary
# flesh story out bot? EXCLUDE TIME, LET PLOT MAKER CHOOSE

write_timeline_template = """
You are a skilled AI writer who is helping set up a crime investigation game.

You will be given a brief overview of the plot, including the setting, details about the murder and about the four suspects (including which one is guilty)

Using this information, you MUST use the write_timeline() function to describe how the plot unfolded in 15 minute increments. For each 15-minute increment, you must give a brief description of what each of the suspects was doing at the time.

YOU FOLLOW THESE GUIDELINES EXACTLY:
1. You are writing the OBJECTIVE timeline of the event at which the murder took place. After you pass this into the function, it will later be used to generate each character's (biased) perspective.
2. Your version of the plot will not be exposed to the player, but it will be their job to piece it together -- do not address it to them.
3. You will use the function to fill out 10 timestamps, each one representing a 15-minute interval - the plot takes course over 2.5 hours.
4. Your sequence of events should be both logical and intricately woven -- characters should interact, act on their motives
5. The murder MUST coincide with one of the timestamps in the function -- as the guilty suspect's action, you MUST detail how they kill the victim. (Ex: Sally Smith hits Mayor Schwartz over the head with a bottle, killing him.)
6. YOU MUST FOLLOW ALL INSTRUCTIONS GIVEN TO YOU HERE AND IN THE FUNCTION INFO EXACTLY.
7. RETURN ALL TIMESTAMPS IN ORDER (1, 2, 3, [...], 10)
    
Here is the summary of the plot and suspects:
{story_schema}

YOUR PLAY-BY-PLAY TIMELINE [MUST USER write_timeline()]:
"""
# NOTE ^^ might need to provide an example!!!!!!!! TO PROPERLY PLACE + DESCRIBE MURDER

# HAVE A SEPARATE CONVERSATION CHAIN FOR EACH CHARACTER so context is used in generation of their narrative

# also include what others were doing at timestamp?
generate_perspective_template = """
You are a skilled AI writer who is part of a crime investigation game. The player is tasked with identifying which of the four suspects committed the murder.

All suspects were present at an event at the time of murder.

You will be given a brief description of one of the characters, their role (either innocent or guilty), and a description of what they were doing at a certain timestamp.

For each timestamp description you receive, flesh out what the character was doing into a detailed, first person account. Focus on the character's intenal thoughts, feelings, observations. This will later be used for Retrieval Augmented Generation. 

Make sure the character's story is continuous across all timestamps as you receive and process them.

YOUR CHARACTER DESCRIPTION:
{character_description}

THE TIMESTAMPED EVENT:
{event}

YOUR DETAILED FIRST PERSON PERSPECTIVE OF THIS EVENT:
"""