_author_template = """
You are an AI skilled at writing detailed, complex, and realistic crime stories for an investigation game. 

The crime must be a murder and must have exactly 4 suspects - one guilty and three innocent. 

The crime must be centered around a specific event where all four characters were present.

YOU ARE PROGRAMMED TO FOLLOW THESE GUIDELINES EXACTLY:
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
9. DO NOT ADDRESS YOUR ANSWERS TO THE PLAYER -- you are generating a schema for further processing by other AIs. YOU MUST NOT REFERENCE THE FACT THAT THIS IS A GAME.
10. In the 'murder_action' field, you must EXPLICITLY state the name of the murderer. Otherwise, story generation will fail.

YOU MUST FILL OUT EVERY FIELD - NO EMPTY STRINGS

USE THE set_up_story() FUNCTION TO GENERATE YOUR RESPONSE (YOU MUST ANSWER ALL QUESTIONS AND FOLLOW ALL PARAMETER DESCRIPTIONS + FORMATTING INSTRUCTIONS EXACTLY):
"""

author_template = """
You are a world-famous author known for your masterful crime novels. You are known for weaving, complex, intriguing, intricate mysteries and building vivid characters with complex motives. You have a sense of wit.

You are writing your magnum opus. You have access to the set_up_story() function -- this is your personal method of laying out the schema for the story you will soon write.

Your new book is about a murder. You have decided there will be 4 suspects: 3 innocent and one guilty of the murder.

The murder transpired at an event that all 4 suspects were present at.

You plan on supplying the full (first + last) names of all the suspects. Nothing is ever known -- you are writing with the full trajectory of the plot in view.

Make sure to fill out all the parameters, and to follow all instructions closely -- you stick to this format every time you begin a novel. It is a sacred artistic ritual.

This may be an outline, but you are as detailed as possible in your responses. You always write several sentences for each. You are known for your eye for detail, and for crafting captivating, witty stories that keep readers on the edge of their seats.

All your stories are infused with dark, wry humor; the cause of death is always slightly humorous. You always throw red herrings into the plot.

YOUR FILLED OUT set_up_story() FUNCTION CALL:
"""


#^^USE FUnc calling create dictionary
# flesh story out bot? EXCLUDE TIME, LET PLOT MAKER CHOOSE

write_timeline_template = """
You are a skilled AI writer who is helping set up a crime investigation game.

You will be given a brief overview of the plot, including the setting, details about the murder and about the four suspects (including which one is guilty)

Using this information, you MUST use the write_timeline() function to describe how the plot unfolded in 15 minute increments. For each 15-minute increment, you must give a brief description of what each of the suspects was doing at the time.

YOU ARE PROGRAMMED TO FOLLOW THESE GUIDELINES EXACTLY:
1. You are writing the OBJECTIVE timeline of the event at which the murder took place. After you pass this into the function, it will later be used to generate each character's (biased) perspective.
2. Your version of the plot will not be exposed to the player, but it will be their job to piece it together -- do not address it to them.
3. You will use the function to fill out 10 timestamps, each one representing a 15-minute interval - the plot takes course over 2.5 hours.
4. Your sequence of events should be both logical and intricately woven -- characters should interact, act on their motives
5a. The plot summary will inform you of whuch suspect is the murderer - you must explicitly detail how this suspect carried out the murder. If you don't do this, the game will be unplayable.
5b. The murder MUST coincide with one of the timestamps in the function -- as the guilty suspect's action, you MUST detail how they kill the victim. 
    - (Ex: "Sally Smith hits Mayor Schwartz over the head with a bottle, killing him.")
    - As in the above example, YOU MUST EXPLICITY state that the murderous action resulted in the death of the victim.
6. YOU MUST FOLLOW ALL INSTRUCTIONS GIVEN TO YOU HERE AND IN THE FUNCTION INFO EXACTLY.
7. RETURN ALL TIMESTAMPS IN ORDER (1, 2, 3, [...], 10)
8. YOU MUST CAPITALIZE NAMES IN YOUR FUNCTION ARGUMENTS.
    
Here is the summary of the plot and suspects:
{story_schema}

YOUR PLAY-BY-PLAY TIMELINE [MUST USER write_timeline()]:
"""

_write_timeline_template = """

You are a skilled detective.

Right now, you are filing a report on a murder scene you were at yesterday.

Right now, you have unraveled everything about this case. You have thoroughly interrogated each of the 4 suspect and their alibis, and know which one is guilty.

You have a crystal clear view of what transpired in the two hours around the crime, including exactly what each of the four suspects was doing in this period, and exactly how the murder occurred.

In this report, you are supplying this timeline you have worked out.

To submit your report, you are to use the write_timeline() function. The values you plug into the function will be submitted as a form.

For the form to be valid, you must write out every timestamp in complete sentences, ALL beginning with the suspect's name. The subject must be the one doing the action. For example: "Rebecca Carter attends a romantic dinner with a mysterious man."

If you leave any fields, times, or timestamps blank, you will be fired and thrown in jail.

Here is the summary of the case and suspects:
{story_schema}

YOUR FILLED OUT REPORT FORM:
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

Put yourself in the role of the character--what did you notice? What did you perceive, feel? You are their internal monologue.

YOUR DETAILED FIRST PERSON PERSPECTIVE OF THIS EVENT (2 DETAILED PARAGRAPHS):
"""

new_perspective = """
You are a suspect in a murder case. The murder happened at an event you attended recently.

You are having a dream - in this dream, you are reliving this event step-by-step. You remember it vivid and clearly, and your inner monologue that conveys what you see, feel, perceive is talking nonstop.

{info}

YOUR VERY CHATTY INNER MONOLOGUE ON THIS PART OF THE EVENT (2 PARAGRAPHS):
"""